---
project: binutils
subsystem: rx
patch_id: null
tags:
- linker
- relaxation
- rx
- error handling
- regression testing
discussion_id: 20261016123644.1429854-6-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 5/8] rx: check relaxation delete range, propagate failures'
headline: 'rx: check relaxation delete range, propagate failures'
tldr: Harden RX linker relaxation by validating deletion ranges and propagating errors.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves robustness by preventing out-of-bounds memory access during relaxation.
- Adds test coverage for underflow conditions.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Validates deletion ranges in RX relaxation, propagates failures, and adds
    a regression test.
  quote: 'Validate deletion range in elf32_rx_relax_delete_bytes using

    _bfd_elf_relax_delete_range_ok and drop redundant BFD_ASSERT.  Wrap

    SNIPNR and SNIP macros in do-while(0) blocks.  Propagate deletion return

    status in elf32_rx_relax_section and branch to error_return on error.

    Add DejaGnu regression test ld-rx/rx-relax-underflow.exp.'
primer_expert: This patch modifies the linker relaxation code for the RX architecture,
  specifically in `bfd/elf32-rx.c`. It introduces checks using `_bfd_elf_relax_delete_range_ok`
  to ensure that byte deletion operations during relaxation do not go out of bounds.
  Failures from these checks are now propagated correctly, and a new regression test
  is added to catch underflow conditions.
primer_glossary:
- term: linker relaxation
  definition: A linker optimization process that adjusts instruction addresses and
    sizes at link time to improve code density or enable features like position-independent
    code. It may involve deleting or replacing instructions.
- term: RX
  definition: Renesas RX microcontrollers, a series of 32-bit embedded processors
    for which the GNU toolchain provides support.
- term: DejaGnu
  definition: A testing framework for regression testing of software, often used for
    compilers and other complex software systems.
- term: underflow
  definition: In the context of memory or arithmetic operations, underflow occurs
    when a value becomes smaller than the minimum representable value. For unsigned
    integers, this typically results in wrap-around to a very large positive number.
series_id: 'binutils:rx: check relaxation delete range, propagate failures'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016123644.1429854-6-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch enhances linker relaxation for the RX architecture by validating deletion ranges in `elf32_rx_relax_delete_bytes` using `_bfd_elf_relax_delete_range_ok`. It also propagates any deletion failures in `elf32_rx_relax_section` to the error handling path. A new DejaGnu test case, `ld-rx/rx-relax-underflow.exp`, is added to cover these scenarios. The patch notes that some out-of-range relocation issues might still cause faults before deletion.
