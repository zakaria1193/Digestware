---
project: binutils
subsystem: binutils
patch_id: null
tags:
- readelf
- memory leak
- elf
- archive
discussion_id: f59bb110-db13-45fb-aa0b-3e75f65a109c@suse.com
source_type: public_inbox
title: 'Re: [PATCH] binutils: avoid leaking section header pointers'
headline: 'binutils: avoid leaking section header pointers'
tldr: Addresses a memory leak in readelf when processing thin archives by correcting
  section header pointer allocation.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: needs_revision
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- The proposed fix aims to prevent memory leaks.
- Discussion involves clarifying the exact conditions for the leak and the correctness
  of the proposed solution.
exchanges:
- author: Alhuda Khan
  role: contributor
  position: Reported a memory leak in `readelf` when dumping a thin archive of ELF
    objects, where `ElfXX(_get_section_headers)` overwrites previous allocations.
  quote: 'readelf leaks memory when dumping a thin archive of ELF objects.

    > ElfXX(_get_section_headers) allocates filedata->orig_section_headers on

    > every non-probe call, so when it runs more than once for the same

    > Filedata the earlier allocation is overwritten and lost.'
- author: Jan Beulich
  role: reviewer
  position: Questions the necessity and correctness of the proposed fix, arguing that
    `get_section_headers` already handles cases where section headers are present
    and points out an unrelated indentation issue in the patch.
  quote: 'There must be more to this: get_section_headers() returns right away when

    > filedata->section_headers is already non-NULL. process_object() has an

    > example where that''s indeed thrown away, but the earlier call passed

    > "true" to get_section_headers() as 2nd argument (i.e.

    > ->orig_section_headers wouldn''t have been set there).


    Why are you, btw, screwing up indentation of this unrelated line?'
primer_expert: The `readelf` utility, specifically within its `ElfXX(_get_section_headers)`
  function, has a potential memory leak when processing thin archives. The function
  allocates `filedata->orig_section_headers` on non-probe calls. If `_get_section_headers`
  is called multiple times for the same `Filedata` without the `probe` flag, earlier
  allocations might be overwritten and lost. The patch attempts to fix this by adding
  a check `filedata->orig_section_headers == NULL` to the allocation condition. However,
  reviewer Jan Beulich suggests the function already has logic to return early if
  section headers a…
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files.
- term: Thin archive
  definition: A type of archive file where member files are not actually duplicated;
    instead, they refer to a single copy of the file elsewhere.
- term: ELF
  definition: Executable and Linkable Format.
- term: Section header
  definition: Metadata within an ELF file that describes the layout and properties
    of a section.
- term: Filedata
  definition: A structure likely used by binutils to hold information about an input
    file being processed.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/f59bb110-db13-45fb-aa0b-3e75f65a109c@suse.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This discussion revolves around a memory leak in the `readelf` utility when processing thin archives. The original patch by Alhuda Khan aimed to fix this by correcting how section header pointers were allocated. Jan Beulich questions the original patch's premise, suggesting that `ElfXX(_get_section_headers)` already returns early if section headers are present. He also points out an unrelated indentation change in the proposed fix and asks for clarification on the exact scenario causing the leak.
