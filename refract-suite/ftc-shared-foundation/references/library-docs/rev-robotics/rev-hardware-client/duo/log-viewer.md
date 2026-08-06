> Source: https://docs.revrobotics.com/rev-hardware-client/duo/log-viewer.md · Fetched: 2026-08-06 · Publisher-provided Markdown (REV serves a .md
> variant of every page, plus an llms.txt index) — not an HTML conversion.
> Exhaustive mirror (I2 sweep). FTC-relevant sections of a combined FRC+FTC+education
> site — see library-docs/_MIRROR-README.md for the scope boundary.

> For the complete documentation index, see [llms.txt](https://docs.revrobotics.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.revrobotics.com/rev-hardware-client/duo/log-viewer.md).

# Using the Log Viewer

When troubleshooting problems with the REV Control System log files provide indicators of what the status of the Control Hub or Expansion Hub were during an event. A look at the Robot Controller,  WiFi log, or Updater log may help you better understand the root cause of the issue.&#x20;

However the logs document all activities that the Control System performs, not just issues, but normal startup procedures or op mode runs. The means that logs often contain more information than can be reasonably sifted through. To make the content in the logs more palatable to sort through, the logs need to be parsed.&#x20;

The REV Hardware Client has a Log Viewer that makes it easier to parse overall log files. Through a series of filters, tags, and a search function makes it easy to see what is happening on the Control Hub or Driver Hub during any opmode run.

## Accessing the Log Viewer

To access the Log Viewer, head to the Utilities Tab.

![](https://gblobscdn.gitbook.com/assets%2F-M4_pJHI8HTuZFQTNfcy%2F-MgHHIm7SkZQ81_t1qfs%2F-MgHV9aAwLZOuFlhM7uS%2FHardware%20Tab%20-%20Utilities%20Tab%20Select.svg?alt=media\&token=c2d3712e-ff57-49b4-b12b-01ab0cb18698)

From there you can select and open log files for connected devices or for ones downloaded onto the computer.&#x20;

![](https://gblobscdn.gitbook.com/assets%2F-M4_pJHI8HTuZFQTNfcy%2F-MgHHIm7SkZQ81_t1qfs%2F-MgHVwfKsz160zA1qObL%2FUtilities%20Tab%20-%20Log%20Viewer%20Opened.svg?alt=media\&token=bba679e0-39cb-466f-8c6b-abcdab548a1a)

## Parsing the Logs

One of the most common issues that arises when trying to interpret logs is the wrong time and date on the Driver Hub or Driver Station phones. Ensuring that your Driver Station is set to the right time before observing or sending a log can help make data between the Robot Controller Log and Driver Station more interpretable. It also helps when observing a unique issue to pay attention to the time of the incident. If a problem or an indicator of a problem starts occurring at 4:38:57 PM then that time can be tracked in the logs to help determine what happened that initiated the issues.

Once you have confirmed the correct date and time you can use the Log Viewer to try to track the problem within the logs.&#x20;

If you select a connected device, such as a Control Hub, the Log viewer will give you an option to select standard logs or matches. Matches are segments of the robot controller log where a particular op mode is running. This is helpful to parse the data further by limiting the content to particular op mode runs that you know a system failure occurred during.&#x20;

![](/files/-MgLs50I5b5EIbPKSFeZ)

### Interpreting Filters

![](/files/-MgM1ZFVS5FEk8-BGc9P)

Aside from helping parse data down to specific time intervals the Log Viewer offers filters to select narrow down data in the logs to a particular type of data. The Log Viewer splits the data from the logs into six types: error, warning, info, fatal, debug, and verbose.&#x20;

#### Errors&#x20;

![](/files/-MgNDSGqWlP8M8wkuflr)

Errors occur when system actions do not execute properly. These log lines are typically indicative of a user created issues, such as errors in code, configuration, or wiring. For instance, in the image above the error is stating that it failed to calibrate the camera, which could be a sign that the USB Camera was detached from the Control Hub.&#x20;

Another common error you might see are compilation errors. These particular errors are the same error messages you receive in OnBot Java when you attempt to Build code and it fails.&#x20;

![](/files/-MgNCH8MxHHB-QqVy_h0)

#### Warnings

![](/files/-MgNF9hyhHqs0bb_gZRf)

When something none fatal occurs in the system, the system sends warning messages. Instances that warrant a warning message, do not cause the Control System to fail, but may cause unexpected behavior. This could be a warning about mismatched versions between the Robot Controller and Driver Station applications, or a warning that your Control System is not receiving enough power to function.&#x20;

#### Info

![](/files/-MgNIbISHQt2-jIzrvCA)

Info messages communication information that my be worthwhile to know for troubleshooting but not necessarily indicative of an issue. This is information like, when a program is initialized, started, or stopped.&#x20;

#### Fatal

![](/files/-MgR2FVIfL6uPomBwMzs)

Like Errors, Fatal actions occur when something within the system does not execute properly. However, fatal actions are indicative that something more severe is happening in a system. If you are having an issues and notice a lot of instances of the fatal data type, please send your [diagnostic data to REV,](https://docs.revrobotics.com/rev-control-system/managing-the-control-system/downloading-log-file#rev-hardware-client) with information on the issue you are having and the status LED behavior.

#### Debug

![](/files/-MgNJS1yO63LrRo85WiC)

The debug filter, showcases instances within the logs where debugging functions built into the SDK are performing their jobs. The Log Viewer defaults to filtering out debug information, as the information is typically not needed for troubleshooting.&#x20;

#### Verbose

![](/files/-MgQv-QBR4dW1cxMR0LK)

Many of the log types we have discussed thus far provide the insight needed to troubleshoot an issue. However, the logs track much more information than what falls in the other categories. The verbose log type covers the rest of the information included in the logs. This information is typically recording normal system behaviors that do not provide much insight to a problem.&#x20;
