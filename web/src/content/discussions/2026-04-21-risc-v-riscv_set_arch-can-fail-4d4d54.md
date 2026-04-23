---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- null pointer
- crash fix
discussion_id: 8fb9900a-9724-4d50-9113-3ea61697a86d@suse.com
source_type: public_inbox
title: 'Re: [PATCH 12/19] RISC-V: riscv_set_arch() can fail'
headline: 'RISC-V: riscv_set_arch() can fail'
tldr: Fixes a potential null pointer dereference in riscv_set_arch() by ensuring a
  default architecture is used.
stakes: Prevents crashes and ensures correct behavior when setting the RISC-V architecture.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Prevents a null pointer dereference and potential crashes.
- Maintains error reporting for invalid architecture specifications.
- Introduces a dependency on `DEFAULT_RISCV_ARCH_WITH_EXT` when no architecture is
  specified.
exchanges:
- author: Simon Richter
  role: other
  position: Asks for confirmation that the patch still reports an error but avoids
    a null pointer dereference.
  quote: Am I reading this correctly that this is still an error, but it avoids a
    follow-up NULL pointer dereference?
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Confirms that the patch still reports an error while avoiding the null
    pointer dereference.
  quote: Yes, as visible from patch context the as_bad() won't be bypassed.
primer_expert: The patch modifies `gas/config/tc-riscv.c` to handle cases where the
  `-march` (architecture) string is empty. The `riscv_set_arch` function would previously
  dereference a null pointer in this scenario, leading to a crash.  The fix assigns
  `DEFAULT_RISCV_ARCH_WITH_EXT` to avoid the crash while still reporting an error.
primer_general: The GNU Assembler (`gas`) is a tool used to translate assembly code
  into machine code. For the RISC-V architecture, the `-march` option specifies the
  target architecture. The `riscv_set_arch()` function handles this specification.
  This patch addresses a potential crash scenario where an empty architecture string
  is provided, ensuring that a default architecture is used and an error is reported.
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

Simon Richter inquired about a patch that fixes a potential null pointer dereference in the `riscv_set_arch()` function. The patch avoids the dereference by assigning a default RISC-V architecture when the architecture string is empty. Jan Beulich confirmed that the patch still reports an error, but prevents a crash by avoiding the null pointer dereference.
