---
project: gcc
subsystem: gcc/libstdc++
patch_id: null
tags:
- libstdc++
- documentation
- compiler flag
commit_hash: eda0f2f0ccc76dfcce0a4d8350611039b0762e05
source_type: github
author: Jonathan Wakely
headline: 'Libstdc++: Update documentation about default -std option.'
tldr: The libstdc++ documentation now correctly describes the default value for the
  ``-std`` compiler option.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies ``doc/xml/manual/using.xml`` (specifically the
  ``Flags`` section) and regenerates ``doc/html/manual/using.html`` to update the
  description of the default value for the ``-std`` compiler option.
primer_general: This commit updates the libstdc++ documentation to clarify the default
  value of the ``-std`` compiler flag. The ``-std`` flag tells the compiler which
  version of the C++ standard to use when compiling code (e.g., C++11, C++17, C++20).  This
  change ensures the documentation accurately reflects the compiler's default behavior
  if no ``-std`` flag is provided.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/eda0f2f0ccc76dfcce0a4d8350611039b0762e05
date: '2026-04-28'
is_stub: true
stub_reason: low-score
---

The libstdc++ documentation has been updated to accurately describe the default value for the ``-std`` compiler option. This option controls the C++ standard used by the compiler. The update ensures that users understand how the compiler interprets their code by default.
