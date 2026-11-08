---
project: gcc
subsystem: libgomp/plugin-gcn
patch_id: null
tags:
- gpu
- libgomp
- amd
- gcn
- bugfix
commit_hash: 4a11605bc1f649ccfd2244e97553b838782d006a
source_type: github
author: Arsen Arsenović
headline: Fix kernarg allocation size in libgomp's GCN plugin.
tldr: Corrected kernarg allocation in GCC's libgomp GCN plugin to include the target
  variable table.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `libgomp/plugin/plugin-gcn.c` file's `allocate_session_kernargs`
  function incorrectly calculated the size for kernarg buffers. It used `sizeof (struct
  kernargs)` which does not account for the necessary space for the target variable
  table. This change rectifies the allocation by using `kernargs_size`, which presumably
  includes this additional required space. A new test, `kernel-launch-many-vars.c`,
  verifies this fix.
primer_glossary:
- term: libgomp
  definition: GCC's runtime library for OpenMP, providing support for parallel programming.
- term: GCN
  definition: Graphics Core Next is a GPU architecture developed by AMD, commonly
    used in their Radeon graphics cards.
- term: kernarg
  definition: Kernel argument. In the context of GPGPU programming, these are the
    parameters passed from the host to the device when launching a compute kernel.
- term: target variable table
  definition: A data structure used by the GCN compute runtime to manage variables
    accessible by the GPU kernel, including their sizes and offsets.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/4a11605bc1f649ccfd2244e97553b838782d006a
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

GCC's libgomp plugin for AMD's GCN (Graphics Core Next) architecture had a bug in kernarg allocation, leaving insufficient space for the target variable table. This commit fixes the `allocate_session_kernargs` function to use the correct `kernargs_size` instead of the size of the `struct kernargs`, preventing potential buffer overflows or incorrect behavior. A new test case is added to verify the fix.
