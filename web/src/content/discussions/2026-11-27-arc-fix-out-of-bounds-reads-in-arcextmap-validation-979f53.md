---
project: binutils
subsystem: arc
patch_id: null
tags:
- binutils
- arc
- validation
- security
- memory safety
discussion_id: 20261127101211.131300-1-claziss@gmail.com
source_type: public_inbox
title: 'Re: [PATCH] arc: validate .arcextmap records'
headline: 'ARC: Fix out-of-bounds reads in .arcextmap validation'
tldr: Reviewer identifies that the proposed patch for validating .arcextmap records
  in binutils does not fully address out-of-bounds reads because checks occur after…
proposer: Claudiu Zissulescu <claziss@gmail.com>
consensus: Proposed
outcome: needs_revision
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensuring robust validation of custom section formats requires careful ordering of
  checks to prevent memory safety issues.
- The patch attempts to fix a bug but is found to be incomplete, requiring further
  refinement.
exchanges:
- author: Claudiu Zissulescu <claziss@gmail.com>
  role: reviewer
  position: Identifies that the proposed patch's validation checks occur too late,
    allowing out-of-bounds reads on EXT_CORE_REGISTER and EXT_LONG_CORE_REGISTER records.
  quote: The declaration initialiser reads p[2] before the p[0] < 4 test runs. For
    a record with p[0] == 2 placed at the very end of the section, p[2] is one byte
    past the end of the buffer allocated in build_ARC_extmap, so the over-read survives
    your patch.
primer_expert: This discussion pertains to the `binutils` ARC target support, specifically
  the parsing and validation of the `.arcextmap` section. The reported issue involves
  out-of-bounds reads when processing malformed records, particularly affecting `EXT_CORE_REGISTER`
  and `EXT_LONG_CORE_REGISTER` types. The validation logic in the proposed patch is
  found to be insufficient as it doesn't reorder checks to precede sensitive memory
  accesses.
primer_glossary:
- term: .arcextmap
  definition: A section in binaries for ARC (Argonaut RISC Core) processors used to
    store extended mapping information.
- term: out-of-bounds read
  definition: An operation that attempts to access memory at an address that is outside
    the allocated buffer boundaries, potentially leading to data corruption or program
    crashes.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261127101211.131300-1-claziss@gmail.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

A reviewer analyzed a patch intended to validate .arcextmap records in binutils' ARC target support. While the patch correctly identifies and attempts to fix some out-of-bounds read issues, the reviewer points out that two validation guards are ineffective because they are placed after the data they are meant to protect has already been read. This allows malformed records to trigger memory accesses beyond buffer limits.
