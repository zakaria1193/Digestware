---
project: binutils
subsystem: avr
patch_id: null
tags:
- linker
- relaxation
- avr
- error handling
discussion_id: 20261016123644.1429854-4-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH v2 3/8] avr: check relaxation delete range and propagate failure'
headline: 'avr: check relaxation delete range and propagate failure'
tldr: AVR linker relaxation now validates deletion ranges and propagates errors.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves robustness of AVR linker relaxation by preventing out-of-bounds operations.
- Enhances error reporting and handling.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Adds range validation and error propagation to AVR relaxation delete operations.
  quote: 'Validate deletion range in elf32_avr_relax_delete_bytes using

    _bfd_elf_relax_delete_range_ok.  Propagate failure returns in

    elf32_avr_relax_section and branch to error_return on error.'
primer_expert: This patch modifies the linker relaxation code for the AVR architecture,
  specifically in `bfd/elf32-avr.c`. It integrates the `_bfd_elf_relax_delete_range_ok`
  function to validate the parameters for `elf32_avr_relax_delete_bytes` before performing
  memory operations. Crucially, it ensures that any failure reported by this validation
  is propagated up to `elf32_avr_relax_section` and handled by the `error_return`
  path, preventing potential heap corruption.
primer_glossary:
- term: linker relaxation
  definition: A linker optimization process that adjusts instruction addresses and
    sizes at link time to improve code density or enable features like position-independent
    code. It may involve deleting or replacing instructions.
- term: AVR
  definition: A family of microcontrollers developed by Atmel (now Microchip Technology),
    widely used in embedded systems. The GNU toolchain supports AVR targets.
- term: error propagation
  definition: The process of passing an error status from a lower-level function or
    module to a higher-level one, allowing the program to handle the error appropriately.
series_id: 'binutils:avr: check relaxation delete range and propagate failure'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261016123644.1429854-4-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch strengthens the AVR ELF relaxation process by validating deletion ranges within `elf32_avr_relax_delete_bytes` using the `_bfd_elf_relax_delete_range_ok` helper. It ensures that any failure during the byte deletion is properly propagated in `elf32_avr_relax_section`, directing execution to the error return path. This change enhances the robustness of the AVR linker.
