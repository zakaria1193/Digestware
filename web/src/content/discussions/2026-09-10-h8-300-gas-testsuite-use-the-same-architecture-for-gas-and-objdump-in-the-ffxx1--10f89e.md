---
project: binutils
subsystem: h8
patch_id: null
tags:
- H8/300
- gas
- objdump
- testsuite
- architecture
discussion_id: 20260910115420.494711-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH] H8/300: gas: testsuite: Use the same architecture for gas and objdump
  in the FFxx1 test case.'
headline: 'H8/300: gas: testsuite: Use the same architecture for gas and objdump in
  the FFxx1 test case.'
tldr: Fixes H8/300 test case by ensuring objdump uses the correct architecture.
proposer: Jan Dubiec
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 10
technical_tradeoffs:
- Ensures test suite accuracy by correctly specifying the target architecture for
  disassembly.
- Minor change that improves reliability of testing for specific architectures.
exchanges:
- author: Jan Dubiec
  role: proposer
  position: Submits a patch to ensure objdump uses the H8/300 architecture in a test
    case, resolving assembly/disassembly mismatches.
  quote: This patch fixes the issue by telling objdump which architecture to use.
- author: Jan Beulich
  role: reviewer
  position: Acknowledges the patch and the problem description.
  quote: null
primer_expert: This patch addresses a specific test case failure in the `gas` assembler's
  test suite for the H8/300 architecture. The issue arises from a discrepancy between
  how `gas` and `objdump` interpret the target architecture. `gas` correctly assembles
  H8/300 instructions (e.g., using 16-bit registers like `r1`), but `objdump` defaults
  to a more recent variant (H8/300H) which uses 32-bit registers (e.g., `er1`). This
  patch forces `objdump` to use the correct H8/300 architecture flag in the test,
  aligning its disassembly with `gas`'s assembly and resolving the test failure.
primer_glossary:
- term: gas
  definition: The GNU Assembler, a component of the binutils package responsible for
    converting assembly language code into machine code.
- term: H8/300
  definition: A family of microcontrollers manufactured by Renesas (formerly Hitachi).
- term: objdump
  definition: A utility in the binutils package used to display information from object
    files, including disassembly of machine code.
- term: test case
  definition: A specific set of conditions and steps designed to test a particular
    feature or bug fix in software.
- term: architecture
  definition: The fundamental design and organization of a computer system's hardware,
    including its instruction set and register set.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260910115420.494711-1-jdx@o2.pl
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This patch corrects a failing test case for the H8/300 architecture in the gas assembler's test suite. The `FFxx1` test fails because `gas` assembles code for H8/300, but `objdump` defaults to disassembling it as H8/300H code, leading to mismatched output. The fix involves explicitly telling `objdump` to use the H8/300 architecture, ensuring consistent interpretation and passing the test.
