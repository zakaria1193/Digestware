---
project: binutils
subsystem: bfd/pdb
patch_id: null
tags:
- linker
- PDB
- debugging
- file format
- performance
discussion_id: 5b04ffc9-dc53-424c-903f-56375bcf248b@suse.com
source_type: public_inbox
title: 'Re: [PATCH] bfd/pdb: Increase the PDB block size to 4096'
headline: 'bfd/pdb: Increase the PDB block size to 4096'
tldr: Increases the PDB block size in Binutils from 1024 bytes to 4096 bytes to support
  larger PDB files, aligning with MSVC usage.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables support for larger PDB files, crucial for complex projects.
- Increases the minimum storage overhead for very small PDB files.
- Aligns Binutils' PDB implementation with common practices (MSVC), improving compatibility.
exchanges:
- author: Oleg Tolmatcev
  role: proposer
  position: Proposes increasing PDB block size to 4096 to support larger PDB files
    and overcome limitations with current 1024-byte blocks.
  quote: 'The block map of the stream directory is itself a single block, so with

    1024 byte blocks it can only hold 256 block numbers, which limits a PDB

    file to about 64 MB.  Writing a larger one fails partway through and

    leaves a truncated file behind, which llvm-pdbutil rejects with "Too

    many directory blocks".'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Questions the necessity of a fixed large block size for smaller PDBs and
    asks for proof of MSVC's usage, suggesting a dynamic block size.
  quote: 'That sounds pretty limiting, making me wonder why it was done like that.
    Mark?



    The claim on what MSVC uses could do with some reference / proof. And

    then, while surely many will say disk space is cheap, isn''t this a little

    wasteful for smallish PDBs? I.e. ... may this want to become dynamically determined?'
primer_expert: This change addresses a limitation in Binutils' PDB writing capabilities
  where the maximum PDB file size is capped at approximately 64 MB due to the use
  of 1024-byte blocks. The stream directory's block map, being a single block itself,
  can only reference 256 sub-blocks, constraining the total file size. The proposal
  is to increase this block size to 4096 bytes, aligning with Microsoft's Visual C++
  compiler usage and extending the maximum supported PDB size to around 4 GB. This
  is essential for larger projects that generate substantial debugging information.
primer_glossary:
- term: PDB
  definition: Program Database. A file format used by Microsoft's compilers and debuggers
    to store information about program symbols and types, often used for debugging
    C/C++ code.
- term: block size
  definition: The fundamental unit of data allocation and transfer within the PDB
    file structure. A larger block size allows for larger files but may be less efficient
    for very small files.
- term: stream directory
  definition: A data structure within the PDB format that manages access to different
    streams (logical data segments) within the PDB file.
- term: block map
  definition: A data structure within the PDB format that maps logical block addresses
    to physical block addresses on disk.
- term: MSVC
  definition: Microsoft Visual C++, Microsoft's C and C++ compiler.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/5b04ffc9-dc53-424c-903f-56375bcf248b@suse.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

Oleg Tolmatcev proposes increasing the PDB block size in Binutils from 1024 bytes to 4096 bytes. The current 1024-byte block size limits PDB files to approximately 64 MB due to the stream directory's block map size, causing LLVM tools to reject larger files. Increasing the block size to 4096, which matches MSVC's usage, raises this limit to around 4 GB.
