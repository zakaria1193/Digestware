---
project: gcc
subsystem: libgomp/documentation
patch_id: null
tags:
- openmp
- gpu
- rocm
- documentation
commit_hash: b6f7035408cc08acef6f05a65d5da1d5f9e29a33
source_type: github
author: Tobias Burnus
headline: 'Libgomp.texi: Mention ROCR_VISIBLE_DEVICES in context of USM'
tldr: Documentation for libgomp now clarifies the use of `ROCR_VISIBLE_DEVICES` for
  unified shared memory with AMD GPUs.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `libgomp.texi` file provides documentation for libgomp, GCC's OpenMP
  runtime library, specifically detailing the GCN (Graphics Core Next) offloading
  capabilities for AMD GPUs. This commit refines the explanation of Unified Shared
  Memory (USM) support, which is critical for efficient data transfer between the
  host and GPU. On heterogeneous systems where not all AMD GPUs support USM, the `ROCR_VISIBLE_DEVICES`
  environment variable becomes a necessary control mechanism to ensure host fallback
  doesn't occur unnecessarily. This documentation update also corrects a subtle confusion
  between USM/…
primer_general: Modern computer systems often combine a main processor (CPU) with
  specialized processors like Graphics Processing Units (GPUs) for faster computation.
  To make these work together efficiently, data needs to be easily accessible by both.
  Unified Shared Memory (USM) is a technology that allows the CPU and GPU to share
  the same memory space, simplifying programming and improving performance. However,
  some older or entry-level GPUs might not fully support USM, especially in systems
  with both an integrated GPU and a separate, more powerful one. This update to the
  GCC documentation for OpenMP (a programming standard for parallel computing) clarifies
  that if you encounter issues with USM on AMD GPUs in such 'mixed' systems, you can
  use the `ROCR_VISIBLE_DEVICES` setting. This setting lets you tell the system which
  specific GPUs should be used, effectively working around the limitation and ensuring
  your programs run correctly with USM.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b6f7035408cc08acef6f05a65d5da1d5f9e29a33
date: '2026-06-09'
is_stub: false
---

This commit updates the `libgomp.texi` documentation to better explain the use of unified shared memory (USM) with AMD GPUs, particularly on mixed systems. It re-adds a crucial half-sentence that was previously lost, clarifying that `ROCR_VISIBLE_DEVICES` serves as a workaround when not all AMD GPUs support USM, especially in configurations with integrated and discrete GPUs. The wording also now correctly differentiates between USM/SVM support and XNACK capabilities.
