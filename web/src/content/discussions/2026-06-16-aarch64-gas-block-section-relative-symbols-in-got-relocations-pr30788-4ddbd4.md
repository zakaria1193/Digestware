---
project: binutils
subsystem: binutils
patch_id: null
tags:
- aarch64
- assembler
- got
- relocations
- binutils
discussion_id: 4888be33-52b9-4e57-bb3b-a87774b86b21@arm.com
source_type: public_inbox
title: 'Re: [PATCH] AArch64 gas: Block section relative symbols in GOT relocations
  [PR30788]'
headline: 'AArch64 gas: Block section relative symbols in GOT relocations [PR30788]'
tldr: A patch blocking section-relative symbols in AArch64 GOT relocations has been
  committed, resolving PR30788.
proposer: '"Richard Earnshaw (foss)" <Richard.Earnshaw@arm.com>'
consensus: Proposed
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Wilco Dijkstra
  role: contributor
  position: Requests for the patch to be committed since they lack write access.
  quote: Since I don't have write access, could someone commit this for me, please?
- author: Richard Earnshaw (foss)
  role: maintainer
  position: Confirms the commitment of the patch and thanks the author.
  quote: Done. Thanks once again.
primer_expert: This interaction confirms the commitment of a patch impacting `gas`
  (the GNU Assembler) for the AArch64 architecture. The patch specifically blocks
  section-relative symbols from being used in Global Offset Table (GOT) relocations.
  GOT relocations are instrumental in Position-Independent Code (PIC) generation,
  enabling shared libraries by resolving addresses at runtime. Section-relative symbols
  (e.g., symbols referencing data within `.text` or `.data` sections) typically should
  not be referenced via the GOT, as their addresses are fixed relative to the section
  start point within an object. Thi…
primer_general: This discussion is about a technical fix that has been applied to
  a part of Binutils called `gas`, the GNU Assembler, specifically for the AArch64
  architecture (used in many mobile phones and servers). The fix prevents certain
  types of 'symbols' (names given to parts of code or data) that are tied to a specific
  section within a compiled program from being used incorrectly with a mechanism called
  the Global Offset Table (GOT). The GOT is crucial for allowing code to be shared
  efficiently between different programs without needing to be recompiled for each
  one, a technique called Position-Independent Code (PIC). This technical update improves
  the reliability and correctness of how programs are put together for AArch64, addressing
  a specific identified issue.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/4888be33-52b9-4e57-bb3b-a87774b86b21@arm.com
bugzilla_url: null
date: '2026-06-16'
is_stub: false
---

This discussion confirms the commitment of a patch to the AArch64 `gas` (assembler) that blocks section-relative symbols in Global Offset Table (GOT) relocations. The change addresses an issue tracked as PR30788 and follows a historical decision to deprecate or remove specific VTABLE-related functionality. The patch improves the correctness and stability of AArch64 assembly generation.
