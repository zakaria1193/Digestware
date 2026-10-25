---
project: binutils
subsystem: bfd
patch_id: null
tags:
- aix
- linker
- bfd
- crash
- debugging
discussion_id: 20261024095819.1905597-2-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH 1/3] bfd: do not dereference absent XCOFF magic sections'
headline: 'bfd: do not dereference absent XCOFF magic sections'
tldr: Prevents crashes in AIX linker emulations by checking for NULL magic sections
  before dereferencing them.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Prevents crashes when linking foreign object files to AIX targets.
- Ensures robust handling of absent XCOFF magic sections.
- Improves the stability of the AIX linker emulation.
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Proposes to check for NULL magic sections before dereferencing them in
    `bfd_xcoff_build_dynamic_sections` to prevent crashes when linking foreign inputs.
  quote: These magic sections are created inside xcoff_link_create_extra_sections
    (called by xcoff_link_add_symbols), and only when the input's xvec matches the
    output's. When a foreign input is linked, none of them are created, so all three
    remain NULL.
primer_expert: This patch resolves a crash in the AIX linker's after-allocation hook
  (`bfd_xcoff_build_dynamic_sections`) when linking a foreign (non-XCOFF) object file.
  Because the input is not XCOFF, the magic sections (`linkage_section`, `toc_section`,
  `descriptor_section`) within the link hash table remain NULL. The function then
  proceeds to dereference these NULL pointers when checking `sec->size`, causing a
  segmentation fault. The fix adds a `sec != NULL` check before accessing `sec->size`,
  effectively handling the case where these sections are absent.
primer_glossary:
- term: magic sections
  definition: Special sections within an object file format (like XCOFF) that hold
    metadata or control information required by the linker.
- term: XCOFF
  definition: Extended Common Object File Format, a file format used on IBM AIX systems.
- term: bfd
  definition: The Binary File Descriptor library, used by GNU Binutils for object
    file manipulation.
- term: link hash table
  definition: A data structure used by the linker to store and quickly access symbol
    information.
- term: segmentation fault
  definition: An error that occurs when a program tries to access a memory location
    that it's not allowed to access.
series_id: 'binutils:bfd: do not dereference absent xcoff magic sections'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261024095819.1905597-2-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-10-24'
is_stub: false
stub_reason: ''
---

This patch addresses crashes in AIX linker emulations that occur when linking foreign inputs. In such cases, the XCOFF magic sections (linkage, TOC, descriptor) are not created and remain NULL. The `bfd_xcoff_build_dynamic_sections` function previously dereferenced these NULL pointers when checking their size, leading to a segmentation fault. The fix adds checks for `sec != NULL` before accessing `sec->size`, ensuring the function handles cases with absent magic sections gracefully.
