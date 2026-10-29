---
project: binutils
subsystem: mips
patch_id: null
tags:
- mips
- architecture
- assembler
- embedded
discussion_id: alpine.DEB.2.21.2610281336190.42255@angie.orcam.me.uk
source_type: public_inbox
title: '[committed v4] MIPS: Add the m6201 architecture'
headline: 'MIPS: Add support for the m6201 architecture'
tldr: Adds support for the M6201 processor core, a MIPS32 Release 6 implementation.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Requires minor fixes to commit message formatting and test case naming before being
  committed.
exchanges:
- author: Matthew Fortune <matthew.fortune@imgtec.com>
  role: proposer
  position: Submitted a patch to add support for the M6201 processor core.
  quote: "Add support for the M6201 processor core, a member of the M6200 family\n\
    implementing the MIPS32 Release 6 Architecture along with the MCU ASE.\n\ngas/\n\
    \t* config/tc-mips.c (mips_cpu_info_table): Add m6201.\n\t* doc/c-mips.texi: Add\
    \ documentation for m6201.\n\ngas/testsuite/\n\t* gas/mips/elf_mach_m6201.d: New\
    \ test.\n\t* gas/mips/mips.exp: Run the new test.\n\nCo-authored by: Faraz Shahbazker\
    \ <fshahbazker@wavec…"
- author: Jovan Dmitrovic via Binutils
  role: reviewer
  position: Requested a commit description and pointed out minor formatting issues
    in the patch.
  quote: "Missing commit description.\n\n Missing full stop and a second space.\n\n\
    \ I don't like that the new test is missing the \"m\" prefix from the core \n\
    name."
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: maintainer
  position: Applied the patch with minor corrections, noting the addressed issues.
  quote: "Since these issues were straightforward to address I went ahead and \ncommitted\
    \ this change as quoted.  Thank you for your contribution."
primer_expert: This change extends the gas assembler's MIPS backend to recognize and
  support the M6201 processor core. This core is part of the M6200 family, implements
  the MIPS32 Release 6 ISA, and includes the MCU ASE. The patch adds a new CPU entry
  to `mips_cpu_info_table`, updates the documentation, and introduces a test case
  to verify the assembler's behavior for this new architecture.
primer_glossary:
- term: MIPS
  definition: A Reduced Instruction Set Computing (RISC) architecture, commonly used
    in embedded systems and historically in workstations.
- term: MIPS32 Release 6
  definition: A specific revision of the MIPS32 architecture, defining the instruction
    set and features for 32-bit MIPS processors.
- term: MCU ASE
  definition: Application Specific Extension for Microcontroller. A set of instructions
    tailored for microcontroller applications.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: assembler
  definition: A program that translates assembly language code into machine code.
- term: MIPS CPU info table
  definition: A data structure within the MIPS assembler that maps CPU names to their
    architectural features and instruction sets.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    component.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2610281336190.42255@angie.orcam.me.uk
bugzilla_url: null
date: '2026-10-28'
is_stub: false
stub_reason: ''
---

This commit introduces support for the M6201 processor core, which is part of the M6200 family and implements the MIPS32 Release 6 Architecture along with the MCU ASE. The changes include adding the `m6201` entry to the `mips_cpu_info_table` in `gas/config/tc-mips.c`, updating documentation in `gas/doc/c-mips.texi`, and adding a new test case `elf_mach_m6201.d` to the gas testsuite. The patch was reviewed and committed with minor fixes for formatting and naming.
