---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- memory management
- strdup
- xstrdup
discussion_id: eafb3dd1-bd0c-4713-9bc0-af2978fdfe62@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH 11/19] RISC-V: avoid strdup()'
headline: 'RISC-V: Avoid strdup()'
tldr: Replaces ``strdup()`` with ``xstrdup()`` in several places within the RISC-V
  backend.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Ready to Land
outcome: ready
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Using ``xstrdup()`` adds a dependency on the custom memory allocation functions.
- The program will exit with a fatal error instead of continuing with potentially
  corrupted data.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: proposer
  position: States that ``xstrdup()`` should be used along with ``xmalloc()``.
  quote: Along with xmalloc(), xstrdup() wants using.
primer_expert: The RISC-V backend uses string duplication in several places, including
  ``riscv_copy_subset_list`` in ``bfd/elfxx-riscv.c`` and ``riscv_set_arch`` in ``gas/config/tc-riscv.c``.
  The patch replaces ``strdup()`` with ``xstrdup()``, which is expected to handle
  memory allocation failures more gracefully.  The callers of these functions do not
  explicitly check the return value of strdup for NULL.
primer_general: In C, ``strdup()`` is a function that duplicates a string by allocating
  memory and copying the string into the new memory. If memory allocation fails, ``strdup()``
  returns NULL, and the program should check for this. However, if the program doesn't
  check, it can crash. This patch replaces ``strdup()`` with ``xstrdup()``, which
  automatically handles the case where memory allocation fails, preventing potential
  crashes.
series_id: 'binutils:risc-v: avoid strdup()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/eafb3dd1-bd0c-4713-9bc0-af2978fdfe62@iscas.ac.cn
bugzilla_url: null
date: '2026-04-29'
---

This patch replaces instances of ``strdup()`` with ``xstrdup()`` in the RISC-V backend. ``xstrdup()`` is a safer version of ``strdup()`` that handles memory allocation failures by calling ``xmalloc()``, ensuring the program exits if memory allocation fails. This change improves the robustness of the code by preventing potential crashes due to out-of-memory conditions.
