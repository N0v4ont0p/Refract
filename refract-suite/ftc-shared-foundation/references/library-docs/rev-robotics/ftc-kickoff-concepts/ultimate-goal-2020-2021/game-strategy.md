> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/ultimate-goal-2020-2021/game-strategy.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/ultimate-goal-2020-2021/game-strategy.md).

# Game Strategy

## Game Introduction

The 2020-2021 FTC game is Ultimate Goal. The Ultimate Goal challenge features game elements such as rings, wobble goals, and tower goals. Each robot starts the match on the start line and must be in possession of an alliance specific Wobble goal. From there each team will progress through the thirty second autonomous period followed by the two minute long driver controlled period. The last thirty seconds of the match is the end game period. Each period has different scoring achievements. See the scoring summary excerpt from Game Manual Part 2 for more information on the game objectives.&#x20;

#### **Scoring Summary**

![Game Manual Part 2](/files/-MHCy50CXVZSLbwDz6Eg)

If you are unfamiliar with the game the following field view can give insight to the field elements.&#x20;

![Game Manual Part 2](/files/-MHNcndVWBsd5mBO_tpm)

For a more in depth explanation of the game check out [Game Manual Part 2 - Traditional Events *Section 4.5 Gameplay* ](https://firstinspiresst01.blob.core.windows.net/first-game-changers/ftc/game-manual-part-2-traditional-events.pdf)*.*&#x20;

{% hint style="info" %}
If you are participating in remote events check out [Game Manual Part 2 - Remote Events *Section 4.5 Gameplay* ](https://firstinspiresst01.blob.core.windows.net/first-game-changers/ftc/game-manual-part-2-remote-events.pdf)*.*
{% endhint %}

## Game Strategy

The first step to any good FTC Game strategy is a full, in-depth understanding of the game. Strong knowledge of scoring achievements, point values, and game rules help teams develop a game strategy that maximizes their scoring ability. Once the knowledge is built the game can be broken down into data points for analysis.&#x20;

A commonly used metric in the competitive robotics worlds is **points per second.** Basing your game strategy based on the amount of points you can gain per second (or even per game period), will help your team make the mechanical choices best for you!

The following section will highlight what we at REV saw as the best strategy for game plan. This choice was based on maximizing points per second.&#x20;

Remember to always strategize and build within your resources! Not all teams will have access to the same resources, whether it is parts or people. A strategy that seems to yield the most points per second on paper may not be as successful as a strategy that focuses on maximizing accuracy.&#x20;

### Autonomous

As always, the autonomous period comes with a lot of different opportunities for scoring. This gives teams a broad range of scoring achievements to choose from. After analyzing the scoring opportunities we decided on a basic 4 part Autonomous strategy.&#x20;

{% hint style="info" %}
We are assuming based on the language provided in Game Manual Part 2 that the Rings in the Starter Stack are not playable until the start of the Driver Controlled period. This is not called out in the Game Specific Rules. Please keep up to date with the [FTC Q\&A forum ](https://ftcforum.firstinspires.org/)for more clarity on this ruling.&#x20;
{% endhint %}

#### Launch the Pre-Loaded Rings&#x20;

The highest point gain overall from the autonomous period is Launching all three rings into the tower goal (High) or at the power Shot. After some basic analysis, we determined a team could launch into the high goal at the start of autonomous before moving on to complete the other autonomous tasks.&#x20;

| Scoring Achievement | Points per Ring | Total Possible Points |
| ------------------- | --------------- | --------------------- |
| High Tower Goal     | 12              | 36                    |
| Power Shot          | 15              | 45                    |

While knocking back all three power shots get teams 45 total points during the autonomous period, there are a couple of reasons the high tower goal may be more beneficial to teams.

In our live stream we found that the high tower goal was a much more consistent scoring achievement. The tower goal is larger than the individual power shots and thus has a higher rate of scoring success. The larger scoring interface also means that teams will not have worry too much about robot location on the field to shoot. Early on in the season as teams are working on an iterating their robots, we think the high goal will yield more points per second than the power shot.&#x20;

#### Analyze the Starter Stack&#x20;

Once the rings have been launched the next scoring opportunity is moving the Wobble Goal to the appropriate target zone. In order to accomplish this task teams will need to take time to analyze the randomized starter stack.

The following table highlights some of the ways to analyze the starter stack:

|                 | Accuracy                                                     | Complexity                     |
| --------------- | ------------------------------------------------------------ | ------------------------------ |
| Vuforia         | Most Accurate                                                | Complex                        |
| Distance Sensor | Won't be able to differentiate as well between 1 and 4 rings | Complexity depends on use case |

Once you've analyzed the starter stack, it will maximize time during Driver Controlled period to try to pick up the starter stack ring(s). When Driver Controller period starts those additional rings are ready to be scored.&#x20;

#### Move the Wobble Goal

Even if analyzing the starter stack takes time to get accurate, moving the wobble goal to the same target zone every time has a 33% chance of success.&#x20;

Moving the wobble goal to a specific part of the field can be accomplished by making small changes to the PushbotAutoDrive sample codes available through the FTC SDK.&#x20;

![](/files/-MHNMfB5_He0YaqKS4g5)

#### Navigating

Navigation is the final step to the 4 part autonomous strategy. Using the PushbotAutoDrive sample codes mention in the [Move the Wobble Goal ](/ftc-kickoff-concepts/ultimate-goal-2020-2021/game-strategy.md#move-the-wobble-goal)step, all teams should be able to navigate to and park over the launch line.&#x20;

### Driver Controlled

Since the only scoring achievement in the Driver Controlled period is scoring into the tower goals the main strategy to is efficiency and accuracy. As we said its always about maximizing points per second!&#x20;

#### Human Player&#x20;

Its important in this game period to keep a few things in mind: rules and the human player. Knowing the rules will help minimize penalties, which this year reduce your alliances overall score. The human player will be the person responsible for make sure that rings are continuously cycling back onto the field. A good strategy for every team is to ensure you understand the role of the human player and build your strategy around their speed.&#x20;

#### Rings&#x20;

Its also very important to analyze and understand how the rings behave once they are returned to the field. The rings have to hit the playing field floor before they are considered legally in play. We did some testing and found that once the rings hit the floor they had the velocity behind them to roll to the audience side of the field. Obviously the faster you pick up these rings the faster the turn around on scoring them.

Once you have analyzed how far the rings can role and what the best strategy for picking them up there is one particular game specific rules to take into consideration&#x20;

#### GS 12&#x20;

![](/files/-MHNVKb0cB0BU0zOH0qX)

Rings must be launched into the mid and high tower goal from behind the launch line. If your intent is to score into either of these goals and the rings are rolling far enough over the line the best strategy may be letting the rings come to you.&#x20;

With all that said the best strategy we can find is minimizing ring recycle time. While the high goal may be worth more points than the mid or low goal, we believe that no goal is counted out. Test your field, your rings, and your human player to make a decision on the best strategy for your team.&#x20;

### End Game&#x20;

The [scoring summary ](/ftc-kickoff-concepts/ultimate-goal-2020-2021/game-strategy.md#scoring-summary)from game manual part 2 includes the following end game scoring opportunities:

* Wobble goal delivered to the start line or to the drop zone&#x20;
* Driver Controlled scoring opportunities (scoring in the tower goal) continues&#x20;
* Launching at the power shots&#x20;
* Scoring rings on the wobble goal&#x20;

#### Wobble Goal Delivery&#x20;

Delivering the wobble goal to the drop zone is worth 20 points per wobble goal delivered. The wobble goals are light but this strategy will likely require an elevator or lift that can move the wobble goal over the field wall into the drop zone. Though it is worth 20 points its important to consider the speed of this activity and the following questions&#x20;

* How many seconds does this take?
* Is it a higher return of points per second to deliver the wobble goal to the start line and focusing on scoring rings?

#### Launching at the Power Shots

Successfully scoring all three power shots in end game yields 45 points. There are some of the same limitations to this as there were in autonomous. Accuracy is key.&#x20;

#### Scoring rings on the Wobble Goal

As we went through analyzing the game we were not able to conclusively decide whether this scoring achievement was valuable. If you are able to score into the high goal with a certain amount of speed and accuracy; it seems like continuing  to do so in end game would be more advantageous. However, a team that primarily scores in the low or mid goal may benefit from scoring rings on the wobble goal in end.&#x20;

The other benefit is that rings scored on the wobble goal are out of play, which will starve the field of rings.&#x20;
