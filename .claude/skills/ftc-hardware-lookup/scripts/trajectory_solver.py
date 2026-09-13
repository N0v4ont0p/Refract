#!/usr/bin/env python3
"""
Deterministic trajectory + launch-angle solver, per season and scoring element (§9; Phase-1; team 24089).

  --season <slug> (default season-extensions/ACTIVE)  --element <name> (file stem in physics/<season>/)
  No-drag angle needs only gravity (season-invariant, physics/invariants.json). The drag-aware angle
  needs the element's diameter/mass/drag — if physics/<season>/<element>.json doesn't exist it
  ABSTAINS (null + reason) instead of borrowing another season's ball: DECODE's constants model a 5 in
  hollow 75 g Artifact; BIOBUZZ launches ~2.8 in POLLEN / ~3.6 in NECTAR whose mass the manual does
  not state.

This is the WORKING artifact of the shooter-finding's PHYSICS counterexample leg. Team 24089
(Iron Lions) took the physics route (proj_motion.py) rather than an empirical table — but their
launch-angle solver (proj_motion.py:39) is broken WIP and their gravity constant was wrong.
Per Phase-1 this script:
  * CONSUMES structured constants from references/physics/decode-2025-26/artifact.json, with
    gravity CORRECTED at the source (385 -> 386.4 in/s^2) — G below is read FROM that file, not
    hardcoded, so the correction is wired in, not just noted.
  * Provides a CORRECT closed-form launch-angle solver (replacing the broken proj_motion.py:39).
  * Provides a deterministic, headless, drag-aware forward simulation (corrected from 24089's
    pygame loop), and a shooting-method drag-aware angle solve seeded by the closed form.

Deterministic-first (operating rule 1): the model reads these numbers; it never generates them.
"""
import json, math, os

HERE = os.path.dirname(os.path.abspath(__file__))
PHYS = os.path.join(HERE, "..", "references", "physics")
G = json.load(open(os.path.join(PHYS, "invariants.json")))["gravity_in_s2"]   # 386.4 in/s^2, read FROM data
CONST = None  # element constants, set by load_element()


def active_season():
    d = HERE
    while True:
        for cand in (os.path.join(d, "season-extensions", "ACTIVE"),
                     os.path.join(d, "ftc-shared-foundation", "season-extensions", "ACTIVE")):
            if os.path.isfile(cand):
                return open(cand).read().strip()
        if os.path.dirname(d) == d:
            return None
        d = os.path.dirname(d)


def load_element(season, element=None):
    """Returns (path, reason). Sets CONST when an element constants file exists for the season."""
    global CONST
    sdir = os.path.join(PHYS, season or "")
    have = sorted(f[:-5] for f in os.listdir(sdir) if f.endswith(".json")) if season and os.path.isdir(sdir) else []
    if element is None and len(have) == 1:
        element = have[0]
    if element is None or element not in have:
        return None, (f"no ballistics constants for element {element!r} in season {season!r} (have: {have}) — "
                      f"drag-aware angle withheld; measure the element's mass/diameter and add physics/{season}/<element>.json")
    path = os.path.join(sdir, element + ".json")
    CONST = json.load(open(path))
    return path, None


def solve_launch_angle(d, h, v0, high_arc=False):
    """Correct closed-form NO-DRAG launch angle. Replaces the broken 24089 proj_motion.py:39.
    d  = horizontal distance to target (in)
    h  = target height ABOVE launch point (in)
    v0 = launch speed (in/s)
    Returns launch angle in radians (measured up from horizontal), or None if the target is
    unreachable at this speed. Derivation:
        h = d*tan(t) - (g d^2)/(2 v0^2)*(1 + tan^2 t)
        => K*tan^2(t) - d*tan(t) + (K + h) = 0,  K = g d^2 / (2 v0^2)
        => tan(t) = [d +/- sqrt(d^2 - 4 K (K + h))] / (2 K)
    Two real roots = the low and high arc that both hit (d, h)."""
    if v0 <= 0 or d <= 0:
        return None
    K = G * d * d / (2.0 * v0 * v0)
    disc = d * d - 4.0 * K * (K + h)
    if disc < 0:
        return None  # unreachable at this speed — need a higher v0
    root = math.sqrt(disc)
    tan_theta = (d + root) / (2.0 * K) if high_arc else (d - root) / (2.0 * K)
    return math.atan(tan_theta)


