---
project: binutils
subsystem: i386/haiku/gas/testsuite
patch_id: null
tags:
- gas
- testsuite
- haiku
- i386
commit_hash: 555a9f3a99524e3f6d4ad18f3f355a272aa0c9ac
source_type: public_inbox
author: Maciej W. Rozycki <macro@sourceware.org>
headline: 'i386/Haiku/GAS/testsuite: Suppress SVR4 comment character test'
tldr: The SVR4 comment character test is now excluded on Haiku targets.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `gas/testsuite/gas/i386/i386.exp` to exclude the
  SVR4 comment character test for Haiku targets.  This is because '/' is not a comment
  character in Haiku assembly, as defined in `gas/config/te-haiku.h`.  The change
  prevents a regression caused by enabling ELF tests for Haiku targets.
primer_general: The GNU Assembler (GAS) translates assembly code into machine code.  GAS
  includes a testsuite to verify its functionality.  System V Release 4 (SVR4) defines
  a specific comment character.  This commit excludes a test related to the SVR4 comment
  character for the Haiku operating system, because Haiku uses a different comment
  character.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260509144150.2F91E4BA543C@sourceware.org
date: '2026-05-09'
---

The SVR4 comment character test is now excluded on Haiku targets in the i386 assembler testsuite.  This prevents a regression caused by enabling ELF tests on Haiku targets, as '/' is not a comment character in Haiku assembly.
