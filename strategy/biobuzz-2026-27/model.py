#!/usr/bin/env python3
"""BIOBUZZ (FTC 2026-27) cycle-time / expected-value model.

DRAFT -- PLAN.md §19 step 4. PROVISIONAL. Revise after the first real events.

This is an estimate under the stated assumptions, NOT a proof of optimal strategy.
It ignores most opponent interaction, has no defense model beyond a cycle-time
multiplier, and many inputs are ASSUMPTION ranges (see MODEL.md for the reasons).

Every input is a named constant tagged with where it came from:
  MANUAL       BIOBUZZ Competition Manual V1 + TU00 (2026-09-12), cited by table/rule/section
  SETUP-GUIDE  Event Field Setup Guide V1.0 §12.3 calibration (a field doc, not a rule)
  ASSUMPTION   our guess, always given as a (low, nominal, high) range

Method: event-driven Monte Carlo of one alliance (2 robots sharing 1 HIVE) through
AUTO (30 s) and TELEOP (120 s). The 8 s transition has no powered movement (G403),
so it is not simulated; match clock here runs 0..30 AUTO, 30..150 TELEOP.
stdlib only; fixed seeds, so output is deterministic.

    python3 model.py               # full report
    python3 model.py --self-test   # invariants
"""
import argparse
import heapq
import random
import statistics
import sys
from dataclasses import dataclass, replace

# =============================================================================
# MANUAL facts (point values, thresholds, timing, staging)
# =============================================================================
AUTO_S = 30                 # MANUAL §10.1 / §10.4: 30 s AUTO
TRANSITION_S = 8            # MANUAL §10.1, G403: no powered movement -> not simulated
TELEOP_S = 120              # MANUAL §10.1: 2:00 TELEOP
LAST_MINUTE_S = 60          # MANUAL G410 (NECTAR->FLOWER), G426.B (all NECTAR entry), Table 9-1 "FLOWER Ownership Unlocked 1:00"
CAPACITY_MAX = 4            # MANUAL G407: may not simultaneously CONTROL more than 4 SCORING ELEMENTS
PRELOAD_POLLEN = 4          # MANUAL §10.3.1 A.iv, G304.G: each ROBOT starts contacting exactly 4 POLLEN
CELL_STAGED_NECTAR = 3      # MANUAL §10.3.1 B.i: 3 NECTAR in each upward-facing CELL
AREA_NECTAR = 5             # MANUAL §10.3.1 B.ii: 5 NECTAR in each ALLIANCE AREA
FLOWER_STAGED_POLLEN = 4    # MANUAL §10.3.1 A.i: 4 POLLEN in each FLOWER (whether they sit in the scoring volume is FIGURE-ONLY)
GARDEN_STAGED_POLLEN = 4    # MANUAL §10.3.1 A.ii/iii: 4 POLLEN in each GARDEN
POLLEN_TOTAL = 40           # MANUAL §10.3.1 A / §9.8
FLOWER_COUNT = 4            # MANUAL §9.7

PTS_LEAVE = 3               # MANUAL Table 10-2: LEAVE, AUTO only
PTS_PARK_AUTO = 5           # MANUAL Table 10-2: PARK (LOADING ZONE), AUTO
PTS_PARK_TELEOP = 5         # MANUAL Table 10-2: PARK, TELEOP
PTS_TIP = 20                # MANUAL Table 10-2: HIVE TIP, AUTO and TELEOP alike (§10.5.1: only by LAUNCHING into upward CELL)
PTS_CELL_ELEMENT = 2        # MANUAL Table 10-2 / §10.5.1: POLLEN or NECTAR in upward-facing CELL at end
PTS_BOTTOM_NECTAR = 5       # MANUAL Table 10-2 / §10.5.2: Bottom NECTAR Bonus (per FLOWER)
PTS_FLOWER_ELEMENT = 2      # MANUAL Table 10-2 / §10.5.2: element in an owned FLOWER (owner = top-most NECTAR)
PTS_GARDEN_ELEMENT = 1      # MANUAL Table 10-2 / §10.5.3: element in own-colour GARDEN at end

SWARM_RP_THRESHOLD = 16     # MANUAL Table 10-3 (All Other Events): combined LEAVE + PARK points
POLLINATOR1_TIPS = 4        # MANUAL Table 10-3: POLLINATOR 1 RP at >= 4 TIPS
POLLINATOR2_TIPS = 7        # MANUAL Table 10-3: POLLINATOR 2 RP at >= 7 TIPS
RP_WIN, RP_TIE = 3, 1       # MANUAL Table 10-2
RP_SWARM = RP_POLL1 = RP_POLL2 = 1   # MANUAL Table 10-2

# =============================================================================
# Uncertain inputs: (low, nominal, high). Monte Carlo draws uniformly in [low, high].
# =============================================================================
# --- HIVE tip mechanics. Unit = "POLLEN-equivalents" (eq) launched into the upward CELL.
TIP_T0_EQ = (6.5, 7.5, 9.0)
# SETUP-GUIDE §12.3: empty CELL, 7th POLLEN no tip / 8th tips => threshold in (7, 8]; nominal 7.5.
# Range widened to tip on the 7th..9th POLLEN: ASSUMPTION, the guide says fields vary.
FIRST_TIP_LAUNCHED_EQ = (1.5, 2.5, 3.5)
# SETUP-GUIDE §12.3: with 3 NECTAR in CELL, 2nd no tip / 3rd tips => (2, 3]; nominal 2.5.
# Range (tips on 2nd..4th) is ASSUMPTION. Staged NECTAR eq is derived per draw: (T0 - this) / 3.
NECTAR_TIP_EQ = (1.0, 1.5, 1.9)
# ASSUMPTION: tip-equivalent of one LAUNCHED NECTAR. The calibration pair implies 3N ~ 5P (1.67) for
# NECTAR staged against the back wall, but the guide says 3P+3N has LESS mass than 8P, so tipping is
# not mass-only; a launched NECTAR lands anywhere. 1.0 = no advantage.
SPILL_RETAIN_FRAC = (0.0, 0.0, 0.5)
# ASSUMPTION: fraction of elements that stay in the CELL that just rotated down. Manual only says
# elements "spill out of a TIPPED HIVE" (G409 intent). Nominal 0 = full spill. Retained elements
# sit on the down side of the pivot and are modelled as counter-weight (simple lever model):
# tip when eq(up) - eq(down) >= T0. They return upward on the next tip (and then help). See MODEL.md.
RETAINED_COUNTERWEIGHT = (0.0, 1.0, 1.0)
# ASSUMPTION: torque weight of a RETAINED element (applies while it is down AND after it rotates back up).
# 1 = full lever effect (nominal, simple physics); 0 = no torque either way (e.g. wedged near the pivot):
# retention then only locks up supply and scores 2 pts if its CELL is upward at the end.

