---
project: binutils
subsystem: binutils/mips
patch_id: null
tags:
- binutils
- mips
- embedded
- cpu support
- elf
commit_hash: 0ea2f63dbf28248746891feb40d0d2e154981797
source_type: public_inbox
author: '"Maciej W. Rozycki" <macro@sourceware.org>'
headline: MIPS Allegrex CPU support added to Binutils.
tldr: Binutils now correctly handles the MIPS Allegrex CPU, including its abiflags
  and machine type.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch enhances Binutils' MIPS support by adding handling for the
  Allegrex CPU. It complements a previous commit that introduced Allegrex as a MIPS2-based
  CPU by defining the missing `AFL_EXT_ALLEGREX` tag in `.MIPS.abiflags`. The Allegrex
  machine type (`bfd_mach_mips_allegrex`) is now correctly registered in `bfd/aoutx.h`
  and `elfcpp/mips.h`, and reordered in `bfd/elfxx-mips.c`'s `mips_mach_extensions`
  array to maintain reverse chronological order within MIPS II extensions. `gas/testsuite`
  and `gold/mips.cc` are also updated.
primer_glossary:
- term: MIPS
  definition: A family of RISC microprocessor architectures developed by MIPS Computer
    Systems (now MIPS Technologies).
- term: Allegrex
  definition: A specific MIPS CPU core, often found in embedded systems, known for
    its power efficiency.
- term: MIPS2
  definition: A version of the MIPS instruction set architecture, introducing new
    instructions and features over MIPS1.
- term: .MIPS.abiflags
  definition: An ELF section used on MIPS architectures to store Application Binary
    Interface (ABI) flags, indicating CPU features and ABI compatibility.
- term: a.out
  definition: A legacy executable file format, historically used on Unix-like systems.
    Binutils still provides support for it.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: bfd_mach_mips_allegrex
  definition: A symbolic constant representing the machine type for the MIPS Allegrex
    processor within the BFD library.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261108184452.E60054BA2E26@sourceware.org
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

Binutils has gained support for the MIPS Allegrex CPU, a MIPS2-based processor. This update defines the necessary `.MIPS.abiflags` tag and integrates the Allegrex machine type into `a.out` and ELF object file handling. The changes also ensure correct ordering within MIPS II extensions.
