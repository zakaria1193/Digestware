---
project: binutils
subsystem: microblaze
patch_id: null
tags:
- microblaze
- gas
- relocation
- fixup
discussion_id: ba523c30-1c30-4428-92f4-d73fd0300350@eagerm.com
source_type: public_inbox
title: 'Re: [PATCH v2] microblaze: add BFD_RELOC_8 and BFD_RELOC_16 cases'
headline: 'microblaze: add BFD_RELOC_8 and BFD_RELOC_16 cases'
tldr: Adds support for 8-bit and 16-bit relocations in MicroBlaze's `md_apply_fix`
  function.
proposer: Michael Eager <eager@eagerm.com>
consensus: Proposed
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Expands the switch statement in `md_apply_fix` to handle more relocation types.
- Fixes two test cases and improves the robustness of the MicroBlaze backend.
exchanges:
- author: Michael Eager <eager@eagerm.com>
  role: maintainer
  position: Notes that the patch has been applied.
  quote: "On 9/21/26 6:29 PM, Sam Price wrote:\n> From: Samuel Price <thesamprice@gmail.com>\n\
    > \n> md_apply_fix has cases for BFD_RELOC_32, BFD_RELOC_64 and for the\n> MicroBlaze-specific\
    \ relocations, but none for BFD_RELOC_8 or BFD_RELOC_16.\n> Those fall through\
    \ to the default and nothing is written, so a byte or\n> halfword datum whose\
    \ value is only known at fixup time assembles to zero.\n> The fixup is then…"
primer_expert: This patch adds handling for `BFD_RELOC_8` and `BFD_RELOC_16` to MicroBlaze's
  `md_apply_fix` in `gas/config/tc-microblaze.c`. Previously, these relocation types
  fell through to a default case, resulting in zero-valued fixups that were not corrected
  by the linker. The change ensures that these smaller relocations are correctly processed,
  resolving issues in the `gas/all/simple-forward` and `gas/all/forward` test cases.
primer_glossary:
- term: BFD_RELOC_8
  definition: A relocation type representing an 8-bit data element.
- term: BFD_RELOC_16
  definition: A relocation type representing a 16-bit data element.
- term: md_apply_fix
  definition: A function within the BFD (Binary File Descriptor) library that applies
    fixups to relocatable data during the assembly process.
- term: Fixup
  definition: A placeholder in assembled code that needs to be resolved by the linker
    to a final address or value. In this context, if a fixup is not properly handled,
    it can lead to incorrect code.
- term: BFD_RELOC_NONE
  definition: A relocation type indicating that no relocation is necessary or that
    a relocation has been resolved and no longer needs further processing.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/ba523c30-1c30-4428-92f4-d73fd0300350@eagerm.com
bugzilla_url: null
date: '2026-09-22'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the MicroBlaze backend where the `md_apply_fix` function lacked cases for `BFD_RELOC_8` and `BFD_RELOC_16`. Without these cases, byte or halfword values known only at fixup time were being assembled as zero, and the subsequent relocation resolution would turn them into `BFD_RELOC_NONE`, preventing the linker from correcting them. The fix adds these cases, replicating the logic for `BFD_RELOC_32` but for smaller data sizes, thereby fixing the `gas/all/simple-forward` testcase and un-xfailing `gas/all/forward`.
