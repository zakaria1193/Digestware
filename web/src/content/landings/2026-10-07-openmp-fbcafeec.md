---
project: gcc
subsystem: openmp
patch_id: null
tags:
- openmp
- vectorization
- aarch64
- risc-v
- optimization
commit_hash: fbcafeec06a66175108be68c34aceafba7a453b9
source_type: github
author: Tobias Burnus
headline: Add 'scaled' modifier to OpenMP 'simdlen' clause
tldr: Supports OpenMP 6.1's 'scaled' modifier for simdlen clause to better target
  vectorization on modern architectures.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'This commit introduces support for the `simdlen( scaled(arith-type
  [, divisor]) : length )` syntax in OpenMP pragmas, originating from OpenMP TR14
  (OpenMP 6.1). The `scaled` modifier allows for a runtime-dependent calculation of
  the vector length, where `length` is the desired SIMD length and `divisor` (optional,
  defaults to 1) is used to calculate the effective vector width based on `VL(type)`.
  This is primarily to handle advanced SIMD vectorization capabilities on targets
  like AArch64 and RISC-V. The implementation involves changes in `attribs.cc`, `omp-general.cc`,
  `gimplify.cc`, and `omp-…'
primer_glossary:
- term: OpenMP
  definition: An API that supports multi-platform shared-memory parallel programming
    in C, C++, and Fortran, primarily used for shared-memory multiprocessing.
- term: simdlen clause
  definition: An OpenMP clause used to specify the desired SIMD vector length for
    loop iterations, influencing how instructions are vectorized.
- term: scaled modifier
  definition: A new modifier for the `simdlen` clause in OpenMP 6.1 that allows the
    vector length to be calculated dynamically based on a type and an optional divisor,
    providing more flexibility for vectorization on diverse hardware.
- term: Vector Length (VL)
  definition: The size of a vector register on a specific processor architecture,
    determining how many data elements can be processed in parallel by a single SIMD
    instruction.
- term: AArch64
  definition: The 64-bit ARM architecture, which includes advanced SIMD (NEON) extensions.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer principles, which can also include vector extensions.
- term: Gimplification
  definition: A compiler pass that converts C/C++ constructs into GCC's internal representation
    (GIMPLE), which is a simpler, three-address-like form suitable for optimizations.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/fbcafeec06a66175108be68c34aceafba7a453b9
date: '2026-10-07'
is_stub: false
stub_reason: ''
---

Support for the OpenMP 6.1 `scaled` modifier in the `simdlen` clause has been added to GCC. This feature allows specifying a scaling factor for vector lengths, crucial for modern architectures like AArch64 and RISC-V that have more complex vectorization capabilities. The `scaled` modifier enables `simdlen(scaled(type [, divisor]) : length)` syntax, providing finer control over vectorization length based on target architecture specifics and runtime information.
