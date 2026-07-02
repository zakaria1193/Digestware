---
project: binutils
subsystem: include/elf
patch_id: null
tags:
- binutils
- elf
- amdgpu
- constants
- header file
discussion_id: 20260511151846.69747-1-simon.marchi@efficios.com
source_type: public_inbox
title: '[pushed] include/elf: fix order of AMDGPU constants'
headline: Fix AMDGPU constant order in include/elf.
tldr: Simon Marchi fixed the order of AMDGPU constants in `include/elf/amdgpu.h` to
  be in ascending value order.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: committed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This commit rearranges the `EF_AMDGPU_MACH_AMDGCN_*` defines in `include/elf/amdgpu.h`
  to be in ascending order.  These constants represent specific AMDGPU architectures
  and are used in ELF files to identify the target GPU.
primer_general: ELF (Executable and Linkable Format) is a common file format for executables,
  object code, shared libraries, and core dumps. This commit involves reordering definitions
  related to AMD GPUs within a header file that helps programs understand the structure
  of ELF files.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260511151846.69747-1-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-05-11'
is_stub: false
---

Simon Marchi corrected the order of AMDGPU machine constants within the `include/elf/amdgpu.h` header file.  The constants were intended to be in ascending order of their values, and this commit enforces that order.