# --- AUTO
AUTO_FIRST_VOLLEY_S = (3.0, 5.0, 8.0)   # ASSUMPTION: start (or phase start) -> preloads launched, no intake needed
AUTO_CYCLE_FACTOR = (1.0, 1.25, 1.6)    # ASSUMPTION: AUTO cycle time / TELEOP cycle time (path-planned intake is usually slower)
AUTO_PARK_TRAVEL_S = (2.5, 4.0, 7.0)    # ASSUMPTION: AUTO time reserved to reach LOADING ZONE (positions FIGURE-ONLY)
P_LEAVE = (0.95, 0.98, 1.0)             # ASSUMPTION: reliability of LEAVE (move off the perimeter wall, §10.5.4)
P_AUTO_PARK = (0.80, 0.90, 1.0)         # ASSUMPTION: reliability of AUTO PARK (at least partially in 23x11 in zone)

# --- TELEOP
TELEOP_PARK_TRAVEL_S = (2.5, 4.0, 7.0)  # ASSUMPTION: TELEOP time reserved to PARK
P_TELEOP_PARK = (0.85, 0.93, 1.0)       # ASSUMPTION: 2 ROBOTS + HUMAN NECTAR entry share one 23x11 in zone (G427.C)
DEFENSE_CYCLE_MULT = (1.0, 1.1, 1.4)    # ASSUMPTION: TELEOP cycle-time multiplier for traffic/defense (G402 protects AUTO)
CYCLE_Q = (0.0, 0.5, 1.0)               # ASSUMPTION: position inside each profile's cycle-time range (0 = fastest end)
HIT_Q = (0.0, 0.5, 1.0)                 # ASSUMPTION: position inside each profile's hit-rate range (0 = worst end)
NECTAR_HIT_FACTOR = (0.8, 0.9, 1.0)     # ASSUMPTION: hit rate on 3.6 in NECTAR relative to 2.8 in POLLEN (§9.8)
NECTAR_EXTRA_S = (0.0, 2.0, 5.0)        # ASSUMPTION: extra seconds for a cycle that loads NECTAR (LOADING ZONE / spill area trip)
POLLEN_SHARE = (12, 16, 24)             # ASSUMPTION: POLLEN this alliance can cycle. MANUAL §10.3.1: 16 preload + 16 FLOWER = 32 non-GARDEN, /2 = 16; low = opponent wins the floor, high = also raids the 8 GARDEN POLLEN

# --- FLOWER (only in the last 60 s for NECTAR per G410; POLLEN-before-1:00 is an open Q&A item, not modelled)
FLOWER_CAPACITY = (5, 6, 7)             # ASSUMPTION: elements at least partially in scoring volume (middle-ring height FIGURE-ONLY; 21.5 in top / 2.8 in balls)
FLOWER_STAGED_REMAIN = (0, 2, 3)        # ASSUMPTION: staged POLLEN still inside scoring volume at 1:00 (robots pull POLLEN from the bottom, G418.B)
FLOWERS_ACCESSIBLE = (2, 3, 4)          # ASSUMPTION: FLOWERS one alliance can realistically work (perimeter positions FIGURE-ONLY)
FLOWER_PRESTAGE_FRAC = (0.0, 0.5, 0.8)  # ASSUMPTION: share of the first FLOWER trip (gathering/driving) done before 1:00; placement is always after
P_FLOWER_STOLEN_OPEN = (0.0, 0.25, 0.6) # ASSUMPTION: opponent tops a not-full FLOWER with its NECTAR (ownership lost; §10.5.2)
P_FLOWER_STOLEN_FULL = (0.0, 0.05, 0.25)# ASSUMPTION: same for a full FLOWER (needs POLLEN pulled from bottom first, G418.B)
P_OPP_NECTAR_FIRST = (0.0, 0.2, 0.5)    # ASSUMPTION: opponent NECTAR already lowest in the FLOWER -> no Bottom NECTAR Bonus

# --- GARDEN
GARDEN_STAGED_REMAIN = (2, 4, 4)        # ASSUMPTION: of the 4 staged (MANUAL §10.3.1) how many are still in own GARDEN at end (not protected, §10.5.3)
P_GARDEN_STAYS = (0.6, 0.85, 1.0)       # ASSUMPTION: per delivered element, still at least partially in the 2 in strip at end

