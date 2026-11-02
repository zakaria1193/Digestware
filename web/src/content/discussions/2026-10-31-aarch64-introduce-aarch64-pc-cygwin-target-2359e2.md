---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- target-support
- aarch64
- cross-compilation
- windows
- gdb
discussion_id: 162e418d-408c-406a-8c80-37c04d7358da@gmail.com
source_type: public_inbox
title: 'Re: [PATCH] aarch64: Introduce aarch64-pc-cygwin target'
headline: 'aarch64: Introduce aarch64-pc-cygwin target'
tldr: Discussion about the lack of a maintainer for the aarch64-pc-cygwin target and
  the need for GDB maintainer approval.
proposer: Luis <luis.machado.foss@gmail.com>
consensus: Under Review
outcome: needs_revision
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Adding new targets increases build system complexity and maintenance burden.
- Ensuring proper GDB integration is critical for debugging newly supported architectures.
exchanges:
- author: Evgeny Karpov <evgeny.karpov@arm.com>
  role: proposer
  position: Submitted a patch to add aarch64-pc-cygwin target support, including changes
    to BFD, binutils, gas, and GDB configurations.
  quote: "The patch adds support for aarch64-pc-cygwin target.\n\nCo-authored-by:\
    \ Radek Barton <radek.barton@microsoft.com>\n    ---"
- author: Christophe Lyon
  role: reviewer
  position: Indicated that GDB-related changes in the patch need approval from GDB
    maintainers.
  quote: I think the GDB parts need approval from GDB maintainers (thus cc'ing gdb-patches).
- author: Luis <luis.machado.foss@gmail.com>
  role: reviewer
  position: Observed that there is no apparent maintainer for the aarch64-pc-cygwin
    target within the binutils project.
  quote: I don´t think we have a maintainer for pc-cygwin/Windows on aarch64.
primer_expert: This discussion concerns adding a new target configuration, `aarch64-pc-cygwin`,
  to binutils. The patch modifies build system files (configure scripts, target definitions)
  across BFD, binutils, gas, and GDB. A key point is identifying maintainership for
  this specific target and securing approval for GDB components.
primer_glossary:
- term: aarch64
  definition: The 64-bit ARM architecture.
- term: cygwin
  definition: A POSIX-compatible environment for Windows, allowing Unix-like applications
    to run.
- term: BFD
  definition: Binary File Descriptor library, a low-level interface for reading and
    writing various executable file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/162e418d-408c-406a-8c80-37c04d7358da@gmail.com
bugzilla_url: null
date: '2026-10-31'
is_stub: false
stub_reason: ''
---

A patch was submitted to introduce the aarch64-pc-cygwin target to binutils. However, a reviewer noted that there appears to be no maintainer for the pc-cygwin/Windows on aarch64 platform. Additionally, the GDB-specific parts of the patch require approval from GDB maintainers.
