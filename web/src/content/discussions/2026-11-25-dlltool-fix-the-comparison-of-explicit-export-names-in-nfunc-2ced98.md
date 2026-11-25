---
project: binutils
subsystem: dlltool
patch_id: null
tags:
- dlltool
- bug fix
- linker
- Windows
discussion_id: SL2P216MB22718DD3013BE8426506F527EF432@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
source_type: public_inbox
title: '[PATCH] dlltool: Fix the comparison of explicit export names in nfunc'
headline: 'dlltool: Fix the comparison of explicit export names in nfunc'
tldr: Corrects a bug in dlltool's export name comparison that caused incorrect sorting
  and hints.
proposer: Zhongteng Gui <dragon-archer@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Zhongteng Gui <dragon-archer@outlook.com>
  role: proposer
  position: Submits a patch to correct a bug in `dlltool`'s `nfunc` function, where
    the comparison of explicit export names was flawed, leading to incorrect sorting
    and hinting.
  quote: nfunc compares the export table names of two exports, using its_name when
    an export has one. The right-hand its_name was assigned to the left-hand name,
    so exports were sorted by the wrong name and given the wrong hints when the second
    export had an explicit name.
primer_expert: This patch corrects a bug in `binutils/dlltool.c` within the `nfunc`
  comparison function. This function is used for sorting export table entries. The
  issue was that when comparing two exports, if the second export (`b`) had an explicit
  name (`its_name`), that name was incorrectly assigned to the variable `an` (intended
  for the first export's name). This resulted in incorrect sorting and the application
  of wrong hints. The fix changes `an = bp->its_name;` to `bn = bp->its_name;` to
  ensure the correct name is used for the right-hand side comparison.
primer_glossary:
- term: dlltool
  definition: A Windows tool that creates import libraries from DLLs or creates DLLs
    from .def files.
- term: export name
  definition: The name under which a function or variable is exported from a dynamic-link
    library (DLL).
- term: nfunc
  definition: Likely refers to a comparison function (often named `nfunc` or similar
    for 'name function') used by `qsort` or similar sorting mechanisms within `dlltool`
    to order export entries.
- term: its_name
  definition: A field within the data structure used by `dlltool` to store an explicit
    export name provided for a function or symbol.
- term: hint
  definition: In this context, likely refers to information or flags associated with
    an export that guide the linker or DLL loading process, such as calling convention
    or decoration.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/SL2P216MB22718DD3013BE8426506F527EF432@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This patch fixes a bug in `dlltool`'s `nfunc` comparison function where the right-hand side's explicit export name (`its_name`) was incorrectly assigned to the left-hand side's variable (`an`). This led to exports being sorted by the wrong name and receiving incorrect hints when an explicit name was present on the right-hand side. The fix ensures the correct `its_name` is used for the right-hand side comparison (`bn`).
