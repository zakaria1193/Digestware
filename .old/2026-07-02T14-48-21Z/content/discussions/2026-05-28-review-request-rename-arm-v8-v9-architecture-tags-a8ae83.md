---
project: binutils
subsystem: bfd
patch_id: null
tags:
- ARM
- architecture
- BFD
- gas
- gold
discussion_id: c28d2959-115c-41da-ba8a-fd8d6a2e326c@arm.com
source_type: public_inbox
title: 'Re: [PATCH] gas, bfd, gold: Rename Arm v8/v9 architecture tags'
headline: 'Review Request: Rename Arm v8/v9 Architecture Tags'
tldr: Richard Earnshaw reviews a patch renaming Arm AEABI CPU architecture tags to
  include the profile suffix for A-profile architectures and requests an indentation…
proposer: '"Richard Earnshaw (foss)" <Richard.Earnshaw@arm.com>'
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Richard Earnshaw (foss)
  role: reviewer
  position: Requests an indentation fix for the second and third elements in `bfd/cpu-arm.c`.
  quote: Please check the indentation here of the second and third elements; they
    should be aligned in the columns.
primer_expert: This patch renames architecture tags within the GNU Binutils, specifically
  affecting the BFD (Binary File Descriptor) library, the GNU Assembler (gas), and
  the gold linker. The tags represent different ARM architecture versions (v8 and
  v9) and profiles (A, R, M). The change aims to standardize the naming convention
  by including the profile suffix for A-profile architectures.  This is primarily
  a code organization and readability improvement.
primer_general: This discussion concerns changes to the way the Binutils (a suite
  of tools for working with binary files) identifies different versions of the ARM
  processor architecture. The patch renames some internal names to make them more
  consistent and easier to understand. This change primarily affects developers working
  on the Binutils tools themselves, rather than users of those tools.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/c28d2959-115c-41da-ba8a-fd8d6a2e326c@arm.com
bugzilla_url: null
date: '2026-05-28'
is_stub: false
---

Richard Earnshaw reviews a patch from Sivan Shani that renames the Arm AEABI CPU architecture tag constants and macro definitions to include the profile suffix for A-profile architectures, making the naming consistent with existing v8-R and v8-M tag names. Earnshaw requests a minor indentation fix in `bfd/cpu-arm.c`.
