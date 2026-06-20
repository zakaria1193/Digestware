---
project: binutils
subsystem: risc-v/bfd
patch_id: null
tags:
- risc-v
- bfd
- attributes
- stack alignment
- warnings
discussion_id: 2fcf62ca-0e51-48fc-a9cf-7a48a40dc82e@suse.com
source_type: public_inbox
title: '[PATCH v3 13/13] RISC-V/bfd: warn about non-power-of-2 stack-align attribute'
headline: 'RISC-V/bfd: warn about non-power-of-2 stack-align attribute'
tldr: Binutils BFD will now warn and ignore `Tag_RISCV_stack_align` values that are
  not powers of two, as only such values are sensible for alignment.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces new warnings for developers using incorrect `stack_align` attributes.
- Implicitly converts invalid non-power-of-2 `stack_align` values to 0 or another
  default, potentially changing expected behavior silently (though a warning is issued).
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes to introduce warnings and ignore `Tag_RISCV_stack_align` attributes
    in BFD that are not power-of-two values, as non-power-of-two alignments are nonsensical.
  quote: Only power-of-2 values are sensible for alignment. Reject other values.
primer_expert: In the RISC-V `bfd` library, specifically `bfd/elfxx-riscv.c`, the
  `riscv_merge_attributes` function is responsible for consolidating object attributes
  during linking. The `Tag_RISCV_stack_align` attribute (Tag 4) specifies the required
  stack alignment. This patch modifies the attribute merging logic to explicitly check
  if the incoming or existing `Tag_RISCV_stack_align` value is a power of two using
  a bitwise `(& (value - 1))` check. If it's not, a warning is emitted through `_bfd_error_handler`,
  and the invalid attribute value is either ignored (set to 0) or converted to a default
  valid val…
primer_general: This patch makes sure that software for RISC-V processors uses proper
  memory alignment for the stack. The "stack" is a reserved area of memory where a
  program stores local variables and function call information. To access this memory
  efficiently, it needs to be aligned to a specific boundary, which is typically a
  "power of two" number (like 2, 4, 8, 16, etc.). The binutils toolchain (which includes
  the linker, `bfd`) uses attributes to describe properties of the code, such as stack
  alignment. This change to the `bfd` component of binutils will now issue a warning
  and ignore any `stack_align` attribute that specifies an alignment that isn't a
  power of two, because such values don't make sense for memory alignment and could
  lead to inefficient code or crashes. This helps ensure that programs built for RISC-V
  are robust and performant.
series_id: 'binutils:risc-v/bfd: warn about non-power-of-2 stack-align attribute'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/2fcf62ca-0e51-48fc-a9cf-7a48a40dc82e@suse.com
bugzilla_url: null
date: '2026-06-19'
is_stub: false
---

This patch for RISC-V BFD modifies `riscv_merge_attributes` to enforce correct `Tag_RISCV_stack_align` values. It introduces a warning and ignores any `stack_align` attribute that is not a power-of-two, as only such values are valid for memory alignment. The change also tidies up a redundant conditional part in the attribute merging logic.
