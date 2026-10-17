---
project: binutils
subsystem: bfd
patch_id: null
tags:
- linker
- relaxation
- bfd
- elf
- security
discussion_id: 20261016123644.1429854-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 0/8] bfd: harden in-place relaxation byte deletion against size
  underflow'
headline: 'bfd: harden in-place relaxation byte deletion against size underflow'
tldr: Series hardens 18 ELF backends against heap corruption from relaxation byte
  deletion underflows.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: null
technical_tradeoffs:
- Significantly improves security and stability by fixing a heap corruption vulnerability.
- Standardizes safety checks across multiple targets, reducing future maintenance.
- Introduces a new shared validation helper and testing infrastructure.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Proposes a series of patches to harden 18 ELF backends against heap corruption
    during relaxation byte deletion by adding range checks.
  quote: "This series hardens 18 ELF backends in BFD against buffer underflow and\
    \ heap\ncorruption during linker relaxation byte deletion.\n\nProblem Description\n\
    ===================\nLinker relaxation backends that shrink code sections slide\
    \ remaining section\nbytes downward over deleted space via memmove:\n\n    memmove\
    \ (contents + addr, contents + addr + count, toaddr - addr - count);\n\nWhen input\
    \ relocations or…"
primer_expert: This is the cover letter for a series of patches fixing a heap corruption
  vulnerability across 18 ELF targets in binutils. The core issue lies in linker relaxation
  functions that shrink code sections using `memmove`. When the calculated deletion
  range is invalid (e.g., `count` exceeds the available space before `toaddr`), the
  `toaddr - addr - count` subtraction wraps around for unsigned integers, leading
  to a massive `SIZE_MAX` value. This causes `memmove` to write far beyond the intended
  buffer, corrupting the heap. The series introduces a shared validation helper (`_bfd_elf_relax_delete_ran…
primer_glossary:
- term: linker relaxation
  definition: A linker optimization process that adjusts instruction addresses and
    sizes at link time to improve code density or enable features like position-independent
    code. It may involve deleting or replacing instructions.
- term: BFD
  definition: Binary File Descriptor library, a GNU library used by binutils and other
    tools to abstract access to various executable file formats.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: memmove
  definition: A C standard library function that copies a block of memory from a source
    location to a destination location. It handles overlapping memory regions safely.
- term: underflow
  definition: In the context of memory or arithmetic operations, underflow occurs
    when a value becomes smaller than the minimum representable value. For unsigned
    integers, this typically results in wrap-around to a very large positive number.
- term: heap buffer overflow
  definition: A type of security vulnerability where a program writes data beyond
    the allocated buffer boundary on the heap, potentially corrupting adjacent memory
    or control structures.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on RISC principles,
    gaining traction in various computing domains.
series_id: 'binutils:bfd: harden in-place relaxation byte deletion against size underflow'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016123644.1429854-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This series addresses a heap corruption vulnerability in 18 ELF backends of the BFD library, caused by unsigned integer underflow during linker relaxation's byte deletion operations. When `memmove` is used to shrink sections, an out-of-range offset or deletion count can cause the size calculation `toaddr - addr - count` to wrap around to `SIZE_MAX`. This series introduces a shared helper function `_bfd_elf_relax_delete_range_ok` to validate these ranges, ensuring that error conditions are correctly propagated and preventing buffer overflows. It also includes updates to specific backends (AVR, M68HC11, RISC-V, RL78, RX) to propagate failures and adds comprehensive testing.
