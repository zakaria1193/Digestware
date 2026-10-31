---
project: binutils
subsystem: binutils/windmc
patch_id: null
tags:
- windmc
- cleanup
- unimplemented option
commit_hash: 2ef801db63c5989fccad14230179cc41c94ef049
source_type: public_inbox
author: Simon Marchi <simark@sourceware.org>
headline: 'Binutils windmc: Remove unused mcset_use_hresult variable'
tldr: The windmc utility removes an unimplemented and unused option variable.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `mcset_use_hresult` static variable in `binutils/windmc.c` is removed.
  This variable was conditionally set by the `-o` command-line option. However, the
  code within the `-o` case immediately calls `fatal()` indicating the option is unimplemented.
  Consequently, `mcset_use_hresult` is set but never read, leading to a `-Wunused-but-set-global`
  warning with strict compiler settings. The commit removes the variable and the related
  code path for the unimplemented option.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261030140319.6DAF24BA2E23@sourceware.org
date: '2026-10-30'
is_stub: true
stub_reason: low_score
---

The `mcset_use_hresult` variable in `binutils/windmc.c` has been removed. This variable was intended to be set by an unimplemented `-o` option, which would have generated an OLE2 header file using HRESULT definitions. Since the option was never implemented and the variable was never used, its removal resolves a compiler warning and cleans up dead code.
