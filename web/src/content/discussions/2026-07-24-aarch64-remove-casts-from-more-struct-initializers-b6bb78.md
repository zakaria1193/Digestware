---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- compiler
- code-generation
- cleanup
discussion_id: 20f5044f-1c6a-4988-bda3-67495b8423e4@suse.com
source_type: public_inbox
title: '[PATCH] aarch64: remove casts from more struct initializers'
headline: 'aarch64: remove casts from more struct initializers'
tldr: Cleans up struct initializers in aarch64 target code.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 9
technical_tradeoffs:
- Minor code simplification versus the minimal risk of introducing regressions in
  opcode generation.
- Improving code clarity by removing casts.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Submitted a patch to remove unnecessary casts from struct initializers
    in the aarch64 code generation, extending previous cleanup efforts.
  quote: 'Commit 0e89ce812b79 ("aarch64: Remove cast from struct initializer") didn''t
    go quite far enough: The building of aarch64-gen itself has a similar issue. Cover
    that as well. Since FLD_CONST_* are used only there, move their #define-s there
    rather than introducing more #undef-s.'
- author: Alice Carlotti
  role: reviewer
  position: Acknowledged the patch and apologized for previous issues caused by related
    changes.
  quote: OK, thanks - and apologies again for the breakage.
primer_expert: This patch in binutils targets the aarch64 architecture's opcode generation.
  It refines `aarch64-gen.c` by removing superfluous casts in struct initializers,
  addressing an oversight from a prior commit (0e89ce812b79). The change also relocates
  `FLD_CONST_*` definitions to reduce boilerplate.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20f5044f-1c6a-4988-bda3-67495b8423e4@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

Jan Beulich submitted a patch to further clean up struct initializers in the aarch64 target's code generation, specifically addressing issues in aarch64-gen.c that were missed by a previous commit. Alice Carlotti acknowledged the patch and apologized for prior breakage.
