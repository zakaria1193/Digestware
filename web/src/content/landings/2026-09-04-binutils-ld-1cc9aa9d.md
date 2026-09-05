---
project: binutils
subsystem: binutils/ld
patch_id: null
tags:
- binutils
- linker
- ARM
- embedded
- TLS
commit_hash: 1cc9aa9de2af3cd54d5433c0e4a522b73719c3cb
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: 'ld: Account for .tbss size on Arm embedded targets'
tldr: Ensures .tbss occupies VMA for ARM embedded targets, aligning with LLVM lld.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Introduces `tls_nobits_occupies_vma` to `ld.h` and conditionally sets
  it in `armelf.em` for embedded ARM targets. When true, `.tbss` (uninitialized TLS
  data) will occupy VMA in the output, preventing overlap with later sections like
  `.bss`. This aligns with `lld` behavior and is tested with various link types in
  `ld/testsuite/ld-arm/`.
primer_glossary:
- term: .tbss
  definition: A section in object files that holds uninitialized data for Thread-Local
    Storage (TLS). Unlike .bss, .tbss is specifically for TLS variables.
- term: VMA
  definition: Virtual Memory Address. The address at which an object file section
    is loaded into memory when the program is executed.
- term: TLS
  definition: Thread-Local Storage. A mechanism that provides thread-specific data,
    ensuring that each thread has its own copy of certain variables.
- term: GNU ld
  definition: The GNU linker, responsible for combining object files and creating
    executable files or shared libraries.
- term: LLVM lld
  definition: The LLVM linker, part of the LLVM compiler infrastructure, known for
    its speed and modern design.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260904134526.8BD2B4BB3B96@sourceware.org
date: '2026-09-04'
is_stub: false
stub_reason: ''
---

This commit modifies the GNU linker (ld) to account for the size of the .tbss section on ARM embedded targets by making it occupy a virtual memory address (VMA). This behavior is necessary for embedded systems where TLS storage is allocated directly and prevents overlap with subsequent sections like .bss. The change introduces a new build-time property `tls_nobits_occupies_vma` and sets it to true for ARM embedded targets, aligning with LLVM's lld behavior. New tests are added to cover static, executable, PIE, and dynamic link scenarios.
