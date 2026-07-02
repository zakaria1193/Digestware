---
project: binutils
subsystem: x86/intel
patch_id: null
tags:
- assembler
- x86
- intel syntax
- recursion
- gas
discussion_id: 6c7ea50b-2bd6-45b8-9112-e452b5a2c376@suse.com
source_type: public_inbox
title: '[PATCH] x86/Intel: avoid infinite recursion in i386_intel_simplify_symbol()
  (again)'
headline: 'X86/Intel: avoid infinite recursion in i386_intel_simplify_symbol() (again)'
tldr: This patch fixes an infinite recursion issue in i386_intel_simplify_symbol()
  and adds a testcase to prevent regressions.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Under Review
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- The patch adds complexity to the symbol simplification logic.
- The added testcase increases the testsuite runtime.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes a patch to fix an infinite recursion issue and adds a testcase
    to prevent regressions.
  quote: 'The same problem has appeared again due to insufficient use of the "resolving"
    property (respective helpers originally introduced for this PR) in 22f8905d9f38
    ("x86/Intel: don''t modify equates'' expressions"). Also put in place a testcase,
    so this (hopefully) won''t regress again.'
- author: Jan Beulich <jbeulich@suse.com>
  role: contributor
  position: Notes a failure on COFF/PE targets when `--32` is used and "noprefix"
    is missing.
  quote: This fails for (at least) COFF/PE targets when as is passed --32. There looks
    to be a separate issue there, but ... ... "noprefix" was missing here anyway (for
    Intel syntax this really should be the default).
primer_expert: This patch addresses a recursion issue in the x86-specific assembly
  simplification logic within GNU as. The `i386_intel_simplify_symbol` function is
  responsible for resolving symbol references in Intel syntax assembly code. The patch
  ensures proper handling of symbol resolution to prevent infinite loops, and adds
  a testcase (`gas/testsuite/gas/i386/intel-equ-loop.s`) to prevent future regressions.
  The surrounding logic deals with `.intel_syntax` assembly.
primer_general: The GNU Assembler (gas) is a tool that translates assembly code (human-readable
  instructions) into machine code (binary instructions that a computer can execute).
  This patch fixes a bug in the assembler's handling of x86 Intel syntax, where it
  could get stuck in an infinite loop when simplifying symbol references.  The patch
  prevents this from happening and adds a test case to ensure the issue doesn't reappear
  in the future.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/6c7ea50b-2bd6-45b8-9112-e452b5a2c376@suse.com
bugzilla_url: null
date: '2026-05-08'
---

Jan Beulich submits a patch to fix an infinite recursion issue in the `i386_intel_simplify_symbol()` function, which is related to PR gas/30308. The issue re-emerged due to insufficient use of the "resolving" property. The patch adds a testcase to prevent future regressions. He also notes a failure on COFF/PE targets when `--32` is used and "noprefix" is missing.
