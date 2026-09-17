---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- documentation
commit_hash: fffdaf05ca485db7c2aceed4f9defd66a107c71b
source_type: github
author: Jonathan Wakely
headline: 'libstdc++: Fix typo in comment in <bits/atomic_wait.h>'
tldr: Corrects a typo in a comment within a libstdc++ header file.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit corrects a typo in a comment within the `<bits/atomic_wait.h>`
  header. This is a documentation-only change for improved clarity.
primer_glossary:
- term: libstdc++
  definition: The C++ standard library implementation used by GCC. It provides core
    C++ language features like containers, algorithms, I/O streams, and threading
    support.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fffdaf05ca485db7c2aceed4f9defd66a107c71b
date: '2026-09-16'
is_stub: true
stub_reason: low_score
---

A typographical error in a comment located in the `<bits/atomic_wait.h>` header file of the libstdc++ library has been fixed. This change improves the accuracy of the code documentation.
