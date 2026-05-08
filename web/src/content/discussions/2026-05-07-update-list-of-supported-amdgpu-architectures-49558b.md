---
project: binutils
subsystem: binutils
patch_id: null
tags:
- AMDGPU
- architectures
- binutils
- GPU
discussion_id: 20260507194615.943267-2-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH v2 1/4] Update list of supported AMDGPU architectures'
headline: Update list of supported AMDGPU architectures
tldr: Updates the list of supported AMDGPU architectures, adding new gfx* and removing
  gfx940.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The update requires modifying several files to add new architecture definitions
  and remove the obsolete one.
exchanges:
- author: Simon Marchi <simon.marchi@efficios.com>
  role: proposer
  position: Proposes updating the list of supported AMDGPU architectures in binutils,
    adding new architectures and removing the obsolete gfx940.
  quote: 'This patch updates the list of supported AMDGPU architectures in bfd/ binutils/
    and include/elf/.


    The following architectures have been added:


    - gfx942

    - gfx950

    - gfx1150

    - gfx1151

    - gfx1152

    - gfx1153

    - gfx1200

    - gfx1201

    - gfx1250


    The following architectures have been removed:


    - gfx940: The compiler no longer supports it.'
primer_expert: This patch updates the architecture definitions in `bfd/`, `binutils/`,
  and `include/elf/`.  The AMDGPU architecture list is used by binutils components
  like the assembler, linker, and disassembler to handle GPU-specific code.
primer_general: This patch updates the list of supported AMDGPU (Advanced Micro Devices
  Graphics Processing Unit) architectures within binutils.  Binutils is a suite of
  tools used for working with binary files, including assembling, linking, and disassembling
  code. By updating the list of supported GPU architectures, binutils can correctly
  process and manipulate binaries targeting different AMD GPUs.
series_id: binutils:update list of supported amdgpu architectures
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260507194615.943267-2-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-05-07'
---

This patch updates the list of supported AMDGPU architectures in binutils, adding support for `gfx942`, `gfx950`, `gfx1150`, `gfx1151`, `gfx1152`, `gfx1153`, `gfx1200`, `gfx1201`, and `gfx1250`. It removes support for `gfx940`, which is no longer supported by the compiler.  Maintaining an accurate list of supported architectures ensures that binutils correctly identifies and processes binaries for different AMD GPUs.
