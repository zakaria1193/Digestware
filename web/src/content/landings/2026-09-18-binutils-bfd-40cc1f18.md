---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- riscv
- linker
- revert
commit_hash: 40cc1f18815d7554a954a9eb2288099451d83b7d
source_type: public_inbox
author: '"H.J. Lu" <hjl@sourceware.org>'
headline: 'RISC-V: Revert undefined symbol value adjustment'
tldr: Reverts a change that adjusted undefined symbol values based on pointer equality
  needs.
impact_score: 3
performance_win: false
breaking_change: true
outcome: committed
primer_expert: This commit reverts a fix in `bfd/elfnn-riscv.c` that conditionally
  set `sym->st_value = 0` based on `!h->ref_regular_nonweak || !h->pointer_equality_needed`.
  The original change was intended to fix a FAIL in `riscv_elf_finish_dynamic_symbol`
  related to undefined symbols. However, subsequent changes made this failure an XFAIL,
  and this revert restores the previous behavior, likely because the original fix
  is no longer necessary or has unintended side effects.
primer_glossary:
- term: undefined symbol
  definition: A symbol that is declared in one object file but not defined, meaning
    its actual memory address or value is not known until link time or runtime.
- term: pointer equality
  definition: A property that determines whether two pointers to the same object must
    be equal, even if they are derived differently. This is relevant for symbol resolution
    and dynamic linking.
- term: PLT
  definition: Procedure Linkage Table. A table in an executable or shared library
    used to indirectly call functions in shared libraries.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260918101746.8C7F54BA798B@sourceware.org
date: '2026-09-18'
is_stub: true
stub_reason: low_score
---

This commit reverts a change made in May that set the value of undefined symbols to 0 if pointer equality was not needed for RISC-V targets. The original fix addressed a testcase FAIL, but a subsequent change reclassified that failure as an XFAIL. This revert removes the adjustment, potentially restoring previous behavior regarding undefined symbol values.
