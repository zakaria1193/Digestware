---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- linker
- refactoring
- assembler
discussion_id: CA+yXCZDignJ_8Et3mKSkkmbQdMiZa+khGSTVqDHt9VLeEcb7Zg@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Describe relax passes with a pass table'
headline: 'RISC-V: Describe relax passes with a pass table'
tldr: A patch refactors the RISC-V relax pass mechanism by introducing a pass table,
  improving maintainability and paving the way for new relax passes.
proposer: Kito Cheng <kito.cheng@gmail.com>
consensus: Committed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased complexity in the linker script due to the pass table structure.
- Potential for new bugs during the introduction of the pass table mechanism.
exchanges:
- author: Kito Cheng
  role: proposer
  position: Announces that the patch refactoring RISC-V relax passes has been pushed.
  quote: pushed :)
- author: Kito Cheng
  role: proposer
  position: Explains that the patch introduces a pass table to describe relax passes,
    simplifying the addition of new passes and improving the structure.
  quote: '_bfd_riscv_relax_section picks the relax function for each reloc with a

    chain of branches on info->relax_pass, and ld hard-codes the number of

    passes. Adding a pass means adding another branch and bumping the

    count in the emulation.


    This is a refactor to make room for more relax passes, such as

    vendor specific ones or one for Zcmt table jump. Each such pass would

    otherwise add its own branch, it…'
primer_expert: This patch refactors the relax pass mechanism in the RISC-V backend
  of binutils. Previously, adding new relax passes involved modifying a chain of branches
  and updating a hardcoded pass count. This change introduces a structured pass table
  (using `struct riscv_relax_pass`) that describes each pass with its selector, hooks,
  and options. This improves maintainability and makes it easier to add future passes,
  such as those for vendor-specific extensions or the Zcmt instruction set extension.
primer_glossary:
- term: Relaxation
  definition: In the context of linkers, relaxation is a process of adjusting machine
    code (e.g., branch offsets) after initial assembly to optimize for different addressing
    modes or to satisfy relocation constraints.
- term: Pass table
  definition: A data structure that defines a sequence of operations or passes to
    be executed. In this case, it lists the different relaxation passes available
    for the RISC-V target.
- term: Reloc
  definition: Relocation. A placeholder in object code that indicates where an address
    or symbol needs to be patched by the linker.
- term: Zcmt
  definition: A proposed RISC-V instruction set extension related to Control-flow
    Mitigation Technology, aimed at enhancing security.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on RISC principles.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZDignJ_8Et3mKSkkmbQdMiZa+khGSTVqDHt9VLeEcb7Zg@mail.gmail.com
bugzilla_url: null
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

Kito Cheng announces that a patch has been pushed, refactoring the RISC-V relax pass mechanism in binutils. The change introduces a pass table to describe each relax pass, which includes a reloc selector and optional hooks. This structure is intended to simplify the addition of new relax passes, such as vendor-specific ones or those for the Zcmt extension, by avoiding repetitive code for each new pass.
