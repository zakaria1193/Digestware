---
project: gcc
subsystem: gcc/genoutput
patch_id: null
tags:
- optimization
- build
- aarch64
commit_hash: 13efaa5e7dcc882734e384f6a3f4061c7a8286b8
source_type: github
author: Kyrylo Tkachov
headline: genoutput writes each output template only once
tldr: Reduces code size and improves compile times by avoiding redundant output template
  definitions.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The genoutput pass in GCC generates output definitions for instruction
  patterns. This change optimizes this process by deduplicating identical output definitions.
  Previously, patterns using mode iterators could generate redundant definitions if
  the template text was the same across different modes. The optimization now keys
  definitions on both template text and source location, and for templates processed
  by `gensupport` without a location, it keys on text alone. Redundant definitions
  are replaced by references to the first emitted definition, with the count of alternatives
  preserved to maint…
primer_glossary:
- term: genoutput
  definition: A GCC pass responsible for generating the output definitions for instruction
    patterns based on the machine description.
- term: output template
  definition: A part of the machine description that specifies how to format the output
    for a particular instruction pattern.
- term: iterator
  definition: A construct in GCC's machine description that allows a single pattern
    to be expanded over multiple modes or values, effectively generating multiple
    instructions.
- term: define_insn
  definition: A directive in the GCC machine description that defines an instruction
    pattern.
- term: mode iterator
  definition: A type of iterator that expands a pattern for each available machine
    mode (e.g., `SImode`, `DImode`).
- term: gensupport
  definition: A tool used by GCC to process machine description files, often handling
    compact syntax for patterns.
- term: '#line'
  definition: A special directive in generated code that indicates the original source
    file and line number, used for debugging and diagnostics.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/13efaa5e7dcc882734e384f6a3f4061c7a8286b8
date: '2026-09-09'
is_stub: false
stub_reason: ''
---

The genoutput pass now ensures that each unique output template is defined only once, significantly reducing the generated code size and improving compilation performance. Previously, identical templates were redefined multiple times, especially when using iterators. By keying on both the template text and its source location, redundant definitions are now avoided, with subsequent identical templates simply referencing the first. This change led to a substantial reduction in output definition counts and decreased compile times and memory usage on aarch64.
