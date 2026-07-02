---
project: binutils
subsystem: bfd/readelf
patch_id: null
tags:
- core-dump
- arm
- aarch64
- debugging
- elf
discussion_id: a6d2bcc6-83c1-5390-3f38-a5a1b5d0c23d@e124511.cambridge.arm.com
source_type: public_inbox
title: 'Re: [PATCH v1] bfd/readelf: Add core file support for FEAT_S1POE'
headline: 'bfd/readelf: Add core file support for FEAT_S1POE'
tldr: Adds support for reading and dumping NT_ARM_POE information from core files.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds functionality for a specific ARM feature, increasing binutils' utility for
  AArch64 debugging.
- Minimal impact on existing functionality or performance.
exchanges:
- author: Srinath Parvathaneni
  role: proposer
  position: Submits a patch to add support for NT_ARM_POE in core files, reporting
    no regressions on the aarch64 target.
  quote: 'Add support for `NT_ARM_POE` dumps/reads for core files.


    Regression tested for aarch64-none-linux-gnu target and

    found no regressions.'
- author: Alice Carlotti
  role: reviewer
  position: Acknowledges and accepts the proposed patch.
  quote: Ok, thanks.
primer_expert: This patch extends binutils' core dump analysis capabilities to include
  ARM's Point Of Exception (POE) notes, specifically relevant for AArch64 debugging.
  It integrates the `NT_ARM_POE` note type into the `readelf` tool by defining a new
  pseudo-section (`.reg-aarch-poe`) and associating it with the corresponding note
  type within the ELF core file parsing mechanism. This allows developers to inspect
  POE-related information when analyzing core dumps.
primer_glossary:
- term: core file
  definition: A file created by the operating system when a program crashes or terminates
    abnormally. It contains a snapshot of the program's memory and execution state
    at the time of the crash.
- term: readelf
  definition: A utility that displays information about ELF files, including headers,
    section details, symbol tables, and relocation entries.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps on many Unix-like systems.
- term: NT_ARM_POE
  definition: A specific note type in an ELF core file that contains information related
    to ARM's Point Of Exception, used for debugging and crash analysis on ARM architectures.
- term: AArch64
  definition: The 64-bit execution state of the ARM architecture.
- term: pseudo-section
  definition: A logical section created by binutils tools to represent data that isn't
    a distinct section in the original object file but is useful for analysis, such
    as note information in core dumps.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/a6d2bcc6-83c1-5390-3f38-a5a1b5d0c23d@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This patch adds support for the ARM POE (Point Of Exception) note type to binutils' core file handling. The `readelf` utility will now be able to interpret and display `NT_ARM_POE` information found in core dumps, particularly for AArch64 targets. The change involves defining a new pseudo-section for this note type and integrating it into the ELF core file parsing logic.
