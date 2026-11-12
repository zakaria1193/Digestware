---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- linker
- tls
- relocations
- got
discussion_id: 20261112013555.60673-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH v2] LoongArch: Fix GOT allocation for TLS PCREL20 relocations'
headline: 'LoongArch: Fix GOT allocation for TLS PCREL20 relocations'
tldr: Fixes an issue in the LoongArch linker where certain TLS relocations were not
  allocated GOT entries, leading to link-time crashes.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures correct linker behavior for a specific set of TLS relocations on LoongArch.
- Adds test cases to verify the fix.
exchanges: []
primer_expert: This patch targets the LoongArch architecture's linker script and relocation
  handling for Thread Local Storage (TLS). It specifically addresses PC-relative relocations
  using a 20-bit signed offset with a scale of 2 (PCREL20_S2) that involve TLS variables.
  The issue arises because the linker was not properly accounting for GOT (Global
  Offset Table) entries needed for these TLS accesses, leading to crashes when the
  GOT table became full or entries were unexpectedly missing during final linking.
  The fix ensures that these specific TLS relocations are recognized and allocated
  their necessary GOT…
primer_glossary:
- term: LoongArch
  definition: A RISC-ISA architecture developed in China.
- term: GOT
  definition: Global Offset Table. A table used by position-independent executable
    code to locate global variables and functions at runtime.
- term: TLS
  definition: Thread Local Storage. A mechanism that allows each thread in a multi-threaded
    program to have its own copy of a variable.
- term: PCREL20_S2
  definition: A type of relocation that uses a 20-bit signed PC-relative offset, scaled
    by 2. This is common for accessing data like TLS variables efficiently.
- term: Relocation
  definition: The process of updating symbolic references in an object file to absolute
    addresses when linking. Relocations contain information about which parts of the
    code need to be modified and how.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261112013555.60673-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the LoongArch ELF linker where specific Thread Local Storage (TLS) relocations (R_LARCH_TLS_LD/GD/DESC_PCREL20_S2) were not being allocated entries in the Global Offset Table (GOT). This omission causes the linker to crash during the final relocation phase due to unallocated GOT entries. The fix involves updating the `loongarch_elf_check_relocs` function to correctly record these references and includes updated test cases.
