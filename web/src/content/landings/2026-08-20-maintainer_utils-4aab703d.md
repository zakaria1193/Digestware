---
project: gcc
subsystem: maintainer_utils
patch_id: null
tags:
- maintainer_utils
- DCO
- data structure
commit_hash: 4aab703df1b7002f7b1d7ae9a842b2d775dfb56e
source_type: github
author: Richard Earnshaw
headline: 'maintainer_utils: Restructure DCO entries outside of roles.'
tldr: DCO entries are now stored separately from roles in maintainer data, with enhanced
  validation.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors the `MAINTAINERS.yml` schema and processing in
  `maintainer_utils.py` and `gen-MAINTAINERS.py`. DCO information, previously nested
  within user roles, is now a distinct top-level attribute. The validation logic (`_check_dco`)
  is enhanced to ensure DCO addresses are present in the user's active or inactive
  email lists. This structural change improves the clarity and integrity of maintainer
  role and DCO data.
primer_glossary:
- term: DCO
  definition: Developer Certificate of Origin, a document stating that the contributor
    has the right to submit the code and that it's their original work.
- term: MAINTAINERS.yml
  definition: A YAML file in the GCC repository that lists project maintainers, their
    contact information, and their areas of responsibility.
- term: roles
  definition: Specific responsibilities or areas of ownership assigned to a maintainer
    within the GCC project.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4aab703df1b7002f7b1d7ae9a842b2d775dfb56e
date: '2026-08-20'
is_stub: true
stub_reason: low_score
---

DCO entries have been logically separated from project roles within the `MAINTAINERS.yml` data structure. They are now stored in a top-level user list, distinct from role assignments. This change simplifies data management and introduces new validation rules: DCO email addresses must exist in either the active or inactive email lists, ensuring data consistency.