RANGE_NAMES = [
    'TIP_T0_EQ', 'FIRST_TIP_LAUNCHED_EQ', 'NECTAR_TIP_EQ', 'SPILL_RETAIN_FRAC', 'RETAINED_COUNTERWEIGHT',
    'AUTO_FIRST_VOLLEY_S', 'AUTO_CYCLE_FACTOR', 'AUTO_PARK_TRAVEL_S', 'P_LEAVE', 'P_AUTO_PARK',
    'TELEOP_PARK_TRAVEL_S', 'P_TELEOP_PARK', 'DEFENSE_CYCLE_MULT', 'CYCLE_Q', 'HIT_Q',
    'NECTAR_HIT_FACTOR', 'NECTAR_EXTRA_S', 'POLLEN_SHARE',
    'FLOWER_CAPACITY', 'FLOWER_STAGED_REMAIN', 'FLOWERS_ACCESSIBLE', 'FLOWER_PRESTAGE_FRAC',
    'P_FLOWER_STOLEN_OPEN', 'P_FLOWER_STOLEN_FULL', 'P_OPP_NECTAR_FIRST',
    'GARDEN_STAGED_REMAIN', 'P_GARDEN_STAYS',
]
INT_PARAMS = {'POLLEN_SHARE', 'FLOWER_CAPACITY', 'FLOWER_STAGED_REMAIN', 'FLOWERS_ACCESSIBLE', 'GARDEN_STAGED_REMAIN'}
PER_ROBOT_Q = {'CYCLE_Q', 'HIT_Q'}   # drawn per robot in Monte Carlo unless overridden


# =============================================================================
# Capability profiles (per robot). All ranges here are ASSUMPTION: they define the
# capability being evaluated ("what if our launcher cycles in 15-22 s"), not facts.
# cycle_s = TELEOP intake-of-up-to-capacity + drive + launch volley.
# =============================================================================
@dataclass(frozen=True)
class Robot:
    name: str
    leave: bool = True
    auto_park: bool = True
    teleop_park: bool = True
    launcher: bool = False
    cycle_s: tuple = (0, 0)
    hit: tuple = (0, 0)
    capacity: int = CAPACITY_MAX       # G407 bound
    nectar_ammo: bool = False          # launcher also fires own NECTAR (spilled / human-entered, G426)
    flower: bool = False               # switches to FLOWER placement for the last 60 s
    flower_trip_s: tuple = (0, 0)
    garden: bool = False               # delivers POLLEN to GARDEN when not otherwise busy
    garden_trip_s: tuple = (0, 0)


_MID = Robot('LAUNCH_MID', launcher=True, cycle_s=(15, 22), hit=(0.65, 0.90))
PROFILES = {r.name: r for r in [
    Robot('NOTHING', leave=False, auto_park=False, teleop_park=False),
    Robot('PARK_ONLY'),
    Robot('GARDEN', garden=True, garden_trip_s=(14, 24)),
    Robot('LAUNCH_SLOW', launcher=True, cycle_s=(24, 34), hit=(0.50, 0.80)),
    _MID,
    Robot('LAUNCH_FAST', launcher=True, cycle_s=(9, 14), hit=(0.80, 0.95)),
    replace(_MID, name='LAUNCH_MID_CAP3', capacity=3),
    replace(_MID, name='LAUNCH_MID_CAP2', capacity=2),
    replace(_MID, name='LAUNCH_MID_NO_AUTO_PARK', auto_park=False),
    replace(_MID, name='LAUNCH_MID_NO_PARKS', auto_park=False, teleop_park=False),
    replace(_MID, name='LAUNCH_MID_NECTAR', nectar_ammo=True),
    replace(_MID, name='LAUNCH_MID_FLOWER', flower=True, flower_trip_s=(12, 20)),
    Robot('FLOWER_GARDEN', garden=True, garden_trip_s=(14, 24), flower=True, flower_trip_s=(12, 20)),
    Robot('LAUNCH_FAST_ALL', launcher=True, cycle_s=(9, 14), hit=(0.80, 0.95), nectar_ammo=True,
          flower=True, flower_trip_s=(10, 16)),
]}

# (label, robot A, robot B, human player enters NECTAR per G426)
ALLIANCES = [
    ('park/leave only',            'PARK_ONLY', 'PARK_ONLY', True),
    ('garden + park',              'GARDEN', 'GARDEN', True),
    ('slow launcher x2',           'LAUNCH_SLOW', 'LAUNCH_SLOW', True),
    ('mid launcher x2',            'LAUNCH_MID', 'LAUNCH_MID', True),
    ('fast launcher x2',           'LAUNCH_FAST', 'LAUNCH_FAST', True),
    ('mid x2, no AUTO park',       'LAUNCH_MID_NO_AUTO_PARK', 'LAUNCH_MID_NO_AUTO_PARK', True),
    ('mid x2, never park',         'LAUNCH_MID_NO_PARKS', 'LAUNCH_MID_NO_PARKS', True),
    ('mid+NECTAR ammo x2',         'LAUNCH_MID_NECTAR', 'LAUNCH_MID_NECTAR', True),
    ('mid+NECTAR x2, no human',    'LAUNCH_MID_NECTAR', 'LAUNCH_MID_NECTAR', False),
    ('mid + mid/flower',           'LAUNCH_MID', 'LAUNCH_MID_FLOWER', True),
    ('mid/flower x2',              'LAUNCH_MID_FLOWER', 'LAUNCH_MID_FLOWER', True),
    ('mid + flower/garden',        'LAUNCH_MID', 'FLOWER_GARDEN', True),
    ('fast + park-only',           'LAUNCH_FAST', 'PARK_ONLY', True),
    ('fast-all x2',                'LAUNCH_FAST_ALL', 'LAUNCH_FAST_ALL', True),
]
REFERENCE_OPPONENT = ('LAUNCH_MID', 'LAUNCH_MID', True)   # for win-probability only


# =============================================================================
# Simulation
# =============================================================================
def sample_params(rng, mc, overrides=None):
    p = {}
    for name in RANGE_NAMES:
        lo, nom, hi = globals()[name]
        u = rng.random()                              # always consume -> common random numbers across overrides
        if name in PER_ROBOT_Q:
            p[name] = None if mc else nom
        elif not mc:
            p[name] = nom
        elif name in INT_PARAMS:
            p[name] = min(hi, lo + int(u * (hi - lo + 1)))
        else:
            p[name] = lo + u * (hi - lo)
    p.update(overrides or {})
    return p


