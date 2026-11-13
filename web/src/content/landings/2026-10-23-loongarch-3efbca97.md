---
project: gcc
subsystem: loongarch
patch_id: null
tags:
- loongarch
- optimization
- RTL
- bugfix
commit_hash: 3efbca97ffe4bf5fb5dd481af524c0bc2227c39a
source_type: github
author: Xi Ruoyao
headline: 'LoongArch: Fix missed optimization for bitwise OR with shift and extend'
tldr: Corrects `bstrins_w_for_ior_ashift_and_extend` optimization by rewriting the
  pattern.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'This patch addresses a failure in `gcc.target/loongarch/bstrins-5.c`
  related to the `bstrins_w_for_ior_ashift_and_extend` optimization. The issue stems
  from two related problems: first, the target-independent optimizer''s preference
  for `plus` over `ior`, which changes the pattern''s recognizability; and second,
  the inability of `sign_extend` to be lowered through `plus` and associate with a
  `subreg` to form a `sign_extract`. The solution involves rewriting the optimization
  pattern in `config/loongarch/loongarch.md` as a `define_insn` rather than a split
  operation. This new definition adapts th…'
primer_glossary:
- term: LoongArch
  definition: An open-source RISC-based instruction set architecture (ISA) developed
    by Loongson Technology, primarily for high-performance computing and embedded
    systems.
- term: define_insn
  definition: A macro in GCC's machine description files (`.md`) used to define a
    specific machine instruction pattern, its operands, and constraints.
- term: RTL (Register Transfer Language)
  definition: An intermediate representation used in GCC that describes operations
    on registers and memory. It's a low-level language that is close to machine code
    but is still target-independent to some extent.
- term: sign_extend
  definition: An operation that extends a smaller integer type to a larger one by
    replicating the most significant bit (the sign bit). This preserves the value's
    sign.
- term: subreg
  definition: A part of a larger register that is treated as a separate operand. For
    example, the lower 32 bits of a 64-bit register might be accessed as a subreg.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3efbca97ffe4bf5fb5dd481af524c0bc2227c39a
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

An optimization for `bstrins_w_for_ior_ashift_and_extend` on LoongArch was failing due to the target-independent code preferring `plus` over `ior`. Additionally, `sign_extend` could not be lowered through `plus`, affecting semantics. This commit rewrites the pattern as a `define_insn` instead of splitting it, adapts it for the `ior` to `plus` optimization, uses a '0' constraint, and removes redundant conditions, fixing a test failure in `bstrins-5.c`.
