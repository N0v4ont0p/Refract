> Source: https://rr.brott.dev/docs/v1-0/log-files/ · Fetched: 2026-08-06 · Retrieved as rendered HTML, converted to text
> Exhaustive mirror (I2 sweep). v1-0 only; v0-5 on the same site is superseded (see script header).
> No public/current doc repo exists for this source, so this is an HTML capture
> rather than an upstream-markdown copy — formatting is lossier than the
> repo-backed libraries in this corpus. Content is verbatim page text.

Log Files | Road Runner Docs

# 
 Log Files
 #

The quickstart logs data from every run to a file for later debugging. The most
recent logs that haven’t been deleted are accessible at
http://192.168.43.1:8080/logs.

Each log consists of a sequence of messages stored in a binary format. Each
message belongs to a channel (e.g., TARGET_POSE), and all messages on a given
channel adhere to a fixed schema. (This should be familiar to
anyone who’s worked with a typical robotics message-passing system.)

Users can add additional types by mimicking the quickstart message
definitions.
The code to turn classes into schemas can be found
here.

A basic Python parser can be found
here.