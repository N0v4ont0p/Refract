**No. The BIOBUZZ manual names FTC Dashboard as prohibited.**

**The rule (2026-2027 Competition Manual, V1, R704.D, p. 140):** software on the Robot Controller Wi-Fi may only stream control data, debugging data and telemetry through the FTC Driver Station app. It says "third party plugins and tools such as FTC Dashboard, FTControl Panels, and others are prohibited." It also bans continuous video streams.

Two related parts of the same rule:
- **R704.B:** only the Robot Controller and Driver Station may talk on the robot's Wi-Fi. Nothing else may try to connect to it.
- **R704.C:** every programming laptop and other device (except the Driver Station) must be disconnected from the robot's Wi-Fi during matches.

**It's not just during matches.** R704.C only covers match play. But R704.D is written about the software itself, with no time limit. My reading is that it covers the whole event, including tuning in the pits. The one way to be sure is the official FTC Q&A.

**What to do:**
1. **Take Dashboard out of your competition build.** Remove the Dashboard dependency from `build.gradle` on a competition branch, and remove or wrap every `FtcDashboard` call. Dashboard starts its web server as soon as the Robot Controller app launches, even if no OpModes use it. So just not opening it on a laptop doesn't clearly comply, and taking it out removes any doubt at inspection. The app menu also has a disable option, but a toggle is easy to forget or flip back on.
2. **At events, show flywheel speed on the Driver Station.** Normal `telemetry.addData("flywheel vel", motor.getVelocity())` goes through the Driver Station app, which R704.D allows. You lose the graph but keep the numbers.
3. **For graphs at events, log to a file.** Write timestamp, target speed and measured speed to a CSV on the Robot Controller. Pull it off over USB/adb after the match and plot it. Nothing is streamed over Wi-Fi, so R704.D shouldn't apply. That's my interpretation, not a rule quote.
4. **Keep using Dashboard at your shop.** The ban is in the Competition Manual, so it shouldn't apply to practice at home.

**Check before your event:** this is manual V1. I didn't find any BIOBUZZ Team Update that changes R704, but look at the latest Team Updates before you compete.

**Questions I'd ask you (no one was available to answer):**
- Do you use Dashboard only to graph, or also to change tuning values live (`@Config` / `FtcDashboard.getTelemetry()`)? If you change values live, you need to hard-code the tuned values before the event, or `@Config` classes will need cleanup. If you only graph, steps 1 and 2 are enough.
- Do you want the CSV logger from step 3? If yes, I'd write a small logger that saves a timestamped file on each OpMode run, plus a script to plot it on a laptop.

Sources:
- [2026-2027 FIRST Tech Challenge Competition Manual (V1)](https://ftc-resources.firstinspires.org/ftc/game/manual)
- [BIOBUZZ Game & Season | FIRST Tech Challenge](https://www.firstinspires.org/programs/ftc/game-and-season)
- [BIOBUZZ Competition Manual Preview Release](https://community.firstinspires.org/biobuzz-cm-preview-release)