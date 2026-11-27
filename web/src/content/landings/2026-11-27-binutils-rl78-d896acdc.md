---
project: binutils
subsystem: binutils/rl78
patch_id: null
tags:
- binutils
- linker
- rl78
- relaxation
- testing
commit_hash: d896acdc5edb8b51fb923952ccd52891055599eb
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: RL78 linker improves relaxation range checks and error propagation
tldr: RL78 linker relaxation is more robust with better range checks and failure propagation.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit enhances the RL78 linker's relaxation mechanism by incorporating
  `_bfd_elf_relax_delete_range_ok` into `elf32_rl78_relax_delete_bytes` for range
  validation. Additionally, `SNIPNR` and `SNIP` macros are wrapped in `do-while(0)`
  for safety. The return status of byte deletion is now propagated correctly in `rl78_elf_relax_section`,
  branching to `error_return` on failure. A DejaGnu test (`rl78-relax-underflow.exp`)
  is added to specifically target relaxation underflow issues.
primer_glossary:
- term: linker
  definition: A program that combines one or more object files and libraries into
    a single executable or library.
- term: relaxation
  definition: A linker optimization that adjusts code or data layout at link time
    to use more efficient, shorter-range instructions or address formats that were
    not initially known at compile time.
- term: RL78
  definition: A microcontroller architecture developed by Renesas.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and shared libraries on many Unix-like systems.
- term: DejaGnu
  definition: A testing framework used for developing and testing software, particularly
    for GNU tools. It provides a way to write portable test suites.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261127094636.C916E43B6F60@sourceware.org
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

The RL78 linker's relaxation process has been made more robust by introducing stricter checks for deletion ranges and improving error propagation. The `elf32_rl78_relax_delete_bytes` function now uses `_bfd_elf_relax_delete_range_ok` to validate deletion ranges, and failures are properly propagated up through `rl78_elf_relax_section`. This change, along with wrapping macros in `do-while(0)` blocks, enhances the reliability of the relaxation process and includes a new DejaGnu regression test to cover underflow scenarios.
