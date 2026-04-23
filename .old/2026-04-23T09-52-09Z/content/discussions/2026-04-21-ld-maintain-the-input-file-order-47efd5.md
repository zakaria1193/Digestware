---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- linker
- input file order
- eh_frame
discussion_id: CAMe9rOrRatiGHzffCBX8NVmT__9G-Aq_kPtpS0gDsQ9doY66-A@mail.gmail.com
source_type: public_inbox
title: '[PATCH] ld: Maintain the input file order'
headline: 'ld: Maintain the input file order'
tldr: Fixes a crash due to incorrect .eh_frame section termination by maintaining
  the input file order when adding new archives in ld.
stakes: Resolves a crash in the output binary, caused by incorrect handling of exception
  handling frames during linking.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Ensures correct program execution by maintaining input file order.
- May introduce minor performance overhead due to the insertion of new input files
  at a specific position.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Proposes inserting the new input file after the current one to maintain
    input file order and prevent crashes due to incorrect .eh_frame section termination.
  quote: 'Insert the new input file after the current input file to

    maintain the input file order'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Restates the problem and the proposed solution.
  quote: null
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Starts reviewing the patch.
  quote: null
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Continues discussion with Jan Beulich.
  quote: null
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Continues reviewing the patch.
  quote: null
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Continues discussion with Jan Beulich.
  quote: null
primer_expert: The linker (`ld`) combines compiled object files into an executable.
  During this process, the order in which input files are processed can be significant,
  particularly for sections like `.eh_frame`, which contains exception handling information.
  This patch addresses a bug where adding a new archive disrupts the input order.
  LTO (Link Time Optimization) can trigger the bug. Failure to maintain correct order
  leads to improperly terminated `.eh_frame` sections, causing crashes during runtime
  registration.
primer_general: When creating a program, the linker combines different pieces of code
  (object files) and libraries into a single executable file. The order in which these
  pieces are combined can sometimes be important, especially for certain types of
  information like exception handling data (used when errors occur). This patch fixes
  a problem in the linker where the order of input files was not being maintained
  correctly, which could lead to a crash when the program tried to handle errors.  The
  problem occurred because of how the linker was adding new libraries during a process
  called link-time optimization.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOrRatiGHzffCBX8NVmT__9G-Aq_kPtpS0gDsQ9doY66-A@mail.gmail.com
bugzilla_url: null
date: '2026-04-21'
---

When adding a new input archive from a linker script, `ld` appends it to the input file list. This can disrupt the expected input file order, leading to incorrect placement of the `.eh_frame` section terminator and causing a crash during EH frame registration. This patch inserts the new input file after the current input file to maintain the correct order.
