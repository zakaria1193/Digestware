---
project: binutils
subsystem: ia64
patch_id: null
tags:
- binutils
- ia64
- linker
- relaxation
- musl
discussion_id: c06d5c31-bc42-416e-ad67-24415f813c2a@suse.com
source_type: public_inbox
title: 'Re: [PATCH] ia64: Fix .rela.got sizing for __ehdr_start during relaxation'
headline: 'ia64: Fix .rela.got sizing during relaxation'
tldr: Patch fixes a BFD assertion failure in ia64 linking related to .rela.got sizing
  during relaxation.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jan Beulich
  role: contributor
  position: Acknowledges the patch and its description.
  quote: "On 21.11.2026 15:52, Frank Scheiner wrote:\n> Noticed during porting musl\
    \ to ia64 ([1]). Trying to link the dynamic\n> libc.so fails an assertion in ld.bfd\
    \ (BFD version 2.46-slack151):\n> \n> ```\n> /usr/bin/ld.bfd: BFD version 2.46-slack151\
    \ assertion fail elfnn-ia64.c:3238\n> ```\n> \n> [1]: https://github.com/johnny-mnemonic/epic-musl\n\
    > \n> The reason is a mismatch between the symbol state seen by diffe…"
- author: Frank Scheiner
  role: proposer
  position: Proposes a patch to fix a linker assertion failure related to .rela.got
    sizing on IA-64.
  quote: 'The reason is a mismatch between the symbol state seen by different

    sizing passes.


    The attached patch solves that and allows for a successful dynamic build

    of musl for ia64.'
primer_expert: This patch addresses a specific linker assertion failure on the IA-64
  architecture when building musl's dynamic linker. The root cause identified is a
  discrepancy in how the linker's BFD backend handles symbol states across multiple
  sizing passes, particularly involving the `__ehdr_start` symbol during relaxation.
  The fix likely involves synchronizing or adjusting the information available to
  the BFD backend during these passes to ensure consistent state for correct relocation
  processing.
primer_glossary:
- term: ia64
  definition: Intel Itanium architecture, a 64-bit Itanium processor family.
- term: BFD
  definition: The Binary File Descriptor library, a low-level library used by GNU
    Binutils to parse and manipulate object file formats.
- term: relaxation
  definition: A linker optimization technique where the linker adjusts branch offsets
    and other relative addressing information to produce smaller or more efficient
    code.
- term: .rela.got
  definition: A section in an ELF object file containing relocation entries for the
    Global Offset Table (GOT), used for dynamic linking.
- term: __ehdr_start
  definition: A linker-defined symbol that typically points to the beginning of the
    ELF header in an object file or executable.
- term: musl libc
  definition: A lightweight, standard C library designed for embedded systems and
    resource-constrained environments, often used in conjunction with the Linux kernel.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/c06d5c31-bc42-416e-ad67-24415f813c2a@suse.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

Frank Scheiner submitted a patch to fix an assertion failure in `ld.bfd` on the IA-64 architecture when linking musl's dynamic libc.so. The issue stems from a mismatch in symbol states during different sizing passes, particularly concerning the `__ehdr_start` symbol and relaxation. The patch, tested on real hardware, resolves this by adjusting how the linker handles these sizing variations.
