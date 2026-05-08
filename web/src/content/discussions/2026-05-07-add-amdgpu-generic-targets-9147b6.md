---
project: binutils
subsystem: bfd
patch_id: null
tags:
- AMDGPU
- generic targets
- binutils
- bfd
- GPU
discussion_id: 20260507194615.943267-3-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH v2 2/4] Add AMDGPU generic targets'
headline: Add AMDGPU generic targets
tldr: Adds generic AMDGPU architectures (gfx9-generic, gfx10-1-generic, etc.) to binutils.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased complexity in architecture handling within binutils.
- Potential for less precise optimization compared to targeting specific GPU architectures.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Proposes adding generic AMDGPU architectures to binutils.
  quote: "Add the following generic AMDGPU architectures:\n\n  - gfx9-generic\n  -\
    \ gfx9-4-generic\n  - gfx10-1-generic\n  - gfx10-3-generic\n  - gfx11-generic\n\
    \  - gfx12-generic\n  - gfx12-5-generic"
primer_expert: This patch adds generic AMDGPU target definitions to the BFD (Binary
  File Descriptor) library, which binutils uses for object file abstraction.  These
  definitions enable binutils tools to recognize and process code targeting these
  generic GPU architectures.
primer_general: This patch introduces support for generic AMDGPU targets within binutils.  Binutils
  uses the BFD library to handle different object file formats and architectures.
  By adding generic target definitions, binutils can now work with code designed to
  run on a range of AMD GPUs, rather than being tied to specific GPU models. This
  improves the flexibility and portability of GPU code development.
series_id: binutils:add amdgpu generic targets
series_role: reply
series_parts:
- title: Add AMDGPU generic targets
  url: https://inbox.sourceware.org/binutils/f3372be4-4476-4a1b-8613-c2835f3dbdb4@polymtl.ca
  n: 2
  total: 3
url: https://inbox.sourceware.org/binutils/20260507194615.943267-3-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-05-07'
---

This patch adds support for generic AMDGPU targets to binutils. These generic targets, such as `gfx9-generic`, `gfx10-1-generic`, and others, allow developers to target a broader range of AMD GPUs without specifying a particular microarchitecture. This simplifies the build process and increases the portability of AMDGPU code.
