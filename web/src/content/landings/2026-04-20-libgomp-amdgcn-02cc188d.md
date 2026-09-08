---
project: gcc
subsystem: libgomp, amdgcn
patch_id: null
tags:
- amd
- gpu
- libgomp
- assembly
- performance
commit_hash: 02cc188d3d9f14975c8285678f937a1ba79bedeb
source_type: github
author: Andrew Stubbs
headline: 'libgomp, amdgcn: Ensure s_memrealtime uses SGPRs'
tldr: AMD GCN time function now correctly uses special function registers (SGPRs)
  for stability.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `libgomp/config/gcn/time.c`, the `omp_get_wtime` function uses an
  inline assembly snippet that calls the `s_memrealtime` intrinsic. Previously, this
  intrinsic used an 'r' constraint for register selection, which was insufficient
  for the AMD GCN architecture's SIMT execution model. The 'r' constraint might pick
  any general-purpose register, but `s_memrealtime` requires specific register types
  for predictable behavior. This change enforces the use of SGPRs by specifying `=Sg`
  as the output constraint, guaranteeing that the intrinsic operates correctly and
  reliably on GCN hardware.
primer_glossary:
- term: libgomp
  definition: The GNU implementation of OpenMP, providing runtime support for parallel
    programming constructs.
- term: amdgcn
  definition: AMD's Graphics Core Next architecture, a GPU instruction set architecture
    used in many AMD Radeon graphics cards.
- term: s_memrealtime
  definition: A specific assembly instruction or intrinsic on AMD GCN architecture
    likely related to measuring real-time performance or elapsed time.
- term: SGPR
  definition: Special General Purpose Register. A type of register on AMD GCN GPUs
    used for scalar values and control information, distinct from vector registers
    (VGPRs).
- term: SIMT
  definition: Single Instruction, Multiple Threads. A parallel execution model used
    in GPUs where multiple threads execute the same instruction simultaneously on
    different data.
- term: constraint
  definition: In inline assembly, a character code specifying the type of operand
    (e.g., register, memory) that a particular part of the assembly instruction can
    use.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/02cc188d3d9f14975c8285678f937a1ba79bedeb
date: '2026-04-20'
is_stub: false
stub_reason: ''
---

The `s_memrealtime` intrinsic within libgomp's AMD GCN backend was using a generic 'r' register constraint. This could lead to instability, especially in SIMT execution, as it might only select a compatible register by chance. This commit changes the constraint to the more specific `Sg` (Special General Purpose Register), ensuring that the intrinsic reliably uses SGPRs, thereby improving the stability and correctness of time-related functions on AMD GPUs.
