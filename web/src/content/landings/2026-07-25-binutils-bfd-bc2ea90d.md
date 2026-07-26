---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- coff
- relocation
- aarch64
commit_hash: bc2ea90d5d53d2f95f5d50979945b3ef9eee39a3
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Use COFF r_ignore for handled relocations
tldr: Fixes bugs in COFF relocation handling by using `r_ignore` instead of changing
  `r_type` for already-processed relocations, preventing incorrect address emissio…
impact_score: 7
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The COFF backend's relocation handling in BFD has been updated to introduce
  and utilize the `r_ignore` flag within the `internal_reloc` structure. When a target-specific
  `relocate_section` implementation (e.g., `coff_pe_aarch64_relocate_section`) fully
  processes a relocation, it now sets `r_ignore` to true instead of altering the `r_type`.
  The generic `_bfd_coff_generic_relocate_section` is then modified to skip any relocations
  where `r_ignore` is set. This addresses bugs in several targets where inappropriate
  `r_type` changes for already-handled dynamic relocations caused incorrect addresses…
primer_glossary:
- term: COFF
  definition: Common Object File Format, a file format for object code used on many
    Unix-like systems. Binutils interacts with COFF files through its BFD library.
- term: relocation
  definition: The process of updating symbolic references in object code to their
    final addresses when linking or loading. Relocations are instructions for the
    linker on how to modify addresses.
- term: r_type
  definition: A field within a relocation entry that specifies the type of relocation
    to be performed (e.g., absolute address, PC-relative).
- term: r_ignore
  definition: A new flag introduced to indicate that a relocation has already been
    handled by a specific backend function and should be skipped by generic processing.
- term: relocate_section
  definition: A function within a target-specific BFD backend responsible for applying
    relocations to a particular section of an object file.
- term: dynamic relocations
  definition: Relocations that are resolved at runtime by the dynamic linker, typically
    used for shared libraries and position-independent code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260725120746.21D2B4BA2E3C@sourceware.org
date: '2026-07-25'
is_stub: false
stub_reason: ''
---

This commit modifies the COFF relocation handling for aarch64, i386, and x86_64 targets to use the `r_ignore` flag when a backend's `relocate_section` function has already handled a relocation. Previously, these relocations might have had their `r_type` modified, leading to incorrect addresses being emitted for dynamic relocations. Using `r_ignore` clearly marks these relocations as processed by the backend, resolving this issue.
