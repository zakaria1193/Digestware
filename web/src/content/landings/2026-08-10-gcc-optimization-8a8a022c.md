---
project: gcc
subsystem: gcc/optimization
patch_id: null
tags:
- optimization
- debugging
- gcc
commit_hash: 8a8a022c81b6105f70f72dfe2dc7b368353b49e6
source_type: github
author: Aldy Hernandez
headline: Add --param=dom-jump-threading to disable DOM jump threading
tldr: New compiler option allows disabling DOM jump threading for debugging.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: DOM jump threading is part of the dominator tree optimization framework.
  This change adds a tunable parameter to disable this specific threading mechanism,
  enabling finer-grained control for debugging and auditing its interaction with PRE
  and other optimizers. The parameter allows isolating regressions related to jump
  threading without disabling all DOM optimizations.
primer_glossary:
- term: DOM
  definition: Dominator Tree. A tree structure representing the control flow graph
    of a program, where a node dominates another if all paths from the entry to the
    second node must pass through the first.
- term: jump threading
  definition: An optimization technique that transforms control flow graphs by 'threading'
    jumps through conditional branches, simplifying paths and potentially enabling
    further optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8a8a022c81b6105f70f72dfe2dc7b368353b49e6
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

A new compiler parameter, --param=dom-jump-threading, has been introduced to selectively disable the jump threading optimization within the DOM (Dominator Tree) pass. This change facilitates debugging and isolation of issues by allowing developers to turn off this specific component of the DOM optimizer without affecting other DOM operations. It is intended to aid in the ongoing effort to untangle DOM's threading mechanism from the rest of the pass.
