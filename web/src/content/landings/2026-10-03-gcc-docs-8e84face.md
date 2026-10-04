---
project: gcc
subsystem: gcc/docs
patch_id: null
tags:
- documentation
- texinfo
- build warnings
commit_hash: 8e84facee1236564d6db77234c656db0f9b79e91
source_type: github
author: Georg-Johann Lay
headline: Clarify Texinfo version for build warning note
tldr: GCC documentation updated to reflect that Texinfo versions older than 7.1.1
  may produce incorrect build warnings.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `doc/install.texi` file is updated to precisely state the Texinfo
  version requirement. The change clarifies that warnings related to `@anchor` within
  table items are only corrected starting with Texinfo 7.1.1, not 7.1 as was previously
  implied.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8e84facee1236564d6db77234c656db0f9b79e91
date: '2026-10-03'
is_stub: true
stub_reason: low_score
---

The GCC installation documentation has been updated to accurately reflect the version of Texinfo that may issue incorrect build warnings. Previously, it noted Texinfo older than 7.1, but the fix for the warning about `@anchor` inside `@item` was only present in Texinfo 7.1.1. This change clarifies that versions older than 7.1.1 are the ones susceptible to this issue.
