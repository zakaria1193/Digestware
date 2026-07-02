---
project: binutils
subsystem: haiku/testsuite
patch_id: null
tags:
- testsuite
- haiku
- elf
commit_hash: 325bb9405e69fc5a0a2e58c920667160adeeece9
source_type: public_inbox
author: Maciej W. Rozycki <macro@sourceware.org>
headline: 'Haiku/testsuite: Mark target as ELF'
tldr: The Haiku target is now explicitly marked as ELF in the testsuite, fixing regressions.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `binutils/testsuite/lib/binutils-common.exp` to
  mark Haiku targets as ELF.  This fixes testsuite regressions related to GNU attribute
  handling.  Haiku targets are defined in `bfd/config.bfd` using the `targ_defvec`
  variable, which specifies the default vector and confirms that all Haiku targets
  are ELF.
primer_general: The binutils testsuite verifies the correct behavior of binutils utilities.
  This commit ensures that the Haiku operating system target is correctly identified
  as using the ELF binary format.  This ensures that the testsuite runs the appropriate
  tests for ELF binaries, which is necessary for Haiku.  The ELF (Executable and Linkable
  Format) is a common file format for executables, object code, shared libraries,
  and core dumps.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260509144155.498A34BA2E12@sourceware.org
date: '2026-05-09'
---

The Haiku target in the binutils testsuite is now explicitly marked as ELF.  This fixes regressions in GNU attribute handling, and allows for broader test coverage. All Haiku targets are ELF.
