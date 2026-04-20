---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- blackfin
- got
- segfault
discussion_id: aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
source_type: public_inbox
title: Don't create got in bfin_relocate_section
headline: Don't create got in bfin_relocate_section
tldr: This patch prevents the linker from creating a .got section too late in the
  linking process, which could lead to a segfault.
stakes: Fixes a potential segfault in the linker when linking Blackfin object files,
  improving reliability.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Removes the creation of the `.got` section in `bfin_relocate_section`.
- May expose unresolvable relocation errors if object files incompatible ABIs are
  linked together and the user suppresses the mismatch warning.
exchanges: []
primer_expert: Commit 7a84e3daf81a introduced the creation of the `.got` section in
  `bfin_relocate_section` (elf32-bfin.c). This patch removes that functionality.  The
  Blackfin ABI requires a Global Offset Table (GOT) for position-independent code.
  The GOT must be created before `relocate_section` is called; otherwise, relocations
  against it will fail.
primer_general: When linking programs, the linker needs to resolve references between
  different parts of the code.  For some architectures like Blackfin, a Global Offset
  Table (GOT) is used to store the addresses of global variables. This patch addresses
  a potential issue where the `.got` section, which stores these addresses, is created
  too late in the linking process. Creating it late can cause the linker to crash.
  The patch ensures the `.got` is created at the correct time, preventing the crash.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeVh7Jc3UNgD6QRL@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-19'
---

Alan Modra proposes a patch to revert a change that creates a `.got` section within the `bfin_relocate_section` function. Creating the `.got` section at this point in the linking process is too late and can lead to a segfault. The patch instead reports an unresolvable relocation error if the `.got` section has not already been created.
