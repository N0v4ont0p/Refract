**Yes, there's a problem. With 10 servos the robot won't pass BIOBUZZ inspection. The 8 motors are fine on count. Take off at least 2 servos.**

This is checked against the BIOBUZZ Competition Manual V1 (2026-27), which includes updates through Team Update 00. The corpus check came back CURRENT (latest live Team Update is 00). Every rule number below was confirmed to exist in this season's manual, and the quotes are copied word for word from it.

```json
{
  "verdict": "illegal",
  "citations": [
    {"id": "R503", "text": "A ROBOT may not have more than 8 motors and 8 servos from the allowable actuator lists per R501 and R502 for all MECHANISMS used in all configurations. If a ROBOT has multiple configurations used at a single event which use different MECHANISMS, the sum total of all motors and servos must be less than or equal to the limit set in this rule."},
    {"id": "I302", "text": "The total number of electronics (motors, servos, Android Devices, etc.) used to build all MECHANISMS and base ROBOT, whether they are used on the ROBOT at the same time or not, may not exceed the constraints specified in Section 12 ROBOT Construction Rules (R)."}
  ],
  "reasoning": "R503 caps a BIOBUZZ ROBOT at 8 motors and 8 servos. 10 servos is 2 over the limit, so the robot as described is illegal. 8 motors is exactly at the limit, which is allowed. I302 says the count includes every MECHANISM you bring, whether or not it's on the robot at the same time, so spare or swap-in mechanisms count too."
}
```

**What this means for you**
- **Servos (the problem):** Get down to 8 or fewer. That total counts every mechanism you bring to the event, not just what's on the robot in one match (R503 and I302). So you can't keep 10 servos by putting 2 of them on a swap-in attachment.
- **Motors (at the limit):** 8 is legal, but you can't add another motor anywhere, including on a spare or alternate mechanism.
- **Doesn't count toward the limit:** Table 12-1 says factory vibration or autofocus motors inside a COTS computing device, and motors built into a COTS sensor like a LIDAR, don't count.

**Last season's robot still has to meet this season's part rules.** A legal count isn't enough; each part has to be legal under the BIOBUZZ tables:
- **R501, motors:** Every motor has to be on Table 12-1. That table lists goBILDA Yellow Jacket 5201-5204 and 5000 series, REV HD Hex and Core Hex, AndyMark NeveRest, Studica Maverick, SWYFT Spike, TETRIX MAX and TorqueNADO, NFR Yuksel, WATTOS Stingray, and the discontinued MR/MATRIX.
- **R502, servos:** Table 12-2 has two classes of servo:
  - Standard servos must be ≤ 8 W mechanical output and ≤ 4 A stall current, both at 6 V.
  - Linear servos must be ≤ 1 A stall current at 6 V (no power limit).
  - A servo has to meet both limits for its class. Unless it's on the Inspection Quick Reference pre-approved list, bring documentation of its specs.
- **R505, controllers:** All actuators must run through a Table 12-3 device, with at most 2 motors or 2 servos per port. The REV SPARKmini is 2 motors per device.

Once you've removed servos, ask for re-inspection for the changed robot (I303 covers when that's needed).

**Questions I'd ask you**
1. **Which 2 servos are you removing, and does that leave a mechanism you still need without a servo?** If so, you'd have to combine functions (for example, one servo driving a linkage) or redesign it. The hardware-lookup skill can size a replacement; this check can't pick which servo goes.
2. **Do you plan to bring any swap-in or alternate mechanisms?** If yes, their motors and servos count toward the 8 and 8, so with 8 motors already, any motor on them puts you over. If no, the only fix needed is 2 fewer servos.
3. **What exact motor and servo models, and which controllers?** With a list, I'd check each one against Tables 12-1, 12-2 and 12-3. For any servo not on the pre-approved list, I'd work out its output power from the 6 V specs (0.25 × stall torque in N·m × no-load speed in rad/s). If a servo's specs can't be documented, it's "ambiguous" until you can show them.