---
project: gcc
subsystem: contrib
patch_id: null
tags:
- build
- contrib
- mirroring
commit_hash: 8cd5fa5e109aec3abc9b7ce6791ce8106e4cdb89
source_type: github
author: Даниил Гусев
headline: 'contrib: Allow overriding download_prerequisites base URL'
tldr: The download_prerequisites script now respects GCC_PREREQUISITES_BASE_URL to
  fetch packages from mirrors.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `contrib/download_prerequisites` script now checks for the `GCC_PREREQUISITES_BASE_URL`
  environment variable. If set, this variable overrides the default base URL (`https://gcc.gnu.org/pub/gcc/`)
  for downloading prerequisite source archives, allowing for local mirroring or staged
  distribution of build dependencies.
primer_glossary:
- term: prerequisites
  definition: Software components or libraries that must be installed before a particular
    program or system can be built or run. For GCC, these can include other libraries
    or tools required for specific configurations.
- term: base URL
  definition: The primary address of a web server or directory from which files can
    be downloaded. In this context, it's the starting point for locating and downloading
    required source code archives.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/8cd5fa5e109aec3abc9b7ce6791ce8106e4cdb89
date: '2026-08-01'
is_stub: true
stub_reason: low_score
---

The `download_prerequisites` script has been updated to allow users to specify a custom base URL for fetching prerequisites via the `GCC_PREREQUISITES_BASE_URL` environment variable. This enables fetching packages from local mirrors or alternative locations, reducing reliance on the default `gcc.gnu.org` server.
