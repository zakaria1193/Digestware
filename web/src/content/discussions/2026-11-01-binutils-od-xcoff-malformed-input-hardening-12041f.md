---
project: binutils
subsystem: binutils
patch_id: null
tags:
- XCOFF
- hardening
- objdump
- parsing
- security
discussion_id: 20261101105139.573422-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 0/6] binutils: od-xcoff: malformed input hardening'
headline: 'binutils: od-xcoff: malformed input hardening'
tldr: A series of patches to harden the XCOFF dumper against malformed input, fixing
  parsing issues and preventing crashes.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increases the complexity of the parsing code for enhanced safety.
- Ensures better handling of non-compliant input files.
- Requires careful review and testing of individual patches.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Submits a series of patches to harden the XCOFF dumper against malformed
    input, detailing the specific problems addressed in each patch.
  quote: 'This series hardens the XCOFF dumper (binutils/od-xcoff.c) against malformed
    input. It bounds section, symbol, loader, typchk, except, and traceback parsing,
    fixes a resource leak, and validates relocation symbol slots before printing them.
    This is robustness hardening for malformed input, not a security fix.


    Problems fixed:


    1. xcoff32_read_symbols reads auxiliary records into &s[j + 1].aux wit…'
primer_expert: This is the cover letter for a six-patch series that enhances the robustness
  of binutils' XCOFF object file dumper (`od-xcoff.c`). The series addresses various
  parsing vulnerabilities, such as out-of-bounds reads, heap overflows, and memory
  leaks, that can be triggered by malformed XCOFF inputs. These fixes ensure that
  `objdump` and related tools handle corrupted object files more gracefully, preventing
  crashes and improving overall stability.
primer_glossary:
- term: XCOFF
  definition: A file format used on IBM AIX systems, similar to COFF and ELF.
- term: objdump
  definition: A command-line utility that displays information from object files,
    including disassembly and symbol tables.
- term: hardening
  definition: The process of making software more secure and resilient against attacks
    or unexpected inputs.
- term: malformed input
  definition: Data that does not conform to the expected format or structure of a
    file or protocol.
- term: heap buffer overflow
  definition: A vulnerability where a program writes data beyond the allocated buffer
    in the heap, potentially corrupting adjacent memory.
series_id: 'binutils:binutils: od-xcoff: malformed input hardening'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261101105139.573422-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This series of six patches aims to improve the robustness of the `binutils/od-xcoff.c` dumper by addressing various issues related to malformed input. The changes focus on validating section bounds, symbol table entries, loader section parsing, traceback tag parsing, and relocation symbol slots. These improvements prevent crashes, memory leaks, and data corruption that could arise from non-compliant XCOFF files, complementing existing validation in the linker.
