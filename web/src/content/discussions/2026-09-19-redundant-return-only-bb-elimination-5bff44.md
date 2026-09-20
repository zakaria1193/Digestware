---
project: gcc
subsystem: gcc
patch_id: null
tags:
- optimization
- cfg
- riscv
discussion_id: aq7cmLNnJVp9Bzy9@bertguix
source_type: public_inbox
title: 'Re: [RISCV] redundant return-only BB not eliminated'
headline: Redundant return-only BB elimination
tldr: Proposes a patch to eliminate redundant return-only basic blocks in CFG cleanup.
proposer: Robert Guthrie <forkbombidable@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Potential for introducing regressions in specific edge cases (e.g., verbatim asm
  diffs) while optimizing CFG.
- Ensuring correct handling of CFG RTL modes is complex.
exchanges: []
primer_expert: This patch modifies cfgcleanup.cc to optimize the control flow graph
  by removing redundant basic blocks that solely contain a return instruction. It
  aims to improve code efficiency by merging such blocks, redirecting predecessors
  to a single return block. The challenge lies in correctly handling CFG RTL modes
  during this optimization.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/aq7cmLNnJVp9Bzy9@bertguix
bugzilla_url: null
date: '2026-09-19'
is_stub: false
stub_reason: ''
---

Robert Guthrie proposes a new patch to address the elimination of redundant return-only basic blocks. This change aims to simplify the control flow graph by merging consecutive blocks that only contain a return instruction. The patch passes most tests, with a minor noted issue on a verbatim asm diff.
