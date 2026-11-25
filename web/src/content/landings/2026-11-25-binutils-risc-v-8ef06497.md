---
project: binutils
subsystem: binutils/risc-v
patch_id: null
tags:
- risc-v
- binutils
- debugging
- assembler
commit_hash: 8ef06497f39c013d98cf3cb08965a589189b240e
source_type: public_inbox
author: Kito Cheng <kito@sourceware.org>
headline: Recognize RISC-V $x.<any> and $d.<any> mapping symbols
tldr: Binutils now correctly interprets RISC-V mapping symbols with suffixes for better
  debugging information.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This patch enhances the RISC-V support in Binutils, specifically in
  `bfd/cpu-riscv.c` and `opcodes/riscv-dis.c`, to correctly handle RISC-V psABI mapping
  symbols that include suffixes. The `riscv_elf_is_mapping_symbols` function is updated
  to use `startswith()` to match symbols like `$d.<any>` and `$x.<any>`, in addition
  to the existing `$xrv` prefix check. This is necessary because Clang can emit symbols
  such as `$x. <n>`, and older matching logic was too strict. This change ensures
  that objdump and other tools can correctly identify these symbols, which are crucial
  for accurate debugging an…
primer_glossary:
- term: psABI
  definition: The Application Binary Interface (ABI) for the process- and thread-local
    storage mechanisms in POSIX-compliant systems. For RISC-V, it defines conventions
    for function calls, register usage, and symbol naming.
- term: mapping symbols
  definition: Special symbols used in debugging information that map specific register
    or state values to meaningful names. In RISC-V, `$x` and `$d` are examples related
    to register file access.
- term: objdump
  definition: A standard Unix utility that displays information from object files.
    It can show disassembly, symbol tables, and other details.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261125100036.B437045D2C69@sourceware.org
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This commit improves Binutils' handling of RISC-V mapping symbols used for debugging. The psABI specification allows for suffixes like `. <any>` on `$x` and `$d` mapping symbols, which compilers like Clang can emit (e.g., `$x. <n>`). Previously, Binutils' disassembler (objdump) and other tools only recognized the bare symbols, leading to incorrect interpretation or display of debugging information. The change updates the recognition logic to use `startswith()` for these symbols, ensuring that suffixed mapping symbols are properly identified.