class Match:
    """Shared alliance state: one HIVE, NECTAR pool, POLLEN budget, FLOWERS, GARDEN."""

    def __init__(self, p, rng, n_robots, human, has_flower_robot):
        self.p, self.rng, self.human = p, rng, human
        self.up = [(2, False)] * CELL_STAGED_NECTAR     # CELL = list of (kind, retained); kind 0 pollen, 1 nectar, 2 staged nectar
        self.down = []
        self.t0 = p['TIP_T0_EQ']
        self.staged_eq = (p['TIP_T0_EQ'] - p['FIRST_TIP_LAUNCHED_EQ']) / CELL_STAGED_NECTAR
        self.tips_auto = self.tips_teleop = 0
        self.area_nectar = AREA_NECTAR
        self.field_nectar = 0
        self.pollen_avail = p['POLLEN_SHARE'] - PRELOAD_POLLEN * n_robots
        self.garden_delivered = 0
        self.flowers = [0] * (p['FLOWERS_ACCESSIBLE'] if has_flower_robot else 0)
        self.last_minute_done = False
        self.max_load = 0
        self.flower_times, self.entries = [], []       # diagnostics for self-test (G410, G426)

    def eq(self, cell):                                # retained elements weigh CW both down (resisting) and back up (helping)
        base = (1.0, self.p['NECTAR_TIP_EQ'], self.staged_eq)
        return sum(base[k] * (self.p['RETAINED_COUNTERWEIGHT'] if ret else 1.0) for k, ret in cell)

    @staticmethod
    def counts(cell):
        return [sum(1 for k, _ in cell if k == kind) for kind in range(3)]

    def clock(self, t):                                # G426.B: all remaining NECTAR at 1:00
        if not self.last_minute_done and t >= AUTO_S + TELEOP_S - LAST_MINUTE_S:
            self.last_minute_done = True
            if self.human:
                self.entries += [(t, 'B')] * self.area_nectar
                self.field_nectar += self.area_nectar
                self.area_nectar = 0

    def add_to_cell(self, kind, t):
        self.up.append((kind, False))
        if self.eq(self.up) - self.eq(self.down) >= self.t0 - 1e-9:
            self.tip(t)

    def tip(self, t):
        if t <= AUTO_S:
            self.tips_auto += 1                        # §10.5.B: TIPS complete before TELEOP count as AUTO
        else:
            self.tips_teleop += 1
        kept = []
        for k, _ in self.up:
            if self.rng.random() < self.p['SPILL_RETAIN_FRAC']:
                kept.append((k, True))
            elif k == 0:
                self.pollen_avail += 1
            else:
                self.field_nectar += 1
        self.up, self.down = self.down, kept
        if self.human and self.area_nectar > 0:        # G426.A: one NECTAR per own-HIVE TIP
            self.area_nectar -= 1
            self.field_nectar += 1
            self.entries.append((t, 'A'))

    def nectar_reserve(self):
        need = sum(1 for f in self.flowers if f == 0)
        return max(0, need - (self.area_nectar if self.human else 0))

    def take(self, t, want_nectar, want_total):
        self.clock(t)
        n = max(0, min(want_nectar, self.field_nectar - self.nectar_reserve()))
        self.field_nectar -= n
        pl = max(0, min(want_total - n, self.pollen_avail))
        self.pollen_avail -= pl
        return n, pl

    def give_back(self, n, pl):
        self.field_nectar += n
        self.pollen_avail += pl

    def volley(self, t, n, pl, hit):
        self.clock(t)
        self.max_load = max(self.max_load, n + pl)
        for kind, count, h in ((1, n, hit * self.p['NECTAR_HIT_FACTOR']), (0, pl, hit)):
            for _ in range(count):
                if self.rng.random() < h:
                    self.add_to_cell(kind, t)          # elements after a TIP land in the new upward CELL
                elif kind:
                    self.field_nectar += 1             # misses stay on the field, recoverable
                else:
                    self.pollen_avail += 1


def launch_phase(m, r, rs, t, end, cyc):
    while True:
        if rs['held']:
            n, pl, dur = 0, rs['held'], m.p['AUTO_FIRST_VOLLEY_S']
            rs['held'] = 0
            held = True
        else:
            n, pl = m.take(t, r.capacity if r.nectar_ammo else 0, r.capacity)
            dur = cyc + (m.p['NECTAR_EXTRA_S'] if n else 0.0)
            held = False
        if n + pl == 0:                                # nothing to pick up: wait for spills/misses
            if t + 2.0 > end:
                return t
            t += 2.0
            yield t
            continue
        if t + dur > end:
            if held:
                rs['held'] = pl
            else:
                m.give_back(n, pl)
            return t
        t += dur
        yield t
        m.volley(t, n, pl, rs['hit'])


def garden_phase(m, r, rs, t, end, dur):
    while True:
        held = rs['held'] > 0
        if held:
            k, rs['held'] = rs['held'], 0
        else:
            k = m.take(t, 0, r.capacity)[1]
        if k == 0:
            if t + 2.0 > end:
                return t
            t += 2.0
            yield t
            continue
        if t + dur > end:
            if held:
                rs['held'] = k
            else:
                m.give_back(0, k)
            return t
        t += dur
        yield t
        m.garden_delivered += k


def flower_phase(m, r, rs, t, end, dur):
    s, cap = m.p['FLOWER_STAGED_REMAIN'], m.p['FLOWER_CAPACITY']
    m.clock(AUTO_S + TELEOP_S - LAST_MINUTE_S)          # human NECTAR is in the zone by the time we collect it
    while t + dur <= end:
        fresh = [i for i, f in enumerate(m.flowers) if f == 0]
        roomy = [i for i, f in enumerate(m.flowers) if s + f < cap]
        i = fresh[0] if fresh else (min(roomy, key=lambda j: m.flowers[j]) if roomy else None)
        if i is None or m.field_nectar < 1:
            return t
        k = min(r.capacity, max(1, cap - s - m.flowers[i]))
        m.field_nectar -= 1                              # NECTAR placed last = top-most = ownership
        pl = max(0, min(k - 1, m.pollen_avail))
        m.pollen_avail -= pl
        m.flowers[i] += 1 + pl                           # claim now so the partner picks another FLOWER
        t += dur
        yield t
        m.flower_times.append(t)
    return t


