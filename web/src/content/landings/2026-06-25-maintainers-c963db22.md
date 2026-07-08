---
project: gcc
subsystem: maintainers
patch_id: null
tags:
- maintainers
- scripting
- workflow
commit_hash: c963db2262568530628f406d3776b9e4ca3831f1
source_type: github
author: Richard Earnshaw
headline: 'MAINTAINERS: Adds script to create new entries'
tldr: New Python script simplifies adding new accounts to the MAINTAINERS data with
  basic information.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: A new utility script `contrib/add-write-after.py` has been added to
  automate the creation of basic entries in `MAINTAINERS.yml`. It handles the boilerplate
  for adding a new account and defaults to the 'write-after' role, making it easier
  for maintainers to add new contributors to the system.
primer_glossary:
- term: MAINTAINERS.yml
  definition: A configuration file used by GCC's infrastructure to define who maintains
    which parts of the codebase and their roles.
- term: script
  definition: A program or sequence of instructions that is interpreted or carried
    out by another program rather than the CPU directly.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/c963db2262568530628f406d3776b9e4ca3831f1
date: '2026-06-25'
is_stub: true
stub_reason: low_score
---

A new Python script, `add-write-after.py`, has been added to the `contrib` directory to streamline the process of creating new entries in the MAINTAINERS.yml file. This script automates the creation of basic account entries in the canonical location, simplifying the common task of onboarding new contributors.
