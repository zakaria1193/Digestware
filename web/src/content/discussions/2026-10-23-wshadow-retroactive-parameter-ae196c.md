---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- warning
- shadowing
- parameters
discussion_id: atvQDqWEqDAERpY5@debian
source_type: public_inbox
title: -Wshadow=retroactive-parameter
headline: Wshadow=retroactive-parameter
tldr: Proposes a new GCC warning flag to catch potentially dangerous retroactive parameter
  declarations.
proposer: Alejandro Colomar <alx+gcc@kernel.org>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Potential for new warnings to flag code that, while unusual, might be intentionally
  written or may not cause runtime issues.
- Balancing strictness of checks against the risk of false positives.
- Ensuring the warning accurately targets the problematic pattern without over-flagging.
exchanges: []
primer_expert: This proposal introduces a new GCC warning option to detect a specific
  type of shadowing issue within function parameter declarations. The concern arises
  when a parameter name shadows a variable that has already been referenced within
  the *same* parameter list, before the parameter itself is declared. This could be
  a footgun for developers expecting intuitive behavior, particularly with C's declaration
  syntax.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/atvQDqWEqDAERpY5@debian
bugzilla_url: null
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

Alejandro Colomar proposes a new GCC warning flag, `-Wshadow=retroactive-parameter`, to detect a specific type of dangerous coding pattern. This pattern involves declaring a function parameter that shadows a previously used variable within the same parameter list, which could lead to programmer confusion and bugs if the intuitive meaning differs from the compiler's interpretation. The proposed warning aims to be included in `-Wextra` and should not break existing code, as it targets likely erroneous constructs.
