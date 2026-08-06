> Source: https://rr.brott.dev/docs/v1-0/modules/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Modules | Road Runner Docs

# 
 Modules
 #

Ever wondered why there are so many modules and repositories in the Road Runner
ecosystem? It’s all to do with dependencies. The fewer dependencies a module
has, the more places and situations it can be used. For Road Runner, the main
dependency to avoid is the FTC SDK. The SDK integrates heavily with the Android
libraries, making it difficult to run on a non-Android machine. But even beyond
those practical concerns, it’s good to keep conceptually separate bits of code
in different modules. Road Runner and FTC Dashboard may have great synergy when
used together, but the core functionality of Road Runner is totally independent
of FTC Dashboard so neither of those modules depend on each other.

The major modules and their dependencies are shown in this diagram:

flowchart TD
 dash[FTC Dashboard] --> dashCore
 actions[Road Runner Actions] --> rrCore[Road Runner Core]
 actions --> dashCore[Dashboard Core]
 quickstart{{Road Runner Quickstart}} --> rrFtc[Road Runner FTC]
 rrFtc --> actions
 rrFtc --> rrCore
 rrFtc --> ftcSdk[FTC SDK]
 rrFtc --> dash
 quickstart --> ftcSdk
 quickstart --> dash
 dash --> ftcSdk
 meepmeep[MeepMeep] --> actions
 meepmeep --> rrCore

The quickstart node has a different shape because it isn’t a fixed module in the
same way that the others are. It’s a template that teams take and customize to
fit their needs.