---
project: binutils
subsystem: gas
patch_id: null
tags:
- BPF
- gas
- assembler
- testing
- byte order
discussion_id: 55e2d94e-d089-4f29-8b6d-93e7964fd66a@linux.dev
source_type: public_inbox
title: 'Re: [PATCH v3 1/5] gas: bpf: actually run the pseudo-C spacing test'
headline: 'BPF gas: Run pseudo-C spacing test'
tldr: BPF gas pseudo-C spacing tests are now executed, fixing byte order issues and
  ensuring correct assembly.
proposer: Vineet Gupta <vineet.gupta@linux.dev>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Enables previously untested code, improving overall test coverage.
- Fixes a byte-order mismatch, ensuring accurate assembly for little-endian targets.
- Reflects correct assembly behavior for instructions with flexible spacing.
exchanges:
- author: Jose E. Marchesi
  role: reviewer
  position: Approves the patch, acknowledging the fix for running BPF pseudo-C spacing
    tests and the correction of byte order issues.
  quote: OK. Thanks for the patch.
- author: Vineet Gupta
  role: proposer
  position: Submits a patch to enable and correct the BPF pseudo-C spacing tests in
    the gas test suite.
  quote: 'Enabling it exposes a second problem: the .d declares -EB while its

    expected encodings are little endian, so the test fails on byte order

    alone.'
primer_expert: 'This patch addresses an issue where BPF gas pseudo-C spacing tests
  (`spacing-pseudoc.s` and `spacing-pseudoc.d`) were defined but never executed because
  they were missing from the `bpf.exp` test runner. The patch adds `run_dump_test
  spacing-pseudoc` to `bpf.exp`. Upon enabling, a byte-order mismatch was found: the
  test''s `.d` file specified big-endian (`-EB`), but the expected output was little-endian.
  The patch corrects this by changing the assembly directive to little-endian (`-EL`),
  ensuring the test accurately reflects the intended behavior for instructions with
  flexible spacing.'
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter, a technology that allows sandboxed programs
    to safely execute code in the Linux kernel, often used for networking and tracing.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    converting assembly language code into machine code.
- term: pseudo-C
  definition: A dialect or style of assembly language that mimics C language syntax
    for clarity or specific testing purposes.
- term: spacing test
  definition: A test case designed to verify how an assembler handles whitespace and
    token boundaries between instruction mnemonics, operands, and labels.
- term: byte order
  definition: The order in which bytes are arranged in computer memory for multi-byte
    data types. Common orders are little-endian (least significant byte first) and
    big-endian (most significant byte first).
series_id: 'binutils:gas: bpf: actually run the pseudo-c spacing test'
series_role: reply
series_parts:
- title: 'gas: bpf: actually run the pseudo-C spacing test'
  url: https://inbox.sourceware.org/binutils/87qzj546y5.fsf@gnu.org
  n: 1
  total: 5
- title: 'gas: bpf: actually run the pseudo-C spacing test'
  url: https://inbox.sourceware.org/binutils/20260907091102.2595057-2-vineet.gupta@linux.dev
  n: 1
  total: 5
url: https://inbox.sourceware.org/binutils/55e2d94e-d089-4f29-8b6d-93e7964fd66a@linux.dev
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

This patch enables the execution of BPF gas pseudo-C spacing tests by adding them to the `bpf.exp` test suite. Previously, these tests were never run, leading to undiscovered issues. Enabling them revealed a byte order problem where the test declared big-endian assembly (`-EB`) but expected little-endian output. The patch corrects this by setting the assembler to little-endian (`-EL`), aligning the test with its expected encodings and filename. This ensures proper assembly of instructions with flexible spacing, such as `goto+1` and conditional jumps.
