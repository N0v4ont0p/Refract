> Source: https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/game-piece.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/ftc-kickoff-concepts/freight-frenzy-2021-2022/game-piece.md).

# Game Elements

{% embed url="<https://www.youtube.com/watch?v=rTR5im2l5IY>" %}

## Freight

This years game comes with a series of different game elements that fall into the Freight category: Cargo, Boxes, and Ducks. Each type of freight varies in size, shape, and material, which may effect mechanism design. An added challenge to calculate for  is that boxes come in three different weight classes.&#x20;

### Cargo

![](/files/-MglJpAb8dlwJmbFkzaR)

Cargo is a standard Wiffle Ball, used in past seasons of FTC (such as Rover Ruckus). From past seasonwe know that the material for the cargo is going to be a rigid plastic.&#x20;

| Diameter | Weight  | Quantity on Field |
| -------- | ------- | ----------------- |
| 2.75 in  | 1.8 oz. | 20                |

### Boxes

Boxes (also known as an FTC Blocks) are also making a reappearance this season along with the Wiffle Ball. Boxes are 2" x 2" x 2" cubes made of polypropylene, a rigid plastic material.&#x20;

![](/files/-MglQaCAsXWXroqbkweO)

One of the key components of Boxes is that they come in different weight classes: Light, Medium, and Heavy. Pre-load Boxes fall in the same weight class as Light Boxes

| Box Type | Weight | Quantity on Field |
| -------- | ------ | ----------------- |
| Pre-Load | 0.9 oz | 4                 |
| Light    | 0.9 oz | 26                |
| Medium   | 3.3 oz | 20                |
| Heavy    | 4.8 oz | 10                |

Box weights can have a massive advantage in the balancing or unbalancing of the Shipping Hub. It will also affect mechanism design as you will have to account for any additional work your mechanism will have to perform to pick and place one of the heavier boxes.&#x20;

### Ducks

Ducks are somewhat of an outlier this season. From what we can tell they are a standard rubber duck, which makes the much more pliable than the other game elements. When designing for a mechanism you may need to do additional intake testing.

| Height    | Width  | Length | Weight | Quantity on Field |
| --------- | ------ | ------ | ------ | ----------------- |
| 2.2125 in | 2.0 in | 2.0 in | 0.6 oz | 20                |

## Shipping Hubs

In Freight Frenzy there are two Game Elements under the classification of Shipping Hub. Both the Alliance Shipping Hub and the Shared Shipping Hub, are 21" tall, structures, that balance on on a rounded base. On of the key objectives of gameplay is the status of the Shipping Hubs at the end of each match. To gain this scoring achievement the Alliance Shipping Hub must be balanced and the Shared Shipping Hub must be unbalanced in the favor of your alliance

### Alliance Shipping Hub

![](/files/-MglvMNFQbXCLBWcAgri)

The Alliance Shipping Hub has three scoring levels, for placing freight. The image above explains the diameter of each level as well as its distance from the playing field floor. This information is good to know for design of a Freight delivery mechanism. However, one other consideration to make is the difference in diameter between each level.&#x20;

![](/files/-MglvrsZ7Sux9KAQSu6U)

For instance, level 1 and level 2 have a 3 inch different in diameter. Which means that, since all levels are centered around a center pole, level 1 and level 2 have a difference of 1.5 inches all the way around the Shipping Hub. A robot will need to be able to account for the difference when attempting to reach another level.&#x20;

Finally, the dimensions surrounding the top of the center pole of the Shipping Hub are need to calculate for capping a Team Shipping Element. After some analysis, we believe one of the best designs for a Team Shipping Element would be to create something that can be capped on the 1.3" diameter of the center pole, while also have roughly the same dimensions so that it can be easily capped on top of.&#x20;

### Shared Shipping Hub&#x20;

![](https://lh4.googleusercontent.com/-vPz6p6IWllNjzpQYvFKS9Kcn4akr4TwWiotQ6xxWsDfDpdnDcKbm7aEDB2iENukvko7RW1X8Qo1XQm3JBg6tqUYniQ_giaW5Ua8iRNzkwL536TgVPwxHAynuYLQ1qbVo63fA6Y)

Unlike the Alliance Shipping Hub, the Shared Hub only has one scoring level. The focus with this particular Shipping Hub is unbalancing it in your alliances favor.&#x20;

## Carousel

The Carousel is an alliance specific Game Element located in the corner of the Audience Side and Alliance Station Side of the field. To deliver ducks to the field, a robot must rotate the carousel until the sweeper plate knocks the duck onto the field. Robots can only interact with the rim of the carousel in order to rotate it.&#x20;

![](/files/-MgqhquYqCCSwOA9U6Eg)

The carousel spins with relative ease. The main issue with the carousel and duck delivery is the risk of ducks falling off of the carousel before they are pushed off by the sweeper plate. This happens when the carousel spins too quickly, flinging the duck off of carousel. We discussed the considerations for this in the [Game Breakdown ](/ftc-kickoff-concepts/freight-frenzy-2021-2022/game-strategy.md#carousel)section.&#x20;

## Barriers

Another Challenge of Freight Frenzy are the Barriers. In order to access the Warehouses and the Shared Shipping Hub, robots must cross over the barriers or move through the 13.7" to 13,75" space between the edge of the barrier and the field wall.&#x20;

![](/files/-MgqR6nAEyretGtX5jPZ)

Each Barrier is made up of two poles connected by the end pieces as shown above. Somethings to be aware of when deciding on your drivetrain design:

* The Center to Center Distance between poles (4.5 inches)
* The Distance from the playing field floor to the top of the poles (1.26 inches)
* The distance from the playing field floor to the top of the end pieces (2.2 inches)