def robot_proc(m, r, rs):
    p = m.p
    t = 0.0
    # ---------------- AUTO ----------------
    auto_end = AUTO_S - (p['AUTO_PARK_TRAVEL_S'] if r.auto_park else 0.0)
    if r.launcher:
        t = yield from launch_phase(m, r, rs, t, auto_end, rs['cyc'] * p['AUTO_CYCLE_FACTOR'])
    elif r.garden:
        t = yield from garden_phase(m, r, rs, t, auto_end, rs['gtrip'] * p['AUTO_CYCLE_FACTOR'])
    # ---------------- TELEOP ----------------
    t = float(AUTO_S)
    d = p['DEFENSE_CYCLE_MULT']
    end = AUTO_S + TELEOP_S - (p['TELEOP_PARK_TRAVEL_S'] if r.teleop_park else 0.0)
    lm = AUTO_S + TELEOP_S - LAST_MINUTE_S
    fdur = rs['ftrip'] * d
    first_end = lm - p['FLOWER_PRESTAGE_FRAC'] * fdur if r.flower else end
    if r.launcher:
        t = yield from launch_phase(m, r, rs, t, first_end, rs['cyc'] * d)
    elif r.garden:
        t = yield from garden_phase(m, r, rs, t, first_end, rs['gtrip'] * d)
    if r.flower:
        t = yield from flower_phase(m, r, rs, max(t, first_end), end, fdur)
        if r.launcher:                                   # FLOWERS done or out of NECTAR: back to launching
            t = yield from launch_phase(m, r, rs, t, end, rs['cyc'] * d)


def simulate(alliance, p, rng, human=True):
    m = Match(p, rng, len(alliance), human, any(r.flower for r in alliance))
    heap = []
    for i, r in enumerate(alliance):
        u_c, u_h, u_f, u_g = rng.random(), rng.random(), rng.random(), rng.random()
        qc = p['CYCLE_Q'] if p['CYCLE_Q'] is not None else u_c
        qh = p['HIT_Q'] if p['HIT_Q'] is not None else u_h
        rs = {'cyc': r.cycle_s[0] + qc * (r.cycle_s[1] - r.cycle_s[0]),
              'hit': r.hit[0] + qh * (r.hit[1] - r.hit[0]),
              'ftrip': r.flower_trip_s[0] + (qc if p['CYCLE_Q'] is not None else u_f) * (r.flower_trip_s[1] - r.flower_trip_s[0]),
              'gtrip': r.garden_trip_s[0] + (qc if p['CYCLE_Q'] is not None else u_g) * (r.garden_trip_s[1] - r.garden_trip_s[0]),
              'held': PRELOAD_POLLEN if (r.launcher or r.garden) else 0}
        g = robot_proc(m, r, rs)
        try:
            heapq.heappush(heap, (next(g), i, g))
        except StopIteration:
            pass
    while heap:                                          # resume robots in time order
        _, i, g = heapq.heappop(heap)
        try:
            heapq.heappush(heap, (next(g), i, g))
        except StopIteration:
            pass

    leave = sum(PTS_LEAVE for r in alliance if r.leave and rng.random() < p['P_LEAVE'])
    apark = sum(PTS_PARK_AUTO for r in alliance if r.auto_park and rng.random() < p['P_AUTO_PARK'])
    tpark = sum(PTS_PARK_TELEOP for r in alliance if r.teleop_park and rng.random() < p['P_TELEOP_PARK'])
    tips = m.tips_auto + m.tips_teleop
    cell = PTS_CELL_ELEMENT * len(m.up)
    garden = PTS_GARDEN_ELEMENT * (p['GARDEN_STAGED_REMAIN']
                                   + sum(rng.random() < p['P_GARDEN_STAYS'] for _ in range(m.garden_delivered)))
    s, cap, flower = p['FLOWER_STAGED_REMAIN'], p['FLOWER_CAPACITY'], 0
    for placed in m.flowers:
        if placed:
            full = s + placed >= cap
            owned = rng.random() >= (p['P_FLOWER_STOLEN_FULL'] if full else p['P_FLOWER_STOLEN_OPEN'])
            bonus = rng.random() >= p['P_OPP_NECTAR_FIRST']
            flower += PTS_BOTTOM_NECTAR * bonus + PTS_FLOWER_ELEMENT * min(cap, s + placed) * owned
    auto = leave + apark + PTS_TIP * m.tips_auto
    teleop = tpark + PTS_TIP * m.tips_teleop + cell + garden + flower
    lp = leave + apark + tpark
    swarm, poll1, poll2 = lp >= SWARM_RP_THRESHOLD, tips >= POLLINATOR1_TIPS, tips >= POLLINATOR2_TIPS
    return {'total': auto + teleop, 'auto': auto, 'teleop': teleop, 'leavepark': lp, 'tips': tips,
            'tips_auto': m.tips_auto, 'cell': cell, 'garden': garden, 'flower': flower,
            'swarm': swarm, 'poll1': poll1, 'poll2': poll2,
            'bonus_rp': RP_SWARM * swarm + RP_POLL1 * poll1 + RP_POLL2 * poll2,
            'max_load': m.max_load, 'flower_times': m.flower_times, 'entries': m.entries}


def run(names, n, seed, mc=True, overrides=None, human=True):
    rng = random.Random(seed)
    alliance = [PROFILES[x] for x in names]
    return [simulate(alliance, sample_params(rng, mc, overrides), rng, human) for _ in range(n)]


# =============================================================================
# Reporting
# =============================================================================
def mean(xs, key):
    return statistics.fmean(float(x[key]) for x in xs)


def pct(xs, key, f):
    v = sorted(x[key] for x in xs)
    return v[min(len(v) - 1, int(f * len(v)))]