def simulate(v0, angle_rad, max_t=5.0):
    """Deterministic drag-aware forward sim (headless; corrected from 24089's pygame loop).
    Coordinates: x forward, y UP from the launch point. Returns [(t, x, y), ...] until the
    projectile falls back below launch height (y < 0)."""
    dt = CONST["sim"]["dt_s"]
    m = CONST["ball"]["mass_slug"]
    rho = CONST["air"]["density_slug_in3"]
    Cd = CONST["drag"]["Cd"]
    D = CONST["ball"]["diameter_in"]
    A = CONST["drag"]["effective_area_factor"] * math.pi * (D / 2.0) ** 2
    vx = v0 * math.cos(angle_rad)
    vy = v0 * math.sin(angle_rad)
    x = y = t = 0.0
    out = [(0.0, 0.0, 0.0)]
    while t < max_t:
        v = math.hypot(vx, vy)
        if v > 0:
            Fd = 0.5 * Cd * rho * A * v * v
            ax = -(Fd / m) * (vx / v)
            ay = -G - (Fd / m) * (vy / v)   # gravity DOWN (y up)
        else:
            ax, ay = 0.0, -G
        vx += ax * dt; vy += ay * dt
        x += vx * dt; y += vy * dt; t += dt
        out.append((t, x, y))
        if y < 0 and t > dt:
            break
    return out


def _height_at_distance(traj, d):
    for i in range(1, len(traj)):
        x0, x1 = traj[i - 1][1], traj[i][1]
        if x0 <= d <= x1 and x1 != x0:
            y0, y1 = traj[i - 1][2], traj[i][2]
            return y0 + (y1 - y0) * ((d - x0) / (x1 - x0))
    return None  # never reached distance d


def solve_with_drag(d, h, v0, high_arc=False, tol=0.5):
    """Drag-aware launch angle via a ROBUST full-range scan for crossings of the target height.

    Why not a seeded bisection: range-vs-angle is only monotonic BELOW 45 deg. DECODE's close-range
    shots are steep (hood angles 58-60 deg are recommended for near shots), so the high-arc branch is
    a real operating regime, not a curiosity — and a bracket seeded around a >45 deg angle wanders
    past vertical and returns garbage (the observed 106 deg bug). Instead scan the full PHYSICAL angle
    range [1 deg, 89 deg], find every angle where the drag trajectory's height at distance d crosses
    the target height h, refine each crossing locally. The first crossing is the low arc, the last is
    the high arc. If none is found, ABSTAIN (return None) rather than emit an unvalidated angle."""
    lo_deg, hi_deg, step = 1.0, 89.0, 0.5
    n = int((hi_deg - lo_deg) / step)
    crossings = []
    prev_a = prev_e = None
    for i in range(n + 1):
        a = math.radians(lo_deg + i * step)
        hy = _height_at_distance(simulate(v0, a), d)
        if hy is None:                       # didn't reach distance d at this angle
            prev_a = prev_e = None
            continue
        e = hy - h
        if prev_e is not None and (e == 0.0 or (e < 0) != (prev_e < 0)):
            # sign change between prev_a and a -> a crossing lies in the bracket; bisect it
            blo, bhi, elo = prev_a, a, prev_e
            mid = (blo + bhi) / 2.0
            for _ in range(40):
                mid = (blo + bhi) / 2.0
                hm = _height_at_distance(simulate(v0, mid), d)
                if hm is None:
                    blo = mid
                    continue
                if abs(hm - h) < tol:
                    break
                if (hm - h < 0) == (elo < 0):
                    blo = mid
                else:
                    bhi = mid
            # only accept a validated crossing
            hv = _height_at_distance(simulate(v0, mid), d)
            if hv is not None and abs(hv - h) < max(tol, 1.0):
                crossings.append(mid)
        prev_a, prev_e = a, e
    if not crossings:
        return None
    return crossings[-1] if high_arc else crossings[0]


