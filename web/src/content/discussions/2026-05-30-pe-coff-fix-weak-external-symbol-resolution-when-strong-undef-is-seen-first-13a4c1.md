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
discussion_id: 20260530191522.57144-2-peter0x44@disroot.org
source_type: public_inbox
title: '[PATCH 1/3] PE-COFF: Fix weak external symbol resolution when strong undef
  is seen first'
headline: 'PE-COFF: Fix weak external symbol resolution when strong undef is seen
  first'
tldr: Fixes an issue where weak external symbols in PE COFF are incorrectly resolved
  when a strong undefined reference is encountered first.
proposer: Peter Damianov <peter0x44@disroot.org>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Increased complexity in symbol resolution logic vs. correct handling of weak externals.
- Potential performance impact due to additional checks during linking.
exchanges:
- author: Peter Damianov <peter0x44@disroot.org>
  role: proposer
  position: Fixes the incorrect resolution of weak external symbols when a strong
    undefined reference is encountered before the weak definition, updating symbol_class
    and aux records and extending the relocation handler.
  quote: 'Fix by extending the condition in coff_link_add_symbols to also update

    symbol_class and aux when the incoming symbol is a PE weak external

    with aux and the existing hash is still undefined.  Also extend the

    relocation handler to resolve the weak alias fallback for

    bfd_link_hash_undefined symbols that carry C_NT_WEAK class and have

    an aux record.'
primer_expert: The patch modifies ``coff_link_add_symbols`` in ``bfd/cofflink.c``
  to store ``symbol_class`` and aux record when a PE weak external with aux meets
  an existing undefined hash entry. It also extends ``_bfd_coff_generic_relocate_section``
  to resolve weak alias fallback for undefined symbols with ``C_NT_WEAK`` class and
  aux.
primer_general: In PE COFF linking, 'weak externals' are symbols that can optionally
  fall back to a default definition if no strong definition is found.  This patch
  fixes a bug where, if code first declares that a symbol MUST exist (a 'strong undefined
  reference'), then later provides a weak definition with a fallback, the linker would
  fail to use the fallback. This patch ensures that the linker correctly handles this
  case, which is important for C++ features like operator new, ensuring programs link
  correctly.
series_id: 'binutils:pe-coff: fix weak external symbol resolution when strong undef
  is seen first'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260530191522.57144-2-peter0x44@disroot.org
bugzilla_url: null
date: '2026-05-30'
is_stub: false
---

When linking PE-COFF objects, a weak external symbol may fail to resolve correctly if a strong undefined reference is encountered first. This patch fixes this issue by ensuring that the COFF-specific symbol class and auxiliary record are stored even when a strong undefined reference is seen first. The patch also extends the relocation handler to resolve the weak alias fallback for undefined symbols with a C_NT_WEAK class and an aux record.
