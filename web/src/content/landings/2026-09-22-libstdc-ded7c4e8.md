---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- regex
- optimization
- performance
commit_hash: ded7c4e851228c008304bad10d6b0aedc9deef3b
source_type: github
author: Tamar Christina
headline: 'libstdc++: Reject impossible regex DFS starts early'
tldr: Added a pre-check to libstdc++'s regex engine to quickly reject impossible match
  starting positions.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `_M_maybe_start_match` function now performs a conservative first-character
  pre-check before initiating the full DFS regex matching state machine. This check
  returns `false` only if all initial paths lead to a consuming match state that immediately
  fails or a dead end. It returns `true` for states that cannot be determined statically
  (e.g., backreferences), indicating that the normal executor should proceed. This
  avoids significant overhead on inputs with many non-matching start positions.
primer_glossary:
- term: DFS regex executor
  definition: The Direct Finite State Machine (DFS) implementation within libstdc++'s
    regex library that handles regular expression matching. It is optimized for certain
    patterns and execution paths.
- term: pre-check
  definition: An initial verification step performed before the main processing begins.
    In this case, it quickly determines if a given starting position in the input
    string could possibly lead to a regex match.
- term: backreferences
  definition: In regular expressions, a backreference allows a previously matched
    group (e.g., in parentheses) to be referred to later in the pattern. These can
    make static analysis of match possibilities difficult.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ded7c4e851228c008304bad10d6b0aedc9deef3b
date: '2026-09-22'
is_stub: false
stub_reason: ''
---

This commit introduces a pre-check to the DFS regex executor that examines the first character of a potential match. It rejects starting positions where no match is possible without building the full DFS state, which can be expensive. This optimization significantly speeds up regex searches, particularly for patterns like IPv4 addresses where many positions cannot possibly start a valid match.
