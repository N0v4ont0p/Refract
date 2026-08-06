> Source: https://github.com/Pedro-Pathing/Docs/blob/531ad19facd351052d3353edacf96d4a1c489e4c/content/docs/pathing/custom/localizer.mdx · Fetched: 2026-08-06 · Ref: master @ 531ad19facd3 · Original format: mdx, content verbatim
> Exhaustive mirror (I2 sweep): every reachable doc file from this source is
> present, not a selection. Completeness is checked by corpus-input-scan.py.

---
title: Custom Localizer
---

You can create your own localizer by extending the `Localizer` class. 
This allows you to implement custom localization logic or different localization hardware that is not supported by the existing localizers.

### Hardware
All hardware should remain in the Localizer class. 
This ensures that the localizer can access the necessary hardware components directly.
For example, if you are using a custom sensor, you would initialize it in the constructor of your localizer class.

### Constants
It is suggested that you create a Constants class for your localizer.
This allows for easy configuration and modification of the localizer's parameters without changing the Localizer itself, although not required.
So, for a `CustomLocalizer`, you would create a `CustomLocalizerConstants` class.
In the `Constants` file, you would then create a `CustomLocalizerConstants` object and pass it to your localizer through the constructor.