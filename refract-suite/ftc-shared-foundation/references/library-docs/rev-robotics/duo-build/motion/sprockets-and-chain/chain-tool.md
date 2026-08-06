> Source: https://docs.revrobotics.com/duo-build/motion/sprockets-and-chain/chain-tool.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-build/motion/sprockets-and-chain/chain-tool.md).

# Chain Tool

Creating a loop of chain requires breaking off the correct number of links by removing a specific chain pin and joining the ends together. Chain can be broken using many methods, including a Chain Tool or various steel cutting blades, like a dremel. Once you have counted the number of links necessary for your application, the chain can be joined using a master link or by replacing the chain pin.

## #25 Chain Tool Basics

This custom-designed #25 Chain Tool ([REV-41-1442](https://www.revrobotics.com/rev-42-1442/)) also commonly referred to as a "chain break" or "chain breaker", allows teams to easily break and re-assemble #25 Chain ([REV-41-1365](https://www.revrobotics.com/rev-41-1365/)). The mandrel is used to push out the chain pin. If using Master Links ([REV-41-1366](https://www.revrobotics.com/rev-41-1366-pk5/)), the pin can be completely removed, but the depth guide screw allows the option of partially pressing out the pin and then re-assembling without master links.

![](/files/-M8HfLA3EUeGfN9mch84)

### Kit Contents&#x20;

The REV Robotics #25 Chain Tool ([REV-41-1442](https://www.revrobotics.com/rev-41-1442/)) comes with the following:

* 1 Chain tool block
* 2 set screw mandrels
* 1 depth guide screw
* 1 cup point set screw
* 1 4mm Allen Wrench

{% embed url="<https://www.youtube.com/watch?v=Y4Ur0f5kra8&>" %}

{% hint style="danger" %}
Before using the #25 Chain Tool for the first time, remove the thread pin screw and use WD-40 or compressed air to remove any shavings left in the tool from the manufacturing process. This will ensure the chain break works smoothly and efficiently breaks your chain. Reinstall the thread pin screw. Once this is complete the chain break is ready for use.
{% endhint %}

## Manipulating Chain&#x20;

In almost all applications, chain links are connected to form a loop. While chain can sometimes be purchased in specific length loops, it is more common and economical to buy chain by the foot and make custom loop lengths to fit the application. It’s recommend to use a specialized tool, a chain breaker, to cut chain into desired lengths to prevent accidental damage.

Chain breakers do not actually cut the chain, instead they are used to press out the pins from an outer link. After the pins have been removed the chain can be separated leaving inner links on both ends of the break.&#x20;

{% hint style="info" %}
Chain Tools have two methods for resetting chain. Using Master Links and resetting the chain pin. Resetting the pin is results in a stronger chain than using a master link.
{% endhint %}

### Master Links

Roller chain is typically connected into a continuous loop. This can be done using a special tool to press the pins in and out of the desired outer link as described in the Custom Length Chain section, or if the chain is already the correct length a common roller chain accessory called a master link, or quick-release link, can be used to connect two ends of the chain.

![](/files/-M9ZHmV4JO45-5f94ULQ)

Master links allow for easy chain assembly/disassembly without any special chain tools. Master links can typically be reused many times, but can become bent with multiple uses. At the point that master links become bent they should be discarded.

#### Steps to using a master link&#x20;

1. Place the loose outer plate onto the two pins pressed into the other outer plate.
2. Ensure the outer plate is inserted onto the pins far enough that the grooves on the pins are fully exposed past the outer plate.
3. Align the widest gap near the middle of the clip with one of the pins.
4. The gap in the clip should allow the clip to slip over the pin and sit flush against the outer plate and aligned with the groove in the pins.
5. Use pliers or another tool to slide the clip towards the other pin until the clip is securely engaged with the grooves on both pins.

![](/files/-M9ZHmV5TRJOW5kxBd7l)

{% hint style="info" %}
Installing the clip as shown in Steps 4 and Step 5 can be sometimes difficult.

There are a number of approaches that may work for these steps, but a common method is to use a pair of needle nose pliers to grip between the back of the clip and the nearest pin to slide the clip.
{% endhint %}

![](/files/-M9ZHmV62sZfi3pZ5BmH)

Master links are used to connect two ends of a section of chain to create a loop of chain. In order to use a master link, the chain ends should both terminate with inside links. Slide the two pins from the master link into the rollers of the two terminating inside links. Follow the [recommended procedure](/duo-build/motion/sprockets-and-chain.md#steps-to-using-a-master-link) to complete the link installation.

![](/files/-M9ZHmV7gSFYnhUQIydp)

## Using the Chain Tool&#x20;

Roller chain is typically connected into a continuous loop. This can be done using a special tool to press the pins in and out of the desired outer link as described in the [Resetting Chain Pins](https://docs.revrobotics.com/ion-build-system/motion/sprockets-and-chain/chain-tool#resetting-chain-pins) section, or, if the chain is already the correct length, a common roller chain accessory called a master link, or quick-release link, can be used to connect two ends of the chain.

### Resetting Chain Pins

<table data-header-hidden><thead><tr><th width="382"></th><th></th></tr></thead><tbody><tr><td>1) Unscrew the Pin Screw and Compression Screw such that the chain channel is free of obstructions.<br></td><td><img src="/files/877q0uysYaz3xopz2Fa8" alt="" data-size="original"></td></tr><tr><td><p></p><p>2) Insert #25 chain (REV-41-1365) into the chain channel and align the desired link between the two pins above the Cup Point Set Screw.</p></td><td><img src="/files/PGGn4Xl4hGhlxu4oTPpW" alt="" data-size="original"></td></tr><tr><td><p></p><p>3) Secure the chain in place with the Compression Screw using the Allen Wrench. Tighten until the chain cannot shift within the channel.</p></td><td><img src="/files/5TflQDTErwcZYjd8vuL6" alt="" data-size="original"></td></tr><tr><td><p>4) Put the Allen Wrench into the Pin Screw and tighten until the pin almost touches the Cup Point Set Screw. You should stop pushing the pin out before it leaves the back plate of the outer links.</p><p></p><p>Considerable pressure will be felt before the pin comes out, but removing the chain from the tool occasionally during the process to check if the pin is unseated from the bushing is recommended.</p><p></p><p>The final result should be the pin still partially connected to the chain, as seen in the second photo.</p></td><td><img src="/files/XOq6tcxf38eEroajIrbY" alt="" data-size="original"><img src="/files/kM2yDuCOfanwZcYrcyVJ" alt=""></td></tr><tr><td><p></p><p>5) Unscrew the Compression Screw until the channel is empty, and place the unseated pin and outer plates into the open channel. Place the desired empty inside link in between the outer plates and unseated pin.</p></td><td><img src="/files/Cyfgkw51TWDFgILFZKy8" alt="" data-size="original"></td></tr><tr><td><p></p><p>6) Tighten the Compression Screw using the Allen Wrench until the pin is reseated</p></td><td><img src="/files/63mIosNpPNd7baiBLKHc" alt="" data-size="original"></td></tr><tr><td>7) Once the pin is fully reseated, release the chain from the tool using the Allen Wrench- your chain should be connected!</td><td><img src="/files/2CGlyzjESVm5Sq1jsZAV" alt="" data-size="original"></td></tr></tbody></table>
