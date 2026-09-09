---
project: gcc
subsystem: gcc/config/microblaze
patch_id: null
tags:
- rtems
- microblaze
- build system
commit_hash: 271186ef46437bb60e9143d8519a3ed71c54481c
source_type: github
author: Joel Sherrill
headline: 'microblaze/rtems.h: Define __USE_INIT_FINI__ for RTEMS'
tldr: RTEMS requires __USE_INIT_FINI__ to be defined on MicroBlaze for correct global
  constructor execution.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: For the MicroBlaze architecture, the RTEMS BSP requires `__USE_INIT_FINI__`
  to be defined. This macro controls the selection of initialization routines, specifically
  influencing how global constructors (functions like static object constructors in
  C++ or functions registered with `__attribute__((constructor))`) are executed at
  program startup within the RTEMS environment.
primer_glossary:
- term: RTEMS
  definition: Real-Time Executive for Multiprocessor Systems. An open-source real-time
    operating system designed for embedded systems.
- term: MicroBlaze
  definition: A soft processor core from Xilinx, implemented in an FPGA. It is a popular
    choice for embedded systems development.
- term: __USE_INIT_FINI__
  definition: A preprocessor macro used in some C library implementations (like glibc)
    to control the inclusion of initialization and finalization routines (e.g., constructors
    and destructors) at program startup and termination.
- term: Global Constructors
  definition: Functions that are automatically executed before the main() function
    in a C++ program, used for initializing global or static objects.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/271186ef46437bb60e9143d8519a3ed71c54481c
date: '2026-09-04'
is_stub: true
stub_reason: low_score
---

The header file `gcc/config/microblaze/rtems.h` has been updated to define the `__USE_INIT_FINI__` macro. This macro is necessary for the RTEMS operating system to select the appropriate procedure for executing global constructors when compiling for the MicroBlaze architecture. Without this definition, the correct mechanism for initializing global variables might not be invoked.
