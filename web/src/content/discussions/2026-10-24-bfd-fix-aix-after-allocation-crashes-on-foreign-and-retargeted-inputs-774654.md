---
project: binutils
subsystem: bfd
patch_id: null
tags:
- aix
- linker
- bfd
- security
- crash
discussion_id: 20261024095819.1905597-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 0/3] bfd: fix AIX after-allocation crashes on foreign and retargeted
  inputs'
headline: 'bfd: fix AIX after-allocation crashes on foreign and retargeted inputs'
tldr: Fixes crashes in AIX linker emulations related to foreign inputs and retargeted
  outputs by adding necessary checks.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Fixes critical crashes in AIX linker emulations.
- Improves robustness against malformed inputs and linker script usage.
- Enhances security by preventing out-of-bounds reads and null pointer dereferences.
- Includes a regression test to validate the fixes.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Submits a series of patches to fix AIX after-allocation crashes triggered
    by foreign inputs and retargeted outputs, including code changes and a new regression
    test.
  quote: A linker script can retarget the output to a generic ELF format with a plain
    bfd_link_hash_table. Both paths previously crashed before the link could terminate.
primer_expert: 'This cover letter introduces a set of fixes for the AIX linker''s
  after-allocation phase, specifically targeting crashes that occur under two conditions:
  linking foreign (non-XCOFF) object files and retargeting the output format to a
  generic ELF via a linker script. For foreign inputs, the XCOFF-specific magic sections
  (linkage, TOC, descriptor) are not created, leading to NULL pointer dereferences.
  For retargeted ELF outputs, a generic `bfd_link_hash_table` is used instead of the
  expected `xcoff_link_hash_table`, causing out-of-bounds reads. The patches introduce
  guards for both scenarios, en…'
primer_glossary:
- term: AIX
  definition: Advanced Interactive eXecutive, a Unix operating system developed by
    IBM.
- term: linker emulation
  definition: Specific configurations and logic within the linker tailored for a particular
    target architecture or operating system.
- term: foreign input
  definition: An input object file that does not match the expected format or architecture
    of the target system.
- term: retargeted output
  definition: An output file format that has been changed from the default or expected
    format, often specified by a linker script.
- term: XCOFF
  definition: Extended Common Object File Format, a file format used on IBM AIX systems.
- term: magic sections
  definition: Special sections within an object file format (like XCOFF) that hold
    metadata or control information required by the linker.
- term: link hash table
  definition: A data structure used by the linker to store and quickly access symbol
    information.
series_id: 'binutils:bfd: fix aix after-allocation crashes on foreign and retargeted
  inputs'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261024095819.1905597-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-24'
is_stub: false
stub_reason: ''
---

This series of patches addresses crashes occurring in AIX linker emulations when processing foreign inputs or when the output format is retargeted via a linker script. Previously, the `bfd_xcoff_build_dynamic_sections` function would crash due to dereferencing NULL magic sections (for foreign inputs) or accessing a generic hash table as if it were an XCOFF hash table (for retargeted outputs). The patches add checks for NULL magic sections and verify the output format before proceeding, ensuring stable linking and a new regression test validates these fixes.
