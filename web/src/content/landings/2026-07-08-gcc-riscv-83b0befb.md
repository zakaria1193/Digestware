---
project: gcc
subsystem: gcc/riscv
patch_id: null
tags:
- risc-v
- scheduling
commit_hash: 83b0befb611af61e0b4efbbc0ee235fe773ae891
source_type: github
author: Jim Lin
headline: 'RISC-V: Fix dead cpop reservation for spacemit-x60'
tldr: Corrects a RISC-V instruction scheduling bug where the cpop instruction was
  not using its intended latency.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `spacemit-x60.md` instruction pattern for RISC-V had conflicting
  reservations for the `cpop` instruction. It was listed in `spacemit_x60_alu` (latency
  1) and a more specific `spacemit_x60_alu2c` (latency 2). Due to the order of pattern
  matching, `cpop` always hit the former, causing it to be scheduled with the wrong
  latency. This change removes `cpop` from `spacemit_x60_alu` to ensure the `spacemit_x60_alu2c`
  reservation is used.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/83b0befb611af61e0b4efbbc0ee235fe773ae891
date: '2026-07-08'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in the RISC-V backend where the 'cpop' instruction was incorrectly assigned a latency of 1 due to a flawed reservation definition. It was being matched by a more general ALU reservation, leaving a dedicated 2-cycle reservation unused. By removing 'cpop' from the general ALU reservation, the compiler now correctly schedules it with its intended 2-cycle latency.
