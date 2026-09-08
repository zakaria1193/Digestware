---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- internal
- optimization
- cleanup
discussion_id: CACAb0qf3QfLDrJR8G_JaYjH=Uhaw1Oqv75KCHxAbZKmjQ6PLiQ@mail.gmail.com
source_type: public_inbox
title: 'RE: Remove double-int.'
headline: Remove double-int.
tldr: Proposes removing the double-int implementation in favor of wide-int.h's fixed_wide_int.
proposer: Kael Andrew Franco <kaelfandrew@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Simplifies build process by removing a component.
- Reduces memory allocation overhead by using heap-less wide integers.
- Requires updating multiple call sites across the compiler.
exchanges: []
primer_expert: The `double-int` implementation in GCC provides 128-bit integer arithmetic,
  likely used for intermediate calculations in tree-ssa or RTL. This RFC suggests
  replacing it with `fixed_wide_int` from `wide_int.h`, which avoids heap allocations
  and may simplify related code, particularly in constant folding and tree node construction.
  The removal would affect multiple parts of the compiler, including AVR backend,
  C++ parser, dwarf2out, and RTL manipulation.
primer_glossary:
- term: double-int
  definition: A GCC internal data type or implementation for handling 128-bit integers,
    likely used for intermediate values in calculations.
- term: wide-int.h
  definition: A GCC header file providing fixed-width arbitrary precision integer
    types, potentially an alternative or replacement for double-int.
- term: PR126622
  definition: A specific bug report within the GCC project, which this change aims
    to help resolve.
- term: build_int_cst
  definition: Likely a function or component within GCC responsible for building integer
    constants, possibly related to tree or RTL representations.
- term: tree-ssa
  definition: GCC's primary intermediate representation (IR) and analysis framework,
    using Static Single Assignment form.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used by GCC
    after the SSA phase.
- term: dwarf2out.cc
  definition: A GCC source file responsible for generating DWARF debugging information,
    version 2.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CACAb0qf3QfLDrJR8G_JaYjH=Uhaw1Oqv75KCHxAbZKmjQ6PLiQ@mail.gmail.com
bugzilla_url: null
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

This RFC proposes to remove the `double-int` component from GCC. The author argues that `wide_int.h`'s `fixed_wide_int` offers similar functionality without heap usage, simplifying parts of the build process and helping with a specific bug (PR126622). The change would involve removing `double-int.{cc,h}` and updating various other GCC components that currently depend on it.
