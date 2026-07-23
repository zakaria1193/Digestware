---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- binutils
- gas
- i386
- bugfix
- recursion
commit_hash: 85fb82cc8c960e97c5a51f51b87b19a3e6263c50
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: PR 30308 more unbounded recursion in i386 gas simplify
tldr: Fixed a stack overflow issue in i386 gas's expression simplification that occurred
  with specific combinations of symbol types.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The i386 gas assembler's `i386_intel_simplify` and `i386_intel_simplify_symbol`
  functions could enter unbounded recursion when simplifying expressions containing
  both `X_add_symbol` and `X_op_symbol`. This commit introduces `symbol_mark_resolving`
  and `symbol_clear_resolving` calls around the recursive invocations to break the
  cycle, similar to how nested bracket handling is managed. A specific test case for
  `intel-equ-loop` is extended to cover this scenario.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into machine code.
- term: X_add_symbol
  definition: An internal representation within the assembler's expression parser
    indicating an addition operation involving a symbol.
- term: X_op_symbol
  definition: An internal representation within the assembler's expression parser
    indicating an operation on a symbol, often used for addressing modes or relocations.
- term: Expression Simplification
  definition: The process by which the assembler analyzes and simplifies arithmetic
    expressions involving symbols and constants, often to resolve addresses or calculate
    relocation values.
- term: Recursion
  definition: A programming technique where a function calls itself to solve smaller
    instances of the same problem. Unbounded recursion can lead to stack overflow.
- term: i386
  definition: A 32-bit extension of the Intel 8086 microprocessor architecture, commonly
    used in older PCs.
discussion_id_link: public_inbox:binutils#30308
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260723005709.2BA874BA2E1B@sourceware.org
date: '2026-07-23'
is_stub: false
stub_reason: ''
---

Addressed a bug in the gas assembler for i386 where certain complex expressions could lead to unbounded recursion, causing a stack overflow. The issue occurred when an expression involved both `X_add_symbol` and `X_op_symbol`. The fix ensures that the assembler correctly handles these cases by marking symbols as resolving during the recursive calls and clearing the mark afterwards, preventing infinite loops.
