---
project: binutils
subsystem: binutils/gprof
patch_id: null
tags:
- binutils
- gprof
- debuginfo
- split debuginfo
- profiling
discussion_id: 20260206190747.GA5540@redhat.com
source_type: public_inbox
title: 'Re: [PATCH] gprof support for split debuginfo'
headline: Gprof support for split debuginfo
tldr: A patch adding gprof support for split debuginfo has been pushed after review.
proposer: '"Frank Ch. Eigler" <fche@redhat.com>'
consensus: Committed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Frank Ch. Eigler
  role: proposer
  position: Pushed the patch with decompression enabled on the debug file.
  quote: Thank you, pushed (accidentally split into two patches).
- author: Alan Modra
  role: reviewer
  position: Suggested setting BFD_DECOMPRESS unconditionally.
  quote: I meant, set
- author: Frank Ch. Eigler
  role: proposer
  position: Fixed the patch to set BFD_DECOMPRESS unconditionally and pushed it.
  quote: Ah ok, fixed, pushed.
primer_expert: This patch enables `gprof` to work with split debuginfo, where debugging
  information is stored in a separate file.  This involves setting the `BFD_DECOMPRESS`
  flag to handle potentially compressed debug sections when the debug file is opened.  `gprof`
  is a profiling tool.
primer_general: '`gprof` is a tool used to profile programs, providing insights into
  where the program spends its time. Split debuginfo is a method of separating debugging
  information from the main executable file, which can reduce the size of the executable.  This
  patch allows `gprof` to work correctly when debugging information is stored separately,
  by ensuring that the debug file is decompressed if necessary.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260430172224.GF30441@redhat.com
bugzilla_url: null
date: '2026-04-30'
---

Frank Eigler pushed a patch to add gprof support for split debuginfo after receiving approval.  The patch enables decompression on the debug file. Alan Modra requested that `BFD_DECOMPRESS` be set unconditionally which was then fixed and pushed.
