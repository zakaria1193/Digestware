---
project: binutils
subsystem: binutils
patch_id: null
tags:
- gprof
- profiling
- debuginfo
- split debuginfo
- stripping
discussion_id: 877bq13a6w.fsf@redhat.com
source_type: public_inbox
title: 'Re: [PATCH] gprof support for split debuginfo'
headline: gprof support for split debuginfo
tldr: Frank Eigler pings a patch adding gprof support for split debuginfo, enabling
  it to work with stripped binaries.
stakes: Improves profiling capabilities for stripped binaries, which are common in
  production environments.
proposer: fche@redhat.com
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Requires changes to `gprof` to locate and process split debuginfo files.
- May introduce dependencies on libraries or tools for handling split debuginfo.
exchanges: []
primer_expert: '`gprof` is a profiling tool that relies on debug information to map
  execution times to source code. Split debuginfo separates debug information into
  a separate file, often used with stripped binaries.  This patch enables `gprof`
  to find and use this split debuginfo.'
primer_general: '`gprof` is a tool used to profile programs, revealing how much time
  is spent in each function. This requires debug information that maps machine code
  back to the original source code.  Often, debug information is removed from production
  binaries to reduce their size, a process called stripping. Split debuginfo is a
  technique where the debug information is placed in a separate file, allowing the
  binary to be stripped while still providing debug information to tools like `gprof`
  when needed. This patch enhances `gprof` to work with this split debuginfo.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/877bq13a6w.fsf@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

Frank Eigler is requesting feedback on a patch that adds support for split debuginfo to `gprof`. This enables `gprof` to work correctly with binaries that have been stripped of debug information using `strip -g`.
