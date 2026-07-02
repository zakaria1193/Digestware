---
project: gcc
subsystem: aarch64
patch_id: null
tags:
- aarch64
- neon
- intrinsics
- compiler
commit_hash: efbc7fbb70d875ec1ff628f0e4b3bcfc80bcb9e6
source_type: github
author: Karl Meakin
headline: aarch64 NEON add intrinsics ported to pragma-based framework
tldr: Ported NEON vadd intrinsics to a new pragma-based definition framework in GCC.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The aarch64 backend's intrinsic definition mechanism is being refactored
  to use a pragma-based framework, similar to how other targets define builtins. This
  commit introduces new .cc, .h, and .def files (e.g., `aarch64-neon-builtins-base.*`,
  `aarch64-neon-builtins-shapes.*`) to define NEON intrinsics. The `vadd` family is
  ported first, likely to simplify future intrinsic additions and ensure the new framework
  correctly handles SIMD operations within the GCC compiler infrastructure.
primer_general: GCC supports specialized functions called intrinsics that allow C/C++
  code to directly use processor instructions. For the ARM architecture's NEON SIMD
  (Single Instruction, Multiple Data) unit, these intrinsics are crucial for high-performance
  multimedia and signal processing. This change moves the definition of these NEON
  intrinsics, specifically the `vadd` (vector add) operations, to a new, more generalized
  framework within GCC. This framework uses pragmas, a preprocessor directive, to
  define the intrinsics, making the process more standardized and easier to maintain
  across different ARM features.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/efbc7fbb70d875ec1ff628f0e4b3bcfc80bcb9e6
date: '2026-02-20'
is_stub: false
stub_reason: ''
---

GCC's aarch64 backend now defines NEON intrinsics using a pragma-based framework. This change introduces the necessary infrastructure and ports the `vadd` family of functions as a demonstration. This refactoring aims to streamline the definition and management of NEON intrinsics.
