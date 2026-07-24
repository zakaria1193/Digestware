---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- solaris
- linker
commit_hash: e3f61fb10d7975fe91722e9afe96f8d59354c53d
source_type: github
author: Rainer Orth
headline: 'testsuite: Use solaris_ld effective target'
tldr: Introduces a solaris_ld effective target to distinguish Solaris linker tests.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The testsuite's `et-static.def` mechanism defines effective targets
  that map to specific tools or configurations. This commit adds `solaris_ld` to distinguish
  tests targeting the Solaris linker from those targeting the GNU linker (`gld`).
  This allows for more precise testing of linker-specific behaviors on Solaris systems.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e3f61fb10d7975fe91722e9afe96f8d59354c53d
date: '2026-07-23'
is_stub: true
stub_reason: low_score
---

The testsuite now uses a new 'solaris_ld' effective target to identify when the Solaris linker is in use. This mirrors an existing mechanism for the Solaris assembler. Tests that specifically check for the Solaris linker will now use this target, while tests focusing on GNU ld features remain unaffected. The change was verified through bootstrapping on Solaris and Linux systems.
