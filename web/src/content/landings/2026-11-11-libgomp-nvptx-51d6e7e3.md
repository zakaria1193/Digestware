---
project: gcc
subsystem: libgomp/nvptx
patch_id: null
tags:
- gpu
- cuda
- libgomp
commit_hash: 51d6e7e3dbf9fefd1a1b1140a9640ac777e79849
source_type: github
author: Thomas Schwinge
headline: libgomp NVIDIA GPU plugin requires CUDA 8.0 or newer
tldr: libgomp's NVIDIA GPU plugin now requires compilation against CUDA 8.0 or newer.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: libgomp's NVIDIA GPU plugin compiles against an internal CUDA header
  unless overridden by `PLUGIN_NVPTX_INCLUDE_SYSTEM_CUDA_H`. This commit enforces
  that the bundled CUDA header, currently CUDA 8.0 (`CUDA_VERSION 8000`), must be
  used for compilation. This codifies a minimum CUDA version requirement for the plugin.
primer_glossary:
- term: libgomp
  definition: The GNU implementation of the OpenMP API, providing support for parallel
    multithreading in C, C++, and Fortran.
- term: CUDA
  definition: Compute Unified Device Architecture, a parallel computing platform and
    programming model created by NVIDIA for general computing on graphical processing
    units (GPUs).
- term: cuda.h
  definition: A header file provided by NVIDIA's CUDA Toolkit that defines interfaces
    for CUDA C/C++ applications. GCC includes its own version for use with its NVPTX
    backend.
- term: NVPTX
  definition: An NVIDIA PTX (Parallel Thread Execution) backend for GCC, allowing
    it to compile code for NVIDIA GPUs.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/51d6e7e3dbf9fefd1a1b1140a9640ac777e79849
date: '2026-11-11'
is_stub: false
stub_reason: ''
---

The libgomp NVIDIA GPU plugin, by default, compiles against GCC's bundled cuda.h header. This commit enforces that the CUDA version used for compilation is at least CUDA 8.0, aligning with the version provided by GCC. This change aims to prevent potential compatibility issues by ensuring a baseline CUDA version is met.
