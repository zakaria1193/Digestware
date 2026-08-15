---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- maintenance
- tic6x
commit_hash: 7e7dd6cfcf60cda2506d19d88ff98622bf670dbd
source_type: public_inbox
author: Joseph Myers <jsm28@sourceware.org>
headline: Mark TIC6X binutils port as unmaintained
tldr: The TIC6X processor port for Binutils is now marked as unmaintained.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes the `TIC6X` entry from the `MAINTAINERS` file in
  the `binutils` directory. This signifies that the Binutils port for the Texas Instruments
  C6000 series DSPs is no longer actively maintained by the project. Such changes
  typically reflect a shift in project focus or a lack of community contribution for
  a specific architecture.
primer_glossary:
- term: MAINTAINERS
  definition: A file in the source code repository that lists individuals or teams
    responsible for maintaining different parts of the project. Removing an entry
    typically indicates that the component is no longer supported or maintained.
- term: TIC6X
  definition: Refers to the Texas Instruments C6000 series of digital signal processors
    (DSPs). This commit indicates that the Binutils toolchain support for this architecture
    is no longer actively maintained.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260814174314.847674BA79A0@sourceware.org
date: '2026-08-14'
is_stub: true
stub_reason: low_score
---

The entry for the TIC6X processor port in the `MAINTAINERS` file has been removed. This action formally marks the port as unmaintained, indicating that active development and support for this architecture within Binutils have ceased.
