---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- alpha
- vms
- bugfix
commit_hash: ebe2f2b098a562b0f19ca99856df7793cd1dcc67
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: PR 34418 alpha_vms_slurp_relocs off-by-one section index check
tldr: Fixed an off-by-one error in BFD's VMS Alpha relocation handling by correcting
  section index bounds checking.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `alpha_vms_slurp_relocs` function in `bfd/vms-alpha.c` previously
  had an off-by-one error in its section index checking. By changing `cur_psect` to
  an unsigned integer (`unsigned int`) and initializing it to `-1u`, and then changing
  the bounds check from `cur_psect < 0 || cur_psect > (int)PRIV (section_count)` to
  `cur_psect >= PRIV (section_count)`, the check now correctly prevents out-of-bounds
  access to the section data, ensuring relocation processing is safe.
primer_glossary:
- term: BFd
  definition: The Binary File Descriptor library, a low-level library used by binutils
    and GDB to read and write object files in various formats.
- term: VMS
  definition: Virtual Memory System. An operating system originally developed by Digital
    Equipment Corporation (DEC) for their VAX and Alpha computer systems.
- term: Alpha
  definition: A 64-bit Reduced Instruction Set Computer (RISC) microarchitecture developed
    by Digital Equipment Corporation (DEC), later continued by Compaq and HP.
- term: relocations
  definition: Information in an object file that tells the linker how to modify certain
    parts of the code or data (e.g., addresses) when linking it with other files or
    loading it into memory.
- term: section index
  definition: An identifier for a specific section (e.g., code, data, BSS) within
    an object file.
- term: off-by-one error
  definition: A common programming error where a loop or conditional check iterates
    one time too many or too few, or accesses an array element just outside its valid
    bounds.
discussion_id_link: public_inbox:binutils#34418
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260722085246.CDC814BA2E11@sourceware.org
date: '2026-07-22'
is_stub: false
stub_reason: ''
---

Corrected an off-by-one error in the `alpha_vms_slurp_relocs` function within BFD, which handles VMS Alpha relocations. The fix involves making the `cur_psect` variable unsigned and adjusting the bounds check to prevent incorrect section indexing, resolving a potential issue where invalid section indices could be accepted.
