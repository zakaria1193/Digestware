---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- x86-64
- optimization
- codegen
discussion_id: 2093154315.245285.1794946002198@connect.xfinity.com
source_type: public_inbox
title: 'Code generation for C compound literals: why so odd?'
headline: 'Code generation for C compound literals: why so odd?'
tldr: GCC generates unusual x86 code for C compound literals, possibly due to an optimization
  quirk.
proposer: Andrey Tarasevich <atarasevich@comcast.net>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- 'Code size vs. performance: The current generation might be a trade-off for some
  unstated performance goal, though it appears suboptimal.'
- 'Compiler complexity: The unusual code might stem from intricate optimization passes
  that are difficult to decipher.'
exchanges: []
primer_expert: This discussion concerns GCC's x86-64 code generation for C compound
  literals, specifically when returning struct P. The generated assembly exhibits
  unusual patterns for initializing the `r` and `e` members, involving stack preparation
  and bitwise operations that seem inefficient compared to direct struct initialization
  or member assignment. The author suspects an optimization pass or instruction selection
  issue.
primer_glossary:
- term: compound literal
  definition: A C language construct that creates an unnamed object with automatic
    storage duration, initialized with a specified value. It's often used for initializing
    structs or arrays without declaring a named variable.
- term: x86-64
  definition: A 64-bit common instruction set architecture, widely used in desktop
    and server processors. GCC generates machine code for this architecture.
- term: -O3
  definition: A GCC compiler optimization flag that enables a high level of aggressive
    optimizations, aiming for maximum performance at the potential cost of increased
    compile time and code size.
- term: ABI
  definition: Application Binary Interface. Defines how low-level binary code is structured,
    including function calling conventions, data type sizes, and register usage, ensuring
    interoperability between compiled code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/2093154315.245285.1794946002198@connect.xfinity.com
bugzilla_url: null
date: '2026-11-17'
is_stub: false
stub_reason: ''
---

The author questions GCC's -O3 code generation for C compound literals, specifically noting an inefficient sequence involving stack-based initialization and register manipulation.  Alternative function implementations produce more straightforward assembly. The issue appears to be specific to compound literals, suggesting a potential optimization or codegen bug.
