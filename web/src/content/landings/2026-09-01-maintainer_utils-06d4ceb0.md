---
project: gcc
subsystem: maintainer_utils
patch_id: null
tags:
- maintainer_utils
- DCO
- data management
commit_hash: 06d4ceb08efd2472dddb60678e1a5d644aac5710
source_type: github
author: Richard Earnshaw
headline: 'maintainer_utils: Add support for inactive DCO entries.'
tldr: Maintainer tools now support `inactive_DCO` entries, mirroring `inactive_email`
  for retired DCO addresses.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change extends the `maintainer_utils.py` schema and processing
  logic to accommodate `inactive_DCO` entries. Similar to `inactive_email`, this allows
  for non-current DCO addresses to be recorded. The `gen-MAINTAINERS.py` script is
  updated to consolidate `DCO` and `inactive_DCO` entries when generating the DCO
  table, while `maintainer_schema` and `_check_dco` validate these new fields.
primer_glossary:
- term: DCO
  definition: Developer Certificate of Origin, a document stating that the contributor
    has the right to submit the code and that it's their original work.
- term: MAINTAINERS.yml
  definition: A YAML file in the GCC repository that lists project maintainers, their
    contact information, and their areas of responsibility.
- term: inactive_DCO
  definition: A field in `MAINTAINERS.yml` used to record a DCO address that is no
    longer active but should be retained for historical purposes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/06d4ceb08efd2472dddb60678e1a5d644aac5710
date: '2026-09-01'
is_stub: true
stub_reason: low_score
---

The `maintainer_utils.py` script and associated tools now support an `inactive_DCO` field in `MAINTAINERS.yml`. This allows for tracking historical DCO (Developer Certificate of Origin) entries when a developer changes their primary DCO address, preventing accidental removal of important historical records and potentially aiding future checks for submissions with retired DCOs.
