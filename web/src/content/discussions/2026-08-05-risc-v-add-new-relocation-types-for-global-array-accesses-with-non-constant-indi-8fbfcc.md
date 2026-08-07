---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- relocations
- compiler
discussion_id: e202ce18-cb7c-48f8-98ff-33946506e754@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH v5] RISC-V: Add new relocation types for global array accesses
  with non-constant indices'
headline: 'RISC-V: Add new relocation types for global array accesses with non-constant
  indices'
tldr: A patch adds new RISC-V relocation types to support efficient global array access
  with non-constant indices.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Enables more efficient code generation for a specific access pattern at the cost
  of introducing new relocation types and complexity in the toolchain.
- Requires careful management of internal vs. emitted relocation types and adherence
  to ABI specifications.
exchanges:
- author: Liqin Weng <liqin.weng@spacemit.com>
  role: proposer
  position: Submits a patch introducing new RISC-V relocation types for efficient
    global array access with non-constant indices.
  quote: null
- author: Jiawei <jiawei@iscas.ac.cn>
  role: reviewer
  position: Approves the patch overall but requests the addition of a function declaration
    to elfxx-riscv.h and minor cleanup of TODOs and comment formatting.
  quote: null
primer_expert: This patch enhances the RISC-V backend in binutils by introducing new
  relocation types. These are designed to optimize how the compiler handles accesses
  to global arrays when the index is determined at runtime rather than compile time.
  This involves changes to how relocations are represented and processed, particularly
  concerning relaxation and the mapping of internal to emitted relocation types.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/e202ce18-cb7c-48f8-98ff-33946506e754@iscas.ac.cn
bugzilla_url: null
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

Liqin Weng's patch introduces new RISC-V relocation types (R_RISCV_BASE_IDX_*) to facilitate more efficient code generation for global array accesses where the array subscript is not a constant. The changes span BFD, gas, and ld, including new relocation definitions and support for internal relaxed relocation types. Jiawei reviewed the patch, approving it with minor requests for header declarations, TODO removal, and GNU comment formatting.
