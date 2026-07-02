---
project: gcc
subsystem: fwd
patch_id: null
tags: []
discussion_id: CAJkdwqHQ6spsMMQOihM0QBuK_JAfwY9FnsaBZE0q2piNBoPKbQ@mail.gmail.com
source_type: public_inbox
title: 'Fwd: Please cherry pick to merge this patch from LLVM upstream'
headline: 'Fwd: Please cherry pick to merge this patch from LLVM upstream'
tldr: A patch merged into LLVM upstream fixes a build breakage in GCC caused by recent
  Linux kernel changes to libsanitizer.
proposer: coshvji cujmlqef <oyzawqgcfc@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: ''
primer_general: ''
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAJkdwqHQ6spsMMQOihM0QBuK_JAfwY9FnsaBZE0q2piNBoPKbQ@mail.gmail.com
bugzilla_url: null
date: '2026-04-25'
---

A user reports that recent changes in the Linux kernel's libsanitizer are causing build failures in GCC.  They request that a specific patch, already merged into the LLVM project, be cherry-picked into GCC to resolve this issue, because their attempts to use `git send-email` have failed.
