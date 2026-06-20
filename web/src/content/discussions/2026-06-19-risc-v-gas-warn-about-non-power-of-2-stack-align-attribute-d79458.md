---
project: binutils
subsystem: risc-v/gas
patch_id: null
tags:
- risc-v
- gas
- attributes
- stack alignment
- warnings
discussion_id: 70bdd397-4326-4c00-841b-7e4a57c82919@suse.com
source_type: public_inbox
title: '[PATCH v3 11/13] RISC-V/gas: warn about non-power-of-2 stack-align attribute'
headline: 'RISC-V/gas: warn about non-power-of-2 stack-align attribute'
tldr: The GNU Assembler for RISC-V will now warn about `stack_align` attributes with
  values that are not powers of two, as only such values are sensical for alignmen…
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces new warnings for developers using incorrect `stack_align` attributes,
  which may require updates to existing build systems or assembly code.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes to introduce warnings in the RISC-V GNU Assembler for `stack_align`
    attributes that are not power-of-two values, as such values are not sensical for
    memory alignment.
  quote: Only power-of-2 values are sensible for alignment.
primer_expert: In the RISC-V `gas` backend, specifically `gas/config/tc-riscv.c`,
  the `s_riscv_attribute` function processes `.attribute` directives. The `Tag_RISCV_stack_align`
  attribute (Tag 4) specifies required stack alignment. The problem arises when an
  assembler directive attempts to set this attribute to a value that is not a power
  of two, such as `0x4444`. From a hardware and ABI perspective, stack alignment typically
  requires power-of-two values for efficient memory access. This patch introduces
  a check `(!attr[Tag_RISCV_stack_align].i || (attr[Tag_RISCV_stack_align].i & (attr[Tag_RISCV_stack_align…
primer_general: This discussion is about a change to `gas`, which is the assembler
  for RISC-V processors (a part of the binutils toolchain). The assembler translates
  human-readable assembly code into machine code. One of the things assembly code
  can specify is how the program's "stack" should be aligned in memory. The stack
  is a dedicated region of memory that programs use to store temporary data, like
  local variables. For a computer to work efficiently, especially with memory, data
  often needs to be aligned to specific boundaries, which are always "power of two"
  numbers (like 2, 4, 8, 16, etc.). This patch makes `gas` smart enough to recognize
  if a developer tries to specify a `stack_align` attribute that isn't a power of
  two. If it finds such a value, it will now issue a warning to the developer, helping
  them catch potential errors and ensuring that programs for RISC-V are built with
  correct and efficient memory layouts.
series_id: 'binutils:risc-v/gas: warn about non-power-of-2 stack-align attribute'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/70bdd397-4326-4c00-841b-7e4a57c82919@suse.com
bugzilla_url: null
date: '2026-06-19'
is_stub: false
---

This patch for the GNU Assembler (`gas`) on RISC-V introduces a warning for `stack_align` attributes that specify a value which is not a power of two. This ensures that developers are notified when using semantically incorrect alignment values, as proper memory alignment fundamentally requires power-of-two values. The patch also includes a test case to verify the warning behavior.
