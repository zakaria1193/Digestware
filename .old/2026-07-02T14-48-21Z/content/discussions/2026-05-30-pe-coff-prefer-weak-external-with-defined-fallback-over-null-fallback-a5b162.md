---
project: binutils
subsystem: pe-coff
patch_id: null
tags:
- PE-COFF
- linker
- weak symbols
- fallback
- bfd
discussion_id: 20260530191522.57144-3-peter0x44@disroot.org
source_type: public_inbox
title: '[PATCH 2/3] PE-COFF: Prefer weak external with defined fallback over null
  fallback'
headline: 'PE-COFF: Prefer weak external with defined fallback over null fallback'
tldr: The linker now prefers weak external symbols with defined fallbacks over those
  with null fallbacks to avoid runtime crashes.
proposer: Peter Damianov <peter0x44@disroot.org>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- More complex symbol resolution logic vs. preventing crashes due to null fallbacks.
- Potential for unexpected behavior if a null fallback is intentionally desired.
exchanges:
- author: Peter Damianov <peter0x44@disroot.org>
  role: proposer
  position: Modifies the linker to prefer weak externals with defined symbols as fallbacks,
    preventing crashes when a weak declaration is linked before a weak definition.
  quote: 'Fix this by comparing the fallback targets when two weak externals

    meet: if the incoming weak external''s fallback resolves to a defined

    symbol and the existing one does not (or points to NULL),

    update the aux record to use the better fallback.'
primer_expert: In ``bfd/cofflink.c``, when two PE COFF weak externals meet, the patch
  checks if the incoming weak external's fallback resolves to a defined symbol and
  the existing one does not (or points to NULL) and updates the aux record to use
  the better fallback.
primer_general: In PE COFF linking, 'weak externals' are symbols that can optionally
  fall back to a default definition if no strong definition is found. This patch addresses
  a scenario where multiple weak externals exist for the same symbol. It ensures that
  if one weak external has a valid fallback (a function), and another has a NULL fallback
  (meaning it resolves to zero if not defined), the linker will choose the valid fallback,
  preventing a crash when the function is called. This is especially relevant for
  C++ features like operator new and personality routines.
series_id: 'binutils:pe-coff: prefer weak external with defined fallback over null
  fallback'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260530191522.57144-3-peter0x44@disroot.org
bugzilla_url: null
date: '2026-05-30'
is_stub: false
---

When linking PE COFF objects, the linker can encounter multiple weak external symbols for the same name. This patch modifies the linker to prefer a weak external with a non-null fallback (i.e., a function body) over one with a null fallback. This prevents runtime crashes that occur when the symbol resolves to address 0.
