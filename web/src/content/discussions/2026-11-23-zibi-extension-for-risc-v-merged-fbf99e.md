---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- risc-v
- instruction set
- compiler
discussion_id: CALLt3TiQ=wh2q64c_w5mgUK2Y7sgh2pMq85LyiK8Ri2tzQCPgg@mail.gmail.com
source_type: public_inbox
title: 'Re: Zibi Extension for RISC-V'
headline: Zibi Extension for RISC-V merged
tldr: Kito Cheng's binutils-gdb patch for the RISC-V Zibi extension has been merged.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Committed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Announces that the Zibi Extension patch for RISC-V has been pushed.
  quote: pushed :)
- author: Jeff Law <jeffreyalaw@gmail.com>
  role: reviewer
  position: Confirms Kito's patch for the RISC-V Zibi extension is ready for commit,
    having reviewed it and made a minor version bump.
  quote: 'This is Kito''s binutils-gdb patch for the Zibi RISC-V extension.


    Zibi introduces two new instructions compare a small constant against a register
    and branch on equality/inequality.


    I manually built the match/mask tables which lined up with Kito''s

    implementation. The only change I made was bumping the version to 0.9.'
primer_expert: This discussion pertains to the binutils-gdb component, specifically
  the integration of the RISC-V 'Zibi' extension. Zibi adds conditional branch instructions
  based on register-immediate comparisons. The patch involves updating the instruction
  tables and dissectors within binutils-gdb to recognize and correctly handle these
  new instructions.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computing principles.
- term: Zibi Extension
  definition: A proposed extension for the RISC-V ISA that adds instructions for comparing
    a register with an immediate value and branching based on the result.
- term: binutils-gdb
  definition: A component of the GNU Binutils project that includes support for the
    GDB debugger, often sharing instruction set definitions.
- term: patch
  definition: A piece of code or a set of changes intended to be applied to existing
    source code to fix bugs or add new features.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CALLt3TiQ=wh2q64c_w5mgUK2Y7sgh2pMq85LyiK8Ri2tzQCPgg@mail.gmail.com
bugzilla_url: null
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

Jeff Law reports that Kito Cheng's patch for the RISC-V Zibi extension in binutils-gdb has been committed. The Zibi extension introduces two new instructions that compare a small constant against a register and branch on equality or inequality. Jeff Law, acting as reviewer, had previously planned to merge the patch and made a minor version bump to 0.9.
