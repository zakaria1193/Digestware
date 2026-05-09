---
project: binutils
subsystem: chore
patch_id: null
tags:
- documentation
- typo
- binutils
- linker
discussion_id: db20c12c-5f3c-4ad4-a56e-bc2a439f2caa@suse.com
source_type: public_inbox
title: 'Re: [PATCH] chore: correct misrepresented wording'
headline: 'Chore: correct misrepresented wording'
tldr: Jan points out that the proposed patch needs to be applied to the source file
  (ld/ld.texi) and the tip of the master branch.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Under Review
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Points out that the patch needs to be applied to the source file and the
    tip of the master branch.
  quote: Indeed, but the patch is then needed against the source file (ld/ld.texi),
    and against the tip of the master branch.
primer_expert: This is a discussion about a trivial spelling correction in the binutils
  documentation, specifically in the linker (`ld`) manual written in Texinfo format
  (`ld/ld.texi`). The correction involves changing 'subseque nt' to 'subsequent'.
  The key point is ensuring the patch is applied to the correct file and branch.
primer_general: This is about fixing a typo in the documentation for binutils, a set
  of essential programming tools. The specific typo is in the documentation for the
  linker (`ld`), which is used to combine compiled code into an executable program.
  The discussion highlights the importance of applying the fix to the correct source
  file and the latest version of the code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/db20c12c-5f3c-4ad4-a56e-bc2a439f2caa@suse.com
bugzilla_url: null
date: '2026-05-07'
---

Jan Beulich comments on a patch submitted by Pranav Joshi to correct the misspelled word 'subseque nt' to 'subsequent'. Jan states that the patch needs to be applied to the source file `ld/ld.texi` and against the tip of the master branch.
