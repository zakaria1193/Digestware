---
project: gcc
subsystem: gcc/genoutput
patch_id: null
tags:
- genoutput
- optimization
- code size
- memory usage
commit_hash: d0b42b0016cdbe3e0ca86be8a888b305c96a8df0
source_type: github
author: Kyrylo Tkachov
headline: Compact insn_data and operand_data emission.
tldr: 'genoutput: Emit instruction and operand data more compactly, reducing file
  size and memory usage.'
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit restructures the generation of `insn_data` and `operand_data`
  in `genoutput.cc` to be more compact. It replaces the conditional logic for `HAVE_DESIGNATED_UNION_INITIALIZERS`
  (a GNU extension) with `constexpr` constructors for union members. This allows each
  table row to be emitted on a single line, drastically reducing source file size
  and indentation. The change also removes the fallback to a larger struct representation
  when designated initializers are unavailable. This improves memory usage during
  compilation and reduces the disk footprint of generated files, particularly for…
primer_glossary:
- term: genoutput
  definition: A component within GCC responsible for generating machine description
    files, which define instructions and their properties for target architectures.
- term: insn_data
  definition: Data structure containing information about machine instructions.
- term: operand_data
  definition: Data structure containing information about the operands of machine
    instructions.
- term: HAVE_DESIGNATED_UNION_INITIALIZERS
  definition: A preprocessor macro or feature that allows specific members of a C++
    union to be initialized using designated initializers. This commit removes its
    usage in favor of C++14 constexpr constructors.
- term: constexpr constructor
  definition: A constructor for a class or struct that can be evaluated at compile
    time. This allows objects to be initialized more efficiently and enables their
    use in compile-time computations.
- term: compact emission
  definition: A process of generating output code or data in a highly condensed format,
    reducing file size and potentially improving loading or processing times.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d0b42b0016cdbe3e0ca86be8a888b305c96a8df0
date: '2026-08-07'
is_stub: false
stub_reason: ''
---

The emission of `insn_data` and `operand_data` in the `genoutput` component has been significantly compacted, resulting in substantial reductions in generated file sizes and peak memory usage during compilation. This was achieved by replacing the use of `HAVE_DESIGNATED_UNION_INITIALIZERS` with `constexpr` constructors and emitting table rows more compactly. The changes lead to a dramatic decrease in the size of `insn-output.cc` and associated object files without affecting compile times.
