---
project: gcc
subsystem: gcc/git_update_version
patch_id: null
tags:
- build-system
- versioning
- maintenance
commit_hash: 9f5f4420659c54cba67e7f86f7d61cd3c2b13b54
source_type: github
author: Jakub Jelinek
headline: Add two further commits to ignored_commits, remove old ones
tldr: GCC's versioning script now ignores two new commit hashes and removes older,
  irrelevant ignored commits.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `git_update_version.py` script within GCC's `gcc-changelog` directory
  is responsible for generating the version string that identifies a specific GCC
  build. This script references a list of `ignored_commits`, which are commit hashes
  that should not influence the calculated version number. Typically, these are commits
  related to internal infrastructure, documentation, or trivial changes that don't
  warrant a version bump. This commit updates this list, adding two new hashes and
  pruning older ones, ensuring the versioning logic remains accurate and relevant
  to the project's development lifec…
primer_general: Software projects, especially large ones like GCC, use version numbers
  (e.g., 11.2.0) to indicate specific releases and track changes. When you build GCC
  from its source code, a script automatically generates a detailed version string
  that often includes information about the exact changes incorporated. Sometimes,
  certain internal or minor changes to the compiler itself shouldn't affect this official
  version string, as they don't represent new features or bug fixes for end-users.
  The `git_update_version.py` script has a list of 'ignored commits' — specific internal
  changes that it should skip when calculating the version. This update simply adds
  two new such commits to that list and removes some old ones that are no longer relevant,
  ensuring that the automatically generated version numbers accurately reflect significant
  changes for users.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9f5f4420659c54cba67e7f86f7d61cd3c2b13b54
date: '2026-06-09'
is_stub: false
---

This update to GCC's versioning script (git_update_version.py) adds two specific commit hashes to the `ignored_commits` list. These commits will now be excluded from the version string generation process, likely because they represent internal or cosmetic changes that shouldn't affect the user-visible version number. Concurrently, older, no longer relevant commit hashes have been removed from the ignored list, streamlining the script's maintenance.
