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
```

Pulls whatever is currently on this repo's `main` branch. Nothing updates automatically — run this
when you want the current version.

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
