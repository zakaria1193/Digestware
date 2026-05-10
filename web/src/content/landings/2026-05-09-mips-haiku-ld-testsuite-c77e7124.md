---
project: binutils
subsystem: mips/haiku/ld/testsuite
patch_id: null
tags:
- ld
- testsuite
- mips
- haiku
- emulation
commit_hash: c77e7124c11fe97460b86442a92b9d85898b1d02
source_type: public_inbox
author: Maciej W. Rozycki <macro@sourceware.org>
headline: 'MIPS/Haiku/LD/testsuite: Set the correct emulation and flags'
tldr: The MIPS Haiku linker testsuite now uses the correct emulation and flags.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit modifies `ld/testsuite/ld-mips-elf/comm-data.exp` and `ld/testsuite/ld-mips-elf/mips-elf.exp`
  to set the correct emulation and flags for MIPS Haiku targets.  Specifically, it
  sets `abi_ldemul(o32)` to `elf_mipsel_haiku` and enables the `irixemul` flag. The
  Haiku target uses its own LD emulation and the IRIX ELF variant.
primer_general: The GNU linker (ld) combines object files into an executable.  Linker
  testsuites verify correct linker behavior for specific architectures and operating
  systems.  Emulation refers to the specific linker behavior that mimics a particular
  system or file format. This commit configures the MIPS linker testsuite for the
  Haiku operating system to use the correct emulation settings, ensuring accurate
  testing.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260509144139.F13364BA543C@sourceware.org
date: '2026-05-09'
---

The MIPS Haiku linker testsuite is updated to use the correct emulation (`elf_mipsel_haiku`) and flags, which aligns it with the IRIX ELF variant. This ensures the testsuite accurately reflects the Haiku target's configuration.
