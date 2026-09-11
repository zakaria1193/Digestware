---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- COFF
- ELF
- sections
- cross-platform
discussion_id: 20260910130303.1692857-2-johannes@johannesthoma.com
source_type: public_inbox
title: '[PATCH v5] gas: support for .previous, .pushsection and .popsection pseudo
  ops for coff'
headline: 'gas: support for .previous, .pushsection and .popsection pseudo ops for
  coff'
tldr: Adds support for .previous, .pushsection, and .popsection pseudo-ops to the
  COFF target in gas.
proposer: Johannes Khoshnazar-Thoma
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Enhances compatibility with build systems that rely on section manipulation, like
  cross-compiling the Linux kernel for Windows.
- Increases the complexity of the COFF backend in the gas assembler.
exchanges:
- author: Johannes Khoshnazar-Thoma
  role: proposer
  position: Submits a patch to add support for .previous, .pushsection, and .popsection
    pseudo-ops to the COFF target in the gas assembler.
  quote: This patch adds support for the .previous, .pushsection and .popsection pseudo-ops
    for COFF targets. The semantics are the same as their ELF counterparts.
primer_expert: This patch extends the `gas` assembler's functionality for COFF object
  file formats by implementing section management pseudo-operations (`.previous`,
  `.pushsection`, `.popsection`). These directives are standard in ELF object file
  generation and allow finer control over section placement and grouping. Their addition
  to COFF is crucial for scenarios where code originating from or targeting ELF-like
  build processes needs to be compatible with COFF, such as building the Linux kernel
  for Windows environments (e.g., as a driver).
primer_glossary:
- term: gas
  definition: The GNU Assembler, a component of the binutils package responsible for
    converting assembly language code into machine code.
- term: COFF
  definition: Common Object File Format, an older standard for object files used on
    some Unix systems and by Windows.
- term: pseudo-ops
  definition: Assembler directives that do not generate machine code but control the
    assembly process, such as defining sections or macros.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: section
  definition: A distinct part of an object file or executable, such as the text (code),
    data, or BSS (uninitialized data) sections.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260910130303.1692857-2-johannes@johannesthoma.com
bugzilla_url: null
date: '2026-09-10'
is_stub: false
stub_reason: ''
---

This patch introduces support for the `.previous`, `.pushsection`, and `.popsection` pseudo-operations in the gas assembler for COFF targets. These pseudo-ops control section manipulation, similar to their ELF counterparts. This enhancement is a necessary step towards enabling the compilation of the Linux kernel as a Windows/ReactOS driver, indicating its importance for cross-platform development and compatibility.
