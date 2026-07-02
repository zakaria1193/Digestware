---
project: binutils
subsystem: binutils/readelf
patch_id: null
tags:
- binutils
- readelf
- elf
commit_hash: 1913e1cb7bf5dce76ffcc2ee4b00d693178bf816
source_type: public_inbox
author: '"H.J. Lu" <hjl@sourceware.org>'
headline: 'readelf: Check for missing DT_REL and DT_RELA dynamic tags'
tldr: readelf now properly errors out when essential relocation dynamic tags are absent.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `process_relocs` function in `readelf.c` needs to ensure that DT_REL
  and DT_RELA dynamic tags are present to correctly parse relocation entries. Previously,
  the code would `abort()` if `rel_type` was `reltype_unknown`, but this did not cover
  the case where the tags themselves were entirely absent. This commit adds an explicit
  check and returns `false` (signaling an error) when these tags are missing, aligning
  with the expected behavior for malformed ELF files.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files, including dynamic sections and relocation information.
- term: DT_REL
  definition: A dynamic tag in an ELF file that specifies the location and size of
    the .rel relocation entries section.
- term: DT_RELA
  definition: A dynamic tag in an ELF file that specifies the location and size of
    the .rela relocation entries section.
- term: dynamic tags
  definition: Key-value pairs in the ELF dynamic section that provide essential information
    for the runtime linker and dynamic loader, such as the locations of symbols, libraries,
    and relocation entries.
- term: relocation entries
  definition: Information in an object file that describes how to modify code or data
    references to point to the correct addresses after linking or loading.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260701222158.CAB224BA2E2A@sourceware.org
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

The `readelf` utility previously did not explicitly check for the presence of DT_REL and DT_RELA dynamic tags, which are crucial for processing relocations. This commit modifies the `process_relocs` function to detect and report an error when these tags are missing, preventing potential issues with malformed ELF files.
