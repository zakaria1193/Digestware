---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- gas
- relocations
- assembler
discussion_id: 20260930071709.1426943-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Emit relocations even after .option norelax'
headline: 'LoongArch: Emit relocations even after .option norelax'
tldr: Ensures LoongArch relocations are emitted even when relaxation is disabled.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Shifting the relocation emission logic from a global `norelax` check to a per-fragment
  check increases complexity but ensures correctness in edge cases.
exchanges: []
primer_expert: This patch addresses a bug in LoongArch's GAS where the `.option norelax`
  directive prevents the emission of relocations that would normally be subject to
  relaxation. The fix removes the global `LARCH_OPTS.relax` check within `_loongarch_force_relocation_sub_same`,
  ensuring that relocations are emitted based on their fragment coverage rather than
  the global relaxation state.
primer_glossary:
- term: relocation
  definition: Information in an object file that describes how to modify (relocate)
    certain memory addresses when the code or data is loaded into memory at a different
    address than the one it was compiled for. This is crucial for position-independent
    code and dynamic linking.
- term: .option norelax
  definition: An assembler directive that disables code or data relaxation for the
    target architecture. Relaxation is a process where the assembler adjusts instruction
    sizes or addresses to optimize code, and disabling it can be necessary for specific
    scenarios.
- term: relax fragment
  definition: A section of code or data within an object file that is subject to relaxation
    by the assembler. The assembler may modify addresses or instruction sizes within
    these fragments to achieve optimizations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930071709.1426943-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch corrects an issue in the LoongArch assembler (gas) where relocations spanning a relax fragment were not emitted when `.option norelax` was active. The fix removes a global check for relaxation status in `_loongarch_force_relocation_sub_same`, instead relying on the relocation's coverage of a relax fragment to determine if it should be emitted.
