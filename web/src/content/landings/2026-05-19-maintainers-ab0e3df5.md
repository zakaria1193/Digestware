---
project: gcc
subsystem: maintainers
patch_id: null
tags:
- maintainers
- sort
commit_hash: ab0e3df5befcd6f8b163719adb9b9c1301291370
source_type: github
author: Richard Earnshaw
headline: 'MAINTAINERS: Improve Write After Approval sort.'
tldr: Improve the MAINTAINERS sort for Write After Approval by adding a secondary
  sort by email address.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies the MAINTAINERS file, specifically the 'Write
  After Approval' section.  The change introduces a secondary sorting key using email
  addresses. This change enhances maintainability by ensuring a consistent and easily
  searchable order.
primer_general: The `MAINTAINERS` file lists who is responsible for different parts
  of the GCC project, and who should review patches. This commit sorts the list to
  make it easier to find the right person.  Specifically, it refines the sorting for
  'Write After Approval' entries by adding email address as a secondary sorting key.  This
  ensures a consistent and easily searchable order of maintainers.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ab0e3df5befcd6f8b163719adb9b9c1301291370
date: '2026-05-19'
is_stub: false
---

The MAINTAINERS file's "Write After Approval" section now sorts by email address as a secondary key. This change improves the organization and readability of the list, making it easier to locate specific maintainers.
