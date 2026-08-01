---
project: binutils
subsystem: bfd
patch_id: null
tags:
- bugfix
- linker
- debuginfo
discussion_id: ffa348aa-ecc1-4a3f-997a-c3e14478d013@suse.com
source_type: public_inbox
title: 'bfd: SEC_DEBUGGING in bfd_generic_get_relocated_section_contents()'
headline: 'bfd: SEC_DEBUGGING in bfd_generic_get_relocated_section_contents()'
tldr: Fixes binutils BFD to correctly handle debugging sections during relocation
  processing.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Reintroduces handling for debugging sections, which may require careful validation
  to avoid new issues.
- Addresses testsuite fallout and warnings from objdump.
exchanges: []
primer_expert: A recent change in BFD's ELF merge logic (`bfd_generic_get_relocated_section_contents`)
  inadvertently excluded debugging sections (marked with `SEC_DEBUGGING`) from relocation
  processing. This patch aims to correct that by re-evaluating the handling of these
  sections. The author notes that a blanket exclusion was wrong and discusses the
  need for specific handling, similar to how other sections are processed, while also
  considering potential issues with non-section symbols.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a backend API for accessing object file
    formats.
- term: SEC_DEBUGGING
  definition: A flag within the BFD library indicating that a section contains debugging
    information.
- term: relocation
  definition: The process of updating symbolic references in relocatable object code
    to absolute symbols, typically done by the linker.
- term: debug info
  definition: Metadata embedded in an object file that allows debuggers to map machine
    code back to source code constructs (variables, functions, line numbers).
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files.
- term: objdump
  definition: A utility that displays information from object files, including disassembled
    code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ffa348aa-ecc1-4a3f-997a-c3e14478d013@suse.com
bugzilla_url: null
date: '2026-07-31'
is_stub: false
stub_reason: ''
---

This patch corrects a regression in binutils' BFD library where debugging sections were incorrectly excluded during relocation processing. The exclusion, introduced in a previous change, led to broken debug info and testsuite failures. The fix ensures these sections are handled appropriately, resolving issues that became more apparent with recent readelf/objdump improvements.
