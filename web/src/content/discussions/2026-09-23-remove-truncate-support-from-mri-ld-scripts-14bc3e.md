---
project: binutils
subsystem: binutils
patch_id: null
tags:
- patch
- binutils
- linker
- cleanup
- mri
discussion_id: arRftQCCRu3atuHw@squeak.grove.modra.org
source_type: public_inbox
title: PR 34670 remove TRUNCATE support from mri ld scripts
headline: Remove TRUNCATE support from MRI ld scripts
tldr: Removes undocumented and unimplemented TRUNCATE support from binutils MRI linker
  scripts.
proposer: Alan Modra
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch removes the `TRUNCATE` token from the GNU `ld` parser for
  MRI (Machine Readable Information) scripts. The `TRUNCATE` keyword, along with its
  associated functionality in `mri.c` and `ldgram.y`, was introduced in 1993 but never
  implemented and remains undocumented. Its removal simplifies the linker script grammar
  and code.
primer_glossary:
- term: MRI ld scripts
  definition: Linker scripts in Machine Readable Information format, used by the GNU
    linker (`ld`) to control the memory layout of output files.
- term: TRUNCATE
  definition: A keyword that was present in the MRI linker script syntax but was never
    implemented. Its intended purpose is unclear but might have related to limiting
    symbol sizes.
- term: linker script
  definition: A file that specifies how the linker should arrange code and data sections
    in the output executable or library.
- term: parser
  definition: A component of a compiler or interpreter that analyzes a stream of tokens
    (from lexing) to determine the grammatical structure of the input.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/arRftQCCRu3atuHw@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-23'
is_stub: false
stub_reason: ''
---

This patch removes the `TRUNCATE` keyword from binutils' MRI linker scripts. The keyword, which appeared in 1993, was never implemented and is undocumented. Its removal cleans up the parser and avoids confusion for users.
