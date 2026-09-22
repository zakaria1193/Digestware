---
project: gcc
subsystem: genextract
patch_id: null
tags:
- code generation
- internal
commit_hash: 3d735adfba3217ee7e968f250eadf5f3f0a34ecd
source_type: github
author: Kyrylo Tkachov
headline: Use numbers instead of characters for genextract path steps
tldr: Replaces character-based path encoding in genextract with numbers, improving
  clarity and removing limitations.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `genextract` pass uses a string literal to encode traversal steps
  into a pattern's structure (XEXP, XVECEXP). This commit refactors this encoding
  from character-based (e.g., '0'-'9', 'a'-'z') to a byte-based numerical representation
  (2*index+1 for XEXP, 2*index+2 for XVECEXP). This resolves implicit limits on indices
  and makes the encoding more robust, albeit at the cost of slightly larger generated
  tables in files like `insn-extract.cc`.
primer_glossary:
- term: genextract
  definition: A GCC internal tool or pass responsible for extracting information from
    instruction patterns, often used in backend code generation.
- term: XEXP
  definition: Represents an expression operand in GCC's internal representation, typically
    a simple value.
- term: XVECEXP
  definition: Represents an element within a vector (or 'vec') expression in GCC's
    internal representation. It includes a vector index.
- term: insn-extract.cc
  definition: A GCC source file that likely contains code related to the genextract
    pass and the definitions of instruction patterns.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3d735adfba3217ee7e968f250eadf5f3f0a34ecd
date: '2026-09-21'
is_stub: false
stub_reason: ''
---

The `genextract` tool previously used characters to encode path steps for locating operands within patterns. This commit replaces the character encoding (digits for XEXP, lowercase letters for XVECEXP, uppercase for out-of-range indices) with a numerical encoding. This change makes the path representation more explicit, removes limitations on index values, and leads to a moderate increase in the size of the generated code.
