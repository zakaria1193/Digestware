---
project: binutils
subsystem: vax
patch_id: null
tags:
- VAX
- PIC
- GOT
- PLT
- binutils
discussion_id: avWG-b2lRivOywGh@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] VAX: PIC: Use GOT for pointer for global function'
headline: 'VAX: PIC: Use GOT for pointer for global function'
tldr: A patch to use GOT for global function pointers in VAX PIC code is ready for
  commit.
proposer: Alan Modra <amodra@gmail.com>
consensus: Ready to Land
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Replaces PLT with GOT for global function pointers in VAX PIC, resolving a bug at
  the potential cost of slight performance differences or changes in dynamic linking
  behavior.
exchanges:
- author: Rin Okuyama <rin@netbsd.org>
  role: proposer
  position: Submitted a patch to use GOT for global function pointers in VAX PIC.
  quote: 'Subject: [PATCH] VAX: PIC: Use GOT for pointer for global function


    in same file, instead of PLT


    This fixes the problem reported as Bug 32941: https://sourceware.org/bugzilla/show_bug.cgi?id=32941'
- author: Jan-Benedict Glaw <jbglaw@gmail.com>
  role: reviewer
  position: Agrees the patch is correct but expresses uncertainty about closing the
    bug ticket.
  quote: The patch is correct, but I think I cannot close the ticket?
- author: Alan Modra <amodra@gmail.com>
  role: maintainer
  position: Instructs to commit the patch and update the Pull Request, implying the
    ticket can now be closed.
  quote: Please commit, and I think you now should be able to update the PR.
primer_expert: This patch modifies the VAX gas configuration to use the Global Offset
  Table (GOT) instead of the Procedure Linkage Table (PLT) for global function pointers
  when compiling Position Independent Code (PIC). This change is intended to fix Bug
  32941, which indicated that the PLT was not handling these calls correctly on the
  VAX architecture. By switching to GOT, the code aims to resolve function calls more
  reliably in a PIC context.
primer_glossary:
- term: VAX
  definition: A line of historically significant 32-bit minicomputers and servers
    produced by Digital Equipment Corporation (DEC).
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and executed at any
    memory address without modification. This is essential for shared libraries and
    security features like ASLR.
- term: GOT
  definition: Global Offset Table. A table used in position-independent code to store
    addresses of global variables and functions, allowing indirect access.
- term: PLT
  definition: Procedure Linkage Table. A table used in position-independent code to
    resolve calls to functions in shared libraries.
- term: Bug 32941
  definition: A specific issue reported in the Sourceware Bugzilla tracking system,
    detailing a problem with VAX PIC global function pointers.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/avWG-b2lRivOywGh@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

Alan Modra confirms that a patch to use the Global Offset Table (GOT) for global function pointers in VAX Position Independent Code (PIC) is ready. This change addresses Bug 32941, which reported issues with using the Procedure Linkage Table (PLT) for this purpose. The patch modifies `gas/config/tc-vax.c` to change the relocation type for function calls.
