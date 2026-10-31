---
project: binutils
subsystem: binutils/srconv
patch_id: null
tags:
- srconv
- obsolete
- cleanup
commit_hash: 4c1ed0b08b1a3347ce6cbd227ec7956da6397ad4
source_type: public_inbox
author: Simon Marchi <simark@sourceware.org>
headline: 'Binutils srconv: Remove unused ''quick'' variable'
tldr: The srconv utility removes an unused variable for an obsolete option.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit removes the unused static variable `quick` from `binutils/srconv.c`.
  The variable was set by the `-q` or `--quick` command-line option. This option is
  documented as obsolete and ignored by the utility. The variable `quick` has not
  been used in the code since at least the earliest `sourceware.org` import. The commit
  removes the variable declaration while keeping the option processing logic that
  accepts and ignores the option.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261030140314.536F44BA2E1C@sourceware.org
date: '2026-10-30'
is_stub: true
stub_reason: low_score
---

The `quick` variable in `binutils/srconv.c` has been removed. This variable was set by the `-q`/`--quick` option, which is documented as obsolete and ignored. The variable itself has been unused since at least the initial import of the sourceware repository. Removing it cleans up the code and resolves compiler warnings without changing the behavior of the `srconv` utility.
