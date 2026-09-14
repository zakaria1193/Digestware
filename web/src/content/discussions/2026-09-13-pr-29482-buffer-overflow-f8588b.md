---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- bfd
- buffer overflow
discussion_id: aqYuGveSLmFJuNMH@squeak.grove.modra.org
source_type: public_inbox
title: PR 29482 buffer overflow
headline: PR 29482 buffer overflow
tldr: Fix buffer overflow in _bfd_ecoff_set_section_contents by adding sanity checks.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enhances security by preventing potential overflows.
exchanges: []
primer_expert: The change applies a fix to `bfd/ecoff.c` and `bfd/coffcode.h` to prevent
  a buffer overflow. Specifically, `_bfd_ecoff_set_section_contents` now includes
  the same division-avoiding sanity checks as `coff_set_section_contents`. This addresses
  a security concern related to how section contents are set, particularly for `.lib`
  sections where a physical address field is repurposed.
primer_glossary:
- term: buffer overflow
  definition: A condition where a program writes data beyond the allocated buffer,
    potentially corrupting adjacent memory or causing a crash.
- term: .lib section
  definition: A section in an object file that, in the context of `coff_set_section_contents`,
    stores information about shared libraries.
- term: sanity check
  definition: A validation step to ensure that input data or program state is within
    expected, safe bounds before proceeding with an operation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aqYuGveSLmFJuNMH@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

This patch addresses a buffer overflow vulnerability in `_bfd_ecoff_set_section_contents` by introducing the same safety checks present in `coff_set_section_contents`. The vulnerability was missed in a previous commit. The fix involves rewriting the sanity check to avoid run-time division.
