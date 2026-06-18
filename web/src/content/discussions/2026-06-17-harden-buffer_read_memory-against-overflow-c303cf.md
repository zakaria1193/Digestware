---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- buffer-overflow
- disassembler
- binutils
discussion_id: ajMz7izBu9fnpXhi@squeak.grove.modra.org
source_type: public_inbox
title: buffer_read_memory hardening
headline: Harden buffer_read_memory against overflow
tldr: Rewrites buffer overflow checks in `buffer_read_memory` to prevent truncation
  issues and addition overflows, improving robustness.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Increased code complexity in comparison to the original bounds checking logic due
  to explicit overflow checks, though this is outweighed by the improved safety.
exchanges:
- author: Alan Modra
  role: proposer
  position: Proposes to rewrite buffer overflow checks in `buffer_read_memory` to
    prevent truncation and addition overflows.
  quote: What drew my attention here was wondering if division of the buffer length
    or the requested length by octets_per_byte could result in trucation and thus
    an incomplete check for possible buffer overflow. Rather than convincing myself
    that this couldn't happen, I decided to rewrite the checks in a way that avoids
    the possibility of truncation, and avoids any addition overflows too.
primer_expert: This patch targets `opcodes/dis-buf.c`, specifically the `buffer_read_memory`
  function used by the disassembler. The change modifies the logic for calculating
  memory offsets and lengths to avoid intermediate truncation errors and addition
  overflows when `octets_per_byte` is involved. This ensures that the buffer boundary
  checks are accurate, preventing potential out-of-bounds reads during disassembly,
  which could lead to crashes or security vulnerabilities. The fix introduces `_bfd_mul_overflow`
  to safely perform multiplication checks.
primer_general: This change enhances the safety of `buffer_read_memory`, a function
  within Binutils that helps disassemble (reverse engineer machine code into human-readable
  assembly) programs. This function reads portions of a binary program from a buffer
  in memory. The patch fixes calculations that determine if a requested read operation
  would go beyond the allocated buffer, potentially causing a 'buffer overflow.' Such
  overflows can lead to crashes or, in some cases, security vulnerabilities where
  malicious code could exploit them. The update makes these calculations more robust
  by preventing issues that could arise from integer division or addition, ensuring
  the disassembler reads only within the safe bounds of its memory buffer.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ajMz7izBu9fnpXhi@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-17'
is_stub: false
---

This patch hardens the `buffer_read_memory` function by rewriting its buffer overflow sanity checks. The change aims to prevent potential truncation issues during division operations and to avoid addition overflows, which could lead to incomplete checks. This improves the overall robustness and security of the function by ensuring more reliable boundary checks.
