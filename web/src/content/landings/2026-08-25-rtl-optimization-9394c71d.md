---
project: gcc
subsystem: rtl-optimization
patch_id: null
tags:
- rtl-optimization
- aarch64
- lra
commit_hash: 9394c71d36980a0abf1502be26608d6055893ed6
source_type: github
author: Kyrylo Tkachov
headline: 'lra: Canonicalize whole-address reloads'
tldr: Ensures correct instruction selection for addresses involving multiplications
  in the AArch64 reloader.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In the AArch64 backend's instruction reloader (LRA), addresses containing
  a multiplication by a power of two, when combined with other address components
  (e.g., a base register offset), could be problematic. The `reload_inner_addr` path
  would pass such an address directly to `lra_emit_move`, resulting in an RTL expression
  like `(mult:DI (subreg:DI ...) (const_int 8))`. This form, outside of specific address
  contexts like prefetch, is not directly instruction-generated. LRA's `lra_set_insn_recog_data`
  would fail because the generated `SET` did not match any instruction. This commit
  resolves th…
primer_glossary:
- term: LRA
  definition: Local Register Allocation. A compiler phase that assigns physical machine
    registers to virtual registers used in the intermediate representation of the
    code, aiming to minimize memory spills.
- term: reload
  definition: In register allocation, a 'reload' operation is inserted when a value
    needed by an instruction is not currently in a register and must be loaded from
    memory.
- term: canonicalize
  definition: To transform an expression or value into a standard or preferred form.
    In this context, it means converting a multiplication by a power of two into an
    equivalent bit-shift operation for better instruction recognition.
- term: RTL
  definition: Register Transfer Language. GCC's primary intermediate representation,
    which describes operations on registers and memory.
- term: AShIFT
  definition: Arithmetic Shift Left. An RTL construct representing a bitwise left
    shift operation, often used as a canonical form for multiplication by powers of
    two.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9394c71d36980a0abf1502be26608d6055893ed6
date: '2026-08-25'
is_stub: false
stub_reason: ''
---

GCC's instruction reloader (LRA) on AArch64 had issues recognizing addresses that involved a multiplication by a power of two, especially when this multiplication was part of a larger address calculation. The reloader would incorrectly generate a `SET` instruction for this part of the address, which didn't match any available instruction, causing LRA to fail. This commit introduces a call to `canonicalize_reload_addr` to convert such multiplications into a canonical left-shift form (`AShIFT`), which LRA can then correctly recognize and emit the appropriate instruction. This fixes PR127056.
