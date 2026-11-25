---
project: binutils
subsystem: binutils/risc-v
patch_id: null
tags:
- risc-v
- binutils
- deprecation
commit_hash: 9e9d08ed5bc2237478299335351954dc50be5ffa
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: Deprecate RISC-V ISA spec classes and -misa-spec option
tldr: Binutils deprecates the -misa-spec option and removes related ISA spec classes
  for RISC-V.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This change in binutils/gdb modifies the RISC-V backend, specifically
  targeting the handling of ISA specifications. The commit deprecates the `-misa-spec`
  command-line option and removes the internal ISA spec classes in `bfd/cpu-riscv.c`
  and `gas/config/tc-riscv.c`. The rationale is that the older spec class mechanism,
  exemplified by `20191213`, is becoming obsolete as newer RISC-V specifications define
  extensions individually rather than relying on monolithic spec versions. The commit
  maintains backward compatibility by keeping `-misa-spec` but makes it a no-op, issuing
  warnings for values o…
primer_glossary:
- term: ISA
  definition: Instruction Set Architecture. Defines the set of instructions that a
    processor can execute.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles. It is designed to be simple, modular, and
    extensible, making it popular for embedded systems and custom hardware.
- term: spec class
  definition: In the context of RISC-V specifications, a 'spec class' historically
    referred to a defined set of extensions and their versions, often associated with
    a particular year or release, like '20191213'.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261125100046.EC49F4588366@sourceware.org
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This commit deprecates the `-misa-spec` option and removes associated ISA specification classes from Binutils' RISC-V support. The `-misa-spec` option, which previously allowed specifying ISA versions like `20191213`, is being phased out as the RISC-V ecosystem evolves towards per-extension versioning. The change simplifies the handling of ISA specifications by treating base extensions as having a single default version (20191213) and removes outdated entries. The option itself is kept for backward compatibility but will have no effect, with warnings issued for non-default values.
