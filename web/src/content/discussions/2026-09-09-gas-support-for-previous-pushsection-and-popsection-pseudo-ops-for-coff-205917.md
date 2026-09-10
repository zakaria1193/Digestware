---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- COFF
- assembler directives
discussion_id: 20260909152715.1524505-2-johannes@johannesthoma.com
source_type: public_inbox
title: '[PATCH v3] gas: support for .previous, .pushsection and .popsection pseudo
  ops for coff'
headline: 'gas: support for .previous, .pushsection and .popsection pseudo ops for
  coff'
tldr: Adds .previous, .pushsection, and .popsection pseudo-ops to gas for COFF targets,
  enabling Linux kernel compilation for Windows drivers.
proposer: Johannes Khoshnazar-Thoma <johannes@johannesthoma.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enhances gas functionality for COFF targets with section management.
- Enables cross-compilation scenarios like Linux kernel for Windows.
exchanges: []
primer_expert: This patch adds support for section management directives `.pushsection`,
  `.popsection`, and `.previous` to the gas assembler when targeting COFF object file
  formats. These directives are crucial for code that needs to dynamically switch
  between different sections during assembly, a common requirement for complex code
  generation scenarios like compiling the Linux kernel for Windows/ReactOS drivers.
  The implementation mirrors the existing functionality for ELF targets.
primer_glossary:
- term: gas
  definition: GNU Assembler, the assembler used in the GNU toolchain.
- term: COFF
  definition: Common Object File Format. A file format for executables, object code,
    and libraries, primarily used on Windows systems.
- term: pseudo-ops
  definition: Assembler directives that do not generate machine code but control the
    assembly process, such as defining sections or symbols.
- term: .previous
  definition: A gas pseudo-op that restores the previously active section.
- term: .pushsection
  definition: A gas pseudo-op that saves the current section and then activates a
    new section.
- term: .popsection
  definition: A gas pseudo-op that restores the section that was most recently saved
    by .pushsection.
- term: ELF
  definition: Executable and Linkable Format. A common file format for object code,
    executables, and shared libraries on Unix-like systems.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260909152715.1524505-2-johannes@johannesthoma.com
bugzilla_url: null
date: '2026-09-09'
is_stub: false
stub_reason: ''
---

This patch introduces support for `.previous`, `.pushsection`, and `.popsection` pseudo-operations in the GNU Assembler (gas) for COFF targets. These directives provide section stacking capabilities, mirroring their ELF counterparts. The implementation is a foundational step towards compiling the Linux kernel as a Windows or ReactOS driver, which requires these section management features.
