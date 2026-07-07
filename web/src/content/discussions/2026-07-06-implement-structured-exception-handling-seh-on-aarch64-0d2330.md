---
project: binutils
subsystem: binutils
patch_id: null
tags:
- aarch64
- seh
- exception handling
- assembler
- unwinding
discussion_id: 20260706163939.9860-1-evgeny.karpov@arm.com
source_type: public_inbox
title: '[PATCH v11 0/1] Implement Structured Exception Handling (SEH) on AArch64'
headline: Implement Structured Exception Handling (SEH) on AArch64
tldr: Evgeny Karpov submits v11 of a patch series to implement SEH on AArch64, including
  big-endian host support and fixes.
proposer: Evgeny Karpov <evgeny.karpov@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: 5
technical_tradeoffs:
- Support for big-endian hosts adds complexity to the implementation.
- Correctly encoding exception handling information (pdata/xdata) requires careful
  handling of function sizes and unwind codes.
exchanges:
- author: Evgeny Karpov <evgeny.karpov@arm.com>
  role: proposer
  position: Submits v11 of the SEH implementation for AArch64, detailing changes including
    big-endian support and bug fixes.
  quote: 'Hello,


    Thank you for reviewing v10!

    v11 contains support for big endian host, a fix for phantom prologue and some

    other minor changes.'
- author: Evgeny Karpov <evgeny.karpov@arm.com>
  role: proposer
  position: Describes the implementation's reliance on shared helpers and Microsoft's
    SEH documentation.
  quote: 'The patch reuses shared helpers for SEH and implements SEH on AArch64.

    The implementation is based on

    (https://learn.microsoft.com/en-us/cpp/build/arm64-exception-handling?view=msvc-170)

    and pdata/xdata SEH records are emitted from md_finish.'
primer_expert: Evgeny Karpov's v11 patch series introduces AArch64 support for Structured
  Exception Handling (SEH) into Binutils, primarily targeting the assembler (`gas`).
  This implementation aligns with Microsoft's AArch64 SEH model, generating `.pdata`
  and `.xdata` records during the `md_finish` phase. Key challenges include calculating
  function sizes on big-endian hosts and ensuring correct prologue/epilogue unwinding
  codes. This work is crucial for enabling SEH-compliant C++ exception handling on
  AArch64 targets within the GCC toolchain ecosystem.
primer_glossary:
- term: SEH
  definition: Structured Exception Handling. A mechanism for handling runtime errors
    and exceptions, commonly used on Windows platforms. This patch brings SEH support
    to AArch64.
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: Binutils
  definition: A collection of binary manipulation tools, including the GNU assembler
    (`gas`), linker (`ld`), and others, essential for software development.
- term: big endian
  definition: A byte order where the most significant byte is stored at the lowest
    memory address.
- term: phantom prologue
  definition: A specific encoding issue related to exception handling prologues that
    needs to be handled correctly for SEH.
- term: .pdata/.xdata
  definition: Sections in PE/COFF object files that store exception handling information,
    including function prologue/epilogue details and unwind codes.
- term: unwinding
  definition: The process of moving up the call stack during exception handling to
    find a suitable handler.
- term: md_finish
  definition: Likely refers to the end of the machine description phase in the assembler,
    where final output sections like exception handling data are generated.
series_id: binutils:implement structured exception handling (seh) on aarch64
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260706163939.9860-1-evgeny.karpov@arm.com
bugzilla_url: null
date: '2026-07-06'
is_stub: false
stub_reason: ''
---

Evgeny Karpov presents the eleventh version of a patch series aimed at implementing Structured Exception Handling (SEH) for the AArch64 architecture in Binutils. This version incorporates support for big-endian hosts, fixes a 'phantom prologue' encoding issue, and includes other minor refinements. Previous versions addressed indentation, limitations, unwinding information reordering, register validation, renaming, and added extensive SEH tests.
