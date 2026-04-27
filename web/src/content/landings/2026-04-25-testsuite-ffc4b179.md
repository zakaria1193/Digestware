---
project: gcc
subsystem: testsuite
patch_id: null
tags:
- testsuite
- freebsd
- x86_64
- abi
commit_hash: ffc4b179a3bc254b7303d7f9ddbe3e9291851cec
source_type: github
author: Rainer Orth
headline: 'testsuite: Fix gcc.target/x86_64/abi tests on FreeBSD'
tldr: The GCC testsuite now passes the x86_64 ABI tests on FreeBSD by adding `.note.GNU-stack`
  and adjusting compiler arguments.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch modifies assembly support files in ``gcc.target/x86_64/abi/``
  to include `.note.GNU-stack` for FreeBSD, similar to other platforms. It also adjusts
  ``GEN_ARGS`` to include ``--omit-rbp-clobbers`` for the ms-sysv ABI tests. Finally,
  it adjusts tests expecting ``-fomit-frame-pointer`` to account for FreeBSD's default.
  These changes are necessary for the testsuite to pass on FreeBSD.
primer_general: A compiler's Application Binary Interface (ABI) defines how code interacts
  at the machine level, specifying things like data layout and calling conventions.  The
  GCC testsuite includes tests to verify ABI compliance on different operating systems.
  This commit fixes test failures on FreeBSD related to stack flags, register usage,
  and frame pointer defaults, ensuring that GCC correctly implements the x86_64 ABI
  on FreeBSD.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ffc4b179a3bc254b7303d7f9ddbe3e9291851cec
date: '2026-04-25'
---

The GCC testsuite's x86_64 ABI tests were failing on FreeBSD due to missing stack executable flags and ABI differences. This commit fixes this by adding `.note.GNU-stack` to assembly support files for FreeBSD. It also adds ``--omit-rbp-clobbers`` to ``GEN_ARGS`` and adapts tests to the default ``-fno-omit-frame-pointer`` setting on FreeBSD. These changes ensure the testsuite passes on FreeBSD with both GNU ld and lld.
