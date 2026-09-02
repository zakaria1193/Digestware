---
project: gcc
subsystem: gcc-changelog
patch_id: null
tags:
- changelog
- c++
- standards
commit_hash: fc54ab94ad257f9ef43a7287a60c21734a7a288f
source_type: github
author: Jason Merrill
headline: 'gcc-changelog: accept "CWG nnnn" header'
tldr: Updates the GCC changelog script to recognize C++ Core Working Group and Library
  Working Group defect report numbers.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `gcc-changelog` script automatically generates GCC's `ChangeLog`
  file from commit messages. This patch modifies the regular expression (`dr_regex`)
  used to identify defect reports. It now includes `CWG` and `LWG` prefixes, alongside
  existing `DR` and `PR` (Problem Report) tags, to categorize issues against the C++
  language and library standards. It also adds support for C++ paper numbers (e.g.,
  `P2037R7`) from the standard's evolution process.
primer_glossary:
- term: gcc-changelog
  definition: A script used within the GCC project to automatically generate or update
    the `ChangeLog` file from commit messages, providing a history of changes.
- term: CWG
  definition: C++ Core Working Group. This group is responsible for maintaining the
    C++ programming language standard.
- term: LWG
  definition: C++ Library Working Group. This group is responsible for maintaining
    the C++ Standard Library.
- term: DR
  definition: Defect Report. An official issue filed against a C++ standard draft,
    which is later resolved by the respective working group.
- term: PR
  definition: Problem Report. A general term for an issue or bug report filed against
    the GCC compiler itself.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fc54ab94ad257f9ef43a7287a60c21734a7a288f
date: '2026-08-26'
is_stub: true
stub_reason: low_score
---

The `gcc-changelog` script, used to parse commit messages, has been updated to recognize defect report tags from the C++ Core Working Group (CWG) and the C++ Library Working Group (LWG). It also now accepts C++ paper numbers like `P2037R7`, improving its ability to categorize and track issues related to C++ standards evolution within the GCC project.
