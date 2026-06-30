---
project: gcc
subsystem: gcc/libgomp
patch_id: null
tags:
- documentation
- libgomp
- cuda
commit_hash: 0e2c5d4b2c16c4b0fbce028f9d74b2d33ccdcc2a
source_type: github
author: Gerald Pfeifer
headline: 'libgomp: Update NVIDIA CUDA link'
tldr: Updates a documentation link for NVIDIA CUDA support in libgomp.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the documentation for libgomp, specifically the
  `libgomp.texi` file, to point to an updated NVIDIA CUDA link for the `nvptx` target.
  This is a routine documentation maintenance task.
primer_general: Libgomp is GCC's implementation of OpenMP, a standard for parallel
  programming. This commit updates a link in the libgomp documentation that relates
  to using GCC with NVIDIA's CUDA platform on the `nvptx` target. The change ensures
  that developers can find the correct information for utilizing GPU acceleration
  with GCC's OpenMP support.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/0e2c5d4b2c16c4b0fbce028f9d74b2d33ccdcc2a
date: '2026-06-28'
is_stub: true
stub_reason: low_score
---

This commit updates a reference within the libgomp documentation to point to the correct or a more current NVIDIA CUDA resource. Specifically, the link associated with the `nvptx` (NVIDIA virtual processor thread) target in the libgomp manual has been adjusted.
