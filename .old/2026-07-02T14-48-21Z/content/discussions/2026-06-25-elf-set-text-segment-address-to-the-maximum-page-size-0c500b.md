---
project: binutils
subsystem: elf
patch_id: null
tags:
- elf
- linker
- aarch64
- memory-management
- bugfix
discussion_id: 05c74589-fa62-4673-bb6e-9154d37024ee@redhat.com
source_type: public_inbox
title: 'Re: [PATCH] elf: Set text-segment address to the maximum page size'
headline: 'ELF: Set text-segment address to the maximum page size'
tldr: A patch for the linker sets the text segment address to the maximum page size
  for ELF Position Dependent Executables, with feedback on user notification and te…
proposer: Nick Clifton <nickc@redhat.com>
consensus: Under Review
outcome: under_review
impact_score: 6
sentiment_score: 8
technical_tradeoffs:
- Ensures proper page alignment for ELF PDEs, improving compatibility and performance
  on systems with specific memory architectures.
- Potential for user confusion if explicit `--image-base` or `--Ttext-segment` values
  are overridden without notification.
- Requires robust test cases to verify the correct application of the maximum page
  size.
- Adherence to PR ld/34184 resolves a known linker issue.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Proposes a patch that aligns the text segment address with the maximum
    page size for ELF Position Dependent Executables when `-z max-page-size` is used,
    to address PR ld/34184.
  quote: 'PR ld/34184 * ldexp.c (fold_binary): Set text-segment address to the maximum
    page size for ELF PDE output with -z max-page-size=SIZE. * testsuite/ld-elf/elf.exp:
    Add ld/34184 test. * testsuite/ld-elf/pr34184.c: New file.'
- author: Nick Clifton
  role: reviewer
  position: Agrees with the patch but suggests adding a warning to users if their
    requested text-segment address is overridden and improving the test case to actively
    verify the address change.
  quote: I think that it would be helpful to inform the user that the text segment
    address is being changed - *if* they have tried to set it using --image-base or
    --Ttext-segment. Otherwise they may wonder why their command line option is being
    ignored.
primer_expert: This patch pertains to the ELF linker's behavior for Position Dependent
  Executables (PDEs) and memory page alignment. Specifically, it involves the `fold_binary`
  function in `ldexp.c` which processes linker scripts and symbol assignments. When
  linking a PDE, the `-z max-page-size` option dictates the maximum alignment for
  memory segments. The issue (PR ld/34184) is that the text segment's base address
  might not respect this `maxpagesize` if explicitly set lower by options like `--image-base`
  or `--Ttext-segment`. The fix ensures the `text-segment` address is elevated to
  the `maxpagesize`, aff…
primer_general: When a program is created, the linker organizes its different parts
  (like code, data, etc.) into 'segments' in the final executable file. For some types
  of programs, called 'Position Dependent Executables' (PDEs), these segments need
  to be placed at memory addresses that are aligned in a specific way, often to a
  'page size' determined by the operating system. This discussion introduces a change
  to the linker that ensures the main code segment ('text-segment') always starts
  at an address that's a multiple of the largest allowed page size, especially when
  a user explicitly requests a maximum page size during linking. This is important
  for how the operating system loads the program into memory. The feedback suggests
  telling the user if their attempt to set a specific starting address for the code
  segment is ignored due to this page size rule; otherwise, they might be confused
  why their command isn't working as expected.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/05c74589-fa62-4673-bb6e-9154d37024ee@redhat.com
bugzilla_url: null
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This discussion centers on an ELF linker patch that modifies the text-segment address for Position Dependent Executables (PDEs) when a maximum page size is specified via `-z max-page-size`. The patch ensures that if the text-segment's address is lower than the specified `maxpagesize`, it is promoted to that value. Feedback on the patch highlights the need to inform users when their explicitly set text-segment address is effectively overridden, and suggests improving the test case to verify the actual address change.
