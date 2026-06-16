---
project: gcc
subsystem: gcc/risc-v
patch_id: null
tags:
- risc-v
- multilib
- toolchain
- configuration
commit_hash: 6dbcda7f978ce7fba81e81971911d00b2d1ccab0
source_type: github
author: Jim Tsung-Chun Lin
headline: RISC-V multilib matching bypasses generic selection for accuracy
tldr: RISC-V multilib selection now always runs a smart, score-based matching algorithm
  instead of deferring to a generic textual match, ensuring the most compatible…
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: GCC's multilib system allows a single compiler installation to target
  multiple architecture variants (e.g., different instruction sets or ABIs). For RISC-V,
  the generic `set_multilib_dir` matcher in `gcc.cc` can fail to fully understand
  the intricate superset relationships of RISC-V architecture extensions, sometimes
  leading to an suboptimal multilib selection when command-line options like `-march`
  are used. This commit modifies `riscv_common.cc`, specifically the `riscv_compute_multilib`
  function, by dropping an early-return check. Now, the `match-score-based` selection
  runs unconditionally…
primer_general: 'When you compile code, a compiler like GCC might need to support
  different versions of the same computer architecture – for example, a basic RISC-V
  processor versus one with special extensions. This is handled by a "multilib" system,
  where the compiler has multiple libraries and configurations pre-built for these
  different variants. Previously, GCC''s RISC-V compiler would sometimes pick the
  wrong set of libraries if the user specified a complex architecture (like one with
  many extensions), because it relied on a simple text-based match. This meant your
  program might link against libraries that weren’t quite right for your specific
  processor. This change makes the compiler smarter: it now *always* runs a sophisticated
  algorithm to find the *best* matching multilib, even if a simple match has already
  been found. This prevents incorrect library choices and ensures that the compiled
  program is always linked against the most appropriate and compatible libraries for
  the target RISC-V proces…'
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6dbcda7f978ce7fba81e81971911d00b2d1ccab0
date: '2026-06-03'
is_stub: false
---

The RISC-V GCC compiler now consistently uses its smart multilib matching algorithm to select the optimal multilib, even if a generic matcher has already made a selection. Previously, the system could incorrectly choose a multilib based on a textual match, leading to incompatible linking against default-arch libraries. This change removes the early-return condition in `riscv_compute_multilib`, guaranteeing the most accurate multilib is used when building applications for RISC-V, particularly with complex feature sets like those for architecture extensions.
