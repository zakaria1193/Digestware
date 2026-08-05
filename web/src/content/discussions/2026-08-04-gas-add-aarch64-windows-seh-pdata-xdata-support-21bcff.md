---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- AArch64
- Windows
- SEH
discussion_id: 20260804180213.1588044-1-oyzawqgcfc@gmail.com
source_type: public_inbox
title: '[PATCH] gas: Add AArch64 Windows SEH (pdata/xdata) support'
headline: 'gas: Add AArch64 Windows SEH (pdata/xdata) support'
tldr: Adds AArch64 Windows exception handling support to the GAS assembler.
proposer: trcrsired <oyzawqgcfc@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds support for a specific Windows ABI on AArch64, increasing code size and complexity
  in GAS.
- Ensures compatibility with Windows exception handling mechanisms, crucial for developing
  robust applications.
exchanges:
- author: trcrsired <oyzawqgcfc@gmail.com>
  role: proposer
  position: Submits a patch to implement Windows SEH unwind info generation for AArch64
    in GAS, extending existing x64 support.
  quote: 'Implement Windows exception-handling (SEH) unwind info generation for

    the aarch64-w64-mingw32 target in GAS.


    The existing obj-coff-seh.c only handled x64.  This adds full AArch64

    support:'
primer_expert: This patch adds AArch64 support for Windows Structured Exception Handling
  (SEH) to GAS, the GNU Assembler. Previously, GAS's SEH handling in `obj-coff-seh.c`
  was limited to x64 targets. This change enables the generation of SEH unwind information
  (pdata and xdata) for AArch64 targets running Windows, including handling AArch64-specific
  directives and ensuring correct format compatibility with Microsoft's ARM64 SEH
  specification.
primer_glossary:
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils suite, which translates
    assembly language code into object files.
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: SEH
  definition: Structured Exception Handling. A mechanism in Windows for handling runtime
    errors and exceptions.
- term: pdata/xdata
  definition: Data structures used in Windows executables to describe how to unwind
    the stack during exception handling. pdata typically contains function length
    and flags, while xdata provides detailed unwind information.
- term: unwind info
  definition: Information embedded in an executable that describes how to restore
    the caller's stack frame when a function returns or an exception is handled.
- term: mingw32
  definition: Minimalist GNU for Windows. A development environment that allows the
    use of GNU tools (like GCC and Binutils) to create Windows applications.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260804180213.1588044-1-oyzawqgcfc@gmail.com
bugzilla_url: null
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

This patch introduces support for Windows Structured Exception Handling (SEH) in the GNU Assembler (GAS) for the AArch64 architecture targeting Windows (aarch64-w64-mingw32). It extends existing SEH handling logic, which previously only supported x64, to include AArch64-specific unwind directives, correct xdata header layout, and accurate function length calculation. This enables GAS to generate correct SEH unwind information for AArch64 Windows executables.
