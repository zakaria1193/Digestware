---
project: binutils
subsystem: elf
patch_id: null
tags:
- elf
- linker
- page size
- pde
- pie
discussion_id: CAMe9rOo5sxQ6x0jdD9JPXunmDt3rywckofJjPKgwXwUqsU-=GQ@mail.gmail.com
source_type: public_inbox
title: '[PATCH v2] elf: Set text-segment address to the maximum page size'
headline: 'elf: Set text-segment address to the maximum page size'
tldr: This patch sets the text-segment address to the maximum page size for ELF Position
  Dependent Executables (PDEs) when specified via command-line to avoid loadin…
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Forcing the text-segment address to the maximum page size might increase the size
  of the executable file due to padding.
- This change could potentially break existing applications that rely on the text-segment
  being loaded at a lower address, although this is unlikely.
exchanges: []
primer_expert: The linker's `fold_binary` function in `ldexp.c` is modified to adjust
  the text-segment address for ELF PDEs. This ensures that the text segment is aligned
  to the maximum page size specified via `-z max-page-size`. This addresses PR ld/34184
  and includes new test cases (`testsuite/ld-elf/pr34184.c`) and updates to the test
  suite (`testsuite/ld-elf/elf.exp`) to cover PIE, static PDE, and static PIE scenarios.
  This is crucial for systems where page alignment affects execution.
primer_general: When creating executable files, the linker assigns memory addresses
  to different parts of the program, including the text segment (containing the program's
  code).  Page size refers to the size of a memory page, which is a unit of memory
  management used by the operating system.  This patch ensures that the starting address
  of the program's code is aligned to the maximum page size specified during linking.  This
  alignment is important for performance and security reasons, especially for Position
  Dependent Executables (PDEs) and Position Independent Executables (PIEs), which
  can be loaded at different memory addresses each time they are run. The `-z max-page-size`
  option controls the maximum page size used by the linker.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOo5sxQ6x0jdD9JPXunmDt3rywckofJjPKgwXwUqsU-=GQ@mail.gmail.com
bugzilla_url: null
date: '2026-05-28'
is_stub: false
---

This patch (v2) addresses an issue where the text-segment address of an ELF Position Dependent Executable (PDE) could be lower than the maximum page size specified on the command line.  The patch modifies the linker to ensure that the text-segment address is set to the maximum page size when generating PDE output with the `-z max-page-size=SIZE` option. This prevents potential loading issues, particularly with PIE (Position Independent Executable), static PDE, and static PIE binaries, and includes added tests for these scenarios.
