---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- gas
- null pointer
discussion_id: 8fb9900a-9724-4d50-9113-3ea61697a86d@suse.com
source_type: public_inbox
title: 'Re: [PATCH 12/19] RISC-V: riscv_set_arch() can fail'
headline: 'RISC-V: riscv_set_arch() can fail'
tldr: Fixes a potential null pointer dereference in riscv_set_arch() by ensuring a
  default architecture is set.
stakes: Prevents potential crashes due to null pointer dereferences, improving the
  stability of the assembler for RISC-V architectures.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding a check for an empty architecture string.
- Using a default architecture when none is specified.
- Prioritizing stability over potentially allowing completely unspecified architectures.
exchanges:
- author: Simon Richter
  role: reviewer
  position: Asks for clarification on the patch's behavior, specifically whether it
    avoids a follow-up NULL pointer dereference.
  quote: Am I reading this correctly that this is still an error, but it avoids a
    follow-up NULL pointer dereference?
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Confirms that the patch avoids the NULL pointer dereference.
  quote: Yes, as visible from patch context the as_bad() won't be bypassed.
primer_expert: This patch modifies `gas/config/tc-riscv.c` in the GNU Assembler (gas)
  to prevent a null pointer dereference in the RISC-V architecture support.  The `riscv_set_arch()`
  function is responsible for parsing and setting the RISC-V architecture based on
  command-line options or ELF attributes. The patch ensures that when an empty architecture
  string is provided, a default architecture is used, preventing subsequent crashes
  due to null pointers.
primer_general: The GNU Assembler (gas) converts human-readable assembly code into
  machine code that a computer can execute.  This patch focuses on the RISC-V architecture,
  a modern open-source processor design.  The patch fixes a potential error in the
  assembler that could occur when specifying the RISC-V architecture.  Specifically,
  if no architecture is specified, the assembler could crash due to trying to access
  a memory location that doesn't exist (a null pointer dereference). This patch ensures
  a default architecture is used to avoid this crash, improving the reliability of
  the assembler.
series_id: 'binutils:risc-v: riscv_set_arch() can fail'
series_role: reply
series_parts:
- title: 'RISC-V: riscv_set_arch() can fail'
  url: https://inbox.sourceware.org/binutils/0a175ede-c573-46e6-babf-388156098dee@hogyros.de
  n: 12
  total: 19
- title: 'RISC-V: riscv_set_arch() can fail'
  url: https://inbox.sourceware.org/binutils/d39a0dc0-110f-400a-9473-090ddf96efa2@suse.com
  n: 12
  total: 19
url: https://inbox.sourceware.org/binutils/8fb9900a-9724-4d50-9113-3ea61697a86d@suse.com
bugzilla_url: null
date: '2026-04-21'
---

This patch addresses a potential null pointer dereference in the `riscv_set_arch()` function within the RISC-V assembler. The issue occurs when the architecture string is empty, leading to unset `riscv_rps_as.subset_list` and `file_arch_str` variables. The patch ensures that if `file_arch_str` is NULL, a default RISC-V architecture is set, preventing the dereference. Jan Beulich confirms that the patch avoids a follow-up NULL pointer dereference.
