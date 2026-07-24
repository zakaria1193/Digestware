---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- RISC-V
- ELF
- linker
- relocation
discussion_id: 20260724012642.21997-1-juewang@linux.alibaba.com
source_type: public_inbox
title: '[PATCH] RISC-V: define elf_backend_dtrel_excludes_plt'
headline: 'RISC-V: define elf_backend_dtrel_excludes_plt'
tldr: RISC-V binutils patch defines elf_backend_dtrel_excludes_plt to correctly handle
  DT_RELASZ, preventing double processing by tools like llvm-bolt.
proposer: wangjue <juewang@linux.alibaba.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- 'ABI Compliance: Ensuring RISC-V''s ELF object file generation adheres to expected
  behavior for dynamic linking and toolchain compatibility.'
- 'Tool Compatibility: Fixing issues that cause incorrect behavior in downstream tools
  that parse ELF structures independently.'
- 'Code Locality: Indirectly improving code locality by ensuring proper symbol resolution
  and section handling.'
exchanges:
- author: wangjue
  role: proposer
  position: Submits a patch to define `elf_backend_dtrel_excludes_plt` for RISC-V
    to fix DT_RELASZ calculation and prevent double processing by tools.
  quote: 'The RISC-V port never defined elf_backend_dtrel_excludes_plt, unlike

    x86-64, AArch64, arm, ppc, mips and s390. As a result DT_RELASZ counted

    .rela.dyn + .rela.plt instead of just .rela.dyn.


    With an empty .rela.dyn this makes DT_RELA alias DT_JMPREL (DT_RELA ==

    DT_JMPREL, DT_RELASZ == DT_PLTRELSZ). glibc accepts the aliased range,

    but tools that read the two ranges independently, such as llvm-bol…'
primer_expert: This patch addresses an ELF parsing detail in binutils for the RISC-V
  architecture. It corrects the calculation of the `DT_RELASZ` dynamic tag by defining
  `elf_backend_dtrel_excludes_plt`. This macro ensures that the size of the relocation
  section (`DT_RELASZ`) correctly excludes the jump slot relocations (`.rela.plt`),
  preventing issues with tools like `llvm-bolt` that parse `.rela.dyn` and `.rela.plt`
  independently. This aligns RISC-V's behavior with other architectures like x86-64
  and ARM.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) based on reduced instruction
    set computing principles.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executable,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: DT_RELASZ
  definition: An entry in the ELF dynamic section that specifies the size of the relocation
    entries (Rela entries).
- term: DT_RELASZ
  definition: An entry in the ELF dynamic section that specifies the size of the relocation
    entries (Rela entries).
- term: .rela.dyn
  definition: An ELF section containing relocation entries that apply to the dynamic
    linker, used for resolving symbolic references at runtime.
- term: .rela.plt
  definition: An ELF section containing relocation entries specifically for the Procedure
    Linkage Table (PLT), used to resolve dynamic function calls.
- term: llvm-bolt
  definition: A post-linkage binary optimization tool from the LLVM project that optimizes
    executables by reordering code and data.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260724012642.21997-1-juewang@linux.alibaba.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch defines `elf_backend_dtrel_excludes_plt` for the RISC-V port in binutils, correcting how `DT_RELASZ` is calculated. Previously, it incorrectly included `.rela.plt` sections, causing aliasing issues when `.rela.dyn` was empty. This led to tools like `llvm-bolt` processing sections twice. Defining the macro ensures `DT_RELASZ` excludes `.rela.plt`, aligning with other targets and resolving the aliasing problem.
