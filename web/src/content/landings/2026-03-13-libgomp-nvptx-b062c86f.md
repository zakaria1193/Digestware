---
project: gcc
subsystem: libgomp/nvptx
patch_id: null
tags:
- gpu
- cuda
- libgomp
- api
commit_hash: b062c86fe0e51bd859496ced40de2f7376c8bca3
source_type: github
author: Thomas Schwinge
headline: libgomp NVIDIA GPU plugin targets CUDA 13 API changes
tldr: Fixes libgomp's NVIDIA GPU plugin build with CUDA 13's cuCtxCreate API changes.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: When `PLUGIN_NVPTX_INCLUDE_SYSTEM_CUDA_H` is used, libgomp's NVPTX
  plugin compiles against the system's CUDA headers. CUDA 13 changed the `cuCtxCreate`
  API signature to `CUctxCreateParams *` for the second argument, requiring an update
  in libgomp's `nvptx_open_device` function to pass the correct number of arguments
  to the `cuCtxCreate_v4` trampoline.
primer_glossary:
- term: cuCtxCreate
  definition: An NVIDIA CUDA driver API function used to create a CUDA context on
    a specified device.
- term: cuCtxCreate_v4
  definition: A versioned CUDA API function, used internally by the driver, that implements
    the `cuCtxCreate` functionality. CUDA 13 changed the signature of this function.
- term: CUctxCreateParams
  definition: A structure introduced in CUDA 13 to pass parameters to `cuCtxCreate`,
    changing the API signature.
- term: PLUGIN_NVPTX_INCLUDE_SYSTEM_CUDA_H
  definition: A preprocessor macro that, when defined, instructs libgomp's NVPTX plugin
    to include the system's CUDA header files instead of GCC's internal version.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/b062c86fe0e51bd859496ced40de2f7376c8bca3
date: '2026-03-13'
is_stub: false
stub_reason: ''
---

CUDA 13 introduced API changes to `cuCtxCreate`, altering its signature and internally aliasing it to `cuCtxCreate_v4`. This commit updates libgomp's NVPTX plugin to correctly handle this new signature, resolving compilation errors that occurred when building with CUDA 13 under the `PLUGIN_NVPTX_INCLUDE_SYSTEM_CUDA_H` configuration.