def win_stats(ours, theirs):
    w = statistics.fmean(a['total'] > b['total'] for a, b in zip(ours, theirs))
    tie = statistics.fmean(a['total'] == b['total'] for a, b in zip(ours, theirs))
    return w, tie


def rate_table():
    nom = {k: globals()[k][1] for k in RANGE_NAMES}
    d, t0, v = nom['DEFENSE_CYCLE_MULT'], nom['TIP_T0_EQ'], PTS_TIP / nom['TIP_T0_EQ']
    mid_c, mid_h = sum(_MID.cycle_s) / 2, sum(_MID.hit) / 2
    fast = PROFILES['LAUNCH_FAST']
    fast_c, fast_h = sum(fast.cycle_s) / 2, sum(fast.hit) / 2
    C, s = nom['FLOWER_CAPACITY'], nom['FLOWER_STAGED_REMAIN']
    k = min(CAPACITY_MAX, C - s)
    full = s + k >= C
    p_own = 1 - (nom['P_FLOWER_STOLEN_FULL'] if full else nom['P_FLOWER_STOLEN_OPEN'])
    flower_first = PTS_BOTTOM_NECTAR * (1 - nom['P_OPP_NECTAR_FIRST']) + PTS_FLOWER_ELEMENT * min(C, s + k) * p_own
    ftrip = 16 * d
    rows = [
        ('TELEOP PARK (travel only)', PTS_PARK_TELEOP, nom['TELEOP_PARK_TRAVEL_S']),
        ('FLOWER, first trip to a fresh FLOWER (mid trip)', flower_first, ftrip),
        ('Launch 4 NECTAR, mid launcher (tip value only)',
         4 * mid_h * nom['NECTAR_HIT_FACTOR'] * nom['NECTAR_TIP_EQ'] * v, mid_c * d + nom['NECTAR_EXTRA_S']),
        ('Launch 4 POLLEN, fast launcher (tip value only)', 4 * fast_h * v, fast_c * d),
        ('Launch 4 POLLEN, mid launcher (tip value only)', 4 * mid_h * v, mid_c * d),
        ('Launch 4 POLLEN, mid, end-of-match CELL value only', 4 * mid_h * PTS_CELL_ELEMENT, mid_c * d),
        ('GARDEN 4 POLLEN (mid trip)', 4 * nom['P_GARDEN_STAYS'] * PTS_GARDEN_ELEMENT, 19 * d),
    ]
    print('\n## 1. Nominal points per robot-second (analytic, no RP, no interaction)\n')
    print(f'Tip value per in-CELL eq = {PTS_TIP}/{t0} = {v:.2f} pts (long-run, ignores end-of-match partial fill)\n')
    print('| action | pts | seconds | pts/s |')
    print('|---|---:|---:|---:|')
    for name, pts, sec in rows:
        print(f'| {name} | {pts:.1f} | {sec:.1f} | {pts / sec:.2f} |')


def alliance_table(n, seed):
    opp = run(REFERENCE_OPPONENT[:2], n, seed + 999, human=REFERENCE_OPPONENT[2])
    print(f'\n## 2. Alliance results (Monte Carlo, {n} matches each, all ASSUMPTION ranges drawn uniformly)\n')
    print('Win% / E[RP] vs reference opponent = mid launcher x2 (independent draws; no interaction modelled).\n')
    print('| alliance | mean | p10 | p90 | AUTO | TELEOP | tips | P(SWARM) | P(POLL1) | P(POLL2) | E[bonus RP] | win% | E[RP] |')
    print('|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|')
    for label, a, b, human in ALLIANCES:
        res = run((a, b), n, seed, human=human)
        w, tie = win_stats(res, opp)
        brp = mean(res, 'bonus_rp')
        print(f"| {label} | {mean(res, 'total'):.0f} | {pct(res, 'total', .1)} | {pct(res, 'total', .9)} | "
              f"{mean(res, 'auto'):.0f} | {mean(res, 'teleop'):.0f} | {mean(res, 'tips'):.1f} | "
              f"{mean(res, 'swarm'):.2f} | {mean(res, 'poll1'):.2f} | {mean(res, 'poll2'):.2f} | {brp:.2f} | "
              f"{100 * w:.0f} | {brp + RP_WIN * w + RP_TIE * tie:.2f} |")


def capacity_table(n, seed):
    print(f'\n## 3. Capacity per cycle (G407 caps at {CAPACITY_MAX}); mid launcher x2, Monte Carlo {n}\n')
    print('| capacity | mean pts | tips | P(POLL1) | P(POLL2) |')
    print('|---:|---:|---:|---:|---:|')
    for name in ('LAUNCH_MID_CAP2', 'LAUNCH_MID_CAP3', 'LAUNCH_MID'):
        res = run((name, name), n, seed)
        print(f"| {PROFILES[name].capacity} | {mean(res, 'total'):.0f} | {mean(res, 'tips'):.1f} | "
              f"{mean(res, 'poll1'):.2f} | {mean(res, 'poll2'):.2f} |")


