---
project: binutils
subsystem: binutils
patch_id: null
tags:
- risc-v
- assembler
- optimization
commit_hash: 21cffe7c0955c6bdb0c14ded96939d409f3c21f0
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: RISC-V assembler supports '.option [no]exact' directives
tldr: RISC-V assembler now supports '.option exact' and '.option noexact' directives
  to control linker relaxation and instruction aliasing.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit introduces support for '.option exact' and '.option noexact'
  in the RISC-V assembler, analogous to LLVM's implementation. The 'exact' mode disables
  linker relaxations (controlled by '.option relax'), prevents instruction aliases
  that alter encoding (e.g., 'addi' to 'c.addi'), and disables branch instruction
  relaxation. The interaction with existing '.option relax' directives is designed
  for LLVM compatibility, where '.option exact' implies '.option norelax' and vice-versa,
  though using both is not recommended.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer (RISC) principles. It is designed to be simple, modular,
    and extensible.
- term: assembler directives
  definition: Instructions to the assembler, not translated into machine code. They
    control aspects like symbol definition, section selection, and macro expansion.
    Examples include '.global', '.section', and in this case, '.option'.
- term: linker relaxation
  definition: A process where the linker adjusts relative addresses and branch offsets
    after the initial assembly. This is often done to optimize code size by using
    shorter instruction encodings where possible. '.option relax' enables this, while
    '.option norelax' disables it.
- term: instruction aliasing
  definition: A situation where a mnemonic can represent multiple underlying machine
    instructions, often differing in encoding or performance. For example, 'addi'
    might alias to 'c.addi' on RISC-V for compressed instruction sets.
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into machine code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261022090610.464F94BA2E3D@sourceware.org
date: '2026-10-22'
is_stub: false
stub_reason: ''
---

The RISC-V assembler in binutils now supports the '.option exact' and '.option noexact' directives, aligning with LLVM's implementation. These directives control linker relaxations, disable instruction aliases that change encoding, and prevent relaxation of branch instructions. While interactions with '.option relax/norelax' are supported to mimic LLVM, using both sets of options concurrently is discouraged.
