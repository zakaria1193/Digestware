---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- sframe
- cfi
discussion_id: 20260413144225.1990952-1-jremus@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH] gas: sframe: Error on open CFI at EOF; missing .cfi_endproc'
headline: 'Gas: sframe: Error on open CFI at EOF; missing .cfi_endproc'
tldr: A patch to prevent segfaults in gas when an open CFI is encountered at EOF has
  been approved.
proposer: Alan Modra <amodra@gmail.com>
consensus: Committed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra
  role: maintainer
  position: Approved the patch to prevent segfaults when an open CFI is encountered
    at EOF.
  quote: null
- author: Jens Remus
  role: proposer
  position: Original patch submitter
  quote: null
primer_expert: This patch addresses a bug in the GNU assembler (`gas`) related to
  handling CFI (Call Frame Information) when generating `.sframe` sections.  CFI is
  used for stack unwinding during debugging or exception handling.  The patch ensures
  that a missing `.cfi_endproc` at the end of the file doesn't cause a segfault, aligning
  the behavior with `.eh_frame` and `.debug_frame` handling.
primer_general: The GNU assembler (`gas`) translates assembly language code into machine
  code.  Call Frame Information (CFI) is metadata that describes the layout of the
  stack, which is essential for debugging and handling exceptions.  This patch fixes
  a bug where the assembler would crash if a function's CFI was started but not ended
  at the end of the assembly file.  The fix ensures a graceful error message instead
  of a crash, and provides more robust assembly processing.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/afL_pdceQflae7q_@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-30'
---

Alan Modra approved a patch from Jens Remus that prevents the assembler (`gas`) from segfaulting when it encounters an open CFI (Call Frame Information) at the end of a file, meaning a `.cfi_startproc` directive is present without a corresponding `.cfi_endproc`. The patch handles this situation similarly to how it's handled in `.eh_frame` and `.debug_frame` generation, by reporting an error and setting the DWARF FDE end address to its start address.
