> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/ivy/command-compositions.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Command Compositions
---

Remember on the [What are Commands?](./what-are-commands) page where we said that
commands can be run in parallel? That's an example of a **command composition**.
A command composition is, at its core, a command that is "composed" of smaller
commands. Let's take a look at the different types of command compositions 
in Ivy.

## Sequential

Sequential compositions are probably the most common type of command composition.
They take a list of commands and run them one after the other. To create a 
sequential composition, use the `sequential` function:

```java
Command myCommand = sequential(
    command1,
    command2,
    command3
);
```

Notice that the command returned by `sequential` is a command itself, which 
means you can nest compositions inside each other. This is one of the 
beauties of command compositions: they can be nested arbitrarily.

You can also create sequential compositions using the `then` method:

```java
Command myCommand = command1.then(command2).then(command3);
Command myCommand = command1.then(command2, command3);
```

## Parallel

Sequential compositions are great for running commands one after the other, but
what if you want to run multiple commands at the same time? For this, you can
use a parallel compositions. Parallel compositions are created using the 
`parallel` function:

```java
Command myCommand = parallel(
    command1,
    command2,
    command3
);
```

As with sequential compositions, you can nest parallel compositions. This 
means you can put a parallel composition inside a sequential composition or 
a sequential composition inside a parallel composition!

You can also create parallel compositions using the `with` method:

```java
Command myCommand = command1.with(command2).with(command3);
Command myCommand = command1.with(command2, command3);
```

## Race

Race compositions are similar to parallel compositions, but instead of 
finishing when all commands finish, they finish when the first command 
finishes. The remaining commands are cancelled. Race compositions are created 
using the `race` function:

```java
Command myCommand = race(
    command1,
    command2,
    command3
);
```

You can also create race compositions using the `raceWith` method:

```java
Command myCommand = command1.raceWith(command2).raceWith(command3);
Command myCommand = command1.raceWith(command2, command3);
```

## Deadline

Deadline compositions are similar to parallel and race compositions, but 
they finish when a specific "deadline" command finishes. The remaining 
commands are cancelled. Deadline compositions are created using the `deadline` 
function:

```java
Command myCommand = deadline(
    deadlineCommand,
    command1,
    command2,
    command3
);
```

## Repeat

A repeat composition is a command that runs a command a specified number of times.
Repeat compositions are created using the `repeat` function:

```java
Command repeatCommand = repeat(command, 3); // repeats command 3 times
```

You can also pass an `IntSupplier` (essentially the same as `Supplier<Integer>` explained on the previous page)
instead of an `int` if you want to dynamically 
determine the number of times the command should be repeated.

## Loop

A loop composition runs a command and restarts it whenever it finishes. Loop 
compositions are created using the `loop` function:

```java
Command loopCommand = loop(command);
```

Loop commands never finish. To make one finish after a condition, you can 
put it in a race composition with another command.
