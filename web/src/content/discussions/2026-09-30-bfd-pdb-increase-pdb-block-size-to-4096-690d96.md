---
project: binutils
subsystem: bfd/pdb
patch_id: null
tags:
- pdb
- linker
- debugging
- performance
- binutils
discussion_id: 20260930193657.733-12-oleg.tolmatcev@gmail.com
source_type: public_inbox
title: '[PATCH] bfd/pdb: Increase the PDB block size to 4096'
headline: 'bfd/pdb: Increase PDB block size to 4096'
tldr: Increases PDB block size to 4096 bytes to support larger files and align with
  MSVC.
proposer: Oleg Tolmatcev <oleg.tolmatcev@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases memory usage for PDB structures due to larger block sizes, but enables
  support for much larger debug information files.
exchanges: []
primer_expert: This change in binutils' BFD library modifies the internal block size
  used for PDB files. The original 1024-byte blocks were insufficient for larger PDBs
  because the stream directory's block map, being a single block itself, could only
  reference a limited number of subsequent blocks. Increasing this to 4096 bytes (the
  size used by Microsoft's compiler) allows for significantly larger PDB files, up
  to approximately 4 GB, and aligns with common tooling expectations.
primer_glossary:
- term: PDB
  definition: Program Database. A file format used by Microsoft for storing debugging
    and project-related information for Microsoft Windows applications.
- term: BFD
  definition: Binary File Descriptor library. A library used by GNU software, including
    binutils, to abstract away differences between various object file formats.
- term: MSVC
  definition: Microsoft Visual C++. A suite of C and C++ development tools from Microsoft,
    which includes a compiler and linker.
- term: stream directory
  definition: In the PDB format, this is a data structure that maps logical block
    numbers to their physical locations within the PDB file.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930193657.733-12-oleg.tolmatcev@gmail.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch increases the PDB block size in the BFD library from 1024 to 4096 bytes. The previous 1024-byte block size limited PDB files to approximately 64 MB due to the block map's capacity. The new size, matching MSVC's standard, increases the limit to about 4 GB and resolves issues with tools like llvm-pdbutil that rejected larger files.
