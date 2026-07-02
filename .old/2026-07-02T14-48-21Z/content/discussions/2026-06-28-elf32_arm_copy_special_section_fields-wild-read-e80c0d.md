---
project: binutils
subsystem: binutils
patch_id: null
tags:
- bugfix
- arm
- elf
- security
- memory
discussion_id: akEfCcsYy1muyyf4@squeak.grove.modra.org
source_type: public_inbox
title: elf32_arm_copy_special_section_fields wild read
headline: elf32_arm_copy_special_section_fields wild read
tldr: Fix integer underflow bug in ARM ELF section handling that could lead to memory
  access errors.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Fixes an integer underflow in `elf32_arm_copy_special_section_fields`
  within `elf32-arm.c`. The loop control `i-- > 0` can result in `i` being -1u if
  the loop condition is false, leading to an invalid index `oheaders[-1u]`. The fix
  changes the loop control to `--i != 0` to ensure `i` is 0 on exit when the element
  is not found.
primer_general: This change fixes a bug in the binutils software that could cause
  incorrect memory access when processing ARM ELF files. Specifically, a loop within
  a function handling section fields could accidentally try to read data from an invalid
  memory location. The fix ensures that loops are controlled more safely, preventing
  potential crashes or data corruption.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/akEfCcsYy1muyyf4@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-28'
is_stub: false
stub_reason: ''
---

This patch corrects a potential bug in `elf32_arm_copy_special_section_fields` where loops controlling array access could result in an index of -1u. This could lead to out-of-bounds reads from the section header table. The fix modifies the loop conditions to prevent this underflow and ensure correct indexing.
