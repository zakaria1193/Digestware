---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- disassembler
- ARC-V APEX
discussion_id: CYYPR12MB887127258414B3363C2BD30FC70A2@CYYPR12MB8871.namprd12.prod.outlook.com
source_type: public_inbox
title: 'RE: [PATCH 0/2] RISC-V: Add ARC-V APEX assembler and disassembler support'
headline: 'RISC-V: Responses to feedback on ARC-V APEX assembler/disassembler support'
tldr: Luis Silva responds to feedback and agrees to present the ARC-V APEX assembler/disassembler
  support at the toolchain SIG meeting.
proposer: Luis Manuel Silva <Luis.Silva1@synopsys.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Luis Manuel Silva
  role: proposer
  position: Agrees to present the ARC-V APEX assembler/disassembler support at the
    toolchain SIG meeting and potentially create a PR to the riscv-c-api-doc repository
    to start the discussion.
  quote: 'Thank you for the positive feedback! I''d be happy to present this at

    the toolchain SIG meeting and have further discussion.'
primer_expert: This thread discusses the proposed addition of ARC-V APEX support to
  the RISC-V assembler and disassembler. APEX allows dynamic definition of custom
  instructions. Standardizing this functionality across toolchains (GNU and LLVM)
  is crucial for interoperability and wider adoption. The discussion aims to achieve
  consensus on the implementation before it proceeds further.
primer_general: Assemblers and disassemblers are tools that translate between human-readable
  assembly code and machine code. This discussion centers around adding support for
  a feature called ARC-V APEX to the RISC-V toolchain. APEX allows developers to define
  their own custom instructions, but it's important to ensure compatibility across
  different toolchains. The goal is to discuss and standardize this feature before
  it's fully implemented.
series_id: 'binutils:risc-v: add arc-v apex assembler and disassembler support'
series_role: cover
series_parts:
- title: 'RISC-V: Add ARC-V APEX assembler and disassembler support'
  url: https://inbox.sourceware.org/binutils/CA+yXCZDh-maTC5xSWJ4NAC3+w_34kLvKzBQvSMWVGzSkk7bn1Q@mail.gmail.com
  n: 0
  total: 2
- title: 'RISC-V: Add ARC-V APEX assembler and disassembler support'
  url: https://inbox.sourceware.org/binutils/20260525133052.1885254-1-luiss@synopsys.com
  n: 0
  total: 2
url: https://inbox.sourceware.org/binutils/CYYPR12MB887127258414B3363C2BD30FC70A2@CYYPR12MB8871.namprd12.prod.outlook.com
bugzilla_url: null
date: '2026-05-25'
is_stub: false
---

Luis Silva replies to Kito Cheng's feedback on the proposed ARC-V APEX assembler and disassembler support for RISC-V. Kito suggested discussing the approach in a toolchain SIG meeting to ensure consensus between LLVM and GNU communities and standardizing it before moving forward. Luis agrees to present the work at the toolchain SIG meeting and potentially create a PR to the riscv-c-api-doc repository to start the discussion.
