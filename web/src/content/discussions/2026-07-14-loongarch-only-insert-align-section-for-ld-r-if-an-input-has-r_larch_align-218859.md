---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- linker
- loongarch
- relocation
- kernel
- binutils
discussion_id: 20260714114920.585718-1-xry111@xry111.site
source_type: public_inbox
title: 'LoongArch: only insert align section for ld -r if an input has R_LARCH_ALIGN'
headline: 'LoongArch: only insert align section for ld -r if an input has R_LARCH_ALIGN'
tldr: Fixes LoongArch linker behavior when using `ld -r` to avoid inserting align
  sections unnecessarily, preventing kernel module loading issues.
proposer: Xi Ruoyao <xry111@xry111.site>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: 7
technical_tradeoffs:
- Making the insertion of align sections conditional improves linker behavior for
  specific use cases like kernel modules.
- Ensuring compatibility with environments that have strict requirements on the presence
  or absence of certain relocations.
exchanges:
- author: Xi Ruoyao <xry111@xry111.site>
  role: proposer
  position: Submits a patch to conditionally insert an align section in `ld -r` for
    LoongArch, fixing a regression that broke kernel modules.
  quote: 'Commit 8bf4b69718d4 ("LoongArch: Fix relaxation alignment with ld -r (PR

    33236)") has broken the kernel modules on Debian sid.  The expectation

    of the kernel is all the source files which would be linked into a

    module are compiled with -mno-relax so the module should not contain

    R_LARCH_ALIGN, thus the module loader rejects any module containing

    R_LARCH_ALIGN.'
primer_expert: This is a revised patch (v2) addressing a regression in LoongArch's
  `ld -r` functionality. The core issue is the unconditional insertion of an align
  section, which breaks kernel module loading because modules compiled with `-mno-relax`
  are expected not to contain `R_LARCH_ALIGN` relocations. The patch makes the insertion
  conditional on the presence of `R_LARCH_ALIGN` in the input files.
primer_glossary:
- term: LoongArch
  definition: A RISC-ISA (Instruction Set Architecture) developed in China.
- term: ld -r
  definition: A linker option that performs a partial link, combining multiple object
    files into a single relocatable object file.
- term: R_LARCH_ALIGN
  definition: A LoongArch-specific relocation type that indicates byte alignment.
- term: -mno-relax
  definition: A compiler flag that disables instruction relaxation, which can affect
    code size and performance but might be required by certain linkers or environments.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260714114920.585718-1-xry111@xry111.site
bugzilla_url: null
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

Xi Ruoyao proposes a fix for the LoongArch linker when using `ld -r`, addressing a regression that broke kernel modules. The issue arose because a previous commit unconditionally inserted an align section, which is not expected by modules compiled with `-mno-relax`. This patch ensures the align section is only created if an input object contains the `R_LARCH_ALIGN` relocation, thus restoring correct behavior for kernel modules and preventing unnecessary output bloat.
