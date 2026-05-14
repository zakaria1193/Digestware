---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- linker
- dynamic linking
- undefined symbols
discussion_id: CAHT-pJzqthybcirJLPU0Rus_5pOmpOnUVgqfpf5Cr7VHLnza3g@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Also output undefined symbols as dynamic symbols'
headline: 'RISC-V: Also output undefined symbols as dynamic symbols'
tldr: A RISC-V linker change ensures undefined symbols are treated as dynamic symbols
  when linking with `--unresolved-symbols=ignore-in-object-file`, fixing crashes…
proposer: Nelson Chu <nelson.chu1990@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Fixes a regression in RISC-V linking behavior.
- Ensures correct handling of undefined symbols during dynamic linking.
- The change may be specific to RISC-V due to its unique linking requirements.
exchanges:
- author: Nelson Chu <nelson.chu1990@gmail.com>
  role: other
  position: Questions why the proposed fix is specific to RISC-V, wondering if other
    targets handle undefined symbols differently and if the patch might be missing
    some broader context.
  quote: Just curious, it seems other targets don't need to handle bfd_link_hash_undefined
    in the following codes, so why and what's the difference between riscv and others?
primer_expert: The bfd (Binary File Descriptor) library within binutils provides a
  generic interface for manipulating object files. The RISC-V port needs to handle
  undefined symbols specially during linking, particularly when `--unresolved-symbols=ignore-in-object-file`
  is specified. Recent changes inadvertently stopped outputting dynamic symbols for
  undefined symbols, leading to incorrect code generation.  The patch addresses this
  by ensuring that undefined symbols are treated as dynamic symbols, allowing the
  dynamic linker to resolve them at runtime.
primer_general: When compiling and linking code, the linker resolves references between
  different parts of the program. Sometimes, a program might refer to a symbol (like
  a function or variable) that is not defined in the current object file.  The `--unresolved-symbols=ignore-in-object-file`
  linker option tells the linker to leave these undefined symbols unresolved and expect
  the dynamic linker (which runs when the program starts) to resolve them. This patch
  ensures that on RISC-V, these undefined symbols are correctly marked for dynamic
  linking, preventing crashes or errors.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAHT-pJzqthybcirJLPU0Rus_5pOmpOnUVgqfpf5Cr7VHLnza3g@mail.gmail.com
bugzilla_url: null
date: '2026-05-13'
is_stub: false
---

Vivian Wang identified that recent binutils changes cause RISC-V linkers to misbehave when encountering undefined symbols, specifically crashing or throwing errors when the desired behavior (with `--unresolved-symbols=ignore-in-object-file`) is to leave the symbol unresolved for the dynamic linker. The proposed patch restores the emission of dynamic symbols for undefined symbols, fixing a regression and a failing test case. Nelson Chu questions the RISC-V-specific nature of the fix.
