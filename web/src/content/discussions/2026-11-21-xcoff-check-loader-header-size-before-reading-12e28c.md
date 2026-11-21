---
project: binutils
subsystem: xcoff
patch_id: null
tags:
- memory-safety
- xcoff
- binutils
- objdump
- security
discussion_id: loopr.28.rjyygqh0aq7f@research.digiscrypt.com
source_type: public_inbox
title: '[PATCH] xcoff: Check loader header size before reading'
headline: 'xcoff: Check loader header size before reading'
tldr: Add a size check to prevent out-of-bounds reads when parsing malformed XCOFF
  files.
proposer: Alhuda Khan <alhuda@research.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures robustness against malformed input at the cost of a minor check.
- Addresses a security vulnerability (heap-buffer-overflow).
exchanges:
- author: Alhuda Khan <alhuda@research.digiscrypt.com>
  role: proposer
  position: Proposes adding a size check for the .loader section to prevent out-of-bounds
    reads in `xcoff_get_ldhdr()` when parsing malformed XCOFF files.
  quote: Reject the section when it is smaller than bfd_xcoff_ldhdrsz (abfd) before
    swapping in the header. After the change the malformed file is reported as "file
    truncated" and a valid XCOFF object still parses correctly.
primer_expert: The `xcoff_get_ldhdr` function in binutils' XCOFF BFD module parses
  the loader header from the `.loader` section. A malformed XCOFF can have a `.loader`
  section smaller than expected, causing `bfd_getb32` to read past the allocated buffer
  during `bfd_xcoff_swap_ldhdr_in`. This patch adds a size check against `bfd_xcoff_ldhdrsz`
  to prevent this overflow.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/loopr.28.rjyygqh0aq7f@research.digiscrypt.com
bugzilla_url: null
date: '2026-11-21'
is_stub: false
stub_reason: ''
---

This patch addresses a memory-safety issue in the XCOFF parser where malformed files with undersized .loader sections could lead to out-of-bounds reads. The fix adds a check to ensure the section is large enough before attempting to parse the loader header, preventing heap-buffer-overflows reported by AddressSanitizer.
