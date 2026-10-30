---
project: binutils
subsystem: ld/emulation
patch_id: null
tags:
- ld
- linker
- PE
- Windows
- emulation
commit_hash: ed4bbf96832daa18d88e5398daee1e79818e5f64
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: Refine PE linker script target definitions
tldr: Correctly assigns PE linker scripts to 32-bit or 64-bit targets, preventing
  misconfiguration.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The linker emulation scripts `pe.em` and `pep.em` define target-specific
  configurations for PE object files. This change refines the `case ${target}` statements
  within these scripts. It removes `x86_64` from `pe.em`'s target list, as `pe.em`
  is intended for 32-bit PE targets, and removes `i[3-7]86` from `pep.em`'s target
  list, as `pep.em` is for 64-bit PE targets. This corrects the association between
  linker scripts and the architectures they are meant to support.
primer_glossary:
- term: PE
  definition: Portable Executable format, the file format used for executables, object
    code, DLLs, and other files on 32-bit and 64-bit versions of Windows.
- term: linker script
  definition: A file that provides directives to the linker, controlling how input
    sections from object files are mapped into the output sections of an executable
    or library.
- term: emulation
  definition: In this context, refers to linker configurations that support specific
    target executable formats, like PE for Windows.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261030072534.D31CC4BA900D@sourceware.org
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

The linker scripts for PE (Portable Executable) object files were not accurately distinguishing between 32-bit and 64-bit targets. This commit adjusts the target definitions in `pe.em` (for 32-bit) and `pep.em` (for 64-bit) to correctly exclude irrelevant architectures. This ensures that the appropriate linker script is used based on the target architecture, preventing potential configuration issues when building PE executables.
