---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- relaxation
- optimization
- performance
discussion_id: 20261120142506.264748-3-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH v5 2/3] RISC-V: Relax eligible jumps and calls through a Zcmt table'
headline: 'RISC-V: Relax eligible jumps and calls through a Zcmt table'
tldr: Implements Zcmt table-jump relaxation in GNU ld for RISC-V, optimizing jumps
  and calls.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables a new code optimization for jumps and calls.
- Adds complexity to the linker's relaxation logic.
- Opt-in nature allows users to control its application.
exchanges: []
primer_expert: This is the second patch in a series that adds opt-in Zcmt table-jump
  relaxation to GNU ld for RISC-V. This patch focuses on the implementation details
  within `bfd/elfnn-riscv.c`. It introduces new types and functions for managing jump
  table targets (JVT), including hashing and comparison logic. The linker state (`riscv_elf_link_hash_table`)
  is augmented to track JVT information. Key functions are added or modified to identify
  candidate symbols, initialize and manage the JVT hash table, check for eligibility
  based on options and ISA, create the JVT section, and perform the actual relocation
  r…
primer_glossary:
- term: RISC-V
  definition: An open standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles.
- term: Zcmt
  definition: A RISC-V standard extension that allows for table-jump relaxation, an
    optimization technique for jumps and calls.
- term: table-jump relaxation
  definition: An optimization technique in linkers where indirect jumps or calls are
    replaced with a more efficient form, potentially using a jump table.
- term: GNU ld
  definition: The GNU linker, responsible for combining object files and libraries
    into executable programs.
- term: PIC
  definition: Position-Independent Code. Code that can run correctly regardless of
    where it is loaded in memory.
- term: ISA
  definition: Instruction Set Architecture. The set of commands and instructions that
    a CPU can understand and execute.
- term: JVT
  definition: Jump Vector Table. A data structure used in conjunction with table-jump
    relaxation to manage indirect jump targets.
series_id: 'binutils:risc-v: relax eligible jumps and calls through a zcmt table'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120142506.264748-3-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch introduces the core logic for Zcmt table-jump relaxation in GNU ld for RISC-V. It enables the linker to identify eligible jumps and calls, plan a profitable jump table, and rewrite the target sites. The passes are opt-in, targeting non-PIC executables with compatible ISA attributes. The implementation handles layout-dependent shortenings after table placement and rewriting, ensuring correct behavior for various transfer types and alignment scenarios.
