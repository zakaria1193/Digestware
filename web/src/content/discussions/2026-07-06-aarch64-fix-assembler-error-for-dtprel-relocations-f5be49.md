---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- assembler
- relocation
- tls
- dwarf
discussion_id: 20260706094728.1788418-1-srinath.parvathaneni@arm.com
source_type: public_inbox
title: '[PATCH v1] aarch64: Fix assembler internal error for %dtprel relocations'
headline: 'aarch64: Fix assembler error for %dtprel relocations'
tldr: Srinath Parvathaneni proposes a fix for an assembler internal error related
  to %dtprel relocations on AArch64.
proposer: srinath.parvathaneni@arm.com
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 7
technical_tradeoffs: []
exchanges:
- author: srinath.parvathaneni@arm.com
  role: proposer
  position: Submits a patch to fix an assembler internal error by correcting the order
    of operations for %dtprel relocations.
  quote: 'The current implementation creates the DTPREL fixup before reserving

    the storage for the corresponding ".xword". GCC''s "%dtprel" support

    for TLS DWARF debug information exposed this during an AArch64 bootstrap,

    where the libsanitizer/tsan DWARF layout places the DTPREL fixup at a

    frag boundary. Reserving the storage before creating the fixup avoids

    this corner case.'
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Acknowledges the issue and the proposed fix.
  quote: null
primer_expert: This patch addresses an ordering issue in the AArch64 assembler (`gas`)
  related to Thread Local Storage (TLS) and Debugging With Attributed Record Prefix
  (DWARF) information. Specifically, it corrects the generation order of DTPREL relocations
  and their associated storage (`.xword`) to prevent an internal error when these
  relocations fall on fragment boundaries, a scenario exposed by GCC's `%dtprel` handling
  for libsanitizer.
primer_glossary:
- term: '%dtprel'
  definition: A directive or syntax used in assembly or by compilers to specify a
    DTPREL (Descriptor Table Pointer Relative) relocation, typically used for Thread
    Local Storage (TLS) access.
- term: DTPREL
  definition: Descriptor Table Pointer Relative. A type of relocation used in some
    architectureABIs, often related to accessing thread-local storage (TLS) variables.
- term: TLS
  definition: Thread Local Storage. A mechanism that allows variables to have unique
    instances per thread.
- term: DWARF
  definition: Debugging With Attributed Record Prefix. A debugging data format used
    by many compilers and debuggers to store information about source code.
- term: assembler
  definition: A program that translates assembly language code into machine code.
    In this context, it refers to `gas`, the GNU Assembler.
- term: relocation
  definition: A placeholder in object code that specifies how to modify addresses
    or other values when the code is linked or loaded into memory. DTPREL is a type
    of relocation.
- term: fragment boundary
  definition: In the context of assemblers like gas, code is often organized into
    fragments. A fragment boundary is the point where one fragment ends and another
    begins.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260706094728.1788418-1-srinath.parvathaneni@arm.com
bugzilla_url: null
date: '2026-07-06'
is_stub: false
stub_reason: ''
---

Srinath Parvathaneni submits a patch to fix an internal assembler error on AArch64 when handling %dtprel relocations. The issue occurs because the DTPREL fixup was created before reserving storage for the corresponding '.xword', causing problems with TLS DWARF debug information, particularly when placed at a fragment boundary. The patch corrects the storage order to resolve this corner case.
