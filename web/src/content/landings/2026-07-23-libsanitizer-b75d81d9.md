---
project: gcc
subsystem: libsanitizer
patch_id: null
tags:
- build
- libsanitizer
- performance
commit_hash: b75d81d95f49d694ed2edbd383207c00c8b1da77
source_type: github
author: Harmen Stoppels
headline: 'libsanitizer: Parallelize subdir builds'
tldr: Builds of libsanitizer subdirectories are now parallelized for faster compilation.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The automake build system's all-recursive directive by default processes
  subdirectories sequentially. For libsanitizer, this limits build parallelism. This
  change modifies the Makefiles to express the build dependencies as a directed acyclic
  graph (DAG), allowing parallel execution of independent subdirectories. This affects
  the overall build orchestration, not internal sanitizer logic.
primer_glossary:
- term: libsanitizer
  definition: A collection of runtime libraries in GCC that detect various types of
    undefined behavior, such as memory errors and race conditions.
- term: Automake
  definition: A tool that automatically generates the 'Makefile' from a more abstract
    'Makefile.am' input file. It's part of the GNU build system.
- term: DAG
  definition: Directed Acyclic Graph. A collection of nodes connected by edges, where
    the edges have a direction and there are no cycles. In build systems, it represents
    dependencies between tasks.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b75d81d95f49d694ed2edbd383207c00c8b1da77
date: '2026-07-23'
is_stub: false
stub_reason: ''
---

This commit replaces the sequential building of libsanitizer subdirectories with an explicit dependency graph. Automake typically builds subdirectories one after another, limiting parallelism. By defining dependencies (asan and hwasan depend on lsan, others on sanitizer_common), builds can now run in parallel. This change significantly reduces build times on multi-core systems, with CPU load increasing from 2.3 to 3.7, resulting in approximately a 30% faster build.
