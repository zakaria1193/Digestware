---
project: gcc
subsystem: gcc/emit-rtl
patch_id: null
tags:
- gcc
- rtl
- codegen
- csky
commit_hash: a25bea7d0b905e54986db218024e854fe1e24c91
source_type: github
author: Trevor Saunders
headline: emit-rtl.cc uses rtx_insn* for setting register notes
tldr: Functions in emit-rtl.cc now use rtx_insn* for setting register notes, improving
  instruction context.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Functions in emit-rtl.cc, such as set_for_reg_notes and its variants,
  are refactored to accept rtx_insn*. This allows register notes to be directly associated
  with the specific instruction being emitted, rather than relying on a broader context.
  This change, also reflected in csky.cc, streamlines the process of annotating instructions
  with register usage information.
primer_glossary:
- term: rtx_insn*
  definition: A pointer to an rtx_insn structure, which represents a machine instruction
    in GCC's intermediate representation (RTL).
- term: emit-rtl.cc
  definition: GCC source file containing functions related to emitting and manipulating
    RTL code, which is an intermediate representation used during compilation.
- term: Register Notes
  definition: Metadata attached to RTL instructions that provide additional information
    about register usage, constraints, or properties.
- term: csky.cc
  definition: GCC source file containing code specific to the C-Sky architecture.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/a25bea7d0b905e54986db218024e854fe1e24c91
date: '2026-10-14'
is_stub: true
stub_reason: low_score
---

This commit updates several functions in emit-rtl.cc and related headers to accept rtx_insn* for setting register notes. Functions like set_for_reg_notes, set_unique_reg_note, and set_dst_reg_note now operate directly on the instruction, enhancing the precision of how register-related information is attached to specific emitted instructions. This also includes a change in csky.cc for emitting instructions.
