# Is "lots of top teams use SolversLib" proof it's best-practice?

Short answer: no. Popularity is evidence that it's a *reasonable, viable* choice — it's not proof that it's the best or "proven" one, and I wouldn't cite it that way in a design notebook or judge presentation.

## Why "many elite teams use it" doesn't establish "proven best-practice"

This is an argument from popularity/authority. It can be true that a widely-adopted tool is also excellent, but the adoption itself doesn't demonstrate that. A few things break the chain:

- **Adoption ≠ independent verification.** Teams copy what winning teams do. If 20 teams use SolversLib, that's often not 20 independent evaluations — it's a handful of original adopters and a lot of downstream copying. Shared lineage counts as roughly *one* data point, not twenty. "Everyone converged on it" and "everyone copied the same alliance partner's repo" look identical from the outside.
- **Survivorship bias.** You see the command framework in the repos of teams that won. You don't see the teams that used it and struggled, or the teams that won with plain iterative OpModes and never posted their code. Winning teams win for many reasons (drivers, hardware, strategy, funding, hours); the framework is rarely the isolated cause.
- **"Best-practice" is context-dependent.** A command-based framework shines when you have many concurrent subsystems, complex autonomous routing, and a codebase several people maintain. For a single shooter subsystem, the framework's scheduling/decoupling benefits are mostly latent — you're paying the abstraction cost without yet cashing the benefit. Whether it's "best" depends on *your* subsystem count, *your* team's experience, and how much your programmers actually understand the command lifecycle.
- **Popular ≠ correct-for-you.** The real risk with an adopted framework is a team that can't debug it. A shooter that misbehaves inside a command framework nobody on the team fully understands is worse than a plain state machine everyone can read.

## What would actually justify the claim

To say SolversLib is the right choice *for your shooter*, cite things you can verify:

- It's actively maintained and documented (check the repo's recent commit activity and release notes yourself).
- Your team understands the command lifecycle well enough to debug it under competition pressure.
- Your robot has enough concurrent subsystems / autonomous complexity that command-based structuring earns its keep.
- You've had it running reliably on your hardware across multiple sessions.

Those are real reasons. "Elite teams use it" is context, not one of them.

## On citing it in judging / your engineering notebook

Judges reward *reasoning*, not bandwagon appeals. Framing to avoid:

> ❌ "We use SolversLib because top teams use it; it's the proven best-practice approach."

That invites the follow-up "why is it best for *your* robot?" — and "because others use it" is a weak answer that can actually cost you.

Better framing:

> ✅ "We evaluated a command-based framework (SolversLib) against plain OpModes. We chose it because our robot has [N subsystems] that need to run concurrently and our autonomous sequences [reason], and our programmers [have this experience with it]. It's actively maintained [link]. Its adoption by experienced teams gave us confidence it was a safe starting point."

That mentions the adoption as *supporting context* while resting the decision on your own requirements. That's honest and it's stronger.

## Bottom line

SolversLib is a legitimate, well-regarded choice — using it is fine. Just don't upgrade "many strong teams use it" into "proven best-practice." Adoption is a reason to take it seriously and investigate; it isn't the justification itself. Cite your own requirements and your team's understanding as the reason, and mention the adoption as context, not proof.
