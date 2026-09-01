---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- elf
- relocation
- dynamic linker
discussion_id: 20260901023318.3503991-3-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 02/11] alpha: set DF_TEXTREL rather than DT_TEXTREL in info->flags'
headline: 'alpha: set DF_TEXTREL rather than DT_TEXTREL in info->flags'
tldr: Correctly sets DF_TEXTREL flag in linker info to avoid misinterpreting read-only
  relocations.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Fixes a bug that has existed since 2001, improving correctness for certain linking
  scenarios.
- Ensures consistent behavior with other ELF targets regarding text relocations.
exchanges: []
primer_expert: This patch corrects an error in `elf64_alpha_calc_dynrel_sizes` where
  the dynamic tag `DT_TEXTREL` (value 22) was OR-ed into `bfd_link_info::flags`, which
  is intended to hold ELF dynamic flags like `DF_TEXTREL` (value 4). This conflation
  caused the dynamic linker to incorrectly apply flags like `DF_SYMBOLIC` and `DF_STATIC_TLS`,
  leading to issues with shared library linking (`-Bsymbolic`) and TLS relaxation.
  The fix ensures that only the `DF_TEXTREL` bit is set when a dynamic relocation
  occurs in a read-only section.
primer_glossary:
- term: DF_TEXTREL
  definition: An ELF dynamic flag indicating that the executable contains relocations
    against read-only sections. This requires special handling by the dynamic linker.
- term: DT_TEXTREL
  definition: A dynamic tag in the ELF header that indicates text relocations. The
    value used in the alpha implementation was conflated with DF_TEXTREL.
- term: dynamic linker
  definition: A system program (e.g., ld.so) that resolves symbols and loads shared
    libraries for an executable at runtime.
- term: TLS
  definition: Thread-Local Storage. A mechanism that allows variables to have distinct
    values for each thread.
- term: relaxation
  definition: An optimization process by the linker that replaces generic relocations
    with more efficient, architecture-specific ones, often based on assumptions about
    the final memory layout.
series_id: 'binutils:alpha: set df_textrel rather than dt_textrel in info->flags'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-3-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch corrects a long-standing issue in the alpha ELF linker where `DT_TEXTREL` was incorrectly OR-ed into `info->flags` as `DF_TEXTREL`. This misuse led to misinterpretations by the dynamic linker, causing shared libraries with text relocations in read-only sections to be treated as if linked with `-Bsymbolic`. It also caused incorrect relaxation of TLS references. The fix replaces the incorrect `DT_TEXTREL` with the proper `DF_TEXTREL` flag, resolving these issues.
