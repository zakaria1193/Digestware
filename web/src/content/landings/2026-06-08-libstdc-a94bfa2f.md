---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- documentation
- style-guide
- libstdc++
commit_hash: a94bfa2fba3c7675724c1142789533b28076568e
source_type: github
author: Gerald Pfeifer
headline: 'Libstdc++: Spell command-line option with a dash'
tldr: Libstdc++ documentation now consistently uses "command-line option" with a dash
  for improved readability.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change in libstdc++'s documentation (specifically `libstdc++-v3/doc/xml/manual/abi.xml`)
  aligns its terminology with the broader GCC documentation style guidance. It consistently
  uses the hyphenated form "command-line option" instead of unhyphenated variants,
  and also simplifies language in some sections. This is a documentation-only change,
  impacting the presentation of information regarding the libstdc++ ABI to developers
  and not altering any code or functionality.
primer_general: Libstdc++ is the GNU Standard C++ Library, a fundamental component
  of the GNU Compiler Collection (GCC). Like GCC itself, libstdc++ has documentation
  that explains how to use it, including details about its 'Application Binary Interface'
  (ABI), which dictates how different compiled parts of a program can work together.
  This update is a minor but important cleanup of that documentation. It standardizes
  how a common term, 'command-line option,' is written—always with a hyphen (e.g.,
  `command-line-option` instead of `command line option`). This kind of consistency
  makes technical documents clearer and easier for developers to read and understand,
  reducing potential confusion.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a94bfa2fba3c7675724c1142789533b28076568e
date: '2026-06-08'
is_stub: true
stub_reason: low-score
---

This commit standardizes the terminology within the libstdc++ documentation, ensuring that "command-line option" is consistently spelled with a hyphen. Specifically, the `abi.xml` file, which describes the Application Binary Interface for libstdc++, has been updated to reflect this stylistic change. This improves clarity and consistency across the documentation, making it easier for developers to read and understand.