def _demo():
    load_element("decode-2025-26", "artifact")
    print(f"gravity consumed by solver: {G} in/s^2  (corrected from 24089's 385.0); demo element: DECODE artifact")
    print(f"{'d(in)':>6} {'h(in)':>6} {'v0':>5} | {'no-drag':>9} {'drag-aware':>11}")
    # mix of reachable and out-of-range cases (out-of-range correctly reports 'unreach' —
    # where 24089's broken solver would crash). max level range = v0^2/g.
    for d, h, v0 in [(80, 24, 210), (120, 0, 400), (150, 24, 500), (100, 36, 350), (120, 0, 210)]:
        a = solve_launch_angle(d, h, v0)
        ad = solve_with_drag(d, h, v0)
        sa = "unreach" if a is None else f"{math.degrees(a):.2f}°"
        sad = "unreach" if ad is None else f"{math.degrees(ad):.2f}°"
        print(f"{d:>6} {h:>6} {v0:>5} | {sa:>9} {sad:>11}")


if __name__ == "__main__":
    import argparse, sys
    ap = argparse.ArgumentParser(
        description="Deterministic launch-angle solver. Model calls this; it never computes the angle itself.")
    ap.add_argument("--season", help="season slug (default: season-extensions/ACTIVE)")
    ap.add_argument("--element", help="scoring element constants file stem, e.g. artifact")
    ap.add_argument("-d", "--distance", type=float, help="horizontal distance to target (in)")
    ap.add_argument("-t", "--height", type=float, default=0.0, help="target height above launch point (in)")
    ap.add_argument("-v", "--speed", type=float, help="launch speed v0 (in/s)")
    ap.add_argument("--high-arc", action="store_true", help="return the high-arc solution")
    ap.add_argument("--demo", action="store_true", help="print the validation table and exit")
    a = ap.parse_args()

    if a.demo or (a.distance is None and a.speed is None):
        _demo()
        sys.exit(0)
    if a.distance is None or a.speed is None:
        print(json.dumps({"abstain": True,
                          "reason": "need both --distance and --speed; height defaults to 0. Without them the angle is undetermined — I will not guess it."}))
        sys.exit(3)

    season = a.season or active_season()
    epath, why = load_element(season, a.element)
    nod = solve_launch_angle(a.distance, a.height, a.speed, a.high_arc)
    drg = solve_with_drag(a.distance, a.height, a.speed, a.high_arc) if epath else None
    out = {
        "inputs": {"distance_in": a.distance, "height_in": a.height, "v0_in_s": a.speed, "arc": "high" if a.high_arc else "low"},
        "gravity_in_s2": G,
        "gravity_source": "references/physics/invariants.json",
        "season": season,
        "element_constants": epath and os.path.relpath(epath, os.path.join(HERE, "..")),
        "no_drag_angle_deg": None if nod is None else round(math.degrees(nod), 2),
        "drag_aware_angle_deg": None if drg is None else round(math.degrees(drg), 2),
        "reachable": nod is not None,
        "caveat": "A correct solver proves the physics is tractable; it is NOT evidence any team fields physics-based power. Report drag-aware if acting on it.",
    }
    if why:
        out["drag_aware_abstain"] = why
    if nod is None:
        out["note"] = "Target unreachable at this speed (need higher v0). Max level range = v0^2/g."
    print(json.dumps(out, indent=2))
