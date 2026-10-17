---
project: binutils
subsystem: m68hc11
patch_id: null
tags:
- linker
- relaxation
- m68hc11
- error handling
discussion_id: 20261016123644.1429854-5-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 4/8] m68hc11: return bool from relax delete helpers'
headline: 'm68hc11: return bool from relax delete helpers'
tldr: M68HC11 linker relaxation now returns bool for delete helpers and propagates
  failures.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Enhances error detection and propagation in M68HC11 relaxation.
- Moves towards a more consistent error handling pattern across backends.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Modifies M68HC11 relaxation helpers to return boolean status and propagate
    errors.
  quote: 'Convert m68hc11_elf_relax_delete_bytes and m68hc11_relax_group to

    return bool.  Validate deletion range with _bfd_elf_relax_delete_range_ok

    and propagate deletion failures in m68hc11_elf_relax_section.'
primer_expert: This change modifies the linker relaxation mechanism for the M68HC11
  architecture within `bfd/elf32-m68hc11.c`. The functions responsible for deleting
  bytes (`m68hc11_elf_relax_delete_bytes`, `m68hc11_relax_group`) are updated to return
  a `bool` status. This allows `m68hc11_elf_relax_section` to properly detect and
  handle errors during deletion, incorporating checks from the new `_bfd_elf_relax_delete_range_ok`
  helper.
primer_glossary:
- term: linker relaxation
  definition: A linker optimization process that adjusts instruction addresses and
    sizes at link time to improve code density or enable features like position-independent
    code. It may involve deleting or replacing instructions.
- term: M68HC11
  definition: A member of the Motorola 68HC11 family of microcontrollers, for which
    the GNU toolchain provides support.
- term: boolean
  definition: A data type that can have only one of two values, typically true or
    false. Used here to indicate success or failure of an operation.
series_id: 'binutils:m68hc11: return bool from relax delete helpers'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016123644.1429854-5-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch updates the M68HC11 ELF relaxation functions, `m68hc11_elf_relax_delete_bytes` and `m68hc11_relax_group`, to return boolean values indicating success or failure. It integrates `_bfd_elf_relax_delete_range_ok` to validate deletion ranges and ensures that any deletion failures are propagated correctly within `m68hc11_elf_relax_section`.
