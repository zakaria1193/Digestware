---
project: gcc
subsystem: gcc/modula2
patch_id: null
tags:
- build
- modula2
- python
commit_hash: dc80afc49b7a0eddaf2152379971e36d4d2bf953
source_type: github
author: Gaius Mulley
headline: Fix mktargetsrc.py to prevent Python hanging on modula2 build failures
tldr: mktargetsrc.py now cleans up temporary files on failure, preventing Python processes
  from hanging.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The mktargetsrc.py script, used in the Modula2 front-end, previously
  did not clean up temporary files when the gm2 compiler failed. This commit modifies
  the quietSystem function to accept and remove a temporary file argument if the invoked
  command returns a non-zero status. This is a build-time fix to prevent hangs in
  downstream Python scripts that process mktargetsrc.py's output, specifically def2doc.py,
  which would spin on zero-byte output files.
primer_glossary:
- term: mktargetsrc.py
  definition: A Python script used within GCC to generate target-specific source files,
    often related to the Modula2 front-end.
- term: gm2
  definition: The GNU Modula-2 compiler, part of the GCC toolchain.
- term: def2doc.py
  definition: A Python script used in GCC to generate documentation from compiler
    internal data structures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dc80afc49b7a0eddaf2152379971e36d4d2bf953
date: '2026-08-19'
is_stub: true
stub_reason: low_score
---

This patch addresses a build issue where Python scripts could hang if the Modula2 compiler (gm2) failed. The mktargetsrc.py script is updated to remove any output or temporary files before exiting with an error. This prevents subsequent scripts, like def2doc.py, from attempting to read empty files, which caused them to spin indefinitely. Additionally, gm2 is now invoked with '-S' to avoid potential issues with missing assemblers.
