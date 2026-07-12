---
project: binutils
subsystem: binutils/h8
patch_id: null
tags:
- h8
- architecture
commit_hash: ebf22fc26326ad138bea9dee536cf081e46dd6e1
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Set H8/300H as default architecture for H8 family
tldr: H8/300H is now the default architecture for the H8 family, affecting address
  size and test cases.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Configures the H8 toolchain within BFD, GAS, and LD to default to the
  H8/300H architecture. This impacts address modes and testsuite expectations for
  H8 targets, aligning with the H8/300H's 32-bit addressing capabilities in its advanced
  modes.
primer_glossary:
- term: H8/300H
  definition: A microcontroller architecture from Renesas (formerly Hitachi) that
    supports 32-bit addressing in its advanced modes.
- term: H8/300
  definition: An older microcontroller architecture in the Renesas H8 family, typically
    using 16-bit addresses.
- term: BFD
  definition: The Binary File Descriptor library, used by Binutils to read and write
    various object file formats.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils suite.
- term: LD
  definition: The GNU linker, part of the GNU Binutils suite.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260711085100.CE8B14BA2E39@sourceware.org
date: '2026-07-11'
is_stub: false
stub_reason: ''
---

This commit establishes the H8/300H as the default architecture for the H8 family within Binutils. The H8/300H architecture supports 32-bit addresses, distinguishing it from the H8/300's 16-bit addressing. Consequently, affected test cases in BFD, GAS, and LD have been updated to reflect this change, particularly concerning address and pointer sizes.
