---
project: gcc
subsystem: gcc/maintainers
patch_id: null
tags:
- maintainers
- automation
- yaml
- gcc
commit_hash: 89d27e500e151cacd94dc6231ad8bc91adff0f5e
source_type: github
author: Richard Earnshaw
headline: Automate MAINTAINERS file generation from YAML
tldr: GCC MAINTAINERS file now auto-generated from YAML, with updated tests and scripts.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Introduces `MAINTAINERS.yml` and accompanying scripts (`gen-MAINTAINERS.py`,
  `maintainer_utils.py`) to automate the generation of the `MAINTAINERS` file. This
  refactors the maintainer information management, moving away from manual upkeep
  of the `MAINTAINERS` file itself towards a data-driven approach. The `gcc.src/maintainers.exp`
  test now validates the generated output, replacing `contrib/check-MAINTAINERS.py`.
primer_glossary:
- term: MAINTAINERS file
  definition: A file in a software project that lists individuals or teams responsible
    for different parts of the codebase. It's used to direct bug reports and patch
    submissions to the appropriate maintainers.
- term: YAML
  definition: YAML Ain't Markup Language, a human-readable data serialization standard
    often used for configuration files and data exchange. It's known for its readability
    compared to formats like JSON or XML.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of the compiler.
    It includes various test cases, configurations, and expected outcomes.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/89d27e500e151cacd94dc6231ad8bc91adff0f5e
date: '2026-05-29'
is_stub: true
stub_reason: low_score
---

This commit converts the GCC `MAINTAINERS` data into a YAML format and introduces scripts to automatically regenerate the `MAINTAINERS` file from this YAML source. The test suite has been updated to verify the correctness of the generated file. The old Python script `contrib/check-MAINTAINERS.py` is removed as it is no longer necessary.
