---
project: binutils
subsystem: binutils/opcodes
patch_id: null
tags:
- security
- disassembler
- buffer-overflow
commit_hash: b81d60ecd1b5ffadd80f51d0d387de3762f47b46
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Buffer read memory function adds hardening against overflows
tldr: Binutils' `buffer_read_memory` function now includes more robust checks to prevent
  buffer overflows during memory reads.
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `buffer_read_memory` function within `opcodes/dis-buf.c` retrieves
  instruction bytes for disassembly. This patch enhances the defensive programming
  around memory access, specifically targeting buffer overflow vulnerabilities. It
  addresses edge cases where `length` or `buffer_length` division by `octets_per_byte`
  could lead to truncation, resulting in incomplete bounds checks. The rewritten checks,
  particularly `_bfd_mul_overflow`, explicitly detect multiplication overflows and
  prevent erroneous address calculations, thereby mitigating potential exploits that
  rely on crafted input to trigg…
primer_general: Disassemblers are tools that convert machine code (the raw instructions
  a computer understands) back into human-readable assembly code. To do this, they
  need to read chunks of memory. This update hardens a function called `buffer_read_memory`
  in the Binutils disassembler. Previously, there was a theoretical risk that if the
  disassembler tried to read a very large or oddly structured piece of code, it might
  miscalculate the boundaries of the memory it was allowed to access, potentially
  leading to a "buffer overflow." A buffer overflow is a security vulnerability where
  a program writes past the end of a designated memory buffer, which can be exploited
  by malicious actors. This change implements more rigorous checks to prevent such
  miscalculations, making the disassembler more secure and robust when processing
  unusual or potentially malicious input files.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260617235605.443D54BA2E33@sourceware.org
date: '2026-06-17'
is_stub: false
---

The `buffer_read_memory` function in `opcodes/dis-buf.c`, used by the disassembler, has been refactored to include hardened buffer overflow sanity checks. The new checks use explicit multiplication overflow detections to ensure that calculations for memory access boundaries are accurate and prevent potential vulnerabilities arising from integer truncation or overflow in address computations. This improves the security and reliability of the disassembler when handling potentially malformed inputs.
