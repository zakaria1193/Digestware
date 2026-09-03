---
project: gcc
subsystem: maintainer_utils
patch_id: null
tags:
- maintainer_utils
- data validation
commit_hash: d6bac80f3ddd4975de9bc8bf1c1e07e7a5579009
source_type: github
author: Richard Earnshaw
headline: 'maintainer_utils: Set minimum array size to 1 for user emails and aliases.'
tldr: maintainer_utils script now enforces that user data must include at least one
  email address, inactive email, or alias.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `maintainer_utils.py` script's schema validation has been tightened.
  The `email`, `inactive_emails`, and `aliases` fields, which were previously optional
  or could be empty, now require at least one entry. This change impacts how maintainer
  data is structured and validated, ensuring that essential contact information is
  always present.
primer_glossary:
- term: maintainer_utils.py
  definition: A Python script used within the GCC project to manage and validate the
    `MAINTAINERS.yml` file, which lists project maintainers and their roles.
- term: schema
  definition: In this context, a data structure that defines the expected format,
    types, and constraints for the `MAINTAINERS.yml` file.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/d6bac80f3ddd4975de9bc8bf1c1e07e7a5579009
date: '2026-08-20'
is_stub: true
stub_reason: low_score
---

The `maintainer_utils.py` script has been updated to enforce a minimum array size of 1 for the `email`, `inactive_emails`, and `aliases` fields in user data. This ensures that every user record is associated with at least one email address, improving data integrity and consistency for managing project maintainers.
