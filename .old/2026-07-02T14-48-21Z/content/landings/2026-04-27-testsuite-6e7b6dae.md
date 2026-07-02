---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- lto
- readelf
- regular expressions
commit_hash: 6e7b6dae6fa40fd98643bf1ac2f181baf1f4b741
source_type: github
author: Muhammad Kamran
headline: Testsuite Extended object-readelf to accept regexes.
tldr: The testsuite's object-readelf function now supports regular expressions for
  more flexible checks of object file metadata.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `object-readelf` function in `lib/lto.exp` is used to verify object
  file metadata within GCC's LTO testsuite.  Previously hardcoded to `readelf -A`,
  this commit broadens its utility by allowing testers to specify arbitrary `readelf`
  flags and regular expressions.  This avoids the need to write separate tests for
  checking notes or ensuring the absence of specific attributes.  The change touches
  `liblto`, a part of GCC not generally known outside the LTO team.
primer_general: The `readelf` utility displays information about object files, such
  as ELF files produced by the compiler.  The LTO (Link-Time Optimization) testsuite
  uses `object-readelf` to check the metadata of these object files, ensuring that
  the compiler is producing the correct information. This commit enhances `object-readelf`
  with regular expression matching, allowing more complex and flexible checks of object
  file contents.  Testers can now verify specific patterns in the `readelf` output,
  expanding the scope and precision of LTO tests.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6e7b6dae6fa40fd98643bf1ac2f181baf1f4b741
date: '2026-04-27'
---

The `object-readelf` function in `lib/lto.exp` was extended to support regular expressions. Previously, it was limited to attribute checks using `readelf -A`. Now, it accepts a `readelf` option and a regex, matching the regex against the full `readelf` output.  This allows for more flexible and comprehensive checks of object file metadata in LTO tests, including checks for notes and negative checks to ensure that a regex is not present in the output.
