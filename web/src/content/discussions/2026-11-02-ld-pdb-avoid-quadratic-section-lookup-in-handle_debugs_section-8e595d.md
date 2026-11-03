---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- linker
- pdb
- performance
- optimization
- windows
discussion_id: 20261102225947.1725-2-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: 'ld/pdb: Avoid quadratic section lookup in handle_debugs_section'
headline: 'ld/pdb: Avoid quadratic section lookup in handle_debugs_section'
tldr: Optimizes symbol-to-section lookup in `handle_debugs_section` for --pdb linking,
  reducing linkage time.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: 9
technical_tradeoffs:
- The optimization improves linking speed for PDB generation at the cost of slightly
  more complex code in `handle_debugs_section` and related functions.
- Using hash tables for section lookups introduces a small constant overhead per lookup,
  but drastically reduces the overall complexity compared to linear scans.
exchanges:
- author: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
  role: proposer
  position: Submitted a patch to optimize section lookup in `handle_debugs_section`
    by using a hash table (`coff_section_from_bfd_index`) instead of linear scans.
  quote: 'To map symbols to their sections, handle_debugs_section scanned all

    symbols once per section, for every .debug$S section.  With many

    sections and symbols per object, this took about half of ld''s time

    when linking with --pdb.


    Use coff_section_from_bfd_index, which looks sections up in a hash

    table cached on the BFD.'
- author: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
  role: contributor
  position: 'Follow-up patch: Skips auxiliary symbol entries in `handle_debugs_section`
    which previously caused missed lookups and fallback to linear scans, impacting
    performance.'
  quote: "handle_debugs_section treated every raw symbol table entry, including\n\
    auxiliary entries, as a symbol and looked up a section for its n_scnum.\nIn auxiliary\
    \ entries that field holds unrelated data, so the lookup\noften missed and fell\
    \ back to a linear scan over all sections.  With\nobjects containing thousands\
    \ of sections this took about 10% of the\nlink time for a large executable with\
    \ --pdb.\n\nld/\n\t*…"
- author: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
  role: contributor
  position: Introduced a fix to round up memory allocation to a power of two in `memory_bwrite`
    and `memory_bseek`, preventing quadratic reallocations when building large in-memory
    BFDs for PDB streams.
  quote: 'memory_bwrite and memory_bseek grew the buffer in 128 byte steps, so

    building a large in-memory BFD out of many small writes reallocated and

    copied the whole buffer over and over.  This made writing PDB streams

    quadratic: linking a 235 MB executable with --pdb spent more than half

    of its time in realloc.


    Round the allocation up to a power of two instead.'
- author: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
  role: contributor
  position: Optimized `pecoff_checksum_contents` by reading the output file in 64
    KB chunks instead of byte-by-byte, significantly reducing the time spent calculating
    PE/COFF checksums.
  quote: 'pecoff_checksum_contents read the output file back one byte at a time,

    seeking before every byte and passing each byte to the hash function

    separately.  For a 235 MB executable this took about 15% of the link

    time.


    Read the file in 64 KB chunks instead.'
- author: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
  role: contributor
  position: Corrected `handle_debugs_section` to use `bfd_coff_symesz` for stepping
    through the symbol table, addressing an issue with 20-byte entries in PE bigobj
    files instead of the standard 18 bytes.
  quote: 'handle_debugs_section stepped through the raw COFF symbol table using

    sizeof (struct external_syment), but symbol table entries in

    pe-bigobj files are 20 bytes rather than 18.  Use bfd_coff_symesz

    instead.


    Run the C13 line info test a second time with objects assembled with

    -mbig-obj on x86.'
- author: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
  role: contributor
  position: Ensures `symbols` and `sectlist` arrays in `handle_debugs_section` are
    allocated with `xcalloc` to prevent reading uninitialized memory for malformed
    objects.
  quote: 'handle_debugs_section only fills in symbols and sectlist for primary

    symbols with a positive section number, so a relocation in a malformed

    object referring to any other symbol read uninitialized memory.

    Allocate both arrays with xcalloc; the relocate_section routines skip

    relocations against a NULL section.'
primer_expert: This series of patches addresses performance regressions in the linker
  (`ld`) when generating PDB (Program Database) files for Windows executables, particularly
  affecting the `--pdb` option. The primary issue identified was a quadratic complexity
  in `handle_debugs_section` due to inefficient symbol-to-section mapping. Subsequent
  patches address related performance bottlenecks in memory buffer handling, PE/COFF
  checksum calculation, and correct handling of COFF symbol table entry sizes for
  bigobj files, all contributing to faster linking times for PDB generation.
primer_glossary:
- term: ld/pdb
  definition: Refers to the linker's (ld) support for generating Program Database
    (PDB) files, which are used by Microsoft's tools for debugging information.
- term: handle_debugs_section
  definition: A function within the linker responsible for processing debug sections
    (.debug$S) and mapping symbols to their corresponding sections within an object
    file.
- term: quadratic lookup
  definition: An algorithm's performance characteristic where the execution time grows
    proportionally to the square of the input size. This is generally inefficient
    for large inputs.
- term: coff_section_from_bfd_index
  definition: A function that likely retrieves a section's information from a BFD
    (Binary File Descriptor) object using an index, presumably leveraging a more efficient
    data structure like a hash table.
- term: BFD
  definition: Binary File Descriptor, a library used by GNU tools (like binutils and
    GCC) to abstract the details of various object file formats (e.g., ELF, COFF,
    Mach-O).
- term: auxiliary entries
  definition: In the context of COFF symbol tables, these are entries that provide
    additional information related to a primary symbol, but do not represent a symbol
    themselves. They can contain unrelated data in certain fields.
- term: PE/COFF
  definition: Portable Executable/Common Object File Format. The file format used
    for executables, object code, DLLs, and other files on 64-bit and 32-bit versions
    of Windows.
- term: bigobj
  definition: A modification to the PE/COFF format that increases the number of sections
    and symbols an object file can contain, often used for very large projects.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20261102225947.1725-2-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-11-02'
is_stub: false
stub_reason: ''
---

This patch optimizes the `handle_debugs_section` function in `ld/pdb.c` to avoid a quadratic lookup time when mapping symbols to their sections. Previously, for each .debug$S section, it scanned all symbols, leading to significant overhead with many sections and symbols. The change introduces `coff_section_from_bfd_index` for efficient hash-table-based section lookup, reducing linking time, especially when using the `--pdb` option.
