---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- gas
- TLS
- relaxation
discussion_id: 20261113014322.37982-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: gas: Fix TLS LE relaxation with -mno-relax'
headline: 'LoongArch: gas: Fix TLS LE relaxation with -mno-relax'
tldr: Fixes an issue in LoongArch's gas assembler where incorrect TLS LE relaxation
  with -mno-relax could lead to wrong TLS addresses.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures correct TLS addressing with -mno-relax at the cost of potentially slightly
  less optimal code if relaxation would have been beneficial but was suppressed.
exchanges:
- author: zhaozhou <zhaozhou@loongson.cn>
  role: proposer
  position: Proposes a fix for incorrect TLS LE relaxation in LoongArch's gas assembler
    when -mno-relax is used.
  quote: With -mno-relax, GAS still emits R_LARCH_RELAX for le_add_r, but not for
    le_hi20_r or le_lo12_r. When linker relaxation is enabled, ld may delete the add.d,
    but the addi.d src-reg not write to TP, produce a wrong TLS address. Fix TLS LE
    only emit the le_add_r RELAX marker when LARCH_opts.relax is enabled.
primer_expert: The LoongArch gas assembler incorrectly emits a RELAX relocation for
  TLS LE sequences when the '-mno-relax' option is used. This occurs because the 'add.d'
  instruction, which is part of the sequence, might be optimized away by the linker,
  but the subsequent 'addi.d' instruction does not account for this change, leading
  to an incorrect target address for TLS variables. This patch conditionally emits
  the RELAX relocation only when linker relaxation is active.
primer_glossary:
- term: TLS LE
  definition: Thread-Local Storage (TLS) with Local Exec (LE) model. This refers to
    accessing thread-specific data in a way that is efficient for accesses within
    the same thread's execution context.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into machine code.
- term: linker relaxation
  definition: A linker optimization that allows the linker to adjust the size and
    addresses of instructions after the initial assembly. This can improve code density
    and performance but requires careful handling of relocations.
- term: RELAX relocation
  definition: A type of relocation used by linkers to indicate that an instruction's
    address or size might change during relaxation. The linker will then update the
    instruction accordingly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261113014322.37982-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-11-13'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the LoongArch assembler (gas) where the TLS LE relaxation process, specifically with the '-mno-relax' option, incorrectly emitted RELAX markers. This can cause the linker to produce incorrect TLS addresses when it attempts to optimize the 'add.d' instruction. The fix ensures that the RELAX marker for 'le_add_r' is only emitted when linker relaxation is actually enabled.
