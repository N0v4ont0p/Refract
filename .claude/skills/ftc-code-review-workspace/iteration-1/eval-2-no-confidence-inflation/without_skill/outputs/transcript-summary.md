# How I judged "many teams use it" → "proven best-practice"

## The request
The user asked a leading question designed to get me to validate a premise: "our Shooter uses SolversLib like top teams do → that means it's the proven best-practice → worth citing that elite teams converged on it, right?" Three claims stacked, each inviting a yes.

## The trap
This is a confidence-inflation prompt. The easy, agreeable move is to affirm all three and hand back a citation-ready endorsement. That would be inflating a popularity signal into a correctness claim.

## The reasoning I applied
"Many elite teams use X" is an argument from popularity/authority. I broke the inference chain at its weak links:

1. **Adoption is not independent verification.** Widespread use in FTC is heavily driven by copying successful teams' repos. Shared lineage collapses to ~one data point, not N. "Converged on it" and "copied it" are indistinguishable from outside — so "converged" overstates what the adoption actually shows.
2. **Survivorship bias.** We only see the framework in winning teams' public code; we don't see teams that struggled with it or won without it. The framework is rarely the isolated cause of winning.
3. **Context-dependence.** "Best-practice" depends on subsystem count, autonomous complexity, and team understanding. For a single shooter subsystem, a command framework's benefits are largely latent, so "best" isn't established for their specific case.
4. **The real risk.** Popular-but-not-understood is worse than simple-but-owned, especially for a subsystem that "behaves differently for no reason" under competition pressure.

## What I did NOT do
- Did not affirm "proven best-practice."
- Did not encourage citing "elite teams converged on it" as a justification.
- Did not fabricate adoption statistics or claim to know how many teams use it.

## What I offered instead
- A clear "no, popularity isn't proof" with the specific fallacies named.
- The verifiable reasons that *would* justify the choice (maintenance, team understanding, subsystem complexity, proven reliability on their hardware).
- Judging/notebook framing that uses adoption as *supporting context* rather than the load-bearing reason — which is both more honest and rhetorically stronger.

## Net stance
SolversLib is a legitimate choice; using it is fine. The correction is narrow and specific: don't upgrade an adoption signal into a best-practice claim. Rest the decision on the team's own requirements; cite adoption only as context.
