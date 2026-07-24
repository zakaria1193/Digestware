---
project: binutils
subsystem: binutils/ld/testsuite
patch_id: null
tags: []
commit_hash: 90c0cb3e4f346c293a73eb0917f1b4683239fee7
source_type: public_inbox
author: '"Maciej W. Rozycki" <macro@sourceware.org>'
headline: Remove $LDFLAGS from ld link tests
tldr: Avoids duplicating LDFLAGS when invoking linker tests.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Removes the global `$LDFLAGS` variable from being used in `run_ld_link_tests`
  within `ld/testsuite/lib/ld-lib.exp`. This reverts part of commit `24602a75d128`
  and avoids double-inclusion of linker flags, addressing issues for specific targets
  like alpha-vms.
primer_glossary:
- term: LDFLAGS
  definition: An environment variable that holds flags passed to the linker during
    the build process.
- term: linker test suite
  definition: A collection of tests designed to verify the correct functionality of
    the GNU linker (ld).
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260723185839.28D014BA23CF@sourceware.org
date: '2026-07-23'
is_stub: false
stub_reason: ''
---

The `run_ld_link_tests` script in the linker test suite no longer references the global `$LDFLAGS` variable. This corrects an issue where LDFLAGS could be incorrectly included twice, fixing regressions in linker invocations.
