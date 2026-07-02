---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- subset parsing
- dead code
- error handling
discussion_id: 16b3399b-1b9f-4692-a9ff-5d8ba71c1a2c@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH 17/19] RISC-V: drop dead code from subset parsing'
headline: 'RISC-V: drop dead code from subset parsing'
tldr: Removes dead code and simplifies error handling in RISC-V subset parsing.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: ready
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- None apparent; this is a straightforward cleanup.
exchanges:
- author: Jiawei
  role: contributor
  position: Agrees with the patch, which drops dead code and clarifies error handling.
  quote: In riscv_update_subset1(), when explicit_subset is NULL, errmsg_internal
    is the empty string. There's no need then to pass this as an extra argument to
    the error handler.
primer_expert: This patch focuses on the RISC-V subset parsing logic, which is used
  to interpret the ISA extensions specified in the object file. Removing dead code
  and simplifying error handling improves the maintainability of the binutils.
primer_general: This patch cleans up the code responsible for interpreting the specific
  features enabled in a RISC-V program. RISC-V is a modular architecture where different
  extensions can be added to the base instruction set. This patch removes unnecessary
  parts of the code and makes the error handling more straightforward, making the
  code easier to understand and maintain.
series_id: 'binutils:risc-v: drop dead code from subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/16b3399b-1b9f-4692-a9ff-5d8ba71c1a2c@iscas.ac.cn
bugzilla_url: null
date: '2026-04-29'
---

This patch removes redundant checks and simplifies error handling in the RISC-V subset parsing logic. Specifically, it removes unnecessary checks for NULL return values from `riscv_parsing_subset_version()` and simplifies the error message construction in `riscv_update_subset1()`. These changes improve code clarity and maintainability.
