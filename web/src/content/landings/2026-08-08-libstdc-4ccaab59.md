---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- SFINAE
- Darwin
- testing
commit_hash: 4ccaab59f55c622c8befa284fb3c291669c445d8
source_type: github
author: Iain Sandoe
headline: 'libstdc++: Arrange for non-constant math_errhandling to SFINAE [PR126807]'
tldr: libstdc++ now correctly uses SFINAE for non-constant math_errhandling macro
  on Darwin, fixing build failures.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: PR126807 highlighted that several SIMD testcases in libstdc++ fail
  to build on Darwin due to the `math_errhandling` macro being used in a non-dependent
  `requires` clause. On Darwin, `math_errhandling` is a macro that expands to a function
  call, not a compile-time constant. This prevents SFINAE from working as expected.
  This commit modifies `simd_details.h` to define `math_errhandling` as a default
  template argument, ensuring that template substitutions involving it are handled
  correctly by SFINAE, thus resolving the build failures.
primer_glossary:
- term: libstdc++
  definition: The C++ standard library implementation used by GCC. It provides fundamental
    C++ functionalities like containers, algorithms, and I/O streams.
- term: SFINAE
  definition: Substitution Failure Is Not An Error. A C++ template metaprogramming
    technique where a failing template substitution is treated as a valid overload
    resolution path, allowing for compile-time selection of functions or classes based
    on type properties.
- term: math_errhandling
  definition: A C macro defined in `<math.h>` that indicates support for, and the
    manner of, reporting math errors. Its value can vary between implementations.
- term: Darwin
  definition: The name of Apple's Unix-like operating system, serving as the foundation
    for macOS, iOS, and other Apple platforms. GCC builds for these platforms use
    Darwin-specific configurations.
- term: SIMD
  definition: Single Instruction, Multiple Data. A type of parallel processing where
    a single instruction operates on multiple data points simultaneously. Libraries
    often provide SIMD intrinsics or vectorized operations.
- term: macro
  definition: A piece of code in a program that is replaced by a value or block of
    code before compilation. Macros are typically used for conditional compilation
    or defining constants.
- term: default template argument
  definition: In C++, a fallback value provided for a template parameter if no explicit
    argument is supplied when the template is instantiated. This can be used to control
    template behavior.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4ccaab59f55c622c8befa284fb3c291669c445d8
date: '2026-08-08'
is_stub: false
stub_reason: ''
---

This change addresses build failures in libstdc++'s SIMD testcases on Darwin, where the `math_errhandling` macro resolves to a function rather than a constant. Previously, this caused issues because the macro was not substituted correctly in dependent clauses. By using the macro as a default template argument, the code now correctly employs SFINAE, allowing the affected testcases to build successfully.
