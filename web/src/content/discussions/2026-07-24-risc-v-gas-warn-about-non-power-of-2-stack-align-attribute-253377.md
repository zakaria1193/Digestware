---
project: binutils
subsystem: risc-v/gas
patch_id: null
tags:
- binutils
- risc-v
- gas
- attribute
- warning
discussion_id: 6f5e4577-ec5e-4393-9df0-3b9c50de7d81@suse.com
source_type: public_inbox
title: '[PATCH v4 10/12] RISC-V/gas: warn about non-power-of-2 stack-align attribute'
headline: 'RISC-V/gas: warn about non-power-of-2 stack-align attribute'
tldr: Warn about non-power-of-2 values for the RISC-V stack_align attribute in the
  assembler.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: ready
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Adds a runtime check (warning) in the assembler for a specific attribute.
- Does not reject non-power-of-2 values outright, allowing for later BFD handling
  or user ignorance.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Introduces a warning in gas for non-power-of-2 values of the stack_align
    attribute.
  quote: Only power-of-2 values are sensible for alignment.
- author: Jiawei <jiawei@iscas.ac.cn>
  role: reviewer
  position: Reviewed the patch, asking whether existing non-zero values should be
    rejected and if 0 should be permitted as an 'attribute not set' indicator.
  quote: null
primer_expert: This patch modifies the RISC-V assembler's attribute handling to check
  the `Tag_RISCV_stack_align` attribute. It issues a warning if the provided value
  is not a power of two, which is a fundamental requirement for alignment values to
  be correctly interpreted by the processor and system. This improves the robustness
  of code generation for RISC-V targets.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is gaining popularity
    for its modularity and extensibility.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: .attribute
  definition: An assembler directive used to specify object file attributes, such
    as target architecture or features.
- term: Tag_RISCV_stack_align
  definition: An ELF tag specific to RISC-V that specifies the required stack alignment.
series_id: 'binutils:risc-v/gas: warn about non-power-of-2 stack-align attribute'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/6f5e4577-ec5e-4393-9df0-3b9c50de7d81@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch adds a warning to the RISC-V GNU Assembler (gas) when the `.attribute stack_align` directive is used with a non-power-of-2 value. This ensures that developers are informed about potentially invalid alignment settings, which could lead to incorrect behavior or performance issues.
