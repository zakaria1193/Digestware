---
project: binutils
subsystem: binutils/risc-v
patch_id: null
tags:
- binutils
- risc-v
commit_hash: cf958e57a623111053f108e6e8fcc5cd9eb12479
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: Merge duplicate zvknhb implicit entries for RISC-V
tldr: Duplicate implicit subset entries for 'zvknhb' in binutils RISC-V ELF code have
  been merged.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `riscv_implicit_subsets` table in `bfd/elfxx-riscv.c` contained
  a redundant entry for `zvknhb`. Commit `60667464054` added a second identical entry,
  leading to the table being scanned twice for this extension. This patch removes
  the redundant entry and consolidates the definition of `zvknhb` to include its dependencies
  `+zvknha` and `+zve32x` in a single, more maintainable line.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computing principles.
- term: implicit entry (RISC-V)
  definition: In the context of RISC-V extensions, an implicit entry defines a set
    of extensions that are automatically included if a base extension is present.
    This simplifies the specification of extension dependencies.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261120141625.6FE334310613@sourceware.org
date: '2026-11-20'
is_stub: true
stub_reason: low_score
---

In the binutils RISC-V ELF backend, there were two identical implicit entries for the 'zvknhb' extension. This commit merges these duplicate entries into a single, clearer entry. While this change has no functional impact, it simplifies the definition of implicit instruction subsets for the RISC-V architecture.
