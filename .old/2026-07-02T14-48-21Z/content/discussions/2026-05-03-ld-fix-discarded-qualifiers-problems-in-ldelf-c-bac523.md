---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- linker
- ld
- warnings
- const
discussion_id: afeogEt856N67LEG@mozart.vkv.me
source_type: public_inbox
title: 'Re: [PATCH 4/4] ld: Fix discarded-qualifiers problems in ldelf.c'
headline: 'Ld: Fix discarded-qualifiers problems in ldelf.c'
tldr: Calvin Owens confirms that their patches to fix discarded-qualifiers warnings
  in ldelf.c were also independently found and fixed by Mark Wielaard.
proposer: Calvin Owens <calvin@wbinvd.org>
consensus: Ready to Land
outcome: ready
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- The patches address compiler warnings, leading to cleaner code.
- The fixes prevent potential unintended modification of constant data.
- The impact is relatively small, as the code likely functioned correctly even with
  the warnings.
exchanges:
- author: Mark Wielaard
  role: other
  position: States that they independently found and fixed the same discarded-qualifiers
    issues in ldelf.c.
  quote: 'This one I also found and fixed in almost the same way in

    https://inbox.sourceware.org/binutils/20260502170132.3303884-3-mark@klomp.org/


    Likewise.'
- author: Calvin Owens <calvin@wbinvd.org>
  role: proposer
  position: Acknowledges that the fixes were duplicated and says it's not necessary
    to use their patches.
  quote: 'No problem at all. It''s really simple stuff, I had spun them for some

    local testing and just thought they might save you all some time. Please

    don''t go to any extra trouble to use them :)'
primer_expert: This concerns fixes for `-Wdiscarded-qualifiers` warnings in the `ldelf.c`
  file of the binutils linker. These warnings occur when a `const` qualifier is implicitly
  removed during an assignment or initialization, potentially leading to unintended
  modification of constant data.
primer_general: This discussion is about resolving compiler warnings in the binutils
  linker, specifically related to discarding `const` qualifiers. The `const` keyword
  in C/C++ indicates that a variable's value should not be changed. The linker combines
  compiled code into an executable program, and these warnings indicate potential
  issues where the linker might be inadvertently stripping away the `const` protection,
  which could lead to bugs.
series_id: 'binutils:ld: fix discarded-qualifiers problems in ldelf.c'
series_role: reply
series_parts:
- title: 'ld: Fix discarded-qualifiers problems in ldelf.c'
  url: https://inbox.sourceware.org/binutils/20260503123422.GY11304@gnu.wildebeest.org
  n: 4
  total: 4
url: https://inbox.sourceware.org/binutils/afeogEt856N67LEG@mozart.vkv.me
bugzilla_url: null
date: '2026-05-03'
---

Calvin Owens responds to Mark Wielaard, noting that the discarded-qualifiers fixes in `ldelf.c` they submitted were independently discovered and resolved by Mark. Calvin indicates that his patches were created for local testing and offered to save time, but there's no need for extra effort to use them.
