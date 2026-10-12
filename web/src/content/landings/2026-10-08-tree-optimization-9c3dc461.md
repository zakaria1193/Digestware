---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- optimization
- tree-ssa
- value-numbering
- pta
commit_hash: 9c3dc461749a1257b9939625ef59b2b056035311
source_type: github
author: Richard Biener
headline: Improve address-taken handling for .ASSUME
tldr: Compiler can better disambiguate calls and replicate IPA analysis by not treating
  .ASSUME arguments as address-taken.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This change modifies operand scanning and address updating logic in
  the SSA (Static Single Assignment) form. Specifically, `operands_scanner::parse_ssa_operands`
  and `execute_update_addresses_taken` now correctly omit address-taken properties
  for `IFN_ASSUME`. This is because `.ASSUME` is a directive that doesn't cause observable
  aliasing, simplifying subsequent analyses like VN and PTA by reducing spurious constraints
  and enabling better propagation of invariants.
primer_glossary:
- term: .ASSUME
  definition: A compiler directive that provides hints about program behavior, such
    as indicating that a certain condition is always true. It does not introduce side
    effects or affect program execution directly.
- term: address-taken
  definition: A variable or expression is considered 'address-taken' if its memory
    address is stored in a pointer. This property is important for optimization because
    it implies that the variable's value might be modified indirectly, limiting certain
    optimizations.
- term: Value Numbering (VN)
  definition: An optimization technique that identifies and merges equivalent expressions
    within a program. It uses unique 'values' or 'numbers' to represent computations,
    simplifying the program by eliminating redundant calculations.
- term: IPA analysis
  definition: Interprocedural Analysis, a type of program analysis that considers
    the entire program, including calls between functions, to understand data flow
    and identify optimization opportunities.
- term: PTA
  definition: Points-To Analysis. A static analysis technique used to determine, for
    each pointer in a program, the set of memory locations that the pointer might
    possibly refer to. This helps in understanding aliasing and enabling optimizations.
- term: SSA
  definition: Static Single Assignment form. An intermediate representation of a program
    where every variable is assigned exactly once. This simplifies many data-flow
    analyses and optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9c3dc461749a1257b9939625ef59b2b056035311
date: '2026-10-08'
is_stub: false
stub_reason: ''
---

The compiler's analysis of .ASSUME directives is improved by not considering its arguments as address-taken. This change allows Value Numbering (VN) to correctly disambiguate against calls and replicate IPA analysis predicate conditions. Point-to-analysis (PTA) also benefits by not generating unnecessary constraints for .ASSUME.
