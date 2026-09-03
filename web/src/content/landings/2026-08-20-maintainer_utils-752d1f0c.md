---
project: gcc
subsystem: maintainer_utils
patch_id: null
tags:
- maintainer_utils
- schema validation
- bugfix
commit_hash: 752d1f0cd94d276b3399f634a47b602343583c96
source_type: github
author: Richard Earnshaw
headline: 'maintainer_utils: Correct schema keywords for size and length validation.'
tldr: Fixes schema validation in maintainer_utils by using correct keywords `minItems`
  and `minLength`.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The YAML schema used by `maintainer_utils.py` for validating `MAINTAINERS.yml`
  contained errors in its size and length constraints. The keywords `minItems` and
  `minLength` were previously misspelled or misused (e.g., using `minlength` for arrays).
  This commit corrects these keywords to ensure that validation rules for minimum
  array sizes and minimum string lengths are correctly interpreted and enforced by
  the underlying YAML validation library.
primer_glossary:
- term: schema
  definition: In this context, a data structure that defines the expected format,
    types, and constraints for the `MAINTAINERS.yml` file.
- term: minItems
  definition: A keyword in JSON Schema (used here for YAML validation) that specifies
    the minimum number of items an array must contain.
- term: minLength
  definition: A keyword in JSON Schema (used here for YAML validation) that specifies
    the minimum number of characters a string must contain.
- term: MAINTAINERS.yml
  definition: A YAML file in the GCC repository that lists project maintainers, their
    contact information, and their areas of responsibility.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/752d1f0cd94d276b3399f634a47b602343583c96
date: '2026-08-20'
is_stub: true
stub_reason: low_score
---

The `maintainer_utils.py` script's schema validation has been corrected to properly enforce minimum item counts for arrays and minimum lengths for strings. Previously, incorrect keywords (`minItems` instead of `minItems` and `minlength` for both) were used, causing these validation checks to be ignored. The fix ensures that array and string size constraints are correctly applied.
