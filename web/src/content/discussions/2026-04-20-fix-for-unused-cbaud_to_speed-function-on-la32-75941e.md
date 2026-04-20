---
project: glibc
subsystem: sysdeps
patch_id: null
tags:
- glibc
- LA32
- sysdeps
- compiler warning
- termios
discussion_id: 20260323071657.1505765-1-mengqinggang@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH] Fix ''cbaud_to_speed'' defined but not used on LA32'
headline: Fix for unused 'cbaud_to_speed' function on LA32
tldr: A patch fixes a 'defined but not used' warning for the `cbaud_to_speed` function
  on the LA32 architecture by conditionalizing its definition.
stakes: Resolves compiler warnings, improving code quality and maintainability, especially
  for less common architectures like LA32.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Ready to Land
outcome: ready
sentiment_score: 9
sentiment_rationale: Patch has been reviewed and approved.
technical_tradeoffs: []
primer: Glibc's `sysdeps` directory contains architecture-specific code.  The `cbaud_to_speed`
  function likely converts a baud rate to a speed value for serial communication.  Compiler
  warnings indicate potential issues in the code, even if they don't cause immediate
  errors.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/e3d206ec-aabe-4803-9f96-abf71fbe3eeb@loongson.cn
bugzilla_url: null
date: '2026-04-20'
---

Mengqinggang provides a patch to fix a 'defined but not used' warning for the `cbaud_to_speed` function on the LA32 architecture. The function is now conditionally defined based on `TEST_COMPAT (libc, GLIBC_2_0, GLIBC_2_42)`. The patch has been reviewed and approved by Adhemerval Zanella Netto, and Mengqinggang asks for it to be pushed to the master branch.
