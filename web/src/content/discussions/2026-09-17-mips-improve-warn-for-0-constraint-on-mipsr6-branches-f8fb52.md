---
project: binutils
subsystem: mips
patch_id: null
tags:
- MIPS
- assembler
- warnings
- R6
- validation
discussion_id: alpine.DEB.2.21.2609171939500.15569@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [PATCH 3 03/16] MIPS: Improve WARN for $0 constraint on MIPSR6 branches'
headline: 'MIPS: Improve WARN for $0 constraint on MIPSR6 branches'
tldr: Change is invalid due to file duplication and incorrect commit message, and
  requires test invocation.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Needs Revision
outcome: needs_revision
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Correctness of assembler warnings for MIPS R6 architecture.
- Avoids code duplication and ensures accurate commit history.
exchanges:
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: reviewer
  position: States the change is invalid due to file duplication, lack of test invocation,
    and an inaccurate commit heading, referencing previous commits.
  quote: "This change is invalid.\n\nIt wouldn't be in its current form owing to the\
    \ missing source and the \nlack of test invocation in mips.exp, but it's just\
    \ that the file was \nalready added with commit 6914869aa73d (\"MIPS: Fix constraint\
    \ issues with \nthe R6 beqc and bnec instructions\") and then renamed with commit\
    \ \ncd4797ee0546 (\"MIPS/gas: Reject $0 as source register for DAUI \ninstruction\"\
    ).\n\nAlso the co…"
- author: Jovan Dmitrovic via Binutils
  role: contributor
  position: Submitted a patch to validate warnings for $0 constraint on MIPS R6 branches,
    aiming to improve assembler reliability.
  quote: 'Validation of warnings and error detection within branching

    instructions for the MIPS R6 architecture. The test ensures that

    the assembler generates accurate warnings when a user makes an

    error involving the use of the $0 register in branching instructions,

    thereby improving the reliability and correctness of binary outputs.'
primer_expert: This pertains to `gas/mips/r6-branch-constraints.l` and `gas/testsuite/gas-mips/mips.exp`.
  The patch attempts to add new warnings for the R6 MIPS architecture related to the
  use of the `$0` register in branch instructions. The reviewer identifies that the
  file already exists from prior commits with different names and that the commit
  message doesn't accurately reflect the changes or the associated test setup.
primer_glossary:
- term: MIPS R6
  definition: The sixth revision of the MIPS Reduced Instruction Set Computer (RISC)
    architecture, featuring specific instruction set extensions and behaviors.
- term: $0 register
  definition: In MIPS assembly, the register `$0` (or `$zero`) is hardwired to the
    value zero. It's often used for specific operations or as a conventional way to
    indicate a null or zero value.
- term: branch instructions
  definition: Instructions that alter the sequential flow of program execution, such
    as jumps and conditional branches.
- term: assembler
  definition: A program that translates assembly language code into machine code.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: commit
  definition: A saved state of changes in a version control system like Git, representing
    a specific point in the project's history.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2609171939500.15569@angie.orcam.me.uk
bugzilla_url: null
date: '2026-09-17'
is_stub: false
stub_reason: ''
---

Maciej W. Rozycki states that a proposed change to improve warnings for the $0 constraint on MIPS R6 branches is invalid. He points out that the source file was already added and renamed in previous commits, the commit heading is inaccurate, and the change is missing test invocation in `mips.exp`. The issues collectively render the patch unusable in its current form.
