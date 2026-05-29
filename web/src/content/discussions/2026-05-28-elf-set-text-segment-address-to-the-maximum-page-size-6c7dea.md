---
project: binutils
subsystem: elf
patch_id: null
tags:
- elf
- linker
- page size
- pde
- alignment
discussion_id: CAMe9rOrEcr3WJKqWWe=puY4wDR5drynCng5o=qmcw+GUS2+1XA@mail.gmail.com
source_type: public_inbox
title: '[PATCH] elf: Set text-segment address to the maximum page size'
headline: 'elf: Set text-segment address to the maximum page size'
tldr: This patch sets the text-segment address to the maximum page size for ELF Position
  Dependent Executables (PDEs) when specified via command-line.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 5
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
  and includes a new test case (`testsuite/ld-elf/pr34184.c`) and updates to the test
  suite (`testsuite/ld-elf/elf.exp`).
primer_general: When creating executable files, the linker assigns memory addresses
  to different parts of the program, including the text segment (containing the program's
  code).  Page size refers to the size of a memory page, which is a unit of memory
  management used by the operating system.  This patch ensures that the starting address
  of the program's code is aligned to the maximum page size specified during linking.  This
  alignment is important for performance and security reasons. The `-z max-page-size`
  option controls the maximum page size used by the linker.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOrEcr3WJKqWWe=puY4wDR5drynCng5o=qmcw+GUS2+1XA@mail.gmail.com
bugzilla_url: null
date: '2026-05-28'
is_stub: false
---

This patch modifies the linker to ensure that the text-segment address of an ELF Position Dependent Executable (PDE) is set to the maximum page size when the `-z max-page-size=SIZE` option is used. If the default text-segment address is lower than the specified maximum page size, the linker will adjust it. This change is intended to address issue PR ld/34184 and includes a new test case and updates to the test suite.
