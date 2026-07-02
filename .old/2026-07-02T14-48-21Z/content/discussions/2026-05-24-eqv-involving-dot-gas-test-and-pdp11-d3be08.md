---
project: binutils
subsystem: binutils
patch_id: null
tags:
- assembler
- gas
- pdp11
- fixups
- byte order
discussion_id: ahLfJAl1s6zeiuUz@squeak.grove.modra.org
source_type: public_inbox
title: eqv involving dot" gas test and pdp11
headline: '"eqv involving dot" gas test and pdp11'
tldr: The patch updates the eqv-dot test to catch fixup issues and fixes a byte-order
  bug in the pdp11 assembler.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The changed eqv-dot test may expose previously hidden issues on other targets.
- Fixing the byte order bug in the pdp11 assembler ensures correct code generation
  for that architecture.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes changes to the eqv-dot test and fixes a byte-order bug in the
    pdp11 assembler.
  quote: When updating the test I noticed seriously odd expected output for pdp11.  Why
    should .long write in different byte order when needing fixups (".long z")?  That
    appears to be a bug in the pdp11 md_apply_fix, which reads section contents using
    pdp-endian but writes them little-endian.
primer_expert: The patch updates the gas testsuite to improve fixup testing, specifically
  for targets that may incorrectly handle ``fx_subsy``. It also fixes a PDP11-specific
  bug in ``md_apply_fix`` within ``gas/config/tc-pdp11.c``, where the byte order was
  incorrect during fixup application. This involves changes to several files in the
  gas testsuite.
primer_general: The GNU assembler (gas) translates assembly language into machine
  code.  Fixups are adjustments made to code or data when addresses are not known
  at assembly time. This patch addresses a bug in the pdp11 assembler that caused
  incorrect byte ordering when applying fixups. It also improves a test case to better
  detect potential issues in different assembler implementations.  These changes ensure
  more reliable code generation across different architectures.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ahLfJAl1s6zeiuUz@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-24'
is_stub: false
---

This patch modifies the ``eqv-dot`` test to ensure that targets which ignore the value of ``fx_subsy`` in fixups will fail. Additionally, it corrects a byte-order bug in the pdp11 assembler (gas) that caused incorrect code generation when fixups were needed. The patch updates the testsuite to account for these changes.
