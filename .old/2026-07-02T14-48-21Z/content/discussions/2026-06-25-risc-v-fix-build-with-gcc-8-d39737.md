---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- gcc
- build-fix
- c-standard
discussion_id: alpine.DEB.2.21.2606252232520.58268@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [PATCH v3] RISC-V: Fix build with GCC-8'
headline: 'RISC-V: Fix build with GCC-8'
tldr: A patch to fix RISC-V Binutils compilation with GCC 8 by adding braces around
  declarations after case labels is reviewed with a suggestion for clearer commit
  m…
proposer: Maciej W. Rozycki <macro@orcam.me.uk>
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures compatibility with GCC 8 and potentially newer versions, allowing broader
  build support.
- Adheres to stricter C language standards, improving code robustness.
- Minor increase in code verbosity due to added braces.
exchanges:
- author: Mark Zhuang
  role: proposer
  position: Proposes a patch to fix build failures with GCC-8 and newer by adding
    braces around declarations after case labels.
  quote: GCC 8.5.0 rejects a declaration right after a case label. Add braces to fix
    it.
- author: Maciej W. Rozycki
  role: reviewer
  position: Suggests improving the commit message by referencing the relevant C standard
    and minimum compiler versions to provide better context for future readers.
  quote: I think it would be more useful to the reader if the commit referred to the
    relevant C language standard and minimum compiler version as given by Andreas.
primer_expert: This patch targets a specific C language conformance issue affecting
  Binutils' RISC-V target when compiled with older GCC versions (specifically GCC
  8 and potentially later, as noted by the reviewer). The problem stems from GCC's
  stricter interpretation of C standards regarding declarations within `switch` statement
  `case` labels, where a declaration immediately following a `case` without explicit
  braces is rejected. This is a common idiom in older C codebases that newer compilers,
  adhering to C99 or later, may flag as an error. The fix involves adding block scope
  (`{}`) to these declarations…
primer_general: Compilers translate code written by humans into instructions that
  computers can understand. Sometimes, different versions of compilers, or compilers
  that follow slightly different rules for the programming language (like C), might
  not agree on how to interpret certain code. This discussion is about a problem where
  the Binutils tools, used for working with compiled programs for RISC-V processors,
  failed to build with GCC-8. The issue was that GCC-8, and even some newer GCC versions,
  are stricter about how you declare variables inside 'switch' statements. The fix
  involves adding curly braces to make it clear where the variable is being declared,
  satisfying the compiler's requirements and allowing the code to build successfully.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2606252232520.58268@angie.orcam.me.uk
bugzilla_url: null
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This discussion reviews a patch (v3) intended to fix compilation issues for RISC-V Binutils when using GCC-8. The problem arises because GCC 8.5.0, and apparently GCC 10.2.1, rejects declarations immediately following `case` labels in `switch` statements, a common C idiom. The proposed fix involves adding braces (`{}`) around these declarations to conform to stricter C standards. A reviewer suggests enhancing the commit message to reference the relevant C language standard and minimum compiler version for future clarity.