def hive_tables(n, seed):
    cfgs = [('mid x2', ('LAUNCH_MID', 'LAUNCH_MID')), ('fast x2', ('LAUNCH_FAST', 'LAUNCH_FAST')),
            ('mid+NECTAR x2', ('LAUNCH_MID_NECTAR', 'LAUNCH_MID_NECTAR'))]
    print(f'\n## 4. HIVE spill alternatives (other params Monte Carlo, {n} matches; SPILL_RETAIN_FRAC fixed)\n')
    print('| alliance | retain | counter-weight | tips | CELL pts at end | P(POLL1) | P(POLL2) | mean pts |')
    print('|---|---:|---:|---:|---:|---:|---:|---:|')
    for label, names in cfgs:
        for r, cw in ((0.0, 1.0), (0.3, 1.0), (0.3, 0.0), (0.6, 1.0), (0.6, 0.0)):
            res = run(names, n, seed, overrides={'SPILL_RETAIN_FRAC': r, 'RETAINED_COUNTERWEIGHT': cw})
            print(f"| {label} | {r:.1f} | {cw:.0f} | {mean(res, 'tips'):.1f} | {mean(res, 'cell'):.1f} | "
                  f"{mean(res, 'poll1'):.2f} | {mean(res, 'poll2'):.2f} | {mean(res, 'total'):.0f} |")
    print(f'\n## 5. Tip threshold (empty-CELL eq) sweep (other params Monte Carlo, {n})\n')
    print('| alliance | T0 | tips | P(POLL1) | P(POLL2) | mean pts |')
    print('|---|---:|---:|---:|---:|---:|')
    for label, names in cfgs:
        for t0 in (6.5, 7.5, 8.5, 9.0):
            res = run(names, n, seed, overrides={'TIP_T0_EQ': t0})
            print(f"| {label} | {t0} | {mean(res, 'tips'):.1f} | {mean(res, 'poll1'):.2f} | "
                  f"{mean(res, 'poll2'):.2f} | {mean(res, 'total'):.0f} |")


def tornado(n, seed):
    cfg = {'ref': ('LAUNCH_MID', 'LAUNCH_MID_FLOWER'), 'mid': ('LAUNCH_MID', 'LAUNCH_MID'),
           'nectar': ('LAUNCH_MID_NECTAR', 'LAUNCH_MID_NECTAR')}

    def stats(ov):
        r = {k: run(v, n, seed, overrides=ov) for k, v in cfg.items()}
        pts = {k: mean(v, 'total') for k, v in r.items()}
        rp = {k: mean(v, 'bonus_rp') for k, v in r.items()}
        return (pts['ref'], rp['ref'], pts['ref'] - pts['mid'], rp['ref'] - rp['mid'],
                pts['nectar'] - pts['mid'], rp['nectar'] - rp['mid'])

    base = stats(None)
    rows = [(name, globals()[name][0], globals()[name][2],
             stats({name: globals()[name][0]}), stats({name: globals()[name][2]})) for name in RANGE_NAMES]
    print('\n## 6. Sensitivity (tornado)\n')
    print(f'Each row pins one parameter at its low / high end while every other parameter is still drawn '
          f'Monte Carlo ({n} matches, common seed). Swings under ~3 pts / ~0.05 RP are within noise.\n')
    print(f'### 6a. Reference alliance mid launcher + mid launcher/flower (baseline {base[0]:.0f} pts, '
          f'{base[1]:.2f} bonus RP), ranked by points swing\n')
    print('| parameter | low -> high | pts @low | pts @high | swing | bonus RP @low | @high | RP swing |')
    print('|---|---|---:|---:|---:|---:|---:|---:|')
    for name, lo, hi, a, b in sorted(rows, key=lambda x: -abs(x[4][0] - x[3][0])):
        print(f'| {name} | {lo} -> {hi} | {a[0]:.0f} | {b[0]:.0f} | {b[0] - a[0]:+.0f} | {a[1]:.2f} | {b[1]:.2f} | {b[1] - a[1]:+.2f} |')
    for title, i, bl in (('6b. Last-minute FLOWER play: (mid + mid/flower) minus (mid x2)', 2, base[2:4]),
                         ('6c. NECTAR as launcher ammo: (mid+NECTAR x2) minus (mid x2)', 4, base[4:6])):
        print(f'\n### {title}. Baseline delta {bl[0]:+.1f} pts, {bl[1]:+.2f} bonus RP. '
              'Positive = capability helps. Top 10 by points swing.\n')
        print('| parameter | low -> high | delta pts @low | @high | delta RP @low | @high |')
        print('|---|---|---:|---:|---:|---:|')
        for name, lo, hi, a, b in sorted(rows, key=lambda x: -abs(x[4][i] - x[3][i]))[:10]:
            print(f'| {name} | {lo} -> {hi} | {a[i]:+.1f} | {b[i]:+.1f} | {a[i + 1]:+.2f} | {b[i + 1]:+.2f} |')


