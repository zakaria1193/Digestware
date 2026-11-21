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
discussion_id: 20261120142506.264748-1-jiawei@iscas.ac.cn
source_type: public_inbox
title: '[PATCH v5 0/3] RISC-V: Add opt-in Zcmt table-jump relaxation'
headline: 'RISC-V: Add opt-in Zcmt table-jump relaxation'
tldr: Introduces an opt-in Zcmt table-jump relaxation feature to GNU ld for RISC-V,
  enhancing optimization.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Introduces a powerful optimization for jump and call instructions.
- Increases linker complexity and potentially compilation time.
- Opt-in nature mitigates risk for users not needing the optimization.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: proposer
  position: Presents a series of patches adding opt-in Zcmt table-jump relaxation
    for RISC-V in GNU ld, detailing changes since v4 and testing results.
  quote: "This series adds opt-in Zcmt table-jump relaxation to GNU ld. The\nrelocation\
    \ definitions (4b013df1822f) and objdump support with its\nstandalone tests (7310b8560eae)\
    \ are already upstream and are not resent.\n\nChanges since v4:\n\n- Introduce\
    \ --relax-tbljal[=zcmt] and --no-relax-tbljal before adding\n  the backend. Table-jump\
    \ relaxation is off by default throughout."
primer_expert: This is the cover letter for a three-part series introducing Zcmt table-jump
  relaxation to GNU ld for RISC-V. The Zcmt extension provides a mechanism for indirect
  jumps and calls to be optimized by the linker into a jump table, reducing code size
  and potentially improving performance. This series adds the necessary infrastructure
  in BFD (`elfnn-riscv.c`), linker passes for analyzing and rewriting jump sites,
  and test cases. Key aspects include making the feature opt-in via new command-line
  options (`--relax-tbljal`), handling various edge cases like non-PIC executables,
  ISA compatibility, and…
primer_glossary:
- term: Zcmt
  definition: A RISC-V standard extension that enables table-jump relaxation, an optimization
    technique for jumps and calls.
- term: table-jump relaxation
  definition: An optimization technique where the linker replaces indirect jumps or
    calls with a more efficient form, often utilizing a jump table, to reduce code
    size or improve performance.
- term: GNU ld
  definition: The GNU linker, responsible for combining object files and libraries
    into executable programs.
- term: RISC-V
  definition: An open standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles.
- term: opt-in
  definition: A feature that is disabled by default and must be explicitly enabled
    by the user or developer.
- term: PIC
  definition: Position-Independent Code. Code that can run correctly regardless of
    where it is loaded in memory.
- term: ISA
  definition: Instruction Set Architecture. The set of commands and instructions that
    a CPU can understand and execute.
- term: relaxation
  definition: An optimization process in linkers that adjusts code, such as branch
    offsets, to improve performance or reduce code size.
series_id: 'binutils:risc-v: add opt-in zcmt table-jump relaxation'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120142506.264748-1-jiawei@iscas.ac.cn
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch series introduces opt-in Zcmt table-jump relaxation to GNU ld for RISC-V. This feature, building on prior work, allows the linker to optimize jumps and calls by utilizing a jump table. It is off by default and requires explicit enabling. The series addresses a regression in text-to-fini range handling, defers certain layout-dependent choices, and ensures correct behavior when the table is not profitable or selected. The implementation has been tested extensively on RISC-V Linux, passing numerous linker tests.
