---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- isa
- memory leak
discussion_id: CALWc1WCcB_TFvaPKTkc26SMptvi6f9y2hgiV6hZrccEMKkJiRw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Check if the merged ISA string is conflicting'
headline: 'RISC-V: Follow-up patch series for conflicting ISA strings'
tldr: Ethan Liang provides a link to a new patch series addressing the RISC-V ISA
  string conflict issue.
proposer: '"Ethan Y. C. Liang" <yclwlcy@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: '"Ethan Y. C. Liang" <yclwlcy@gmail.com>'
  role: proposer
  position: Acknowledges the memory leak concern and provides a link to a new patch
    series that addresses it.
  quote: 'Yep, you''re right. I''ve already sent another patch series to address this:


    https://sourceware.org/pipermail/binutils/2026-July/150010.html'
- author: Jeffrey Law <jeffrey.law@oss.qualcomm.com>
  role: reviewer
  position: Raises a concern about potential memory leaks in the initial patch.
  quote: 'The question I have is don''t we possibly leak memory for various objects

    allocated by riscv_parse_subset and its children and stored into the

    subsets and perhaps other fields of riscv_rps_merged?'
primer_expert: This discussion concerns a follow-up to a patch that added ISA string
  conflict checking to the RISC-V linker. The original patch introduced a memory leak
  in error paths, which this new series aims to fix. The context is the BFD and linker
  subsystem's handling of RISC-V architecture attributes.
primer_glossary:
- term: ISA string
  definition: A string representing the instruction set architecture (ISA) extensions
    supported by a RISC-V processor or compilation target. For example, 'rv64i_zfinx'
    or 'rv64if'.
- term: linker
  definition: A program that combines object files and libraries into an executable
    program or another object file. In binutils, this is typically the `ld` command.
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by Binutils
    to handle various object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CALWc1WCcB_TFvaPKTkc26SMptvi6f9y2hgiV6hZrccEMKkJiRw@mail.gmail.com
bugzilla_url: null
date: '2026-07-06'
is_stub: false
stub_reason: ''
---

Ethan Y. C. Liang states that a new patch series has been sent to address the issue of conflicting RISC-V ISA strings during linking. This follow-up aims to resolve the problem he previously raised, where the linker did not check for conflicting extensions when merging ISA strings.
