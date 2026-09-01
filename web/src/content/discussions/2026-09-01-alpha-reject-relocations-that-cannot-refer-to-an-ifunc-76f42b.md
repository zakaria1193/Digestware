---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- ifunc
- relocation
- error handling
discussion_id: 20260901023318.3503991-7-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 06/11] alpha: reject relocations that cannot refer to an IFUNC'
headline: 'alpha: reject relocations that cannot refer to an IFUNC'
tldr: Reject invalid relocation types that incorrectly attempt to reference an IFUNC
  directly.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves robustness by catching incorrect relocation usage.
- May require users to adjust their code or build process if these invalid relocations
  are being generated.
exchanges: []
primer_expert: This series of patches adds validation to the alpha ELF linker to prevent
  the use of certain relocation types (R_ALPHA_BRADDR, R_ALPHA_BRSGP, gp-relative,
  R_ALPHA_REFLONG) when referencing an IFUNC. These relocations attempt to resolve
  the IFUNC symbol directly, bypassing the intended mechanism which involves a GOT
  entry or an R_ALPHA_IRELATIVE relocation. The linker will now emit errors for these
  invalid combinations.
primer_glossary: []
series_id: 'binutils:alpha: reject relocations that cannot refer to an ifunc'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-7-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch series introduces checks in the alpha ELF linker to reject specific relocation types that cannot correctly reference an IFUNC. These include R_ALPHA_BRADDR, R_ALPHA_BRSGP, gp-relative relocations, and R_ALPHA_REFLONG, which name the symbol directly or have insufficient field size. By reporting these errors, the linker ensures that all references to IFUNCs go through the appropriate GOT entry or data word that utilizes R_ALPHA_IRELATIVE.
