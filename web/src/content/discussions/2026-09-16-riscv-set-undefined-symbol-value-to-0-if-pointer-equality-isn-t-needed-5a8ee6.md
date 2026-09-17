---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- linker
- symbols
discussion_id: CA+yXCZA+mXQjobWiUmJhMAQ-gFy_NhyWVreU0ZVkYXFSwhy7bw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] riscv: Set undefined symbol value to 0 if pointer equality isn''t
  needed'
headline: 'riscv: Set undefined symbol value to 0 if pointer equality isn''t needed'
tldr: 'Patch accepted: RISC-V undefined symbols now default to 0 if pointer equality
  is not required.'
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Ready to Land
outcome: ready
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Simplifies symbol resolution in certain RISC-V ELF dynamic linking scenarios by
  defaulting undefined symbols to 0, potentially improving build stability for specific
  cases like PR29655, but requires careful consideration if pointer equality is essential.
exchanges:
- author: Kito Cheng <kito.cheng@gmail.com>
  role: other
  position: Approves the patch and thanks the author.
  quote: LGTM, thanks :)
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Submitted a patch to set undefined symbol values to 0 for RISC-V when
    pointer equality is not needed, fixing PR29655.
  quote: 'This fixes:


    FAIL: Build pr29655


    * elfnn-riscv.c (riscv_elf_finish_dynamic_symbol): Set undefined

    symbol value to 0 if pointer equality isn''t needed.'
primer_expert: This patch adjusts the handling of undefined symbols in the RISC-V
  ELF linker implementation within binutils. It specifically targets the `riscv_elf_finish_dynamic_symbol`
  function. When a symbol is undefined and its value is not critical for pointer equality
  comparisons (e.g., in cases not related to dynamic linking where addresses must
  be exact), the symbol's value is now set to 0. This resolves a build issue identified
  as PR29655.
primer_glossary:
- term: undefined symbol
  definition: A symbol (e.g., a variable or function name) that is referenced in one
    object file but not defined within it. The linker resolves these by finding their
    definition in another object file or library.
- term: pointer equality
  definition: In the context of symbol resolution, ensuring that two pointers, even
    if undefined, are resolved to the same address or value if they represent the
    same logical entity.
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) based on RISC principles.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and core dumps on Unix-like systems.
- term: dynamic symbol
  definition: A symbol that is visible and resolved at runtime, typically used in
    shared libraries and dynamically linked executables.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZA+mXQjobWiUmJhMAQ-gFy_NhyWVreU0ZVkYXFSwhy7bw@mail.gmail.com
bugzilla_url: null
date: '2026-09-16'
is_stub: false
stub_reason: ''
---

This patch modifies the RISC-V ELF backend to set the value of undefined symbols to 0 when pointer equality is not a concern. This resolves a specific build failure for PR29655. The change in `riscv_elf_finish_dynamic_symbol` improves the linker's handling of undefined symbols in certain contexts.
