---
project: binutils
subsystem: gas
patch_id: null
tags:
- PDP-11
- assembler
- patch
discussion_id: 20260907065924.660482-1-bson@rockgarden.net
source_type: public_inbox
title: '[PATCH] GAS: Add WORKING_DOT_WORD to tc-pdp11.h'
headline: 'GAS: Add WORKING_DOT_WORD to tc-pdp11.h'
tldr: Patch adds WORKING_DOT_WORD to PDP-11 GAS configuration to fix .WORD directive
  issues.
proposer: Jan Brittenson <bson@rockgarden.net>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 6
technical_tradeoffs:
- Disabling a workaround for specific architectures versus maintaining compatibility
  or robustness for others.
- Clarity of macro definitions (e.g., `WORKING_DOT_WORD` vs. `BROKEN_DOT_WORD`).
exchanges:
- author: Jan Brittenson
  role: proposer
  position: Submitted a patch to add WORKING_DOT_WORD to tc-pdp11.h, explaining it
    resolves issues with .WORD directives.
  quote: 'Without WORKING_DOT_WORD for pdp11 a .WORD with a forward reference

    will sometimes produce bogus 8-byte sequences.  Since it''s strictly

    16-bit, it should never need the workaround this #define turns off.'
- author: Jan Beulich
  role: reviewer
  position: Questioned the rationale for disabling the workaround without sufficient
    explanation, requesting more context on WORKING_DOT_WORD's purpose.
  quote: 'This is too little of an explanation for suddenly, after many years,

    disabling a workaround. (It''s not even clear to me whether

    WORKING_DOT_WORD is purely a gas-internal thing, or providing some

    level of "compatibility" with native assemblers. In'
- author: Hans-Peter Nilsson
  role: reviewer
  position: Agreed with Jan Beulich that the explanation is insufficient and suggested
    that the workaround is likely unnecessary for the PDP-11's 16-bit architecture.
  quote: "I agree with Jan ...er, Jan B ...er, \"bson\" (just cherishing the \nname\
    \ collision :) that this doesn't seem useful in the PDP11 \nworld, where you wouldn't\
    \ need handling overflow of 16-bit \nsigned offsets in a 32-bit context as it's\
    \ all 16-bit."
- author: Hans-Peter Nilsson
  role: reviewer
  position: Suggested creating a bug report with a test case if the issue is indeed
    reproducible, and proposed an alternative define name.
  quote: "That said, a test-case for PDP11 where this produced wrong code \nwould\
    \ be interesting.  May I suggest to open a bugzilla entry \nand add assembly code\
    \ there?\n\nbrgds, H-P"
- author: Jan Brittenson
  role: proposer
  position: Responded to feedback, suggesting that only a few machines (m68k, s390)
    require the workaround and that defining BROKEN_DOT_WORD might be a clearer approach.
  quote: 'Yeah, as far as I can tell there''s only two machines that require, or

    rely on it: m68k and s390.  Every'
- author: Hans-Peter Nilsson
  role: reviewer
  position: Suggested an alternative approach of defining BROKEN_DOT_WORD instead
    of WORKING_DOT_WORD for clarity.
  quote: null
primer_expert: This patch addresses a specific issue in the PDP-11 GAS backend related
  to the `.WORD` directive when dealing with forward symbol references. The `WORKING_DOT_WORD`
  macro, when defined, disables a workaround that was originally intended for architectures
  where 16-bit operations might interact with larger address spaces, potentially causing
  issues. For the PDP-11, which is strictly 16-bit, this workaround is unnecessary
  and can lead to incorrect code generation (bogus 8-byte sequences). The patch adds
  this define to `tc-pdp11.h` to correct this behavior.
primer_glossary:
- term: GAS
  definition: The GNU Assembler.
- term: WORKING_DOT_WORD
  definition: A preprocessor macro used in GAS to control specific behaviors related
    to the `.WORD` directive, often to disable workarounds on architectures where
    they are not needed.
- term: PDP-11
  definition: A popular 16-bit minicomputer from Digital Equipment Corporation, known
    for its influence on computer architecture and programming.
- term: .WORD directive
  definition: An assembler directive that defines a 16-bit data word.
- term: Forward reference
  definition: A reference to a symbol (like a label or variable) that is defined later
    in the source code.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260907065924.660482-1-bson@rockgarden.net
bugzilla_url: null
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

Jan Brittenson proposes adding the WORKING_DOT_WORD define to the PDP-11 GAS configuration. This change aims to fix an issue where .WORD directives with forward references could produce incorrect 8-byte sequences on the strictly 16-bit PDP-11 architecture. The define is intended to disable a workaround that is not needed for this architecture.
