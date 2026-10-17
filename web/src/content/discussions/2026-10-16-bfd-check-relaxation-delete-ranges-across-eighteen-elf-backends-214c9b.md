---
project: binutils
subsystem: bfd
patch_id: null
tags:
- linker
- ELF
- relaxation
- security
- testing
discussion_id: CAOX--DSCQqnycWV_yh1a1MePU2Mkxh6s9uiTccuAgzc0iNyGEg@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] bfd: check relaxation delete ranges across eighteen ELF backends'
headline: 'bfd: check relaxation delete ranges across eighteen ELF backends'
tldr: Discussion about a patch series (v2) that hardens ELF in-place relaxation against
  size underflow by adding checks and tests.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: needs_revision
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Enhances security and stability by preventing potential buffer overflows caused
  by malformed input.
- Increases code complexity by adding a new helper function and validation logic.
- Requires extensive testing across multiple ELF backends to ensure correctness.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Announces a superseding v2 patch series for ELF relaxation hardening and
    requests review of the new series.
  quote: 'This v1 is superseded by the 8-patch v2 series, posted today:


    [PATCH v2 0/8] bfd: harden in-place relaxation byte deletion against

    size underflow

    https://patchwork.sourceware.org/project/binutils/list/?series=67993


    v2 splits the single patch by subsystem, adds a shared helper

    (_bfd_elf_relax_delete_range_ok), propagates failures in the callers

    that ignored them (AVR, M68HC11, RX, RL78, RISC-V),…'
primer_expert: This discussion concerns a patch series aimed at improving the robustness
  of the ELF linker's relaxation mechanism within Binutils' BFD library. Relaxation
  involves adjusting code or data addresses at link time. The patch series addresses
  a potential integer underflow vulnerability in backends that perform in-place byte
  deletion during relaxation. This underflow could lead to out-of-bounds memory operations
  if the input object contains malformed relocation data. The solution introduces
  a shared helper function `_bfd_elf_relax_delete_range_ok` to validate deletion ranges
  across multiple ELF ba…
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by GNU Binutils
    to provide a common interface for reading and writing various object file formats.
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: linker relaxation
  definition: A process in linkers where certain instructions or data are temporarily
    placed at arbitrary addresses and then later adjusted (relaxed) to their final,
    optimal positions. This is often used for optimizing code size or adapting to
    specific processor constraints.
- term: in-place byte deletion
  definition: A technique used in linker relaxation where bytes representing deleted
    code or data are removed by shifting subsequent bytes forward within the same
    memory buffer.
- term: size underflow
  definition: An arithmetic operation where a value is subtracted from a smaller value,
    causing the result to wrap around to a very large positive number due to integer
    representation limits.
- term: DejaGnu
  definition: A testing framework for software development, commonly used to test
    GNU software.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAOX--DSCQqnycWV_yh1a1MePU2Mkxh6s9uiTccuAgzc0iNyGEg@mail.gmail.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

Harshit Kumar announces that the submitted patch v1 is superseded by an 8-patch v2 series. The v2 series aims to harden ELF in-place relaxation byte deletion by preventing size underflow. It introduces a shared helper function, propagates failures in callers that previously ignored them, and adds DejaGnu tests for multiple targets. Kumar requests that reviewers focus on the v2 series instead of v1.
