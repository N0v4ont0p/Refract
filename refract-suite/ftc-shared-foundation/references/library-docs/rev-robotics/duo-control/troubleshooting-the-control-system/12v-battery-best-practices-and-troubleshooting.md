> Source: https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/12v-battery-best-practices-and-troubleshooting.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/duo-control/troubleshooting-the-control-system/12v-battery-best-practices-and-troubleshooting.md).

# 12V Battery Best Practices and Troubleshooting

### Best Practices

1. When first picking up the [12V Slim Battery Charger](https://www.revrobotics.com/rev-31-1299/), you'll notice the switch on the top of the charger may be set to 0.9A. Setting the switch to 1.8A will increase the electrical current when charging your battery.
2. Plugging a battery that has been used into the charger will illuminate a red LED on the top. When the LED turns green, your battery is finished charging.
3. Before using your freshly charged battery, be sure to let the 12V Battery cool down as it may be warm from charging up. Once it acclimates to room temperature, it is safe to use.
4. To remove the battery from the Control Hub, try to avoid pulling on the XT30 sheathing. This can result in the XT30 solder points being exposed.

{% hint style="warning" %}
Do NOT use the 12V Slim Battery if the protective wire sheathing is fraying or severe damage is evident on the battery.
{% endhint %}

### Troubleshooting

1. If your battery isn't providing power to the Control Hub, check that:
   1. The XT30 connector isn't damaged or loose.
   2. There's no visible damage to the black and red wires.
   3. The fuse isn't tripped; carefully open the black fuse housing on the red wire to see if the fuse bridge is broken. If it is, simply remove the fuse and replace it with a new one.&#x20;
2. If you notice that your 12V Slim Battery isn't holding a charge as well as it used to, depending on how old it is, it could be time to replace it.

{% hint style="info" %}
12V Slim Battery fuses are common 20A fuses that can be purchased in auto stores or online.&#x20;
{% endhint %}
