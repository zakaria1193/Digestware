---
project: binutils
subsystem: readelf
patch_id: null
tags:
- readelf
- AMDGPU
- ELF
- GPU
- code object
discussion_id: 20260507194615.943267-4-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH v2 3/4] readelf: Add support for AMDGPU code object V6'
headline: 'readelf: Add support for AMDGPU code object V6'
tldr: readelf now decodes the EF_AMDGPU_GENERIC_VERSION_V flag for AMDGPU code object
  V6.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased complexity in `readelf` due to the addition of new AMDGPU-specific flags.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Proposes a patch to add support for AMDGPU code object V6 in readelf,
    including decoding the EF_AMDGPU_GENERIC_VERSION_V field.
  quote: AMDGPU code object V6 adds the EF_AMDGPU_GENERIC_VERSION_V field. Decode
    it when decoding the e_flags value for amdgpu.
primer_expert: '`readelf` parses ELF headers and section data. AMDGPU code objects
  are ELF files with GPU-specific metadata. The ELF header''s e_flags field contains
  architecture-specific flags; this patch decodes the `EF_AMDGPU_GENERIC_VERSION_V`
  flag introduced in AMDGPU code object V6.'
primer_general: '`readelf` is a command-line utility that displays information about
  ELF (Executable and Linkable Format) files, a common format for executables, object
  code, shared libraries, and core dumps on Linux and other Unix-like systems.  AMDGPU
  code objects are ELF files containing code and data for AMD GPUs. This patch extends
  `readelf` to recognize and display information about a new version of AMDGPU code
  objects, allowing developers to inspect the properties of GPU binaries.'
series_id: 'binutils:readelf: add support for amdgpu code object v6'
series_role: reply
series_parts:
- title: 'readelf: Add support for AMDGPU code object V6'
  url: https://inbox.sourceware.org/binutils/ee3f3e7e-51ca-445c-9f50-831716b1c153@polymtl.ca
  n: 3
  total: 3
url: https://inbox.sourceware.org/binutils/20260507194615.943267-4-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-05-07'
---

This patch updates `readelf` to support AMDGPU code object V6, which introduces the `EF_AMDGPU_GENERIC_VERSION_V` flag. The patch decodes this flag and displays the generic code object version when examining AMDGPU ELF files.  This allows developers to inspect binaries compiled for AMD's GPUs, ensuring compatibility with the latest architecture features.
