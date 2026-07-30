---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- sframe
- cfi
- debugging
discussion_id: 20260729163445.2563223-3-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 2/2] gas: sframe: Add test for signal frame with unsupported CFI'
headline: 'gas: sframe: Add test for signal frame with unsupported CFI'
tldr: Adds a test case for gas's SFrame generation when encountering unsupported CFI
  directives in signal frames.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensuring robustness of SFrame generation with malformed CFI.
- Graceful error handling vs. strict enforcement of CFI rules.
- Maintaining compatibility with different CFI specifications.
exchanges: []
primer_expert: This patch adds a new test case to the gas testsuite to verify the
  behavior of the SFrame (Stack Frame) generation when processing signal frames that
  contain unsupported CFI directives. The test ensures that gas gracefully handles
  such unsupported directives by generating an 'empty' FDE without any Resource Entries
  (FREs), rather than encountering a crash or producing malformed SFrame data. This
  is important for robust stack unwinding and debugging information generation.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of GNU Binutils.
- term: sframe
  definition: Stack Frame, a data structure used by debuggers and runtime systems
    to reconstruct the call stack.
- term: CFI
  definition: Call Frame Information, a set of directives used in DWARF debugging
    information to describe how to unwind the stack.
- term: FDE
  definition: Frame Description Entry, a component of DWARF debugging information
    that describes a function's stack frame setup and teardown.
- term: signal frame
  definition: A specific type of stack frame used when handling asynchronous signals,
    which may have different unwinding requirements than regular function calls.
- term: unsupported CFI
  definition: Call Frame Information directives that are not recognized or handled
    by the current version of the assembler or debugging information generator.
series_id: 'binutils:gas: sframe: add test for signal frame with unsupported cfi'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260729163445.2563223-3-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

This patch introduces a new test case for the GNU Assembler's (gas) SFrame generation mechanism. It specifically targets scenarios where unsupported Call Frame Information (CFI) directives are used within signal frames, ensuring that gas behaves correctly by producing an empty FDE (Frame Description Entry) instead of crashing or generating invalid data.
