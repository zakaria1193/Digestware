---
project: gcc
subsystem: docs
patch_id: null
tags:
- documentation
- GIMPLE
- compiler internals
discussion_id: 2b560ae9-c894-44c2-8d79-e1df8f811384@gjlay.de
source_type: public_inbox
title: 'docs: confusing gimple "Statement and operand traversals"'
headline: Confusing GIMPLE statement and operand traversal documentation
tldr: Documentation for GIMPLE statement and operand traversals contains type mismatches
  and unclear return value mappings.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 8
technical_tradeoffs: []
exchanges:
- author: Georg-Johann Lay <avr@gjlay.de>
  role: proposer
  position: Identifies several inconsistencies between the GCC online documentation
    and the `gimple-walk.h` header file regarding GIMPLE traversal function signatures
    and return types.
  quote: 'has: tree walk_gimple_op (gimple stmt, walk_tree_fn callback_op, struct
    walk_stmt_info *wi) but according to gimple-walk.h, the 1st arg is of type gimple*.'
- author: Andrea Pinski <andrew.pinski@oss.qualcomm.com>
  role: other
  position: Suggests that the documentation may be outdated due to a specific commit
    that renamed structures and removed types.
  quote: Looks like the documentation was not updated after r6-3402-g355fe0884b8097
    which changed the name of the struct from gimple_statement_base to gimple and
    then removed t
primer_expert: This discussion concerns the documentation for GIMPLE's traversal functions,
  specifically `walk_gimple_op` and `walk_gimple_seq`. The issue lies in discrepancies
  between the documented function signatures (types of arguments and return values)
  and the actual definitions in `gimple-walk.h`, potentially due to recent code changes
  affecting GIMPLE data structures.
primer_glossary:
- term: GIMPLE
  definition: An intermediate representation used by GCC. It is a three-address code
    form designed to be easier to optimize than the earlier GENERIC representation.
- term: Statement and operand traversals
  definition: Refers to functions within GCC that systematically visit and process
    GIMPLE statements and their constituent operands, typically for optimization or
    analysis passes.
- term: tree
  definition: In GCC, 'tree' is a generic term for the internal data structure used
    to represent code during compilation, encompassing both GENERIC and GIMPLE forms.
- term: gimple*
  definition: A pointer to a GIMPLE structure, representing a GIMPLE statement or
    related data.
- term: walk_tree_fn
  definition: A callback function type used in GCC's tree traversal utilities. It
    is invoked for each node visited during a traversal.
- term: gimple-walk.h
  definition: A header file within the GCC source code that defines functions and
    data structures for traversing GIMPLE code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/2b560ae9-c894-44c2-8d79-e1df8f811384@gjlay.de
bugzilla_url: null
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

Johann Lay points out discrepancies in the GCC documentation for GIMPLE statement and operand traversals. Specifically, the function signatures in the online documentation do not match those defined in `gimple-walk.h`, and the return types and their mappings between different traversal functions are unclear, causing confusion for developers.
