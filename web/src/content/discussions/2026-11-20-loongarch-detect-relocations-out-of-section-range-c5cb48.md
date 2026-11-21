---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- loongarch
- linker
- relocation
- error checking
discussion_id: 20261120103744.627321-1-harshit7kr@gmail.com
source_type: public_inbox
title: 'Re: [PATCH] LoongArch: Detect relocations out of section range'
headline: 'LoongArch: Detect relocations out of section range'
tldr: Improves relocation error checking for LoongArch by detecting relocations that
  fall outside their designated section range.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves linker robustness by catching invalid relocation offsets.
- Ensures correct behavior for LoongArch targets.
- Potential for slight performance overhead due to additional checks.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Submits a patch to improve LoongArch relocation error checking by detecting
    out-of-range relocations, suggesting it might supersede a previous RFC.
  quote: 'The RFC I posted on Monday does this check for every ELF target where

    the linker reads relocations (elf_link_read_relocs_from_section), so it

    covers the sections check_relocs skips, and runs before relaxation:

    https://inbox.sourceware.org/binutils/20261116184333.3297411-1-harshit7kr@gmail.com/'
- author: Alan Modra
  role: reviewer
  position: Suggests performing the relocation range check within `relocate_section`
    for better coverage, as `check_relocs` is not always called.
  quote: 'This is better done in relocate_section, unless loongarch reads

    section contents in check_relocs. check_relocs is not called for some

    sections (see _bfd_elf_link_iterate_on_relocs), so for instance, debug

    sections won''t have their relocations sanity checked.'
primer_expert: This patch for LoongArch binutils addresses relocation validation.
  The core issue is ensuring that relocation offsets are within the bounds of their
  target sections. The reviewer, Alan Modra, points out that the existing `check_relocs`
  function isn't universally called, potentially missing checks in sections like `.debug_info`.
  The proposer, Harshit Kumar, suggests that a previous RFC provides a generic ELF
  solution that might cover this, and this patch implements the check specifically
  for LoongArch, possibly by integrating it into `relocate_section` as advised.
primer_glossary:
- term: LoongArch
  definition: A RISC-based instruction set architecture developed by China.
- term: relocation
  definition: The process of updating symbolic references and memory addresses in
    object code or executable files after compilation, typically performed by the
    linker.
- term: section
  definition: A part of an object file or executable that contains code, data, or
    other information (e.g., .text for code, .data for initialized data).
- term: linker
  definition: A program that combines object files and libraries into an executable
    program.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files, executables, and shared libraries on Unix-like systems.
- term: relocate_section
  definition: A function within the linker that handles the process of applying relocations
    to a specific section of code or data.
- term: check_relocs
  definition: A function or mechanism within the linker that performs sanity checks
    on relocations.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120103744.627321-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch enhances the LoongArch linker's error detection by implementing checks for relocations that are out of their section's range. This addresses a potential issue where invalid relocation offsets could be accepted, leading to incorrect linking or runtime errors. The proposed solution integrates this check into the `relocate_section` function for broader coverage.
