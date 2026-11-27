---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- tls
- relocation
discussion_id: 20261127044839.1321551-1-Shivam98.tkg@gmail.com
source_type: public_inbox
title: '[PATCH] RISC-V: Don''t partially relax TLS LE address sequences [PR ld/34957]'
headline: 'RISC-V: Don''t partially relax TLS LE address sequences'
tldr: Fixes RISC-V linker bug where incorrect relaxation of TLS LE address sequences
  could lead to incorrect program behavior.
proposer: Shivam Gupta <shivam98.tkg@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds a new check function (`riscv_tls_le_has_unrelaxable_lo`) to `elfnn-riscv.c`
  to determine if a TLS LE relocation consumer is relaxable.
- Modifies `_bfd_riscv_relax_section` to incorporate the new check before relaxing
  specific TPREL relocation types.
- Introduces new test cases (`tlsle-partial-relax.s` and `tlsle-partial-relax.d`)
  to verify the fix.
exchanges:
- author: Shivam Gupta
  role: proposer
  position: Submits a patch to prevent the linker from incorrectly relaxing TLS LE
    address sequences on RISC-V architectures, fixing a bug where instruction deletion
    could lead to incorrect program behavior.
  quote: 'When R_RISCV_TPREL_HI20 / R_RISCV_TPREL_ADD are marked with

    R_RISCV_RELAX but a R_RISCV_TPREL_LO12_I/S for the same symbol and

    addend is not, ld deleted the lui/add while leaving the consumer using

    its original base register, reviving a dead incoming value.


    Only delete the producers when every TPREL_LO12 consumer of the same

    symbol+addend in the section is itself relaxable.'
primer_expert: This patch for the RISC-V GNU ld linker corrects a bug in TLS LE (Local
  Exec) relaxation. The relaxation process can remove `lui` and `add` instructions
  that establish a base register for accessing TLS variables. The bug occurs when
  a `R_RISCV_TPREL_HI20` or `R_RISCV_TPREL_ADD` relocation is marked relaxable, but
  its corresponding `R_RISCV_TPREL_LO12_I` or `R_RISCV_TPREL_LO12_S` consumer is not.
  The linker would incorrectly remove the producer instructions, leaving the consumer
  to use a stale register value, thus breaking TLS access. The fix adds a check to
  ensure all consumers of the base re…
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261127044839.1321551-1-Shivam98.tkg@gmail.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

This patch addresses a bug in the RISC-V linker (ld) related to Thread-Local Storage (TLS) LE address sequences. When certain relocation types (R_RISCV_TPREL_HI20/ADD) are marked for relaxation, but their corresponding R_RISCV_TPREL_LO12_I/S consumers are not, the linker incorrectly deletes instructions. This can revive a dead incoming value, leading to program errors. The fix ensures that such producer instructions are only deleted if all their LO12 consumers are also relaxable.
