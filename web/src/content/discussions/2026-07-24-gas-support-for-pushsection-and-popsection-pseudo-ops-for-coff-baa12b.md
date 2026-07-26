---
project: binutils
subsystem: gas
patch_id: null
tags:
- assembler
- binutils
- gas
- COFF
- section management
discussion_id: 20260724122850.469382-2-johannes@johannesthoma.com
source_type: public_inbox
title: '[PATCH v2] gas: support for .pushsection and .popsection pseudo ops for coff'
headline: 'gas: support for .pushsection and .popsection pseudo ops for coff'
tldr: Adds support for .pushsection and .popsection directives to the COFF object
  file format in the gas assembler.
proposer: Johannes Khoshnazar-Thoma <johannes@johannesthoma.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 8
technical_tradeoffs:
- Reusing code from ELF for COFF simplifies development but may not perfectly map
  all semantics if underlying format differences are significant.
- Adding support for these directives enables cross-platform compilation scenarios,
  increasing flexibility for kernel developers targeting Windows.
exchanges:
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: reviewer
  position: Acknowledged the patch and requested a reword of the commit message and
    description to use the imperative mood, as is standard for Git commit messages.
  quote: 'Please reword using the imperative mood both for the change heading and

    the description.'
- author: Johannes Khoshnazar-Thoma <johannes@johannesthoma.com>
  role: proposer
  position: Submits a patch to add .pushsection and .popsection support to gas for
    the COFF format, enabling compilation of Linux kernel drivers for Windows/ReactOS.
  quote: 'Current Linux kernels make heavy use of the .pushsection and

    .popsection pseudo ops. Normally, the Linux kernel is built

    as an ELF object, where the assembler supports those pseudo

    ops. When compiling the Linux kernel as a Windows/ReactOS

    driver however, it must be compiled as a COFF object, since

    the Windows/ReactOS kernel does not know how to load ELF

    binaries.


    In order to be able to compile t…'
primer_expert: This patch extends the GNU Assembler's (gas) support for section manipulation
  to the COFF object file format. It backports the `.pushsection` and `.popsection`
  directives, previously only available for ELF, to COFF. This is crucial for building
  components like the Linux kernel drivers that rely on these directives when targeting
  Windows/ReactOS environments (PE32/COFF). The implementation leverages existing
  ELF logic.
primer_glossary:
- term: gas
  definition: The GNU Assembler, a component of the GNU Binutils package that translates
    assembly language code into machine code.
- term: COFF
  definition: Common Object File Format. A standard binary file format for executables,
    object code, and libraries, primarily used on Windows systems.
- term: ELF
  definition: Executable and Linkable Format. A standard binary file format commonly
    used on Unix-like operating systems for executables, object code, shared libraries,
    and core dumps.
- term: .pushsection / .popsection
  definition: Assembler directives that allow temporarily saving the current section
    and switching to a new one, with .popsection restoring the previously active section.
    Used for managing code/data placement.
- term: pseudo-ops
  definition: Assembler instructions that do not generate machine code directly but
    control the assembly process, such as defining sections or symbols.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260724122850.469382-2-johannes@johannesthoma.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch adds support for the `.pushsection` and `.popsection` pseudo-operations to the GNU Assembler (gas) when generating COFF object files. These directives are heavily used in current Linux kernels compiled as ELF, and this change enables the Linux kernel to be compiled as a COFF object for Windows/ReactOS drivers. The implementation was copied from the ELF object code, and includes a new test case.
