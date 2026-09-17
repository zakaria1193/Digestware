---
project: binutils
subsystem: riscv
patch_id: null
tags:
- binutils
- risc-v
- linker
- attributes
discussion_id: CA+yXCZBSLYss8vaeBd3dvGjGi64=GSYt4H7BJKpwrQdzg26t3Q@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] riscv: Ignore attributes in empty input file'
headline: 'riscv: Ignore attributes in empty input file'
tldr: 'Patch accepted: RISC-V assembler now ignores attributes in empty input files.'
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Ready to Land
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves the robustness of the RISC-V linker by correctly handling edge cases with
  empty files and specific sections, at the cost of minor complexity in attribute
  merging logic.
exchanges:
- author: Kito Cheng <kito.cheng@gmail.com>
  role: other
  position: Approves the patch and thanks the author.
  quote: LGTM, thanks :)
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Submitted a patch to ignore attributes in empty input files and .note.gnu.build-id
    sections for RISC-V, resolving linker test failures.
  quote: 'Ignore empty and .note.gnu.build-id sections when merging attributes.

    The following linker tests now pass for riscv:


    FAIL: Diagnostics - Wrong magic number mixed with valid CTF sections

    FAIL: --gc-sections with --defsym

    FAIL: --gc-sections with KEEP

    FAIL: --gc-sections with __start_SECTIONNAME

    FAIL: ld-plugin/lto-10r

    FAIL: ld-plugin/lto-3r

    FAIL: ld-plugin/lto-4r-a

    FAIL: ld-plugin/lto-4r-b

    FAIL:…'
primer_expert: This patch modifies the BFD library's RISC-V ELF backend (`elfnn-riscv.c`)
  to correctly handle attribute merging. It ensures that attributes found in empty
  input files or sections like `.note.gnu.build-id` are ignored, preventing issues
  with linker operations such as garbage collection (`--gc-sections`) and symbol definition.
  This resolves several previously failing linker test cases.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, used by GNU Binutils and GDB to provide
    a common interface to various object file formats.
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) based on RISC principles.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for object files,
    executables, and core dumps on Unix-like systems.
- term: attributes
  definition: Metadata embedded within object files that can provide information about
    symbols, sections, or the file itself, used by linkers and other tools.
- term: --gc-sections
  definition: A linker option that removes unused sections from the output file, reducing
    its size.
- term: .note.gnu.build-id
  definition: An ELF section used to store a unique identifier for the build of an
    executable or library, often used for debugging and crash report correlation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZBSLYss8vaeBd3dvGjGi64=GSYt4H7BJKpwrQdzg26t3Q@mail.gmail.com
bugzilla_url: null
date: '2026-09-16'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the RISC-V assembler where attributes in empty or .note.gnu.build-id sections were not being ignored during merging. The change modifies `_bfd_riscv_elf_merge_private_bfd_data` to correctly handle these cases, passing several linker test cases that previously failed. The patch has been accepted.
