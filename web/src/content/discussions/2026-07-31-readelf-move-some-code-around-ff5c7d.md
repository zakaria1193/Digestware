---
project: binutils
subsystem: readelf
patch_id: null
tags:
- refactoring
- readelf
- code organization
discussion_id: e9b5fffb-b982-4d1d-b507-acbec117d086@suse.com
source_type: public_inbox
title: 'readelf: move some code around'
headline: 'readelf: move some code around'
tldr: Refactors readelf.c to improve code organization and reduce forward declarations.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improves code readability and maintainability by reducing forward declarations and
  grouping related functions.
- May require careful review to ensure no functional changes are introduced by the
  code rearrangement.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Proposes to reorganize functions in `readelf.c` to group related code
    and reduce forward declarations.
  quote: 'Avoid the need to forward-declare get_program_headers() and

    get_dynamic_section(); put them right after their bitness-dependent

    helpers (i.e. after the readelf-nn.c inclusion point). Then, to keep

    related things together, move get_section_headers() and get_elf_symbols()

    as well.'
- author: Jan Beulich
  role: proposer
  position: Notes that using function pointers for `get_elf_symbols` might be an alternative
    but would not extend well to other functions, making the current reorganization
    a more practical approach.
  quote: 'One aspect I noticed: Instead of the trivial get_elf_symbols() wrapper we

    could use a function pointer. That, however, already wouldn''t quite extend

    to get_section_headers() and get_dynamic_section(), let alone

    get_program_headers(), so would - overall - be of little help.'
primer_expert: This patch series refactors `binutils/readelf.c` by rearranging function
  definitions. The goal is to improve code locality and reduce the number of forward
  declarations. Bitness-specific helper functions are now placed directly before the
  main functions they support (e.g., `get_program_headers`), and related functions
  like `get_section_headers` and `get_elf_symbols` are also moved to keep related
  code together. The `validate_section_info` function and its helper are also relocated
  to avoid forward declarations.
primer_glossary:
- term: readelf
  definition: A utility that displays information about ELF (Executable and Linkable
    Format) files.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for object
    files used in Unix-like systems.
- term: forward declaration
  definition: A declaration of an identifier (like a function or variable) before
    it is fully defined, allowing it to be used in the interim.
- term: bitness-dependent
  definition: Code that behaves differently or is specifically implemented for different
    data sizes, such as 32-bit or 64-bit.
- term: section headers
  definition: Data structures within an ELF file that describe each section (e.g.,
    code, data, symbols).
- term: program headers
  definition: Data structures within an ELF file that describe segments, which are
    mappings of sections into memory for execution.
- term: dynamic section
  definition: An ELF section containing information needed for dynamic linking and
    runtime execution.
series_id: 'binutils:readelf: move some code around'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/e9b5fffb-b982-4d1d-b507-acbec117d086@suse.com
bugzilla_url: null
date: '2026-07-31'
is_stub: false
stub_reason: ''
---

This patch series for the `readelf` utility reorganizes functions within `readelf.c` to enhance code structure and minimize the need for forward declarations. Specifically, bitness-dependent helper functions are now placed immediately before their respective main functions (`get_program_headers`, `get_dynamic_section`, `get_section_headers`, `get_elf_symbols`), grouping related code. This change also eliminates the forward declaration for `validate_section_info` by defining it alongside its helper.
