---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- ELF
- refactoring
- patch
discussion_id: aqZi6croPQWR5QZK@squeak.grove.modra.org
source_type: public_inbox
title: Consolidate creation of stub bfd
headline: Consolidate creation of stub bfd
tldr: Patch consolidates stub BFD creation logic into `ldelf.c`, simplifying code
  and fixing MIPS target orphan section placement.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Centralizing code reduces maintenance effort and potential for inconsistencies but
  requires careful handling of target-specific variations.
- Early creation of stub BFDs resolves issues with section placement but might introduce
  a slight overhead if not all targets strictly require it.
- Modifying linker behavior, even for internal structures, necessitates thorough testing
  to ensure compatibility across all supported targets and scenarios.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch to centralize stub BFD creation in `ldelf.c` and fix related
    issues, particularly on MIPS.
  quote: This patch replaces the code creating a stub bfd in various ELF targets with
    one copy in ldelf.c.  This shouldn't change target behaviour, except for mips
    which now creates the stub bfd like all other targets rather than delaying until
    the first stub section is needed.
primer_expert: This patch refactors the Binutils linker (`ld`) by consolidating the
  logic for creating a 'stub' BFD (Binary File Descriptor) across different ELF targets.
  Previously, this creation logic was duplicated in various `elfxx-*.c` files. The
  new approach centralizes this in `ldelf.c`. A side effect, noted as a fix, is on
  MIPS targets where the stub BFD was previously created lazily. This lazy creation
  affected the placement of orphan sections. By forcing earlier creation, the patch
  resolves these test failures, requiring adjustments to section placement in the
  test scripts.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor. An abstract data structure used by GNU tools
    to represent object files, providing a common interface for handling different
    object file formats.
- term: Stub BFD
  definition: A minimal BFD structure created early in the linking process for ELF
    targets. It serves as a placeholder or base for more detailed BFD structures.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executable
    files, object code, shared libraries, and core dumps.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: Orphan section
  definition: A section in an object file that is not explicitly placed or defined
    by the linker script, potentially leading to unpredictable placement.
- term: MIPS
  definition: Microprocessor without Interlocked Pipeline Stages. A family of RISC
    instruction set architectures.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aqZi6croPQWR5QZK@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

Alan Modra proposes a patch to refactor Binutils' ELF handling by consolidating the creation of stub BFDs into a single location in `ldelf.c`. This change aims to reduce code duplication across various ELF targets. While intended to not alter target behavior, it fixes an issue on MIPS where the stub BFD was created later, affecting orphan section placement. The patch resolves this by ensuring earlier creation and adjusting test cases accordingly.
