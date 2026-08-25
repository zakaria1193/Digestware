---
project: gcc
subsystem: risc-v
patch_id: null
tags:
- risc-v
- build
- bugfix
commit_hash: 4bdedfd9bdf9a6c79ecee844459a7f284b33baf6
source_type: github
author: Kito Cheng
headline: 'RISC-V: Fix build error in driver-riscv.cc'
tldr: Corrects a build issue in RISC-V driver code by using the updated hardware probe
  extension name.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The RISC-V target configuration's `driver-riscv.cc` file contained
  a stale reference to `RISCV_HWPROBE_IMA_V` after this macro was removed during a
  cleanup, causing a build failure. This change updates the `riscv_arch_from_hwprobe`
  function to use `RISCV_HWPROBE_EXT_V`, which is defined in `riscv-hwprobe.def` and
  is the correct name for the V extension in the hardware probe context.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on Reduced
    Instruction Set Computer principles.
- term: driver-riscv.cc
  definition: A source file within GCC that handles target-specific driver logic for
    the RISC-V architecture.
- term: RISCV_HWPROBE_EXT_V
  definition: A macro or symbol representing the 'V' extension (Vector extension)
    within the RISC-V hardware probe interface.
- term: hardware probe
  definition: A mechanism used to query the hardware for supported features and extensions,
    often used during runtime or configuration.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4bdedfd9bdf9a6c79ecee844459a7f284b33baf6
date: '2026-08-24'
is_stub: true
stub_reason: low_score
---

A recent cleanup in the RISC-V configuration code inadvertently removed the `RISCV_HWPROBE_IMA_V` macro. However, its usage persisted in `driver-riscv.cc` within the `riscv_arch_from_hwprobe` function. This commit resolves the build failure by changing the function to use the correct, remaining macro name, `RISCV_HWPROBE_EXT_V`.
