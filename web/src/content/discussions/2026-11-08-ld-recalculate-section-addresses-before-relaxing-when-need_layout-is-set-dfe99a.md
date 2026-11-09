---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- linker
- RISC-V
- relocation
- relaxation
discussion_id: 20261108133319.2719608-1-xeonacid@archlinuxcn.org
source_type: public_inbox
title: '[PATCH] ld: Recalculate section addresses before relaxing when need_layout
  is set [PR34979]'
headline: 'ld: Recalculate section addresses before relaxing when need_layout is set'
tldr: Patch recalculates section addresses before relaxation to fix RISC-V relocation
  errors caused by stale VMAs.
proposer: Zhuo Zhi <xeonacid@archlinuxcn.org>
consensus: Under Review
outcome: under_review
impact_score: 6
sentiment_score: 5
technical_tradeoffs:
- Introducing an extra pass to recalculate section addresses might increase link time
  for some targets, but it resolves critical relocation errors on RISC-V.
- The proposed solution might be RISC-V specific, and its applicability or benefit
  to other architectures is questioned.
exchanges:
- author: Zhuo Zhi
  role: proposer
  position: Proposes recalculating section addresses before relaxation when `need_layout`
    is true to fix RISC-V relocation errors.
  quote: 'Recalculate section addresses prior to the relaxation loop when

    need_layout is set so that all output sections start relaxation with

    consistent VMAs.'
- author: Kito Cheng
  role: reviewer
  position: Requests a test case to be added to the patch.
  quote: Could you add test case to the patch?
- author: Alan Modra
  role: reviewer
  position: Questions the necessity of an extra sizing pass for other targets and
    suggests an alternative approach if the fix is RISC-V specific.
  quote: 'I would need to be convinced that an extra sizing pass is of benefit

    to other targets.  If you really need to do this for riscv then I

    think it should be done by  increasing link_info.relax_pass, then not

    doing anything on pass 0.'
primer_expert: This patch in the GNU linker (ld) aims to resolve a RISC-V specific
  relocation error (R_RISCV_JAL overflow) that occurs when section addresses are not
  properly updated before relaxation. The issue arises when `need_layout` flag is
  set, indicating that section placement might change. The linker's relaxation process
  uses section VMAs to calculate offsets for PC-relative branches. If these VMAs are
  stale (from before `elf_ldlang_before_allocation` updates), the calculated distance
  can exceed the instruction's range. The fix ensures VMAs are recalculated via `lang_size_sections_1`
  before entering…
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: relaxation
  definition: A linker optimization process where initial address assignments are
    refined to allow for more compact code, particularly for PC-relative branches
    and symbol resolution.
- term: need_layout
  definition: A flag within the linker that indicates whether the layout of sections
    (their addresses and sizes) needs to be re-evaluated and potentially adjusted.
- term: VMA
  definition: Virtual Memory Address, the address at which a program's memory is expected
    to be loaded and run.
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is modular and
    extensible.
- term: R_RISCV_JAL
  definition: A relocation type specific to RISC-V architecture, used for JAL (Jump
    and Link) instructions, indicating the target address for a relative jump.
series_id: 20261108133319.2719608-1-xeonacid@archlinuxcn.org
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261108133319.2719608-1-xeonacid@archlinuxcn.org
bugzilla_url: null
date: '2026-11-08'
is_stub: false
stub_reason: ''
---

This patch addresses a relocation error on RISC-V by ensuring section addresses are consistently recalculated before the relaxation process begins. When `need_layout` is set (due to changes in .eh_frame or segment headers), previous relaxation passes used stale section VMAs. This led to incorrect distance calculations for instructions like `auipc+jalr`, causing relocation truncation. The fix recalculates addresses upfront so all sections start relaxation with accurate VMAs, preventing the issue.
