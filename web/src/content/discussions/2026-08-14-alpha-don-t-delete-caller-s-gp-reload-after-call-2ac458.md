---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- optimization
- GP
- bug fix
discussion_id: 20260814192712.1016834-1-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH] alpha: don''t delete a caller''s gp reload after a call'
headline: 'alpha: Don''t delete caller''s gp reload after call'
tldr: Fixes a bug in Alpha relaxation where deleting a GP reload after a call can
  lead to incorrect GP values and crashes, especially in multi-sub-GOT scenarios.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Ensuring correct program behavior and preventing crashes by retaining GP reloads
  vs. a potential (though minimal in this case) code size increase by not optimizing
  away instructions that were previously deemed redundant.
exchanges:
- author: Matt Turner
  role: proposer
  position: Identified and proposed a fix for an Alpha relaxation optimization that
    incorrectly removes GP reload instructions, causing issues with GP value consistency
    after function calls.
  quote: "elf64_alpha_relax_with_lituse turns\n\n    ldq  t12,lit(gp)          bsr\
    \  ra,callee+8\n    jsr  ra,(t12)       ==>   unop\n    ldah gp,hi(ra)       \
    \     unop\n    lda  gp,lo(gp)\n\nwhenever elf64_alpha_relax_opt_call returns\
    \ a non-zero destination, i.e.\nwhen the callee starts with our gp (or is marked\
    \ NOPV).  That justifies\nentering the callee past its own ldgp, since the ldgp\
    \ would recompute the\ngp we…"
primer_expert: This patch addresses an incorrect optimization in the Alpha linker's
  relaxation pass (`elf64_alpha_relax_with_lituse`). The pass incorrectly rewrites
  a GP (Global Pointer) reload sequence into no-ops when a `jsr` (jump to subroutine)
  is encountered and the callee meets certain conditions (e.g., shares the caller's
  GP). However, $gp is caller-saved, and the callee is not obligated to preserve it.
  This optimization breaks when the callee performs a tail call, especially into a
  different sub-GOT, leaving the caller with an incorrect GP. This can lead to crashes
  when `disp(gp)` instructions acces…
primer_glossary:
- term: GP
  definition: Global Pointer, a dedicated register used in some architectures (like
    Alpha) to access global variables and constants efficiently.
- term: relaxation
  definition: A linker optimization technique where relocations are resolved at link-time
    rather than runtime, potentially allowing for more compact or efficient code,
    especially in architectures like Alpha.
- term: caller-saved
  definition: Registers that a calling function must preserve if it uses them; the
    called function (callee) is not responsible for saving or restoring them.
- term: tail call
  definition: A function call that is the very last operation in a function, allowing
    it to be optimized by the compiler or linker to reuse the existing stack frame.
- term: sub-GOT
  definition: Within a larger Global Offset Table, sub-GOTs are smaller, independently
    managed sections that can improve performance or manage address space limitations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260814192712.1016834-1-mattst88@gmail.com
bugzilla_url: null
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This patch corrects an optimization in the Alpha linker's relaxation process that incorrectly deleted a GP reload instruction. The optimization was applied when a function call was followed by specific instructions, assuming the callee would preserve the caller's GP. However, this assumption fails in cases involving tail calls or when the callee resides in a different GOT subsection, leading to the caller resuming with an incorrect GP. This can cause runtime crashes, particularly when indirect calls jump through corrupted GOT entries. The patch retains the GP reload instruction to ensure correct GP values are maintained.
