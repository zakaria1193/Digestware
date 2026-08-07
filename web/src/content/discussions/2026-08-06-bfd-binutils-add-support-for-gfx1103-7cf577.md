---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- amd
- gpu
- gfx1103
- elf
discussion_id: 20260806110812.27469-1-shahab.vahedi@amd.com
source_type: public_inbox
title: '[PUSHED] bfd,binutils: add support for gfx1103'
headline: 'bfd,binutils: add support for gfx1103'
tldr: Support for the AMD GPU 'gfx1103' architecture has been added to BFD and binutils.
proposer: Shahab Vahedi <shahab.vahedi@amd.com>
consensus: Committed
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables support for new hardware, requiring updates to machine definitions.
- Prompts discussion on establishing dedicated maintainership for specific hardware
  architectures within binutils.
exchanges:
- author: Shahab Vahedi <shahab.vahedi@amd.com>
  role: proposer
  position: Adds ELF header definitions for the AMD 'gfx1103' GPU architecture to
    BFD and binutils.
  quote: null
- author: Lancelot SIX <Lancelot.Six@amd.com>
  role: reviewer
  position: Reviews the patch positively for binutils, noting its consistency with
    GDB's needs, but raises the question of establishing a dedicated binutils maintainer
    for AMDGPU support.
  quote: null
primer_expert: This change introduces support for a new AMD GPU microarchitecture,
  'gfx1103,' into the binutils toolchain. Specifically, it updates BFD (the binary
  file descriptor library) and related tools like `readelf` to recognize and correctly
  interpret ELF information pertaining to this new hardware. This is essential for
  developers targeting the latest AMD GPUs.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260806110812.27469-1-shahab.vahedi@amd.com
bugzilla_url: null
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

This commit adds support for the 'gfx1103' AMD GPU architecture by defining its corresponding machine-specific values in the BFD library and related binutils components. This enables binutils tools like `readelf` to correctly identify and process binaries targeting this new GPU. The canonical source for this definition is noted as LLVM's AMDGPUUsage documentation.
