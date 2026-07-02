---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- smtgcc
- testing
- compiler-validation
- performance
discussion_id: Pine.NEB.4.64.2607011339410.4763@gateway.kwa
source_type: public_inbox
title: smtgcc mid-year update
headline: smtgcc mid-year update
tldr: Update on smtgcc, a translation validator for GCC, highlighting performance
  improvements, real-world testing, backend support, and ongoing GCC test suite runs.
proposer: Krister Walfridsson <krister.walfridsson@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adopting Bitwuzla improved performance but requires integrating and maintaining
  support for a new SMT solver.
- Expanding backend support increases complexity but broadens the tool's applicability.
- Testing with `-fno-strict-aliasing` and `-fno-section-anchors` limits the scope
  of validation but allows for broader initial testing (e.g., on the Linux kernel).
exchanges:
- author: Krister Walfridsson
  role: proposer
  position: Provides a status update on smtgcc, detailing performance improvements,
    expanded backend support, and its use in testing real-world software and the GCC
    test suite.
  quote: null
primer_expert: This is a status report for 'smtgcc', a tool that acts as a translation
  validator for GCC. It checks that the generated assembly code is a refinement of
  the GIMPLE Intermediate Representation (IR). The report details improvements in
  performance (aided by the Bitwuzla SMT solver), expanded backend support (AArch64,
  RISC-V, BPF, SH, m68k), and its usage in finding bugs in real software like the
  Linux kernel and in the GCC test suite itself. Notably, smtgcc currently does not
  support strict aliasing or section anchors, requiring specific testing configurations.
primer_glossary:
- term: smtgcc
  definition: A translation validator for GCC that checks if the generated assembly
    code correctly reflects the GIMPLE Intermediate Representation.
- term: SMT solver
  definition: Satisfiability Modulo Theories solver, a tool used in program analysis
    to determine the satisfiability of logical formulas.
- term: GIMPLE
  definition: GCC's Internal Representation (IR) used after the parsing and initial
    tree construction stages, optimized before generating machine code.
- term: Canonicalization
  definition: The process of converting data into a standard or canonical form, often
    used to simplify comparisons or processing.
- term: Translation validator
  definition: A tool that verifies the correctness of a translation process, in this
    case, ensuring the compiler's IR is accurately translated to assembly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/Pine.NEB.4.64.2607011339410.4763@gateway.kwa
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

Krister Walfridsson provides a mid-year update on smtgcc, his translation validator for GCC. Significant performance improvements have been achieved, reducing timeouts by 90% through the addition of the Bitwuzla SMT solver and better canonicalization. Smtgcc is now capable of finding issues in real-world software, with two bugs found during Linux kernel compilation. The smtgcc-tv-backend now supports AArch64, RISC-V, BPF, SH, and m68k targets. Weekly runs of the GCC test suite continue, with testing focused on specific optimization levels and architectures, and with known limitations regarding type-based aliasing and section anchors.
