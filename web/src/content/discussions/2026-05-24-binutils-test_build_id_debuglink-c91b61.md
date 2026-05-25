---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- testsuite
- build-id
- debuglink
- cross-compilation
discussion_id: ahLeYCYkXMCS4Iqy@squeak.grove.modra.org
source_type: public_inbox
title: binutils test_build_id_debuglink
headline: Binutils test_build_id_debuglink
tldr: The patch modifies the build-id-debuglink test to avoid glibc source dependencies
  and improve test reliability.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Building with -shared -nostdlib changes the nature of the test executable.
- Removing CFLAGS_FOR_TARGET simplifies the test setup but might limit flexibility
  in some scenarios.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes changes to the build-id-debuglink test to remove glibc source
    dependencies and improve test reliability.
  quote: I saw build-id-debuglink test failures on a number of targets due to deleting
    the glibc source I'd used when building the cross toolchains. The tests failed
    with timeouts.
primer_expert: This patch modifies the ``test_build_id_debuglink`` test in ``binutils/testsuite/binutils-all/objdump.exp``.
  It addresses test failures caused by missing glibc sources during cross-compilation.
  The changes involve building the test program with ``-fPIC -shared -nostdlib``,
  and using ``additional_flags`` instead of ``CFLAGS_FOR_TARGET`` to pass options
  to the compiler.
primer_general: The binutils suite includes tools for manipulating binary files. The
  ``build-id-debuglink`` test verifies that debug information can be linked to stripped
  binaries using build IDs. This patch improves the reliability of this test by removing
  dependencies on external glibc source code during cross-compilation, ensuring that
  the test can run in environments where the glibc source is not available.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ahLeYCYkXMCS4Iqy@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-24'
is_stub: false
---

This patch modifies the ``test_build_id_debuglink`` test in binutils to avoid dependencies on glibc source code during cross-compilation. The original test setup resulted in timeouts due to the test trying to locate glibc sources. The updated test builds executables with ``-shared -nostdlib`` and uses ``additional_flags`` instead of ``CFLAGS_FOR_TARGET`` to pass extra options to the compiler. This improves test reliability by eliminating the external source dependency.
