---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- avr
- coding-style
- cleanup
discussion_id: 23934801-2f1c-4fbb-b3dc-23ebe4dc7fc9@gjlay.de
source_type: public_inbox
title: '[patch, avr, applied] Fix indentations to follow GNU style'
headline: Fix indentations to follow GNU style
tldr: A patch was applied to the AVR Binutils component to standardize indentation
  to use tabs instead of spaces, conforming to GNU coding style.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Committed
outcome: committed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves code readability and maintainability by enforcing a consistent coding style.
- Reduces potential for style violations in future contributions.
- No functional impact on the AVR toolchain or compiled binaries.
exchanges: []
primer_expert: This patch is a purely cosmetic change to the `gas/config/tc-avr.c`
  and `gas/config/tc-avr.h` files, which are part of the GNU Assembler's (GAS) backend
  for the AVR architecture. The modification specifically addresses code formatting
  by enforcing the GNU coding style's indentation policy, which mandates the use of
  TAB characters rather than spaces for indentation. This is a common practice in
  projects like Binutils to maintain code uniformity and readability across a large
  codebase.
primer_general: This discussion is about a small, non-functional change to the source
  code of Binutils, the set of programming tools for microcontrollers like the AVR.
  The change simply updates how the code is indented, replacing spaces with tabs.
  This is done to make the code more consistent with the 'GNU coding style,' a set
  of rules for how to write code that helps multiple developers work together on large
  projects. It's like making sure everyone uses the same formatting in documents,
  even if it doesn't change the meaning of the words.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/23934801-2f1c-4fbb-b3dc-23ebe4dc7fc9@gjlay.de
bugzilla_url: null
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This patch, which has already been applied to the trunk, modifies the AVR target's source code within Binutils to enforce GNU coding style for indentation. Specifically, it replaces all instances of spaces used for indentation with tabs in `tc-avr.c` and `tc-avr.h`. This change is purely stylistic and does not alter the code's functionality, focusing solely on code cleanliness and consistency with project standards.
