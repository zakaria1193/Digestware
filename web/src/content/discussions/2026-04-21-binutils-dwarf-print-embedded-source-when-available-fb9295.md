---
project: binutils
subsystem: binutils/dwarf
patch_id: null
tags:
- binutils
- dwarf
- debugging
- embedded source
- objdump
discussion_id: 20260421020204.2759264-1-hawkinsw@obs.cr
source_type: public_inbox
title: 'Re: [PATCH v3] binutils/dwarf: Print embedded source, when available'
headline: 'Binutils/dwarf: Print embedded source, when available'
tldr: A patch adds the ability to print embedded source code from DWARF debugging
  information, but needs testing on more architectures.
stakes: This feature improves debugging by allowing developers to view source code
  directly from the executable, which is especially useful when the original source
  files are unavailable.  It streamlines the debugging process and removes the need
  to search for the correct source version.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Under Review
outcome: ready
sentiment_score: 7
sentiment_rationale: The patch is progressing with identified issues being addressed.
  Reviewers are providing constructive feedback.
technical_tradeoffs:
- Embedding source code increases the size of the executable.
- The patch needs to be tested on various architectures to ensure compatibility.
- Displaying the source code within objdump can improve the debugging experience.
exchanges:
- author: Jens Remus <jremus@linux.ibm.com>
  role: reviewer
  position: Requests that the original commit message from v1 of the patch be included
    in v3 for clarity.
  quote: it would be helpful if you could keep the original commit message from v1
    of your patch (except for the last two paragraphs), including the description
    and motivation
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Asks whether the patch has been tested on other targets, including 32-bit
    architectures.
  quote: What about other targets, including 32-bit ones?
- author: Will Hawkins <hawkinsw@obs.cr>
  role: proposer
  position: Acknowledges that the patch has not yet been tested on 32-bit architectures.
  quote: I, unfortunately, have not tested on that target, yet.
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Points out an issue in the code where name/source display is delayed.
  quote: null
primer_expert: This patch modifies binutils, specifically the DWARF handling component.
  DWARF is a debugging data format used to describe the program's structure, variables,
  and source code location. Embedded source refers to the source code being directly
  included within the DWARF debugging information, rather than just references to
  external files.
primer_general: Binutils is a collection of tools for working with binary files, including
  executables and object code. DWARF is a standard for storing debugging information
  in executable files, mapping machine code back to the original source code. This
  debugging information can include the source code itself, embedded directly in the
  executable. This allows debuggers to display the original source code even if the
  source files are not available.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/d2b8db37-d4d7-4378-9e75-f86072457918@linux.ibm.com
bugzilla_url: null
date: '2026-04-21'
---

This patch adds functionality to binutils to print embedded source code directly from DWARF debugging information, when available. The patch has been updated to fix a failing test on aarch64.  Reviewers requested testing on additional architectures, including 32-bit targets, and suggested improving the commit message to include the original description and motivation.
