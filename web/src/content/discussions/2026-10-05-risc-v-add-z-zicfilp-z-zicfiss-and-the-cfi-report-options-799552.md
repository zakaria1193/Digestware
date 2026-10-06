---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- cfi
- security
- elf
discussion_id: 20261005104510.2634206-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH] RISC-V: Add -z zicfilp=, -z zicfiss= and the CFI report options'
headline: 'RISC-V: Add -z zicfilp=, -z zicfiss= and the CFI report options'
tldr: Kito Cheng adds linker options for RISC-V CFI properties (-z zicfilp=, -z zicfiss=)
  and reporting, following RISC-V toolchain conventions.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the linker command line with new options. Ensures better CFI
  compliance for RISC-V targets.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Submits a patch to add RISC-V CFI linker options (`-z zicfilp`, `-z zicfiss`)
    and reporting flags, following toolchain conventions.
  quote: null
primer_expert: This patch introduces support for two new RISC-V GNU properties, `zicfilp`
  and `zicfiss`, into the binutils linker. These properties relate to Control Flow
  Integrity (CFI) mechanisms, specifically for distinguishing between implicit, unlabeled,
  and always-present CFI information. The patch adds linker flags (`-z zicfilp=`,
  `-z zicfiss=`) and report options to control these properties, aligning binutils
  with the RISC-V toolchain conventions and the behavior of LLVM's `lld`.
primer_glossary:
- term: RISC-V
  definition: An open-standard Instruction Set Architecture (ISA) based on Reduced
    Instruction Set Computing principles.
- term: CFI
  definition: Control Flow Integrity, a security technique that aims to prevent attackers
    from manipulating the program's control flow.
- term: linker options
  definition: Flags passed to the linker (e.g., `ld`) to control its behavior during
    the process of combining object files into an executable or library.
- term: -z
  definition: A common prefix for linker options that control specific aspects of
    the output file format or linking process.
- term: GNU properties
  definition: A mechanism in some object file formats (like ELF) to embed specific
    metadata or attributes about the code, often defined by conventions or standards.
- term: lld
  definition: The LLVM linker, a high-performance linker developed as part of the
    LLVM project.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005104510.2634206-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

Kito Cheng has submitted a patch to binutils that introduces new linker options for RISC-V Control Flow Integrity (CFI) properties. These options, `-z zicfilp=` and `-z zicfiss=`, along with corresponding reporting flags, are defined by the RISC-V toolchain conventions and align with similar functionality in LLVM. The patch enables control over how CFI properties are handled and reported during the linking process, with options for implicit, labeled, and explicit settings, as well as reporting severity.
