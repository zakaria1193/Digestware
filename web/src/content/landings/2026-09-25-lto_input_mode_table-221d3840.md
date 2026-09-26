---
project: gcc
subsystem: lto_input_mode_table
patch_id: null
tags:
- lto
- offloading
- target support
- compiler modes
commit_hash: 221d38405f99e5c51f26e09759e79aee482611fa
source_type: github
author: Tobias Burnus
headline: 'LTO: Check mode availability on offload targets'
tldr: Ensures that compiler modes used in LTO are actually supported on the offload
  target device.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `lto_input_mode_table` function, responsible for processing modes
  from LTO input, now includes a runtime check for mode availability on offload targets.
  This addresses issues where modes supported by the host compiler (e.g., `_Float16`)
  might not be fully enabled or available on the device (e.g., `nvptx` with `-mexperimental`,
  `amdgcn`). The change adds a call to `targetm.scalar_mode_supported_p` within the
  `ACCEL_COMPILER` branch to dynamically verify if a mode is supported at runtime
  before accepting it, issuing an error if not. This complements the existing check
  for modes that are ent…
primer_glossary:
- term: LTO
  definition: Link-Time Optimization. A compilation process where optimization is
    performed across multiple source files during the linking stage, allowing for
    more aggressive optimizations.
- term: offload targets
  definition: Hardware accelerators or co-processors (e.g., GPUs) that a host system
    can offload computation to. Compilers supporting offloading generate code for
    both the host and the target device.
- term: mode
  definition: In GCC, a 'mode' represents a data type and its size, such as 'SI' for
    signed integer, 'DF' for double-precision float, or 'HF' for half-precision float.
- term: runtime availability
  definition: Whether a specific feature or data type is supported and functional
    by the target hardware and its drivers at the time the program is executed.
- term: ACCEL_COMPILER
  definition: A compiler targeting an accelerator device, distinct from the host compiler.
- term: targetm.scalar_mode_supported_p
  definition: A target-specific function pointer in GCC used to query whether a given
    scalar data type (mode) is supported by the target architecture at runtime.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/221d38405f99e5c51f26e09759e79aee482611fa
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

This change enhances the LTO input mode table to verify that floating-point and integer modes are supported at runtime on offload targets. Previously, only a general check for mode existence was performed. Now, for `ACCEL_COMPILER` targets, it calls `targetm.scalar_mode_supported_p` to confirm runtime availability. This is crucial for modes like `_Float16` which may have device-specific or conditional support, preventing errors caused by using unsupported data types on the target hardware. New test cases are added to verify this functionality.
