> Source: https://rr.brott.dev/docs/v1-0/guides/ftclib-commands/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

FTCLib Commands | Road Runner Docs

# 
 FTCLib Commands
 #

FTCLib has a commands
system
that is similar to Road Runner actions.

Here’s a generic FTCLib command for wrapping actions.

public class ActionCommand implements Command {
 private final Action action;
 private final Set<Subsystem> requirements;
 private boolean finished = false;

 public ActionCommand(Action action, Set<Subsystem> requirements) {
 this.action = action;
 this.requirements = requirements;
 }

 @Override
 public Set<Subsystem> getRequirements() {
 return requirements;
 }

 @Override
 public void execute() {
 TelemetryPacket packet = new TelemetryPacket();
 action.preview(packet.fieldOverlay());
 finished = !action.run(packet);
 FtcDashboard.getInstance().sendTelemetryPacket(packet);
 }

 @Override
 public boolean isFinished() {
 return finished;
 }
}

This pretty much works with some caveats.

- Actions have no concept of requirements, so they need to be given for each
command.

- Actions do not know when they’re interrupted, while commands have a chance to
do some final cleanup. Of course, a custom command wrapping one
particular action (e.g., following a trajectory) may specifically override
end() to perform some work (e.g., stopping drive motors).

- Commands don’t have a mechanism analogous to preview(). This means the
quickstart trajectory preview will only work for the currently executing
command (of course you can bundle several actions together into one composite
action and wrap that).