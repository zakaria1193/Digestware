---
project: gcc
subsystem: gcc/testsuite
patch_id: null
tags:
- testsuite
- LTO
- build
commit_hash: 13ecbd80dbfce33f443950c593c9c6be0766f410
source_type: github
author: Torbjörn SVENSSON
headline: Isolate incremental LTO links from board link settings
tldr: Prevents board-specific linker flags from interfering with incremental LTO link
  tests.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `lto.exp` test suite file, specifically the `lto-link-and-maybe-run`
  procedure, now disables board-provided `ldflags` and `libs` during incremental LTO
  link operations. This is done by temporarily setting `-nostdlib` and clearing these
  environment variables, then restoring them after the link. This addresses an issue
  where board configurations could pull in non-LTO object files (e.g., semihosting
  functions from libc.a when testing Newlib without supplied syscalls), which would
  interfere with the incremental LTO build process.
primer_glossary:
- term: LTO
  definition: Link-Time Optimization. A compiler optimization technique where the
    entire program is available during the linking phase, allowing for cross-file
    optimizations.
- term: incremental LTO
  definition: A form of LTO where only changed object files are re-optimized and relinked,
    rather than the entire program, to speed up build times.
- term: linker flags
  definition: Options passed to the linker program (e.g., `ld`) to control how object
    files are combined into an executable or library. Examples include specifying
    search paths for libraries or defining symbols.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/13ecbd80dbfce33f443950c593c9c6be0766f410
date: '2026-10-06'
is_stub: false
stub_reason: ''
---

GCC's testsuite now isolates incremental Link-Time Optimization (LTO) linking steps from board-specific linker settings. This is achieved by using `-nostdlib` and temporarily clearing board-defined linker flags and libraries during these incremental links, then restoring them afterward. This isolation was necessary because certain board configurations, particularly when building Newlib without supplied syscalls, would inadvertently pull in non-LTO object files containing semihosting functions due to board linker flags.

This change ensures that LTO tests accurately reflect LTO behavior by preventing external, board-specific configurations from interfering with the linking process, leading to more reliable test results.
