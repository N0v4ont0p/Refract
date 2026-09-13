**Short answer: yes, the servos are a problem. You have 10 and BIOBUZZ allows 8. The 8 motors are fine as a count, since that is exactly the limit.**

I checked this against the BIOBUZZ Competition Manual V1 (2026-2027). The local copy includes updates through Team Update 00, and the freshness check reported CURRENT today (2026-09-13), so there's no warning that it's out of date.

```json
{
  "verdict": "illegal (as described: 10 servos exceeds the limit; 8 motors is at the limit and OK on count)",
  "citations": [
    {"id": "R503", "text": "A ROBOT may not have more than 8 motors and 8 servos from the allowable actuator lists per R501 and R502 for all MECHANISMS used in all configurations. If a ROBOT has multiple configurations used at a single event which use different MECHANISMS, the sum total of all motors and servos must be less than or equal to the limit set in this rule."},
    {"id": "I302", "text": "The total number of electronics (motors, servos, Android Devices, etc.) used to build all MECHANISMS and base ROBOT, whether they are used on the ROBOT at the same time or not, may not exceed the constraints specified in Section 12 ROBOT Construction Rules (R)."},
    {"id": "R501", "text": "The only allowed motor actuators are: Table 12-1: Motor allowances [[TABLE:12-1]] Additional motors may be added to the legal motor list in future Competition Manual updates. Many legal gearmotors are sold with labeling based on the entire assembly. These motors may be used with or without the provided gearbox, and/or with any other compatible gearbox."},
    {"id": "R502", "text": "Servo actuators must meet the requirements below. Servos must be compatible with the power regulation devices they are ultimately used with (per R505) and may include additional servo position output interfaces (e.g., 4th Wire Position Feedback). Table 12-2: Servo Requirements at 6V [[TABLE:12-2]] Servos must meet both requirements to be legal for use. ..."}
  ],
  "reasoning": "R503 caps a robot at 8 motors and 8 servos. 10 servos is 2 over, so the robot fails as described. 8 motors meets the cap. I302 closes the obvious workaround: parts on swap-in mechanisms count even if they are never on the robot at the same time."
}
```

**What this means for you**
- **Servos (10, limit 8): you must remove 2.** Unplugging them isn't enough, and neither is moving them to a swap-in mechanism. Both R503 and I302 count every servo across all configurations you use at an event. Common fixes are combining two servo jobs into one, driving a mechanism from a motor you already have, or replacing a servo job with something passive like springs or surgical tubing.
- **Motors (8, limit 8): OK on count, but you have no spare.** If you add a motor for a BIOBUZZ mechanism, you have to remove one. A swap-in mechanism with its own motor also pushes you over. Each motor also has to be on Table 12-1. Most common FTC motors are listed, including goBILDA Yellow Jacket 5201–5204, REV HD Hex and Core Hex, AndyMark NeveRest, and TETRIX MAX TorqueNADO. Motors built into a COTS sensor (like a LIDAR) or into a phone don't count toward the limit.
- **Servo models: check them again this season.** Under R502 and Table 12-2, each servo must be at most 8 W output power and at most 4 A stall current at 6V. The table's examples include the goBILDA Dual Mode Servo, REV Smart Servo, Axon MAX+ and DSSERVO DS3235MG. For a servo not on the Inspection Quick Reference list, bring documentation of its specs to inspection. Don't assume last season's approvals still apply: rule numbers and details change between seasons.

**Things I couldn't settle without asking you.** No one could answer, so here are the questions and how each answer would change things:
1. **Which exact motor and servo models are on the robot?** I would check each motor against Table 12-1 and each servo against Table 12-2. Any servo outside the limits or not on the list would get flagged.
2. **Do you use any swap-in or alternate mechanisms at an event, and what motors and servos do they have?** Those get added to the total. If that pushes motors over 8 or servos above 10, the fix gets bigger.
3. **Are any of the 8 "motors" actually built into a sensor or a phone?** Those don't count, so the motor count could drop below 8 and give you some room.

**Checks I ran:** freshness came back CURRENT, and `rules.py verify R503 R501 R502 I302 --season biobuzz-2026-27` confirmed all four rules exist.