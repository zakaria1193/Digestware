---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- compiler
- linker
- optimization
discussion_id: 20261001090404.108916-1-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[RFC PATCH v4 1/5] RISC-V: Add Zcmt table-jump relocation definitions'
headline: 'RISC-V: Add Zcmt table-jump relocation definitions'
tldr: Adds definitions for RISC-V Zcmt table-jump relocations to binutils.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 8
technical_tradeoffs:
- Adds new symbols and sections, potentially increasing binary size slightly.
- Introduces new relocation types, requiring careful handling by the linker and assembler.
- The complexity of jump table management needs to be balanced against performance
  gains.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: proposer
  position: Submits RFC v4 to add linker-internal table-jump marker and instruction
    encoding definitions for RISC-V Zcmt, noting the marker has no public ELF relocation
    or howto entry.
  quote: 'Add the linker-internal table-jump marker and instruction encoding

    definitions. The marker has no public ELF relocation or howto entry.'
- author: Jiawei <jiawei@iscas.ac.cn>
  role: contributor
  position: Provides an update on the patch series, describing the process of recording,
    planning, and rewriting passes for shortening and alignment, and selecting target
    groups after complete recording.
  quote: 'Register recording, planning and rewriting passes between ordinary

    shortening and alignment. Select profitable residual target groups after

    complete recording, then size the table before rewriting. Keep optional

    JVT-base references symbolic until final linking; preserve normal

    alignment accounting.


    Consume table-jump markers in the dedicated relocation handler. Use the

    NONE howto for common disc…'
- author: Kito Cheng <kito.cheng@gmail.com>
  role: reviewer
  position: Notes that subsequent patches in the series have been pushed to facilitate
    progress on the Zcmt table-jump relocation definitions.
  quote: 'I pushed this and

    https://patchwork.sourceware.org/project/binutils/patch/20260924155402.420585-5-jiawei@iscas.ac.cn/

    ahead to make some progress here :)'
primer_expert: This RFC introduces support for the RISC-V Zcmt extension's table-jump
  (JT) mechanism within binutils. It defines new ELF relocation types and internal
  linker structures (`.riscv.jvt` section, `R_RISCV_TABLE_JUMP` reloc) to handle indirect
  jumps via a jump table. The changes are necessary for optimizing control flow in
  performance-sensitive code on RISC-V platforms supporting Zcmt.
primer_glossary:
- term: RISC-V
  definition: An open standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles.
- term: Zcmt
  definition: A RISC-V extension that provides instructions for efficient table-based
    indirect jumps, improving performance for switch statements and virtual method
    calls.
- term: Relocation
  definition: Information in an object file that describes how to modify certain byte
    values (e.g., addresses) when the code or data is combined with other files or
    loaded into memory.
- term: ELF
  definition: Executable and Linkable Format, a common file format for object files,
    executables, and shared libraries on Unix-like systems.
- term: Linker
  definition: A program that combines object files and libraries into an executable
    program or another object file. Binutils provides the GNU linker, `ld`.
- term: Table-jump
  definition: A control flow technique where a program jumps to a target address stored
    in a table, often used to implement efficient switch statements or virtual function
    calls.
series_id: 'binutils:risc-v: add zcmt table-jump relocation definitions'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261001090404.108916-1-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-10-01'
is_stub: false
stub_reason: ''
---

Jiawei proposes adding linker-internal definitions for RISC-V Zcmt table-jump relocations to binutils. This change introduces new relocation numbers, symbol names, and section names to support this feature. The RFC is intended to move forward with the implementation, with one reviewer noting they have pushed subsequent patches to make progress.
