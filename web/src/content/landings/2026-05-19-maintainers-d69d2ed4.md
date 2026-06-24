---
project: gcc
subsystem: maintainers
patch_id: null
tags:
- maintainers
- DCO
- organization
commit_hash: d69d2ed43fda2d882d1126d82964c1f52eb10be8
source_type: github
author: Richard Earnshaw
headline: 'MAINTAINERS: Sort DCO entries by email address.'
tldr: Sorts the DCO section of the MAINTAINERS file secondarily by email address.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit simply modifies the MAINTAINERS file to include a secondary
  sort by email address in the DCO section.
primer_general: The MAINTAINERS file lists the developers responsible for various
  parts of the GCC project. The Developer Certificate of Origin (DCO) is a lightweight
  mechanism for contributors to assert that they have the right to contribute the
  code they are submitting. This commit provides a slightly more organized maintainers
  list.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d69d2ed43fda2d882d1126d82964c1f52eb10be8
date: '2026-05-19'
is_stub: true
stub_reason: low-score
---

This commit modifies the MAINTAINERS file to sort the "Contributing under the DCO" section secondarily by email address. This change provides a more organized and easily searchable list of contributors who have signed the Developer Certificate of Origin (DCO).
