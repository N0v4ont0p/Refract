> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/powerplay-2022-2023/game-breakdown.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/powerplay-2022-2023/game-breakdown.md).

# Game Breakdown

## Game Introduction

<figure><img src="/files/sUcTdOF0tSiiebuYbVxD" alt=""><figcaption></figcaption></figure>

The 2022-2023 FTC season game is POWERPLAY. The POWERPLAY challenge features game elements such as Cones, Junctions, Substations, and Terminals. At the start of the match, each robot begins against their alliance wall and is able to be pre-loaded with one cone. Once the match starts, teams race to score cones and create circuits during the thirty second autonomous period followed by the two minute driver controlled period. During the last thirty seconds of the match called the end game, teams continue to score cones and have the opportunity to cap a junction with a beacon and park in their alliance's terminal for extra points. See the scoring summary below for more information on the game objectives.&#x20;

&#x20;[**FIRST Tech Challenge Game and Resources&#x20;*****LINK***](https://www.firstinspires.org/resource-library/ftc/game-and-season-info)

{% embed url="<https://youtu.be/huT3cQoNNGk>" %}

### Scoring Summary

The following table shows the possible scoring achievements and their point values. The table is a quick reference guide and not a substitute for a thorough understanding of the game manual. All achievements are scored at rest.

<figure><img src="/files/dT1msun7QPwKXIMolk61" alt=""><figcaption></figcaption></figure>

### Field Layout

If you are unfamiliar with the game field structure the following view can give insight to the different elements and their locations.&#x20;

{% hint style="success" %}
For a more in depth explanation of the game check out the official Game [Manual Part 2- Section 4.4 Gameplay](https://www.firstinspires.org/resource-library/ftc/game-and-season-info).&#x20;
{% endhint %}

<figure><img src="/files/0Wme7ksdqUDBEn2d4uT8" alt=""><figcaption></figcaption></figure>

<figure><img src="/files/GuPAJyGxN9hha1gXLyVL" alt=""><figcaption></figcaption></figure>

## Game Breakdown

The first step to any good FTC Game strategy is a full, in-depth understanding of the game. Strong knowledge of scoring achievements, point values, and game rules help teams develop a game strategy that maximizes their scoring ability. Once the knowledge is built the game can be broken down into data points for analysis.&#x20;

A commonly used metric in the competitive robotics world is **points per second.** Basing your game strategy based on the amount of points you can gain per second (or even per game period), will help your team make the mechanical choices best for you!

Remember to always strategize and build within your resources! Not all teams will have access to the same resources, whether it is parts or people. A strategy that seems to yield the most points per second on paper may not be as successful as a strategy that focuses on maximizing accuracy.&#x20;

The following section will breakdown the major scoring achievements of the game as well as provide some of the strategic considerations, we at REV noticed. While this breakdown may provide you with a basic knowledge of this years game it is always advised to consult Game Manual Part 2 to better understand the rules.&#x20;

### Autonomous

#### Navigating

Most FTC games include some sort of navigation or parking task in the autonomous period and this years game is no different. Typically, these are autonomous scoring achievements where a robot has moved to a particular portion of the field and parked. Adding to the navigation challenge this year is the Signal Bonus. Robots will earn extra points when parked completely in the designated zone as indicated by their signal.

| Condition            | Location    | Points                                                                 |
| -------------------- | ----------- | ---------------------------------------------------------------------- |
| Parked In            | Substation  | 2                                                                      |
| Parked In            | Terminal    | 2                                                                      |
| Parked Completely In | Signal Zone | <p>10 - Field Supplied Signal <br>20 - Team Supplied Signal Sleeve</p> |

To understand the full break down of navigating, it helps to understand how Game Manual Part 2 defines **In** and **Completely in**. Once you have a grasp on how these concepts are defined you can make a decision about which navigation achievements will give you the most points per second, when compared against the rest of your autonomous strategy.&#x20;

In general, navigation during autonomous is a very achievable goal. While you may have to consider some obstacles, like the junctions, using our Hello Robot - Encoder Navigation guides for[ Blocks](/duo-control/hello-robot-blocks/part-3/using-encoder.md) and [Java](/duo-control/hello-robot-java/part-3/using-encoder.md), you can easily create the code needed to meet many of the navigation achievements.&#x20;

{% hint style="info" %}
Want to take a look at how to navigate in autonomous. Check out our [Programming Autonomous](/ftc-kickoff-concepts/freight-frenzy-2021-2022/autonomous.md) guide for more information.&#x20;
{% endhint %}

#### Cones

During the Autonomous period of POWERPLAY teams can also earn points by scoring cones. Cones scored in the autonomous period will earn additional points at the end of the Driver-Controlled Period if they remain in place.&#x20;

| Junction        | Points |
| --------------- | ------ |
| Ground Junction | 2      |
| Low Junction    | 3      |
| Medium Junction | 4      |
| High Junction   | 5      |

### Driver Controlled

Directly following the end of the Autonomous Period, Drive Teams have five (5) seconds plus a "3-2-1-go" countdown to prepare their Driver Stations for the start of the 2 minute Driver-Controlled Period. On the countdown word "go," the Driver-Controlled Period starts, and Drive Teams press their Driver Station start button to resume playing the Match.&#x20;

**Cones**

During the Driver Controlled period teams strategically place cones on junctions to complete a circuit. All cones placed during the Driver-Controlled period are scored at rest after the match.&#x20;

| Junction        | Points |
| --------------- | ------ |
| Ground Junction | 2      |
| Low Junction    | 3      |
| Medium Junction | 4      |
| High Junction   | 5      |

### End Game&#x20;

The last thirty seconds of the Driver-Controlled Period is called the End Game. Driver-Controlled Period Scoring can still take place during the End Game and this is when the Beacon (team scoring element) is introduced into the Playing Field.&#x20;

#### Junction Ownership

Alliances can earn points for owning a junction by fulfilling one of two conditions:

| Condition                                | Points |
| ---------------------------------------- | ------ |
| Having the top scored Cone on a Junction | 3      |
| Capping a Junction with a Beacon         | 10     |

If both conditions are met, a beacon will take precedence over the top scored cone and the alliance will receive 10 points

<figure><img src="/files/FBFt1jHa9KawYq3mzjUh" alt=""><figcaption></figcaption></figure>

#### Circuit

A completed Circuit earns 20 points for the alliance. Only one circuit can be awarded per match.&#x20;

See the example of a completed circuit (Red Alliance) and a partial or incomplete circuit (blue) below.

<figure><img src="/files/wlNpWOCcRsXEUCEOPJ8L" alt=""><figcaption></figcaption></figure>

#### Navigating

Robots that end the match parked in either of the Alliance's terminals will earn 2 points.&#x20;
