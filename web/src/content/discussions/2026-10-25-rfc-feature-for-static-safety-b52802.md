---
project: gcc
subsystem: rfc
patch_id: null
tags:
- gcc
- sanitizers
- optimization
- safety
- rfc
discussion_id: f16135445fd8fb0c7415d16646ed244a943a3c39.camel@tugraz.at
source_type: public_inbox
title: 'RFC: feature for static safety'
headline: 'RFC: feature for static safety'
tldr: Martin Uecker proposes using UBSan trapping mode with -O2 and `[[gnu::warning("UNSAFE")]]
  void __builtin_trap()` to statically prove safety properties.
proposer: Martin Uecker <uecker@tugraz.at>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Potential for false positives where the optimizer cannot prove a trap is unreachable,
  requiring manual analysis.
- Limited applicability to certain UBSan checks and code structures.
- Reliance on aggressive optimization levels (-O2) which may not always be desirable
  or applicable.
exchanges:
- author: Martin Uecker <uecker@tugraz.at>
  role: proposer
  position: Proposes using UBSan trapping mode with a `__builtin_trap` declaration
    and -O2 optimization to statically identify and fix remaining safety issues.
  quote: What happens is that the sanitizer annotates the program with __builtin_trap()
    where there is a potential problem, while the optimizer then removes all traps
    it can show to be unreachable.
primer_expert: This RFC explores a technique to leverage GCC's UBSan and optimization
  passes to statically prove safety properties. By enabling UBSan traps and applying
  aggressive optimization, unreachable traps are eliminated, leaving behind only verifiable
  issues or false positives. This approach aims to complement traditional sanitization
  and fuzzing by providing a stronger guarantee against undefined behavior and safety
  violations, particularly for critical code segments.
primer_glossary:
- term: UBSan
  definition: Undefined Behavior Sanitizer. A runtime instrumentation tool that detects
    various types of undefined behavior in C/C++ code.
- term: trap
  definition: In this context, a trap refers to a signal or exception raised by the
    program, often used to halt execution when an error or critical condition is detected.
- term: optimization
  definition: The process by which a compiler transforms code to improve its performance
    (speed, size, power consumption) while preserving its functional behavior.
- term: statically prove
  definition: To mathematically demonstrate a property of a program without executing
    it, typically through analysis of its source code or intermediate representations.
- term: __builtin_trap
  definition: A GCC built-in function that causes the program to trap (terminate abnormally),
    usually used for indicating unrecoverable errors or unexercised code paths.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/f16135445fd8fb0c7415d16646ed244a943a3c39.camel@tugraz.at
bugzilla_url: null
date: '2026-10-25'
is_stub: false
stub_reason: ''
---

Martin Uecker proposes a novel technique for statically verifying safety properties by combining Undefined Behavior Sanitizer (UBSan) in trapping mode with GCC's -O2 optimization and a `__builtin_trap` declaration. This method aims to identify remaining edge cases that sanitizers might miss, thereby ensuring program safety.
