---
project: gcc
subsystem: maintainers
patch_id: null
tags:
- maintainers
- script
- organization
commit_hash: 911d91af025eae3d581ae0da59646fdba0e173b0
source_type: github
author: Richard Earnshaw
headline: 'MAINTAINERS: Improve checking in check-MAINTAINERS.py.'
tldr: Enhances the check-MAINTAINERS.py script with stricter sorting and regex-based
  field matching.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The patch reworks `check_group` to use regex matches and supports additional
  fields for secondary sorting. It also reworks the `sections` to use regexs and add
  rules for other sections in the MAINTAINERS file. The goal is to maintain the desired
  sorting order and accommodate variations in the MAINTAINERS file format.
primer_general: The MAINTAINERS file lists the developers responsible for various
  parts of the GCC project. The `check-MAINTAINERS.py` script is used to verify the
  format and consistency of this file. This commit introduces more robust checks to
  ensure the file is correctly sorted and formatted, which helps to maintain the accuracy
  and usability of the information in the MAINTAINERS file.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/911d91af025eae3d581ae0da59646fdba0e173b0
date: '2026-05-19'
is_stub: false
---

This commit enhances the `check-MAINTAINERS.py` script with additional checks to maintain the new sorting order in the MAINTAINERS file. The changes include sorting names by surname, using regular expressions for field matching to accommodate fields spilling over into the next column, and supporting sorting by multiple fields. These improvements ensure the consistency and correctness of the MAINTAINERS file.
