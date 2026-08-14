---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- ld
- aarch64
- optimization
- relocation
- review
discussion_id: cc2a28f2-e71d-9054-4e42-c61a8b772668@e124511.cambridge.arm.com
source_type: public_inbox
title: 'Re: [PATCH] AArch64: Optimize ADD relocations that resolve to zero'
headline: AArch64 ADD relocation optimization invalid with pending relocations
tldr: Reviewer flags that optimizing ADD instructions to MOV/NOP when relocations
  resolve to zero is invalid if the linker still emits relocations, as it breaks idem…
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: needs_revision
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Performing the optimization improves code density and potentially performance but
  risks correctness if relocations are still active.
- Adding checks for relocation status increases complexity in the linker.
exchanges:
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: reviewer
  position: Raises a concern that the proposed optimization for AArch64 `ADD` instructions
    to `MOV`/`NOP` is invalid if the linker still emits relocations, as it breaks
    idempotency.
  quote: I think this optimization is invalid if we're still emitting relocations,
    because it breaks idempotency, so we probably need to add a check for that.
primer_expert: A proposed optimization in the AArch64 backend of GNU `ld` aims to
  replace `ADD` instructions where the immediate operand becomes zero after relocation
  with equivalent `MOV` or `NOP` instructions, following an ELF specification recommendation.
  However, a reviewer points out that this optimization is problematic if the linker
  still emits relocations for these instructions, as it violates idempotency. The
  reviewer requests guidance on how to correctly detect and handle this situation,
  particularly concerning the state of pending relocations.
primer_glossary:
- term: AArch64
  definition: The 64-bit instruction set architecture for ARM processors.
- term: relocation
  definition: A process performed by the linker to adjust symbolic references in object
    files to their final memory addresses in the executable or shared library.
- term: ADD instruction
  definition: A processor instruction that performs addition.
- term: idempotency
  definition: In this context, it refers to the property that applying an operation
    multiple times has the same effect as applying it once. If an optimization breaks
    idempotency, repeated linking or processing could lead to incorrect results.
- term: linker
  definition: A program that combines object files and libraries into an executable
    or shared library, resolving symbol references and performing relocations.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and shared libraries on Unix-like systems.
- term: MOV instruction
  definition: A processor instruction that moves data from one location to another.
- term: NOP
  definition: No Operation. A processor instruction that does nothing but consume
    CPU cycles.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/cc2a28f2-e71d-9054-4e42-c61a8b772668@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

A reviewer has raised a concern regarding a proposed optimization for AArch64 `ADD` instructions. The optimization replaces `ADD` instructions whose immediate value becomes zero after relocation with `MOV` or `NOP` instructions. The reviewer argues this is invalid if the linker continues to emit relocations for these instructions, as it breaks idempotency. Further clarification from maintainers is requested on how to check for this condition.
