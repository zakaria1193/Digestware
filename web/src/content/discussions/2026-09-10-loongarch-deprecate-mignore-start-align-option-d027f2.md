---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- assembler
- GAS
- deprecated
- optimization
discussion_id: 20260910092253.526336-2-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH 1/3] LoongArch: Deprecate -mignore-start-align'
headline: 'LoongArch: Deprecate -mignore-start-align option'
tldr: Deprecates the -mignore-start-align option in LoongArch GAS as it's no longer
  needed.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Simplifies the assembler's option set by removing redundant functionality.
- Maintains backward compatibility by issuing a warning instead of immediate removal.
exchanges: []
primer_expert: This patch deprecates the `-mignore-start-align` option in the LoongArch
  GAS backend. This option previously existed to prevent GAS from optimizing alignment
  before the first relaxable relocation. However, subsequent changes have made this
  optimization the default behavior, rendering the option unnecessary. The patch now
  makes the option issue a warning and removes the associated internal `LARCH_opts.ignore_start_align`
  flag, simplifying the assembler's configuration.
primer_glossary:
- term: GAS
  definition: The GNU Assembler, a component of the GNU Binutils package that translates
    assembly language code into machine code.
- term: deprecated
  definition: Marked for removal in a future version. While still functional, its
    use is discouraged, and users should migrate to alternatives.
- term: linker-relaxable
  definition: A code fragment or instruction whose size or position can be adjusted
    by the linker during the relaxation phase to optimize code density or performance.
- term: relocation
  definition: A process performed by the linker or dynamic loader to resolve symbolic
    references between different object files or libraries. It involves adjusting
    addresses based on the final memory layout.
series_id: 'binutils:loongarch: deprecate -mignore-start-align'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260910092253.526336-2-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

The -mignore-start-align option for LoongArch's assembler (GAS) is deprecated and now only issues a warning. This is because the assembler's default optimization for alignment before the first relaxable relocation makes the special handling provided by this option redundant. The internal flag `LARCH_opts.ignore_start_align` has also been removed.
