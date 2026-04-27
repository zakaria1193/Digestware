---
project: gcc
subsystem: fwd
patch_id: null
tags:
- gcc
- llvm
- kernel
- libsanitizer
- build breakage
discussion_id: CAJkdwqHQ6spsMMQOihM0QBuK_JAfwY9FnsaBZE0q2piNBoPKbQ@mail.gmail.com
source_type: public_inbox
title: 'Fwd: Please cherry pick to merge this patch from LLVM upstream'
headline: Request to cherry-pick LLVM patch to fix build breakage.
tldr: A request is made to cherry-pick a patch from LLVM upstream into GCC to fix
  a build breakage caused by recent Linux kernel changes affecting libsanitizer.
proposer: coshvji cujmlqef <oyzawqgcfc@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Balancing the need for a quick fix with the potential for introducing instability
  through a cherry-picked patch.
- Managing dependencies between different projects (GCC, LLVM, Linux kernel).
exchanges: []
primer_expert: This situation illustrates the interdependence of toolchains and the
  kernel.  Changes in kernel APIs or ABIs can break userspace components like GCC's
  libsanitizer.  Cherry-picking is a common method for backporting specific fixes.
primer_general: This email discusses a problem where recent updates to the Linux kernel
  are causing GCC (the GNU Compiler Collection) to fail to build correctly.  The solution
  involves taking a specific fix (a patch) from the LLVM project (another compiler
  toolchain) and applying it to GCC.  This process is called "cherry-picking" a patch.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAJkdwqHQ6spsMMQOihM0QBuK_JAfwY9FnsaBZE0q2piNBoPKbQ@mail.gmail.com
bugzilla_url: null
date: '2026-04-25'
---

A developer requests that a patch from LLVM upstream be cherry-picked into GCC. The patch is needed to fix a build breakage introduced by recent changes in the Linux kernel that affect libsanitizer.  This is a request for a quick fix to restore GCC's buildability.
