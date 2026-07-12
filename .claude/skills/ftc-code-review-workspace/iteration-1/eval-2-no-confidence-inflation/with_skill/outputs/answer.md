# Does "lots of top teams use SolversLib command framework" make it proven best-practice?

Short answer: **No — not in the way you're framing it, and I specifically shouldn't cite it that way.** Using SolversLib is a perfectly reasonable choice. But "a bunch of elite teams converged on it" is *not* independent evidence that it's the best-practice architecture, and the pattern corpus this review runs against is built to catch exactly this reasoning.

## Why the headcount doesn't count as convergence

Your `Shooter.java` extends `com.seattlesolvers.solverslib.command.SubsystemBase` — the SolversLib command framework (the maintained FTCLib successor). When six teams all `extends SubsystemBase`, they aren't six teams *independently arriving at* a subsystem/command design. They're six teams **importing the same library**. The design decision was made once, by the library authors; every adopter inherits it. In provenance terms that collapses to **one** data point, not six.

The corpus has a name and a gate for this: the **§12 shared-library import gate**. Before any "teams converged on X" claim gets a confidence tag, it checks whether the shared thing is a shared *import*. If it is, it's tagged **shared-ancestry**, and shared-ancestry adoption is explicitly *not* counted as independent design validation. From the corpus, on this exact library:

- **15083-B** (`solverslib-command-adoption`): `confidence: single-source`, `provenance: shared-ancestry`. Verbatim basis: *"Subsystem/command substrate is SolversLib (FTCLib-successor)… Both shared libraries. Collapses to those sources; NOT an independent orchestration data point."* It's recorded as a **provenance guard, not a transferable pattern** (`applicable_when: n/a`).
- **22105**: *"SolversLib (FTCLib-lineage) — orchestration is shared-ancestry, not an independent leg."*
- **12808-B** (Pedro's `ivy` command framework) and **16093** (FTCLib `CommandScheduler`): same verdict — shared-ancestry, collapses to the library. 12808-B is why the import gate was elevated to a *standing detection rule*: teams on the same library will "FALSELY appear to converge."
- **3543** (Titan's own trclib/ftclib): even a mature, competition-hardened framework is tagged **single-source** with the note *"maturity/popularity only, not design validation"* and *"not promoted on adoption."*

So the honest framing is: SolversLib being widely adopted tells you it's **mature and popular** — a real, useful signal (it's maintained, other teams hit fewer sharp edges, there's help available). It does **not** tell you it's the architecturally-correct choice for your robot, and citing "N elite teams use it" as if it were N endorsements would be inflating popularity into a design proof (that's the R43 no-headcount rule).

## What I can and can't say for you to cite

- ✅ Citeable: "SolversLib is a maintained, widely-adopted FTCLib-successor command library" — that's a maturity/popularity fact.
- ❌ Not citeable as convergence: "Elite teams independently converged on this architecture, so it's proven best-practice." The corpus tags every instance of this exact adoption as shared-ancestry; repeating a team count as if it were independent confirmation is precisely what the provenance work rules out.

## One separate thing worth a look (not the question, but adjacent)

Your `team-config.yaml` has `software_stack.opmode_style: raw_linear_opmode (confirmed)`, yet `Shooter.java` is built on the SolversLib command framework. Those are two different orchestration models. That's not illegal or wrong — but adopting a command framework *is* a real architectural commitment (scheduler, command lifecycle, subsystem periodic loop), especially for a rookie team. If you're genuinely going command-based, the config's `opmode_style` should probably say so; if the config is right and you just wanted `Shooter` as a class, you may not need the framework dependency at all. That's a config-vs-code question for ftc-team-config, not something I'd resolve inside this review — flagging it so it doesn't drift.

Bottom line: use SolversLib if it fits how you want to structure the robot. Just don't sell it — to judges, to yourselves, or in an engineering notebook — as "elite teams converged on it therefore it's proven." The adoption is shared-ancestry; the corpus counts it as one library's design, not many teams' independent verdict.
