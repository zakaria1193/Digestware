---
project: binutils
subsystem: objdump
patch_id: null
tags:
- objdump
- pe/coff
- windows
- aarch64
- bugfix
discussion_id: 20260619134339.73604-1-jon.turney@dronecode.org.uk
source_type: public_inbox
title: 'Re: [PATCH] objdump: Fix private header (''-p'') import table output for pe-aarch64'
headline: 'objdump: Fix private header (''-p'') import table output for pe-aarch64'
tldr: Corrects truncation of import table output for PE32+ (64-bit) executables, particularly
  on AArch64.
proposer: Jon Turney <jon.turney@dronecode.org.uk>
consensus: Proposed
outcome: ready
impact_score: 5
sentiment_score: 9
technical_tradeoffs:
- Improves accuracy of `objdump` output for 64-bit PE files.
- Addresses a bug that could lead to incomplete analysis of executable dependencies.
exchanges:
- author: Jon Turney
  role: proposer
  position: Submits a patch to fix truncated import table output for PE32+ executables,
    noting the distinction between PE32 and PE32+ formats.
  quote: 'The private header (''-p'') import table output for pe-aarch64 (and

    probably all other 64-bit arches apart from x86_64) is truncated after the

    first import.


    The distinction between the conditional branches here should be between

    PE32 (32-bit) and PE32+ (somewhat confusingly, the 64-bit version of the

    PE format).


    PE file format specification [1] states under "Import Lookup Table":


    "An import look…'
- author: Jan Beulich
  role: reviewer
  position: Suggests code formatting improvements, specifically line splitting for
    readability, and proposes consolidating related manifest constants.
  quote: 'Okay, albeit preferably with ...


    ... this line split for each part to remain within 80 columns (no matter

    that other such long lines exist). Perhaps they all should be consolidated

    into the checking of a single (new) manifest constant, such that mistakes

    like the one being fixed here are easier to avoid. But that''s for later.'
- author: Jon Turney
  role: proposer
  position: Provides a revised patch based on Jan Beulich's suggestions regarding
    code formatting and proposes consolidating manifest constants for better maintainability.
  quote: "I attach a revised patch since I'm not entirely sure of the desired \nformatting\
    \ and indentation here.\n\nYes, that seems like a very good idea.\n\nThis condition\
    \ (or its negation) is repeated multiple times (along with \nsome almost similar\
    \ conditions which would probably benefit from a \ncomment if they really are\
    \ meant to be different)."
primer_expert: This patch corrects an issue in `objdump` where the import lookup table
  for PE32+ (64-bit) executables was being truncated, particularly affecting AArch64
  and other non-x86_64 64-bit architectures. The fix involves refining the conditional
  logic to correctly identify PE32+ files, ensuring that the 64-bit entries in the
  import lookup table are processed and displayed according to the PE format specification,
  thus resolving the truncation problem.
primer_glossary:
- term: objdump
  definition: A utility that displays information from object files, including disassembly
    and symbol tables.
- term: PE
  definition: Portable Executable, the file format for executables, object code, DLLs,
    and system files used in 32-bit and 64-bit versions of Windows.
- term: import table
  definition: A table within a PE executable that lists the functions and libraries
    the program needs to import from dynamic-link libraries (DLLs).
- term: PE32
  definition: The 32-bit version of the PE file format.
- term: PE32+
  definition: The 64-bit version of the PE file format, also known as 'long mode'
    on some architectures.
- term: AArch64
  definition: The 64-bit execution state of the ARM architecture.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/17d4f2f8-e520-4c16-91a0-6db4aa75db57@dronecode.org.uk
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This patch fixes an issue where the import table output for PE32+ (64-bit) executables, processed with `objdump -p`, was truncated after the first import on AArch64 and potentially other 64-bit architectures. The fix correctly distinguishes between PE32 (32-bit) and PE32+ (64-bit) formats based on the PE specification, ensuring that 64-bit import lookup table entries are handled appropriately.
