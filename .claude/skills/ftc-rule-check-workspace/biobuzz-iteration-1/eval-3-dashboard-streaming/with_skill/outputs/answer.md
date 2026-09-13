**Short answer: No. At a BIOBUZZ event you can't have FTC Dashboard streaming your flywheel graph, and FTC Dashboard is named in the rule itself.**

Season: BIOBUZZ (2026-27), checked against Competition Manual V1 including Team Update 00. The freshness check says CURRENT (live Team Update 0 = stored Team Update 0), so no staleness warning. Every rule cited below was confirmed to exist with `rules.py verify`, and all are base-manual text that no Team Update has changed.

```json
{
  "verdict": "illegal (Dashboard streaming during competition); ambiguous - worth filing a Q&A (Dashboard installed but idle, or used only in the pits or during field calibration)",
  "citations": [
    {"id": "R704", "text": "Teams and ROBOTS must use Wi-Fi networks and bandwidth in a way that enables fair play and does not interfere with other teams or ARENA operations. Teams must abide by the following guidelines: A. Teams may not use any other form of wireless communication, except those offered by the provided official tools, to communicate to, from, or within the ROBOT. B. Teams may not interfere with the ROBOT networks. All communication signals must originate from only the ROBOT CONTROLLER device or the DRIVER STATION device using the ROBOT CONTROLLER Wi-Fi network. No other devices may attempt to connect to, interfere with, or alter the ROBOT CONTROLLER Wi-Fi network. C. Ensure all programming laptops and other devices (other than the DRIVER STATION device) are disconnected from the ROBOT CONTROLLER Wi-Fi network during MATCH play. D. Software with access to the ROBOT CONTROLLER Wi-Fi network must limit the amount of data being streamed (i.e., continuous transmission of data) over Wi-Fi. Software may only stream robot control data, debugging data, and telemetry to and from the ROBOT using the FTC Driver Station Application. Additional logging/streaming services, such as those hosted by third party plugins and tools such as FTC Dashboard, FTControl Panels, and others are prohibited. No continuous video stream is allowed. E. Some events may assign Wi-Fi bands and/or channels to teams. If requested by event staff, teams must use the specific frequency band or channel on the day of the competition."},
    {"id": "R904", "text": "Other than the connection controlled by the ROBOT CONTROLLER app running on the ROBOT and the DRIVER STATION app running on the DRIVER STATION device, no other form of wireless communications shall be used to communicate to, from, or within the OPERATOR CONSOLE during a MATCH. Examples of prohibited wireless systems include, but are not limited to, active wireless network cards, wireless gamepad communication, and Bluetooth devices."},
    {"id": "T405", "text": "During any period when the ARENA is open for measurement, ROBOTS may run OpModes but cannot move the ROBOT (e.g., CHASSIS) under its own power around the FIELD. Violation: VERBAL WARNING. YELLOW CARD if subsequent violations occur during the event. ... Allowed activities during ROBOT calibration and measurement time(s) include: A. ROBOT may be powered on, B. team may initialize an OpMode, ... E. ROBOT may be connected to programming laptops and other devices, ..."}
  ],
  "reasoning": "See below."
}
```
(T405 is shortened with "..." here. The full text came back from `rules.py lookup T405`.)

**Why:**
- **R704.D names FTC Dashboard.** Streaming data or telemetry is only allowed through the FTC Driver Station app. It says "logging/streaming services, such as those hosted by third party plugins and tools such as FTC Dashboard, FTControl Panels, and others are prohibited." A live flywheel graph in Dashboard is exactly that kind of stream.
- **R704.C** says programming laptops and other devices (other than the Driver Station) must be off the Robot Controller Wi-Fi during matches. **R704.B** says only the Robot Controller and Driver Station may send signals on that network. A laptop watching Dashboard during a match breaks both.
- **R904** also bans any wireless link other than the Robot Controller and Driver Station apps to, from or within the driver station setup (the "operator console") during a match.

**What you can do instead:** Send the flywheel velocity through normal `telemetry` so it shows on the Driver Station. R704.D allows "debugging data, and telemetry" through the Driver Station app. You lose the graph but keep the number. If you use Dashboard's `MultipleTelemetry`, the Driver Station half of it is fine. The Dashboard stream is the part that isn't.

**Still unclear (worth a Q&A, which opens September 28, 2026, 12:00 p.m. ET):**
1. **Dashboard still in the code but nobody connected.** The Dashboard library starts its own server on the Control Hub whenever the app runs. R704.D bans the "streaming service," but the manual doesn't say whether an idle server with no viewer counts. The safe choice is to remove the dependency or turn Dashboard off in your competition build. Don't assume "no laptop connected" is enough.
2. **Using Dashboard in the pits or during field calibration.** R704.C is limited to "during MATCH play," but the Dashboard ban in R704.D has no time limit. T405.E does let a robot "be connected to programming laptops" while the field is open for calibration. It doesn't say Dashboard streaming is OK then, so the two rules don't settle it. Treat pit or calibration use as unresolved and ask the head referee or the technical advisor at the event (the FTA), or file a Q&A.

**Questions I'd ask you (no one was available to answer):**
- "Is Dashboard only open on a laptop, or does your code call `FtcDashboard.getInstance()` / `MultipleTelemetry` in the OpModes you'll run at competition?" If it's in the code, I'd point you to the ftc-code-review skill to strip or disable it for competition. If it's only a laptop habit, I'd just say to disconnect the laptop and read telemetry on the Driver Station.
- "Do you want it only for tuning in the pits, or on the field too?" Pits only: I'd help you word the Q&A about R704.D vs R704.C and T405.E. Field: the answer stays no.

Commands run from the repo root: `python3 scripts/check_freshness.py` (CURRENT), then from `.claude/skills/ftc-rule-check`: `rules.py lookup R704 R904 E301`, `section 12`, `section 12.7`, `term MATCH`, `lookup T405` and `verify R704 R904 E301 T405` (all valid). No repo files were changed.