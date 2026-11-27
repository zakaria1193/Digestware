---
project: binutils
subsystem: dlltool
patch_id: null
tags:
- binutils
- dlltool
- bugfix
- sorting
discussion_id: ec8a70d5-419a-431e-b118-f3891a3e75a2@suse.com
source_type: public_inbox
title: 'Re: [PATCH] dlltool: Fix the comparison of explicit export names in nfunc'
headline: 'dlltool: Correct export name comparison in nfunc'
tldr: A patch for dlltool correctly addresses an issue where explicit export names
  were being compared incorrectly, leading to wrong sorting and hints.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Correctness of sorting and metadata assignment in `dlltool`.
- Ensures predictable behavior when dealing with explicitly named exports.
exchanges:
- author: Zhongteng Gui
  role: proposer
  position: Submitted a patch to fix an issue in `dlltool`'s `nfunc` where explicit
    export names were compared incorrectly.
  quote: nfunc compares the export table names of two exports, using its_name when
    an export has one. The right-hand its_name was assigned to the left-hand name,
    so exports were sorted by the wrong name and given the wrong hints when the second
    export had an explicit name.
- author: Jan Beulich <jbeulich@suse.com>
  role: maintainer
  position: Approved the patch, confirming that the fix is correct.
  quote: Okay.
primer_expert: This patch for `binutils`' `dlltool` addresses a bug in the `nfunc`
  function's sorting logic. Specifically, when comparing exports that have explicit
  names, the function was using the wrong name for comparison, leading to incorrect
  ordering and associated metadata. The fix ensures that the correct explicit name
  is used, resolving the sorting issue.
primer_glossary:
- term: dlltool
  definition: A tool in the binutils package that creates DLL import libraries for
    Windows systems.
- term: nfunc
  definition: Likely a specific function or routine within dlltool responsible for
    handling named functions or exports.
- term: its_name
  definition: A field or variable likely representing the explicit name of an export
    in the context of dlltool.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/ec8a70d5-419a-431e-b118-f3891a3e75a2@suse.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

The `nfunc` function in `dlltool` was incorrectly comparing explicit export names. The patch rectifies this by ensuring the right-hand side's explicit name (`its_name`) is used for comparison, which fixes incorrect sorting and the assignment of wrong hints when the second export had an explicit name. The change has been acknowledged and approved.
