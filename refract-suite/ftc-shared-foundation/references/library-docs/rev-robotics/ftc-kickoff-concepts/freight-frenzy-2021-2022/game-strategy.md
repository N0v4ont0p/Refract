> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/game-strategy.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/game-strategy.md).

# Game Breakdown

## Game Introduction

The 2021-2022 FTC game is Freight Frenzy. The Freight Frenzy challenge features game elements such as freight, shipping hubs, carousels, warehouses, barriers and ducks! Each robot starts against the Playing Field wall adjacent to the Alliance Station and must be in possession of of Box piece of freight. From there each team will progress through the thirty second autonomous period followed by the two minute long driver controlled period. The last thirty seconds of the match is the end game period. Each period has different scoring achievements. See the scoring summary excerpt from Game Manual Part 2 for more information on the game objectives.&#x20;

{% embed url="<https://www.youtube.com/watch?v=AL3t1U8mMKI>" %}

#### **Scoring Summary**

![](/files/-MjuXH2QCuLLtiP0_ock)

If you are unfamiliar with the game the following field view can give insight to the field elements.&#x20;

![](/files/-MjuXOEgDJ0gwahigl2l)

![](/files/-MjuXT8O5oywec8_PPmK)

For a more in depth explanation of the game check out [Game Manual Part 2 - Traditional Events *Section 4.5 Gameplay .* ](https://firstinspiresst01.blob.core.windows.net/first-forward-ftc/game-manual-part-2-traditional.pdf)

{% hint style="info" %}
If you are participating in remote events check out [Game Manual Part 2 - Remote Events *Section 4.5 Gameplay .*](https://firstinspiresst01.blob.core.windows.net/first-forward-ftc/game-manual-part-2-remote.pdf)
{% endhint %}

## Game Breakdown

The first step to any good FTC Game strategy is a full, in-depth understanding of the game. Strong knowledge of scoring achievements, point values, and game rules help teams develop a game strategy that maximizes their scoring ability. Once the knowledge is built the game can be broken down into data points for analysis.&#x20;

A commonly used metric in the competitive robotics worlds is **points per second.** Basing your game strategy based on the amount of points you can gain per second (or even per game period), will help your team make the mechanical choices best for you!

Remember to always strategize and build within your resources! Not all teams will have access to the same resources, whether it is parts or people. A strategy that seems to yield the most points per second on paper may not be as successful as a strategy that focuses on maximizing accuracy.&#x20;

The following section will breakdown the major scoring achievements of the game as well as provide some of the strategic considerations, we at REV noticed. While this breakdown may provide you with a basic knowledge of this years game it is always advised to consult Game Manual Part 2 to better understand the rules.&#x20;

### Autonomous

#### Navigating

Most FTC games include some sort of navigation or parking task in the autonomous period. Typically, these are autonomous scoring achievements where a robot has moved to a particular portion of the field and parked there.&#x20;

This year there are four potential navigation achievements.&#x20;

|                      |                       |    |
| -------------------- | --------------------- | -- |
| Parked In            | Alliance Storage Unit | 3  |
| Parked Completely In | Alliance Storage Unit | 6  |
| Parked In            | Warehouse             | 5  |
| Parked Completely In | Warehouse             | 10 |

To understand the full break down of navigating, it helps to understand how Game Manual Part 2 defines **In** and **Completely in**. Once you have a grasp on how these concepts are defined you can make a decision about which navigation achievements will give you the most points per second, when compared against the rest of your autonomous strategy.&#x20;

In general, navigation during autonomous is a very achievable goal. While you may have to consider some obstacles, like the barriers, using our Hello Robot - Encoder Navigation guides for[ Blocks](/duo-control/hello-robot-blocks/welcome.md) and [Java](/duo-control/hello-robot-java/welcome.md), you can easily create the code needed to meet any of the navigation achievements.&#x20;

{% hint style="info" %}
This year we decided to take a look at how to navigate in autonomous. Check out our [Programming Autonomous](/ftc-kickoff-concepts/freight-frenzy-2021-2022/autonomous.md) guide for more information.&#x20;
{% endhint %}

#### Carousel

Each alliance's carousel starts with a duck placed on it in the pre-match setup. This duck can be delivered to the field by rotating the carousel. We tested the carousel and took a look at the rules to factor in all considerations for this scoring achievement.&#x20;

The first thing to take a look at is the rules constraining and defining carousel interaction and delivery. **Deliver** is a glossary term defined in section **4.4 Game Definitions** of Game Manual Part 2. Information on the carousel can be found in **Game Specific Rule 7 \<GS7>** and delivery restrictions are in **Game Specific Rule 9 \<GS9>** of Game Manual Part 2. One of our main concerns with the constraints, particularly in the autonomous period is that the definition of delivered specifically states that in order for a duck to be considered delivered "the Sweeper Plate must knock the Duck or Teams Shipping Element off of the carousel onto the playing field floor." Which implies that a properly delivered duck must enter the playing field by making contact with the sweeper plate.&#x20;

Paying attention to the rules for delivery is crucial for maximizing points per second. But why? After testing the carousel we quickly realized that the speed at which the carousel is rotated, affects whether the duck enters the playing field. Spin the carousel too fast and the duck flies off of the carousel before it can be knocked off by the sweeper plate. Finding the speed the carousel can be rotated that allows the duck to be properly delivered and maximize points per second is crucial for this scoring achievement.&#x20;

The final consideration we'd like to make is for traditional events. There is only one duck that is deliverable in autonomous. When also considering that travel time to the carousel affects the points per second of the delivery score, we think that going for this scoring achievement is maximized if your robot starts on the side of the field closest to the carousel.&#x20;

#### Autonomous Bonus

In Freight Frenzy the randomization factor includes being able to identify which Barcode position a duck (or Team Shipping Element) is in and using that information to correctly place the Pre-Loaded Box onto the correct level of the Alliance Shipping Hub.&#x20;

The following table highlights some of the ways to analyze the Barcode:

|                 | Accuracy                                               | Complexity                     |
| --------------- | ------------------------------------------------------ | ------------------------------ |
| Vuforia         | Most Accurate                                          | Complex                        |
| Distance Sensor | May loose accuracy depending on changes in environment | Complexity depends on use case |

While Vuforia will likely be easier to tune to the Duck game element over the Team Shipping Element, using the Team Shipping Element is worth more points.

#### Placing Freight

Each robot is required to start with a pre-loaded box. Even if you are unable to properly read the Barcode location at the start of the match, placing the pre-loaded box onto the same level every round, yields a 33% chance of getting the autonomous bonus. This is in addition to the points gained from placing a piece of freight on Alliance Shipping Hub, which is the same amount of points regardless of the level it is placed on. &#x20;

### Driver Controlled

Since the only scoring achievement in the Driver Controlled period is placing Freight in one of the designated areas the main strategy is efficiency and accuracy. As we said its always about maximizing points per second!&#x20;

#### Freight

The main scoring opportunity in the Driver Controlled period is placing Freight. A robot can control one freight at a time, per game specific rule \<GS8>. Score freight by placing freight completely in the Alliance Specific Storage Unit, on one of the levels of the Alliance Shipping Hub, or on the Shared Shipping Hub.&#x20;

There are a few considerations to make when deciding on your strategy for placing Freight:&#x20;

#### Balancing

At the end of the match additional points may be awarded depending on whether your Alliance Shipping Hub is balanced or the Shared Shipping Hub is unbalanced in your alliances favor. Understanding how to identify the weight difference, and decide how that may effect your strategy.&#x20;

#### GS5 and Warehouse Operations

Rule GS5 defines the expectations for each robot in regards to Warehouse Operations. In order for a Freight to be consider legally removed from the Warehouse, each piece of Freight must follow the Warehouse Operations

1. Start Completely Out of the Warehouse, then&#x20;
2. Drive Completely In the Warehouse, then&#x20;
3. Collect one (1) piece of Freight, then&#x20;
4. Drive Completely Out of the Warehouse with the collected Freight.&#x20;

### End Game&#x20;

During End Game you can continue to gain points by placing Freight or do one of the End Game specific tasks.&#x20;

#### Duck and Team Shipping Element Delivery

In end game, ducks and team shipping elements can be introduced to the field by rotating the carousel, similar to the autonomous task. Delivering a duck or team element is worth 6 points a piece. Removing the ducks from autonomous from the overall count, nine ducks (or team elements) can be scored in end game. That's a potential of 54 points in the end game period just for delivering ducks. Obviously this score is reliant on being able to score all nine in the end game period, which would require that the delivery process take around three seconds to complete per duck.&#x20;

#### Capping

Capping involves taking the Team Shipping Element and attempting to score it on top of the center pole above level 3, or on another capped team shipping element. Accuracy is key with this scoring achievement.&#x20;

#### Shipping Hub Status

Shipping Hub Status focuses on where the Shipping Hubs are at, at the conclusion of a match. If the Alliance Shipping Hub is balanced at the end of the match you receive 10 points. If the Shared Shipping Hub is Unbalance you receive 20 point.

After looking at Game Manual Part 2, we believe the best strategy for the Shared Hub is to try to maintain balance as you are placing objects. This way you do not have to scramble at the end of the match to try to balance it.&#x20;

#### Parking

Parking is also considered where the robot is at the end of the match. Calculating how long it would take you to get from one side of the field to the Warehouse will help you decide if the potential points per seconds are worth the points you would have to give up to park.&#x20;
