---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- cygwin
- binutils
- target
- linker
discussion_id: 20260907081941.900753-1-dennis@dennisameling.com
source_type: public_inbox
title: '[PATCH 0/2] aarch64: add the aarch64-pc-cygwin target'
headline: 'aarch64: add the aarch64-pc-cygwin target'
tldr: Adds aarch64-pc-cygwin target to binutils, based on existing Windows on Arm
  toolchain patches.
proposer: Dennis Ameling <dennis@dennisameling.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Replacing the generic `mingw_behavior` boolean with explicit per-target DLL characteristic
  lists prevents unintended side effects from future mingw-specific changes, improving
  maintainability at the cost of slightly more verbose configuration.
- The new target reuses existing AArch64 PE tests, ensuring a baseline level of correctness
  but relies on prior patches for full functionality with auto-imported data symbols.
exchanges:
- author: Dennis Ameling
  role: proposer
  position: Submits a series of patches to add the aarch64-pc-cygwin target, detailing
    changes to linker DLL characteristics and test configurations.
  quote: null
primer_expert: This series adds a new target triplet, aarch64-pc-cygwin, to binutils.
  It involves modifications in BFD, GAS, and LD to accommodate Cygwin's PE/COFF environment
  on AArch64. The key change is in `ld/emultempl/pep.em`, where the default DLL characteristics
  are precisely controlled to meet AArch64 Cygwin's requirements for relocatability
  (DYNAMIC_BASE) and to disable high-entropy ASLR (HIGH_ENTROPY_VA), which differs
  from existing mingw targets. This ensures compatibility with Cygwin's runtime loader.
primer_glossary:
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, a file format used for
    executables, object code, and DLLs in Windows systems. It's also used by MinGW
    and Cygwin.
- term: BFD
  definition: The Binary File Descriptor library, a component of GNU Binutils used
    for reading and writing object file formats.
- term: GAS
  definition: The GNU Assembler, part of GNU Binutils, responsible for assembling
    source code into machine code.
- term: LD
  definition: The GNU linker, part of GNU Binutils, responsible for combining object
    files and libraries into an executable or shared library.
- term: DYNAMIC_BASE
  definition: A linker flag that enables Address Space Layout Randomization (ASLR)
    for executables and DLLs, making them relocatable at load time.
- term: HIGH_ENTROPY_VA
  definition: A linker flag that enhances ASLR by using a larger entropy pool for
    address randomization, increasing security but potentially incompatible with older
    systems or specific runtime environments.
series_id: 'binutils:aarch64: add the aarch64-pc-cygwin target'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260907081941.900753-1-dennis@dennisameling.com
bugzilla_url: null
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

Dennis Ameling proposes adding the aarch64-pc-cygwin target to binutils, BFD, GAS, and LD. This series is based on existing downstream patches from the Windows on Arm GNU toolchain. The primary change refines linker DLL characteristics to correctly handle AArch64 Cygwin binaries, which have specific relocation and ASLR requirements distinct from existing mingw targets. The proposal includes tests to ensure no regressions are introduced.
