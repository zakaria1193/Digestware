---
project: gcc
subsystem: diagnostics
patch_id: null
tags:
- diagnostics
- sarif
- standardization
commit_hash: 277bce3287c5dc5b1a695395120c20735b706032
source_type: github
author: David Malcolm
headline: Update SARIF 2.2 prerelease version and schema.
tldr: GCC diagnostics now use the updated SARIF 2.2 Committee Specification Draft
  01, improving compatibility with the latest SARIF standard.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The GCC diagnostics module is updated to reflect the release of SARIF
  2.2 Committee Specification Draft 01 (CSD01). This involves updating the `sarif_version`
  enum in `diagnostics/sarif-sink.h` and modifying functions in `diagnostics/sarif-sink.cc`
  and `diagnostics/output-spec.cc` to use the new `v2_2_prerelease_csd01` identifier.
  Consequently, the SARIF schema URL and associated properties are updated to point
  to the CSD01 version. Test cases in `gcc.dg/plugin/crash-test-ice-in-header-sarif-2_2.py`
  and related schema files are also updated to match the new specification.
primer_glossary:
- term: SARIF
  definition: Static Analysis Results Interchange Format. A standard JSON-based format
    for the output of static analysis tools, designed for interoperability.
- term: Committee Specification Draft (CSD)
  definition: A stage in the OASIS standardization process where a specification is
    formally drafted and reviewed by committee members.
- term: diagnostics
  definition: The GCC subsystem responsible for generating and reporting errors, warnings,
    and other messages during compilation.
- term: diagnostic sink
  definition: An output destination or handler for diagnostic messages produced by
    the compiler, such as console output, files, or structured formats like SARIF.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/277bce3287c5dc5b1a695395120c20735b706032
date: '2026-10-23'
is_stub: true
stub_reason: low_score
---

This commit updates the GCC diagnostics system to use the latest SARIF 2.2 Committee Specification Draft 01 (CSD01), replacing an older prerelease snapshot. The update involves changing version identifiers, schema URLs, and related properties within the SARIF output generation code. This ensures that GCC's SARIF output adheres to the most current version of the SARIF standard, enhancing interoperability with tools that consume SARIF reports.
