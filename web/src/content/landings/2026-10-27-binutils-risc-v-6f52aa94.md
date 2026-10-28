---
project: binutils
subsystem: binutils/risc-v
patch_id: null
tags:
- binutils
- risc-v
- disassembler
- feature
commit_hash: 6f52aa942cb016131d6ebc1895b9d32fe395f697
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: RISC-V disassembler gains 'arch=' option for ISA specification.
tldr: Users can now specify the RISC-V architecture using an 'arch=' option with the
  disassembler.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The RISC-V disassembler in `opcodes/riscv-dis.c` now supports an `arch=`
  command-line option. This option allows overriding the ISA determined from the object
  file's architecture attribute or the default `rv64gc`. It's especially useful for
  core files or stripped objects where the ISA is not embedded. The option sets the
  default ISA for the object, taking precedence over attributes but respecting mapping
  symbols like `$xrv`.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computing principles.
- term: Disassembler
  definition: A tool that translates machine code (binary instructions) back into
    human-readable assembly language.
- term: ISA
  definition: Instruction Set Architecture. Defines the set of instructions that a
    processor can execute.
- term: Core file
  definition: A file containing the memory image of a process that terminated abnormally,
    used for debugging.
- term: Mapping symbol
  definition: In the context of RISC-V disassembly, these symbols (e.g., `$xrv`) can
    indicate specific ISA extensions or configurations that override general settings.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261027140324.808844BA2E23@sourceware.org
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

A new `arch=` option has been added to the RISC-V disassembler, allowing users to explicitly specify the Instruction Set Architecture (ISA). This is particularly useful for core files or stripped binaries where the ISA information might not be present in the object file itself. The option overrides the default ISA derived from the object's attributes, providing greater flexibility in disassembling RISC-V code.
