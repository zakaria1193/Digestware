---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- sframe
- bug fix
- pointer
discussion_id: 20261125001820.1115341-2-pietro@sociotechnical.xyz
source_type: public_inbox
title: '[PATCH] gas: sframe: Clear caller''s warning flag, not the pointer'
headline: 'gas: sframe: Clear caller''s warning flag, not the pointer'
tldr: Fixes a bug in sframe where a caller's warning flag was not being cleared due
  to incorrect pointer handling.
proposer: Pietro Monteiro <pietro@sociotechnical.xyz>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Pietro Monteiro <pietro@sociotechnical.xyz>
  role: proposer
  position: Submits a patch to fix a bug in `gas`'s sframe handling where a caller's
    warning flag was not being cleared due to incorrect pointer manipulation.
  quote: sframe_xlate_do_escape_cfa_expr set its caller_warn_p parameter to false
    instead of storing false through it, so the local pointer was nulled and the caller's
    flag left untouched. This was harmless only because the caller initializes the
    flag to false.
primer_expert: This patch addresses an issue in `gas/gen-sframe.c` related to the
  `sframe_xlate_do_escape_cfa_expr` function. The function receives `caller_warn_p`
  as a pointer to a boolean flag. The bug was that instead of writing `false` to the
  location pointed to by `caller_warn_p` (i.e., `*caller_warn_p = false;`), it assigned
  `false` to the pointer variable itself (`caller_warn_p = false;`). This nullified
  the pointer, leaving the original flag untouched. The fix involves changing the
  assignment to the correct dereferenced form. This was discovered during an autoconf
  2.73 upgrade and GCC 14.2 build, po…
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Compiler Collection (GCC).
- term: sframe
  definition: A library for handling stack frame records, often used in debugging
    and profiling tools. In this context, it's used by the assembler.
- term: CFA
  definition: Canonical Frame Address. A value that represents the base of the current
    stack frame.
- term: pointer
  definition: A variable that stores the memory address of another variable.
- term: dereference
  definition: Accessing the value stored at the memory address pointed to by a pointer.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261125001820.1115341-2-pietro@sociotechnical.xyz
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This patch corrects a bug in the sframe functionality within `gas` where the `sframe_xlate_do_escape_cfa_expr` function incorrectly handled its `caller_warn_p` parameter. Instead of dereferencing the pointer to set the caller's warning flag to false, it assigned false to the local pointer variable itself. This meant the caller's flag remained unchanged (and effectively true, due to initialization), potentially leading to incorrect behavior. The fix ensures the flag is correctly cleared.
