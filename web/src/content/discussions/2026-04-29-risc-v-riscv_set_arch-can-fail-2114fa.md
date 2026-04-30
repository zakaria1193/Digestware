---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- error handling
- null pointer
discussion_id: 9e1a5fd2-e547-4bbb-be77-c97e115e40bf@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH 12/19] RISC-V: riscv_set_arch() can fail'
headline: 'RISC-V: riscv_set_arch() can fail'
tldr: Avoid passing NULL pointers to functions when ``riscv_set_arch()`` fails to
  set architecture string.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Ready to Land
outcome: ready
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Using a default architecture string might not always be the desired behavior, but
  it avoids a crash.
- The assembler will proceed with a default arch if the expected arch string is missing.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: proposer
  position: States that the patch prevents NULL pointers from being passed to functions
    when the architecture string is empty, and also catches cases where the frontend
    fails to provide the architecture string.
  quote: So this should still catch cases like a frontend failing to provide the archstring,
    while avoiding a follow-up crash.
primer_expert: The ``riscv_set_arch()`` function, located in ``gas/config/tc-riscv.c``,
  parses the RISC-V architecture string. This patch addresses a scenario where the
  architecture string is empty, which could lead to NULL pointers being passed to
  other functions. To avoid this, the code now uses a default architecture string
  when the input is empty.
primer_general: When the assembler processes RISC-V code, it needs to know the target
  architecture. The ``riscv_set_arch()`` function is responsible for setting the architecture
  based on the input string.  This patch fixes a bug where if the architecture string
  is empty, the assembler could crash. Now, if the string is empty, a default architecture
  is used.
series_id: 'binutils:risc-v: riscv_set_arch() can fail'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9e1a5fd2-e547-4bbb-be77-c97e115e40bf@iscas.ac.cn
bugzilla_url: null
date: '2026-04-29'
---

This patch fixes a potential crash in ``riscv_set_arch()`` when the architecture string is empty. In such cases, the code now avoids passing NULL pointers to subsequent functions by using a default architecture string (``DEFAULT_RISCV_ARCH_WITH_EXT``). This prevents crashes when the frontend fails to provide a valid architecture string.
