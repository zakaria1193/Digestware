---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- coff
- section
discussion_id: 20260718162202.2902067-1-johannes@johannesthoma.com
source_type: public_inbox
title: '[PATCH] gas: support for .pushsection and .popsection pseudo ops for coff'
headline: 'gas: support for .pushsection and .popsection pseudo ops for coff'
tldr: Adds support for .pushsection/.popsection to the COFF object file format in
  GAS.
proposer: Johannes Khoshnazar-Thoma <johannes@johannesthoma.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables COFF support for complex section management used in projects like the Linux
  kernel, at the cost of adding code to the COFF backend.
exchanges: []
primer_expert: This patch extends the GNU Assembler's (GAS) COFF backend to support
  section management directives `.pushsection` and `.popsection`. These are essential
  for building Linux kernel components for Windows/ReactOS (COFF/PE targets), allowing
  developers to maintain section state across nested code/data segments, similar to
  the existing ELF support. The implementation is a direct port from `obj-elf.c` to
  `obj-coff.c`.
primer_glossary:
- term: .pushsection
  definition: An assembler pseudo-operation that saves the current section description
    and then starts a new section.
- term: .popsection
  definition: An assembler pseudo-operation that restores the section description
    that was previously saved by a corresponding `.pushsection`.
- term: COFF
  definition: Common Object File Format, a file format for executable and object code,
    primarily used on Windows systems.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executable,
    object code, shared libraries, and core dumps, commonly used on Unix-like systems.
- term: GNU assembler (GAS)
  definition: The assembler program distributed as part of the GNU Binutils package.
    It supports multiple input and output formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260718162202.2902067-1-johannes@johannesthoma.com
bugzilla_url: null
date: '2026-07-18'
is_stub: false
stub_reason: ''
---

This patch adds support for the `.pushsection` and `.popsection` pseudo-operations to the COFF object file format in the GNU assembler (GAS). These directives are crucial for building current Linux kernels, which normally use ELF. When targeting Windows/ReactOS drivers (COFF), these operands were previously unsupported. The implementation was copied from the ELF backend, enabling Linux kernel compilation as a COFF object.
