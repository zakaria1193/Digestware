---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- linker
- LTO
- exception handling
- eh_frame
discussion_id: CAMe9rOrRatiGHzffCBX8NVmT__9G-Aq_kPtpS0gDsQ9doY66-A@mail.gmail.com
source_type: public_inbox
title: '[PATCH] ld: Maintain the input file order'
headline: ld maintains input file order during linking
tldr: The linker 'ld' will now maintain the intended input file order, preventing
  crashes related to exception handling metadata.
stakes: Fixes a crash caused by incorrect ordering of object files during linking,
  which can lead to runtime errors and instability.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Potential impact on LTO performance due to the change in input file order.
- Increased complexity in the linker's input file management.
- The fix might expose other ordering-related issues.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Proposes a patch to maintain input file order in the linker to prevent
    crashes related to exception handling metadata.
  quote: Insert the new input file after the current input file to maintain the input
    file order
primer_expert: The linker (`ld`) processes input files in a specific order to resolve
  symbols and construct the final executable.  This order matters for features like
  exception handling, which relies on the `.eh_frame` section.  The patch addresses
  a scenario where LTO (Link-Time Optimization) causes archives to be added out of
  order, disrupting the `.eh_frame` section and leading to crashes. The fix involves
  modifying the linker's input file list management when handling archives specified
  in linker scripts.
primer_general: The linker is a crucial part of the software build process that combines
  compiled code (object files) into a single executable or library. It resolves references
  between different parts of the code. The order in which the linker processes these
  files can be important, especially for features like exception handling, which needs
  specific data structures in the correct sequence. This patch fixes a bug where the
  linker was reordering files, causing problems with exception handling and leading
  to program crashes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOrRatiGHzffCBX8NVmT__9G-Aq_kPtpS0gDsQ9doY66-A@mail.gmail.com
bugzilla_url: null
date: '2026-04-21'
---

The patch addresses an issue where the linker 'ld' reorders input files, particularly when adding archives from linker scripts. This reordering can lead to the `.eh_frame` section terminator being placed before exception handling code, causing crashes. The patch ensures that new input files are inserted in the correct order, resolving the crash.
