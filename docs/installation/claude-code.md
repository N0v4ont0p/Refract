# Install for Claude Code

This is the native path — Refract ships as a proper Claude Code plugin.

```
/plugin marketplace add N0v4ont0p/Refract
/plugin install refract-suite@refract
```

That's it. All 5 skills, the safety hooks (blocking accidental writes into reference-only
directories), and the shared foundation data install together.

## Update

```
/plugin marketplace update refract
/plugin uninstall refract-suite@refract
/plugin install refract-suite@refract
```

**All three steps are needed, verified directly rather than assumed** — a real, live fresh-install
test (via the CLI-equivalent commands, `claude plugin marketplace update` / `claude plugin install`,
since interactive slash commands aren't scriptable) found that `marketplace update` alone refreshes
the marketplace's own clone and catalog, but does **not** refresh what's actually installed and
running — re-running `install` on an already-installed plugin no-ops ("already installed"). The
installed copy only picks up the update after an uninstall/reinstall. Confirmed on the reinstalled
copy: the exact commit hash of the update (`gitCommitSha` in Claude Code's own
`installed_plugins.json`) matched what was actually pushed, and a real file-count check on the
reinstalled copy's `library-docs/` confirmed the content came through, not just the version number.
Nothing updates automatically either way — run this when you want the current version.

## Uninstall

```
/plugin uninstall refract-suite@refract
/plugin marketplace remove refract
```

Uninstall the plugin first, then remove the marketplace entry.

## Verify it's working

Ask something that should trigger a skill — e.g. "is a pneumatic system legal this season" (should
route to `ftc-rule-check` and cite a real rule) or "what's the free speed of a goBILDA 5203 motor"
(should route to `ftc-hardware-lookup` and cite the catalog). If nothing routes, check that the
plugin actually installed: `/plugin marketplace list` should show `refract`.
