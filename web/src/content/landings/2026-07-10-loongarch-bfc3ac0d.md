---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- tls
- relocations
- elf
commit_hash: bfc3ac0d13b52a400aea7221603a5ac69510f471
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: 'LoongArch: Simplify TLS DTPREL relocation processing'
tldr: Improves LoongArch TLS DTPREL32/64 relocation handling by simplifying logic
  and setting partial_inplace to false for RELA relocations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The change modifies `elfnn-loongarch.c` to streamline the handling
  of `R_LARCH_TLS_DTPREL32` and `R_LARCH_TLS_DTPREL64` relocations when `resolved_dynly`
  is true. Instead of complex logic involving `outrel` and `unresolved_reloc`, it
  now directly returns the offset to the TLS block. Crucially, it sets `partial_inplace`
  to `false` for these relocations, reflecting LoongArch's use of RELA rather than
  REL relocations for TLS descriptor access, aligning the BFD backend with the architecture's
  ABI.
primer_glossary:
- term: R_LARCH_TLS_DTPREL32/64
  definition: LoongArch-specific relocation types used for accessing Thread-Local
    Storage (TLS) variables relative to the thread descriptor area. They specify whether
    the offset is 32-bit or 64-bit.
- term: TLS (Thread-Local Storage)
  definition: A mechanism that allows each thread in a multi-threaded program to have
    its own private copy of a variable. Toolchains generate specific relocations to
    manage access to these per-thread variables.
- term: RELA relocations
  definition: A type of ELF relocation that includes an explicit addend. This is in
    contrast to REL relocations, which do not have an explicit addend and are often
    used for simpler address calculations.
- term: partial_inplace
  definition: A flag within the BFD relocation handling that indicates whether a relocation
    can be resolved in-place within the output section. Setting it to false means
    the relocation requires a separate relocation entry in the output.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260710070158.466074BA2E0B@sourceware.org
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

This commit simplifies the processing of R_LARCH_TLS_DTPREL32/64 relocations on LoongArch by returning the offset to the TLS block for the symbol. It also corrects the relocation type by setting `partial_inplace` to false, acknowledging that LoongArch uses RELA relocations. This change contributes to more accurate and efficient handling of Thread-Local Storage (TLS) in the LoongArch toolchain.
