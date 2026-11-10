---
project: gcc
subsystem: configury
patch_id: null
tags:
- build
- autoconf
commit_hash: a44acda568b6740ca2396205ec1db3514bc0325c
source_type: github
author: Pietro Monteiro
headline: Configuration scripts update to use AC_CANONICAL_TARGET
tldr: GCC's configuration scripts are updated to use AC_CANONICAL_TARGET, resolving
  an automake bug and simplifying target alias handling.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change addresses inconsistencies in how various GCC libraries
  handle target aliases by migrating from `AC_CANONICAL_SYSTEM` to `AC_CANONICAL_TARGET`
  in their `configure.ac` files. This is safe due to an automake bug fix in the version
  of automake used by GCC. The commit also removes redundant `AC_CANONICAL_HOST` (which
  was pulled in by `AC_CANONICAL_TARGET` via `AC_REQUIRE`) and `AC_SUBST(target_alias)`
  calls, simplifying the configuration logic. The primary motivation was to resolve
  PR103459, which highlighted these inconsistencies.
primer_glossary:
- term: AC_CANONICAL_TARGET
  definition: An Autoconf macro that determines the canonical triplet for the target
    system (e.g., `x86_64-linux-gnu`). It helps ensure consistency in how the target
    is identified across different build configurations.
- term: AC_CANONICAL_SYSTEM
  definition: An Autoconf macro similar to `AC_CANONICAL_TARGET`, but it determines
    the canonical triplet for the system the configure script is running on (the build
    system). It was previously used in some GCC libraries but is now being replaced.
- term: target alias
  definition: A shorthand or alternative name for a target system's triplet. Consistent
    handling of target aliases is important for cross-compilation and build system
    correctness.
- term: AC_SUBST
  definition: An Autoconf macro used to substitute variables in generated Makefiles
    and other configuration files. `AC_SUBST(target_alias)` would make the `target_alias`
    variable available to the build system.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a44acda568b6740ca2396205ec1db3514bc0325c
date: '2026-11-10'
is_stub: true
stub_reason: low_score
---

This commit updates various GCC libraries' configuration scripts to replace `AC_CANONICAL_SYSTEM` with `AC_CANONICAL_TARGET`. This change is possible because a relevant automake bug has been fixed in newer versions. The update also removes redundant `AC_CANONICAL_HOST` and `AC_SUBST(target_alias)` calls, which are now handled by `AC_CANONICAL_TARGET`. These changes clean up the configuration process and ensure consistent target alias management across libraries.
