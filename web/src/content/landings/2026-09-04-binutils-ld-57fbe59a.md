---
project: binutils
subsystem: binutils/ld
patch_id: null
tags:
- binutils
- linker
- testsuite
- ARM
- embedded
commit_hash: 57fbe59ab342c1deb9d36c8b0da1e679fdf57e10
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Adjust ld testsuite for .tbss VMA consumption
tldr: ld testsuite adjusted to accept .tbss consuming virtual memory address.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Modifies `ld` testsuite files (`size-1.d`, `size-2.d`, `rgn-at10.d`,
  `rgn-at11.d`) to allow for variants of the `.tbss` section that consume VMA. This
  addresses failures on ARM embedded targets and other platforms where `.tbss` might
  not be marked as a TLS section, or where its VMA consumption differs from expected.
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
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260904134531.A55C94BB3BB5@sourceware.org
date: '2026-09-04'
is_stub: false
stub_reason: ''
---

The GNU linker (ld) testsuite has been updated to accommodate .tbss sections that consume a virtual memory address (VMA). This adjustment is necessary to fix failures on ARM embedded targets where .tbss is not always recognized as a TLS section. The changes also resolve issues on hppa64-hp-hpux11.23 and v850 targets, ensuring that the testsuite correctly handles variations in .tbss section behavior across different architectures.
