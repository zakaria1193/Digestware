---
project: binutils
subsystem: x86/intel
patch_id: null
tags:
- gas
- assembler
- x86
- intel syntax
- recursion
discussion_id: 8ffded37-0027-4de5-9e23-37ed43dba6f8@suse.com
source_type: public_inbox
title: '[PATCH v2] x86/Intel: avoid infinite recursion in i386_intel_simplify_symbol()
  (again)'
headline: 'x86/Intel: avoid infinite recursion in i386_intel_simplify_symbol() (again)'
tldr: Fixes a potential infinite recursion in the x86 assembler's symbol simplification
  logic, and adds a test case to prevent regressions.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Added complexity to symbol resolution logic to prevent infinite recursion.
- Slight performance impact due to additional checks during symbol simplification.
exchanges: []
primer_expert: The `i386_intel_simplify_symbol` function in `gas/config/tc-i386-intel.c`
  simplifies symbols during assembly of x86 Intel syntax. The function can enter infinite
  recursion when processing chains of equates. The patch uses the `symbol_resolving_p`
  property to detect and prevent such loops. A new test case `gas/testsuite/gas/i386/intel-equ-loop.l`
  is added.
primer_general: The GNU assembler (`gas`) translates assembly language into machine
  code. Equates (using the `.equ` directive) define symbolic constants.  The assembler
  simplifies symbols, replacing them with their constant values where possible. This
  patch fixes a bug in the x86-specific symbol simplification logic that could cause
  the assembler to get stuck in an infinite loop when processing complex chains of
  equates, leading to a build failure. The fix prevents this recursion and improves
  assembler robustness.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/8ffded37-0027-4de5-9e23-37ed43dba6f8@suse.com
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

This patch addresses a re-emergence of an infinite recursion issue within the `i386_intel_simplify_symbol()` function in the x86 assembler. The problem arises when dealing with equates and symbol chains. The patch enhances the use of the 'resolving' property to prevent the recursion. A new test case is added to ensure this issue doesn't reappear in future updates, enhancing the assembler's stability.
