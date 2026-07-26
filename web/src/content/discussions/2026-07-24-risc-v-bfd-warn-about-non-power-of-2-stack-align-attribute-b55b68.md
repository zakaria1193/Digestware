---
project: binutils
subsystem: risc-v/bfd
patch_id: null
tags:
- binutils
- risc-v
- bfd
- elf
- attribute
discussion_id: 9ab61932-ebdf-4136-bb1f-b9482aa75ea7@suse.com
source_type: public_inbox
title: '[PATCH v4 12/12] RISC-V/bfd: warn about non-power-of-2 stack-align attribute'
headline: 'RISC-V/bfd: warn about non-power-of-2 stack-align attribute'
tldr: Warn about and ignore non-power-of-2 values for the RISC-V stack_align attribute.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: ready
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Enforces stricter validation of the stack_align attribute, potentially rejecting
  some previously accepted code.
- Improves robustness by preventing the use of non-sensical alignment values.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes to warn about and ignore non-power-of-2 values for the RISC-V
    stack_align attribute, ensuring sensible alignment.
  quote: 'Only power-of-2 values are sensible for alignment. Reject other values.


    While there also drop a redundant part of a related conditional.'
- author: Jiawei jiawei@iscas.ac.cn
  role: reviewer
  position: Reviewed the patch, suggesting adding an underscore to the diagnostic
    message in version 4.
  quote: null
primer_expert: This patch modifies the BFD library's ELF handling for RISC-V to validate
  the `Tag_RISCV_stack_align` attribute. It ensures that only power-of-2 values are
  accepted for stack alignment, aligning with hardware capabilities and preventing
  incorrect interpretations of alignment specifications that could impact performance
  or correctness.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a GNU component that abstracts different
    object file formats.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps.
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is gaining popularity
    for its modularity and extensibility.
- term: tag_RISCV_stack_align
  definition: An ELF tag specific to RISC-V that specifies the required stack alignment.
series_id: 'binutils:risc-v/bfd: warn about non-power-of-2 stack-align attribute'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9ab61932-ebdf-4136-bb1f-b9482aa75ea7@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch introduces a warning for non-power-of-2 values used with the RISC-V `stack_align` attribute, enforcing sensible alignment. It also refactors some conditional logic for clarity. The change ensures that only power-of-2 alignment values are accepted, promoting correct code generation.
