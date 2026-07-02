---
project: binutils
subsystem: binutils
patch_id: null
tags:
- AMDGPU
- architectures
- binutils
- GPU
- readelf
discussion_id: 20260507194615.943267-1-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH v2 0/4] Add support for new AMDGPU architectures'
headline: Add support for new AMDGPU architectures
tldr: This patch series adds support for new AMDGPU architectures and related features
  to binutils.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Increased code complexity due to the addition of new architecture-specific handling.
- Potential maintenance overhead to keep the architecture list and feature support
  up-to-date.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Proposes a patch series to add support for new AMDGPU architectures in
    binutils, addressing review comments from the previous version and adding new
    architectures.
  quote: 'This is v2 of:


    https://inbox.sourceware.org/binutils/20251031175411.1303161-1-luis.machado@amd.com/


    I address the review comments, and I also added the gfx1250 and

    gfx12-5-generic architectures.


    Patch 4 is new.'
primer_expert: This series updates the AMDGPU architecture support in binutils, affecting
  the BFD library, the `readelf` utility, and related header files.  These changes
  allow binutils to correctly identify, disassemble, and link code targeting newer
  AMD GPUs.
primer_general: This patch series enhances the binutils suite to better support AMD
  GPUs.  Binutils is a set of essential tools for working with binary files, including
  assemblers, linkers, and utilities for inspecting object files. By adding support
  for new AMDGPU architectures, this series ensures that developers can use binutils
  to build, debug, and analyze code for the latest AMD GPUs.
series_id: binutils:add support for new amdgpu architectures
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260507194615.943267-1-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-05-07'
---

This patch series updates binutils to support new AMDGPU architectures, including adding generic targets and updating the list of supported architectures.  It also adds support for AMDGPU code object V6 in `readelf` and includes documentation updates with reference URLs. These changes ensure that binutils can correctly process and analyze binaries targeting the latest AMD GPUs, which is crucial for developers working on GPU-accelerated applications.
