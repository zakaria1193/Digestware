---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gprof
- profiling
- debuginfo
- split debuginfo
discussion_id: aegD7n91hCHgOeW0@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] gprof support for split debuginfo'
headline: Gprof support for split debuginfo
tldr: A patch is approved to enable decompression on the debug file for gprof support
  of split debuginfo.
stakes: Fixing bugs or improving features in profilers directly impacts developers
  using those profilers for their projects which helps them identify performance bottlenecks
  and optimize their applications.
proposer: Alan Modra <amodra@gmail.com>
consensus: Under Review
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs: []
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: maintainer
  position: The patch is approved with the conditional removed.
  quote: The patch is OK with the conditional removed here.
primer_expert: gprof is a performance analysis tool. Split debuginfo separates debugging
  information from the executable, typically to reduce the size of the deployed binary.
  This patch likely modifies gprof to correctly locate and use the split debuginfo
  files. BFD is the Binary File Descriptor library, which provides a generic interface
  for accessing object files; `BFD_DECOMPRESS` likely flags a file requiring decompression.
primer_general: Gprof is a tool used to profile programs, identifying which functions
  consume the most time.  'Debuginfo' is extra data added to compiled programs that
  helps debuggers understand the code's structure and variables.  'Split debuginfo'
  is when this debuginfo is stored in a separate file, reducing the size of the main
  program. BFD is a library that handles different binary file formats. This discussion
  is about a patch that improves gprof's ability to work with split debuginfo.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aegD7n91hCHgOeW0@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-21'
---

A patch that enables decompression on the debug file for gprof support of split debuginfo has been approved with a minor code cleanup.
