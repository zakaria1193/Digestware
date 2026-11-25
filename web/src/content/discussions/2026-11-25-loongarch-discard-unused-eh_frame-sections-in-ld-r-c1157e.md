---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- linker
- LoongArch
- relocation
- eh_frame
discussion_id: 20261125090908.3386491-1-mengqinggang@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Discard unused .eh_frame sections in ld -r'
headline: 'LoongArch: Discard unused .eh_frame sections in ld -r'
tldr: Fixes linker errors caused by stale .eh_frame relocations in relocatable links.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: mengqinggang <mengqinggang@loongson.cn>
  role: proposer
  position: Introduces a change to call `bfd_elf_discard_info` for relocatable links
    to prevent stale .eh_frame relocations, and adds a new test case to verify the
    fix.
  quote: Previously, bfd_elf_discard_info was skipped for relocatable links. With
    --gc-sections, ld -r retained the FDE of a discarded section. This left a stale
    .eh_frame relocation pointing beyond the end of the section, so a following final
    link could fail with a bad relocation offset. Call bfd_elf_discard_info for relocatable
    links.
primer_expert: This patch modifies `ld/emultempl/loongarchelf.em` to call `bfd_elf_discard_info`
  even for relocatable links. Previously, this function was skipped in relocatable
  linking, causing `--gc-sections` to retain stale Frame Description Entries (FDEs)
  in `.eh_frame`. These stale entries resulted in invalid relocation offsets that
  could break a final link. The change ensures that unused `.eh_frame` sections are
  correctly discarded during relocatable linking.
primer_glossary:
- term: .eh_frame
  definition: A standard ELF section containing Call Frame Information (CFI) used
    for stack unwinding and exception handling.
- term: FDE
  definition: Frame Description Entry. A data structure within the .eh_frame section
    that describes how to unwind the stack for a particular function.
- term: ld -r
  definition: A linker option that performs a partial link, producing a relocatable
    object file from multiple input object files.
- term: --gc-sections
  definition: A linker option that removes unused sections from the output. Garbage
    Collection (GC) of sections.
- term: relocatable link
  definition: A linking process that produces an object file that can be further linked
    with other object files. This is often an intermediate step before a final executable
    or shared library is created.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261125090908.3386491-1-mengqinggang@loongson.cn
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where the linker (`ld -r`) with garbage collection (`--gc-sections`) retained stale .eh_frame relocations for discarded sections. This could lead to a bad relocation offset during a subsequent final link. The change ensures that `bfd_elf_discard_info` is called for relocatable links, preventing these errors.