def report(n, seed):
    print('# BIOBUZZ 2026-27 quant model output -- DRAFT, §19 step 4, PROVISIONAL (revise after first events)')
    print(f'seed={seed}  matches/config={n}')
    rate_table()
    alliance_table(n, seed)
    capacity_table(n, seed)
    hive_tables(n // 2, seed)
    tornado(n // 2, seed)


# =============================================================================
# Self-test
# =============================================================================
def self_test():
    g = globals()
    certain = {'P_LEAVE': 1.0, 'P_AUTO_PARK': 1.0, 'P_TELEOP_PARK': 1.0, 'GARDEN_STAGED_REMAIN': GARDEN_STAGED_POLLEN}

    # 1. park/leave-only alliance: exactly 2*(3+5+5) = 26 LEAVE+PARK, plus MANUAL staging gifts
    for res in run(('PARK_ONLY', 'PARK_ONLY'), 50, 1, mc=True, overrides=certain):
        assert res['leavepark'] == 2 * (PTS_LEAVE + PTS_PARK_AUTO + PTS_PARK_TELEOP) == 26, res
        assert res['total'] == 26 + PTS_CELL_ELEMENT * CELL_STAGED_NECTAR + PTS_GARDEN_ELEMENT * GARDEN_STAGED_POLLEN, res
        assert res['auto'] == 2 * (PTS_LEAVE + PTS_PARK_AUTO) and res['tips'] == 0
        assert res['swarm'] and res['bonus_rp'] == RP_SWARM
    # 2. one robot alone cannot reach SWARM (13 < 16)
    for res in run(('PARK_ONLY', 'NOTHING'), 20, 2, overrides=certain):
        assert res['leavepark'] == 13 and not res['swarm']

    # 3. RP thresholds are read from the constants at call time
    saved = (g['SWARM_RP_THRESHOLD'], g['POLLINATOR1_TIPS'], g['POLLINATOR2_TIPS'])
    try:
        g['SWARM_RP_THRESHOLD'] = 27
        assert not run(('PARK_ONLY', 'PARK_ONLY'), 5, 3, overrides=certain)[0]['swarm']
        g['SWARM_RP_THRESHOLD'], g['POLLINATOR1_TIPS'], g['POLLINATOR2_TIPS'] = 26, 0, 0
        r = run(('PARK_ONLY', 'PARK_ONLY'), 5, 3, overrides=certain)[0]
        assert r['swarm'] and r['poll1'] and r['poll2'] and r['bonus_rp'] == 3
    finally:
        g['SWARM_RP_THRESHOLD'], g['POLLINATOR1_TIPS'], g['POLLINATOR2_TIPS'] = saved

    # 4. HIVE tip accounting against the SETUP-GUIDE calibration (nominal thresholds)
    p = sample_params(random.Random(0), mc=False)
    m = Match(p, random.Random(0), 2, True, False)
    for i in range(1, 4):                                 # staged 3 NECTAR: 3rd POLLEN tips
        m.add_to_cell(0, 10.0)
        assert m.tips_auto == (1 if i == 3 else 0), i
    assert m.up == [] and m.down == [] and m.field_nectar == 3 + 1 and m.area_nectar == 4
    for i in range(1, 9):                                 # empty CELL: 8th POLLEN tips
        m.add_to_cell(0, 50.0)
        assert m.tips_teleop == (1 if i == 8 else 0), i
    for i in range(1, 6):                                 # 5 launched NECTAR * 1.5 eq = 7.5 -> tips on 5th
        m.add_to_cell(1, 60.0)
        assert m.tips_teleop == (2 if i == 5 else 1), i
    assert m.area_nectar == 2 and len(m.entries) == 3
    p_keep = dict(p, SPILL_RETAIN_FRAC=1.0)               # everything retained -> counter-weight
    m = Match(p_keep, random.Random(0), 2, True, False)
    for _ in range(3):
        m.add_to_cell(0, 10.0)
    assert m.tips_auto == 1 and m.counts(m.down) == [3, 0, 3] and abs(m.eq(m.down) - (3 + (7.5 - 2.5))) < 1e-9
    for i in range(1, 17):                                # needs eq(up) - 8 >= 7.5 -> 16 POLLEN
        m.add_to_cell(0, 50.0)
        assert m.tips_teleop == (1 if i == 16 else 0), i
    assert m.counts(m.up) == [3, 0, 3]                    # retained elements come back up
    m = Match(dict(p_keep, RETAINED_COUNTERWEIGHT=0.0), random.Random(0), 2, True, False)
    for _ in range(3):
        m.add_to_cell(0, 10.0)
    for i in range(1, 9):                                 # no counter-weight: empty CELL tips on 8th again
        m.add_to_cell(0, 50.0)
        assert m.tips_teleop == (1 if i == 8 else 0), i
    assert m.counts(m.up) == [3, 0, 3] and m.eq(m.up) == 0  # ...and the returning retained elements do not help

    # 5. Monte Carlo invariants on every profile pair
    for label, a, b, human in ALLIANCES:
        rs = run((a, b), 150, 7, human=human)
        for r in rs:
            for k in ('total', 'auto', 'teleop', 'leavepark', 'tips', 'cell', 'garden', 'flower'):
                assert r[k] >= 0, (label, k, r[k])
            assert r['total'] == r['auto'] + r['teleop']
            assert r['max_load'] <= CAPACITY_MAX, (label, r['max_load'])                  # G407
            assert all(t > AUTO_S + TELEOP_S - LAST_MINUTE_S for t in r['flower_times'])   # G410
            assert len(r['entries']) <= AREA_NECTAR                                        # G426
            assert sum(1 for _, why in r['entries'] if why == 'A') <= r['tips']           # G426.A
            assert human or not r['entries']
            assert r['poll1'] or not r['poll2']
            assert r['auto'] <= 2 * (PTS_LEAVE + PTS_PARK_AUTO) + PTS_TIP * r['tips_auto']
    assert all(pr.capacity <= CAPACITY_MAX for pr in PROFILES.values())
    assert all(g[n][0] <= g[n][1] <= g[n][2] for n in RANGE_NAMES)
    # MANUAL §10.3.1 staging adds up, and ASSUMPTION ranges stay inside it
    assert POLLEN_TOTAL == FLOWER_COUNT * FLOWER_STAGED_POLLEN + 2 * GARDEN_STAGED_POLLEN + 4 * PRELOAD_POLLEN
    assert POLLEN_SHARE[1] == (FLOWER_COUNT * FLOWER_STAGED_POLLEN + 4 * PRELOAD_POLLEN) // 2
    assert FLOWER_STAGED_REMAIN[2] <= FLOWER_STAGED_POLLEN and FLOWERS_ACCESSIBLE[2] <= FLOWER_COUNT
    assert GARDEN_STAGED_REMAIN[2] <= GARDEN_STAGED_POLLEN and CELL_STAGED_NECTAR + AREA_NECTAR == 8

    # 6. determinism
    x = [r['total'] for r in run(('LAUNCH_FAST_ALL', 'LAUNCH_MID'), 100, 11)]
    y = [r['total'] for r in run(('LAUNCH_FAST_ALL', 'LAUNCH_MID'), 100, 11)]
    assert x == y
    # 7. launchers actually tip; faster launchers tip more (sanity, not a proof)
    slow, fast = run(('LAUNCH_SLOW',) * 2, 300, 5), run(('LAUNCH_FAST',) * 2, 300, 5)
    assert mean(fast, 'tips') > mean(slow, 'tips') > 0
    print('self-test OK: 7 groups of invariants passed')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--self-test', action='store_true')
    ap.add_argument('--n', type=int, default=2000, help='Monte Carlo matches per alliance config')
    ap.add_argument('--seed', type=int, default=20260912)
    args = ap.parse_args()
    if args.self_test:
        self_test()
        sys.exit(0)
    report(args.n, args.seed)
