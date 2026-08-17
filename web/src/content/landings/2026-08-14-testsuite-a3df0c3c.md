---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- pytest
- reliability
commit_hash: a3df0c3c54c61cc0fc4b1e5f7bbb29050f1ea7e2
source_type: github
author: Lewis Hyatt
headline: Testsuite pytest stability improvements
tldr: Increases pytest timeouts and improves cache handling for more reliable test
  execution.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Testsuite invocation of pytest via `lib/gcov.exp` and `lib/scanhtml.exp`
  (among others) used a default `expect` timeout that was insufficient for module
  import and filesystem scanning on slower I/O. This commit introduces `pytest_invoke`
  in `lib/target-supports.exp` to manage pytest invocations, increasing the default
  timeout to 300 seconds and enabling explicit failure reporting on timeout. It also
  addresses an issue where pytest would incorrectly set its root directory to a common
  parent of the build and source directories, potentially causing parallel test issues
  due to cache collisions; t…
primer_glossary:
- term: pytest
  definition: A popular Python testing framework that provides a rich set of features
    for writing and running tests, including fixtures, parametrization, and test discovery.
- term: expect
  definition: A tool and scripting language used for automating interactions with
    programs that expose a text-based interface, often used in test harnesses.
- term: NFS mount
  definition: Network File System mount. A way to access files stored on a remote
    server as if they were on a local disk, which can sometimes have higher latency
    than local storage.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a3df0c3c54c61cc0fc4b1e5f7bbb29050f1ea7e2
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

The testsuite's Python-based tests using pytest were prone to instability due to default timeouts that were too short for imports and file system scanning, especially on slower network mounts. This change increases the timeout and ensures failures are reported on timeout. Additionally, it prevents pytest from using a shared cache directory outside the build directory when source and build trees share a common parent, improving parallel test run reliability.
