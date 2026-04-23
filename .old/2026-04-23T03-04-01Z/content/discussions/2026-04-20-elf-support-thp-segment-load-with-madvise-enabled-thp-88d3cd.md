---
project: glibc
subsystem: elf
patch_id: null
tags:
- THP
- elf
- glibc
- regression
- arm
discussion_id: CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v4] elf: Support THP segment load with madvise enabled THP'
headline: 'Elf: Support THP segment load with madvise enabled THP'
tldr: A patch enabling THP segment load with madvise has caused regressions on 32-bit
  Arm.
stakes: This regression blocks the deployment of THP support in glibc and impacts
  the performance of applications on 32-bit Arm.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Proposed
outcome: needs_revision
sentiment_score: 3
sentiment_rationale: The patch caused regressions, indicating a problem that needs
  to be resolved.
technical_tradeoffs:
- Fixing the regression may require disabling THP support on 32-bit Arm, potentially
  reducing performance.
- Alternative solutions may be more complex and require significant code changes.
- The fix must be carefully tested to avoid introducing new regressions.
- Impacts a specific architecture (32-bit Arm) and requires targeted testing on that
  platform.
- The fix should not negatively impact performance on other architectures.
exchanges:
- author: Carlos O'Donell <carlos@redhat.com>
  role: reviewer
  position: Reports that the patch has caused regressions on 32-bit Arm.
  quote: "This has a 32-bit Arm regression:\nhttps://patchwork.sourceware.org/project/glibc/patch/CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com/\n\
    \nProduces 4 regressions:\n   |\n   | regressions.sum:\n   | Running glibc:elf\
    \ ...\n   | FAIL: elf/tst-thp-1-no-s-code-pde\n   | FAIL: elf/tst-thp-1-no-s-code-static\n\
    \   | FAIL: elf/tst-thp-1-pde\n   | FAIL: elf/tst-thp-1-static"
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Acknowledges the regressions and mentions ongoing discussions with Linaro.
  quote: null
primer_expert: This discussion concerns a patch modifying the ELF loader in glibc
  to support THP with madvise. The patch introduces a regression on 32-bit Arm, specifically
  failing THP tests. The issue likely stems from incorrect handling of memory alignment
  or THP flags during segment mapping on the affected architecture.
primer_general: This discussion is about a bug in the glibc library that affects how
  programs use Transparent Huge Pages (THP) on 32-bit Arm systems. THP is a feature
  that can make programs run faster by using larger chunks of memory. However, a recent
  change to glibc, intended to improve THP support, has introduced a bug that causes
  programs to crash or fail to start correctly on 32-bit Arm devices. This needs to
  be fixed to ensure that programs work properly on those devices.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/8dcc2eba-5118-48ad-a0b7-cc5ea122e187@redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This patch, which aims to support THP segment load with madvise enabled THP, has introduced regressions on 32-bit Arm. The regressions were reported by Carlos O'Donell and further information is available in a Linaro report.
