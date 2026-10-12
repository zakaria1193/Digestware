---
project: binutils
subsystem: alpha
patch_id: null
tags:
- linker
- Alpha
- relocation
- optimization
discussion_id: asWHzxitW9qAnAww@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] alpha: don''t merge .got subsections once GPREL relocs exist'
headline: 'alpha: don''t merge .got subsections once GPREL relocs exist'
tldr: Fixes a linker bug on Alpha where .got subsections could be merged after GPREL
  relocations were created, causing errors.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Fixes a bug that could lead to linker errors.
- Potentially simplifies the relaxation process by preventing certain merges.
exchanges:
- author: Matt Turner
  role: proposer
  position: Proposed a fix for the Alpha linker bug related to .got subsection merging
    after GPREL relocs.
  quote: "But ldelf_map_segments reruns lang_relax_sections, starting again from\n\
    pass 0, when it has to redo the layout.  Merging can then still happen\nafter\
    \ GPREL16 relocs exist, giving\n\n  relocation truncated to fit: GPREL16 against\
    \ symbol `...'\n\nRemember that pass 1 has been reached and don't merge after\
    \ that."
- author: Alan Modra <amodra@gmail.com>
  role: maintainer
  position: Applied the patch, indicating acceptance.
  quote: Applied, thanks.
primer_expert: This patch modifies `bfd/elf64-alpha.c` to prevent the merging of `.got`
  subsections in the Alpha ELF linker. The issue arises because `ldelf_map_segments`
  can trigger `lang_relax_sections` multiple times. If a relaxation pass has already
  processed `GPREL16` relocations (indicated by `relax_pass` being non-zero), further
  merging of `.got` sections is disallowed. This avoids a specific relocation error
  on Alpha targets.
primer_glossary:
- term: Alpha
  definition: A 64-bit RISC instruction set architecture developed by Digital Equipment
    Corporation (DEC).
- term: .got
  definition: Global Offset Table, a section in an executable or object file used
    for indirect function calls and global variable access, especially in position-independent
    code.
- term: subsections
  definition: Smaller divisions within a larger section of an object file, allowing
    for more fine-grained control over layout and relaxation.
- term: GPREL
  definition: Global Pointer Relative, a type of relocation used in position-independent
    code on some architectures, where addresses are relative to a global pointer.
- term: relaxation
  definition: A linker optimization process where the linker adjusts the size and
    addresses of code and data sections to optimize for size or performance, often
    after initial assembly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/asWHzxitW9qAnAww@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-06'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the Alpha linker where merging of `.got` subsections could still occur even after `GPREL16` relocations were established. This merging was happening because the linker could re-run relaxation passes from the beginning, leading to errors like 'relocation truncated to fit'. The fix prevents merging of `.got` subsections after the relaxation pass has progressed beyond the initial stage.
