> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/ivy/requirements-and-priorities.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Requirements and Priorities
---
In the previous example with the arm raising command, you would likely also have a command
that lowers the arm. Let's imagine a situation in which the arm is actively raising.
There are numerous different ways that you may
want to schedule the lowering command. In some situations, you may want to lower the arm
immediately, overriding the raising command. In others, you may want to wait until the raising
command finishes before lowering the arm, but you may decide this after you scheduled the raising
command (meaning you can't use a sequential composition, as described in a later section).
You may also want to immediately lower the arm, but then immediately raise it again.

With the tools provided so far, it would be inconvenient and verbose to have to write a
separate command for each of these scenarios. To solve this problem, Ivy provides
**requirements**. Requirements are a way to specify that a given command uses certain objects
or subsystems on your robot. In the above example, you would have the raising and lowering commands
require the arm motor(s) or the arm subsystem if you've created a class. In general, a command can 
have any number of requirements, and a requirement can be any object.

By themselves, requirements are not very useful. However, when combined with priorities,
they allow you to specify how commands that share requirements should interact. A priority is an integer that specifies
how important a command is. The default priority is 0.

When you try to schedule a command with conflicting requirements with any currently scheduled
commands, there are three types of behaviors that can occur:

- **Interrupted Behavior**: If all currently scheduled commands have a lower priority than the new,
  conflicting command, this determines what happens to each currently scheduled command.
  `InterruptedBehavior` is an enum with types `END` and `SUSPEND`. `END` means that each
  currently scheduled command will terminate and not be run again, while `SUSPEND` means
  that the currently scheduled command will be suspended and continue when the conflicting
  command finishes. In both cases, `end()` will be called on each currently scheduled command.
  Defaults to `END`.
- **Blocked Behavior**: If any currently scheduled command has a higher priority than the new,
  conflicting command, this determines what happens to the conflicting command. `BlockedBehavior`
  is an enum with types `CANCEL` and `QUEUE`. `CANCEL` means that the conflicting command will be
  canceled, while `QUEUE` means that the conflicting command will be queued and run after the currently
  scheduled conflicting commands finish.
  Defaults to `CANCEL`.
- **Conflict Behavior**: If the highest priority of all currently scheduled commands is equal to
  the new conflicting command, this determines what happens to the new conflicting command.
  `ConflictBehavior` is an enum with types `CANCEL`, `QUEUE`, and `OVERRIDE`. `CANCEL` means that
  the new conflicting command will not be scheduled, `QUEUE` means that the new conflicting command will
  be queued and run after the currently scheduled conflicting commands finish, and `OVERRIDE` means that
  the new conflicting command will interrupt the currently scheduled conflicting commands and run instead
  (note, this triggers the `InterruptedBehavior` of the currently scheduled conflicting commands).
  Defaults to `OVERRIDE`.

Returning to our arm example, instead of creating separate commands for each of the scenarios,
we can create a single command and modify its priority to handle each scenario.

Note that requirements are a completely optional feature, and you can use Ivy perfectly well
without them. However, they are a powerful tool that can help you write simpler and safer code
should you want to use them.
