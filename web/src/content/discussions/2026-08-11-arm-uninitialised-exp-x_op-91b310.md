---
project: binutils
subsystem: arm
patch_id: null
tags:
- binutils
- arm
- gas
- assembler
- initialization
discussion_id: anpmjFuksL3g7r8d@squeak.grove.modra.org
source_type: public_inbox
title: 'arm: uninitialised exp.X_op'
headline: 'arm: uninitialised exp.X_op'
tldr: Alan Modra fixes an uninitialized variable issue in binutils' ARM gas assembler.
proposer: Alan Modra
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Addresses an immediate correctness issue with minimal code change.
- Defers a potentially larger refactoring of error handling to maintainers.
exchanges:
- author: Alan Modra
  role: proposer
  position: Submits a fix for an uninitialized variable in the ARM gas assembler,
    suggesting that the function's error handling could be more robustly tested.
  quote: 'Really, I think my_get_expression return status ought to be tested

    everywhere the function is called, to trim multiple error messages if

    for no other reason.  I''m going to leave that change to one of the ARM

    maintainers if they feel so inclined.  Meanwhile make this obvious fix.'
primer_expert: This patch addresses an uninitialized `expressionS::X_op` field in
  binutils' ARM gas assembler. The `my_get_expression` function in `tc-arm.c` initializes
  the `expressionS` struct after some processing, potentially leading to uninitialized
  reads if the struct's members are accessed before the `memset`. The fix moves the
  `memset` call to the beginning of the function, ensuring `expressionS` is zero-initialized
  before use. The author notes that more comprehensive error handling for the function's
  return value might be beneficial.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project. It translates assembly
    language code into machine code.
- term: expressionS
  definition: A structure likely holding parsed expression data within the assembler,
    containing fields such as `X_op` which represents an operation code or type.
- term: uninitialized variable
  definition: A variable that has been declared but not assigned a value before its
    first use. This can lead to unpredictable program behavior or crashes.
- term: ARM
  definition: A family of reduced instruction set computing (RISC) architectures for
    computer processors. Binutils includes support for assembling code for various
    ARM processor versions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/anpmjFuksL3g7r8d@squeak.grove.modra.org
bugzilla_url: null
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

Alan Modra proposes a fix for an uninitialized `exp.X_op` variable within the `my_get_expression` function in binutils' ARM gas assembler configuration. While the immediate fix is applied, Modra suggests that a more thorough review of `my_get_expression`'s return status testing is warranted but defers that larger task to ARM maintainers.
