---
project: binutils
subsystem: pe-coff
patch_id: null
tags:
- PE-COFF
- linker
- weak symbols
- symbol resolution
- bfd
discussion_id: 20260530191522.57144-1-peter0x44@disroot.org
source_type: public_inbox
title: '[PATCH 0/3] PE-COFF: Fix weak external symbol resolution bugs'
headline: 'PE-COFF: Fix weak external symbol resolution bugs'
tldr: This series fixes two bugs related to PE COFF weak external symbol resolution
  in the BFD linker and adds testsuite coverage.
proposer: Peter Damianov <peter0x44@disroot.org>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: null
technical_tradeoffs:
- Increased code complexity in the linker vs. correct handling of weak externals.
- Increased testsuite maintenance vs. improved confidence in linker correctness.
exchanges:
- author: Peter Damianov <peter0x44@disroot.org>
  role: proposer
  position: This series fixes bugs in PE COFF weak external symbol resolution in the
    BFD linker and adds testsuite coverage.
  quote: 'This series fixes two bugs in the PE COFF weak external symbol

    resolution in the BFD linker, plus adds testsuite coverage.'
primer_expert: The series modifies ``bfd/cofflink.c`` to fix weak external symbol
  resolution and adds a new test suite in ``ld/testsuite/ld-pe/``. The first patch
  addresses issues with strong undefined references, while the second prefers defined
  fallbacks over null fallbacks. The test suite provides comprehensive coverage of
  weak/strong interactions.
primer_general: This patch series focuses on the PE COFF file format, commonly used
  for executables on Windows. It fixes two bugs related to how the linker handles
  'weak symbols'. Weak symbols are optional; if a strong symbol isn't found, the linker
  may use the weak symbol as a fallback. The first bug fix ensures that the linker
  correctly resolves weak symbols even when a strong, but undefined, symbol is encountered
  first. The second fix ensures that the linker prefers a valid fallback definition
  over a null definition. A new test suite validates these fixes and improves the
  robustness of the linker.
series_id: 'binutils:pe-coff: fix weak external symbol resolution bugs'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260530191522.57144-1-peter0x44@disroot.org
bugzilla_url: null
date: '2026-05-30'
is_stub: false
---

This patch series addresses two bugs in the BFD linker related to PE COFF weak external symbol resolution. The first patch fixes an issue where the linker loses the weak symbol's aux record and fails to resolve the fallback alias when a strong undefined reference is seen first. The second patch corrects the handling of two weak externals for the same symbol, ensuring the linker prefers a real definition over NULL. The series also includes a new test suite covering a wide range of weak/strong symbol interactions.
