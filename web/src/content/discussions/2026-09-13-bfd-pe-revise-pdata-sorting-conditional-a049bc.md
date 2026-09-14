---
project: binutils
subsystem: bfd
patch_id: null
tags:
- bfd
- pe
- pdata
- sorting
- architecture
discussion_id: 20260913123323.9734-4-jon.turney@dronecode.org.uk
source_type: public_inbox
title: '[PATCH 3/4] bfd: pe: Revise pdata sorting conditional'
headline: 'bfd: pe: Revise pdata sorting conditional'
tldr: Correctly sort PE .pdata sections for architectures that support it.
proposer: Jon Turney <jon.turney@dronecode.org.uk>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures correct sorting of .pdata sections across more architectures.
- Addresses a potential misinterpretation of PE specification requirements.
exchanges: []
primer_expert: This patch refactors the conditional that enables sorting of the `.pdata`
  section in `bfd/peXXigen.c`. The original condition was negative and limited to
  specific architectures (x86_64, AArch64, LoongArch64, RiscV64), potentially missing
  other PE32 architectures that should have this sorting. The rewrite aims to correctly
  identify architectures where `.pdata` sorting is applicable, aligning with the PE
  specification's requirements and fixing potential oversights for platforms like
  ia64.
primer_glossary:
- term: .pdata section
  definition: A section in PE files containing runtime function lookup information,
    used for exception handling and debugging. It requires specific sorting.
- term: PE specification
  definition: The document defining the structure and conventions of the Portable
    Executable (PE) file format, used for executables, object code, and shared libraries
    on Windows.
- term: ia64
  definition: Intel Itanium Architecture, a 64-bit instruction set architecture.
series_id: 'binutils:bfd: pe: revise pdata sorting conditional'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260913123323.9734-4-jon.turney@dronecode.org.uk
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

This patch revises the conditional logic for sorting the `.pdata` section in PE files. Historically, sorting was limited to x86_64, which is seen as an oversight as the PE specification mandates sorting for all relevant architectures. The change rewrites the condition to positively identify architectures that support `.pdata` sorting, addressing potential issues for architectures like ia64 and others where it might have been incorrectly disabled.
