---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- pdb
- linker
- debugging
- codeview
- specification
discussion_id: 6602570a-365e-4df1-a92e-e9476a9186cd@harmstone.com
source_type: public_inbox
title: 'Re: [PATCH] ld/pdb: Terminate the string list in S_ENVBLOCK'
headline: 'ld/pdb: Terminate the string list in S_ENVBLOCK'
tldr: Mark Harmstone asks Oleg Tolmatcev to verify if a PDB string list termination
  issue observed in llvm-pdbutil is also present in Microsoft's cvdump.exe.
proposer: Mark Harmstone <mark@harmstone.com>
consensus: Under Review
outcome: under_review
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Fixing the PDB string list termination relies on reverse-engineering or observed
  behavior due to the lack of a formal specification, potentially leading to compatibility
  issues with other PDB tools.
exchanges:
- author: Mark Harmstone <mark@harmstone.com>
  role: proposer
  position: Requests verification of a PDB string list termination bug in Microsoft's
    `cvdump.exe` to ensure the patch correctness, given the absence of a formal PDB
    specification.
  quote: null
- author: Oleg Tolmatcev <tolmatcev@gmail.com>
  role: contributor
  position: Explains that LLVM's `CodeViewRecordIO::mapStringZVectorZ` consumes NUL-terminated
    strings until an empty string is encountered and explicitly terminates the list
    with a zero byte.
  quote: null
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Previously asked for a pointer to the PDB specification that mandates
    this termination, indicating a need for formal backing for the change.
  quote: null
primer_expert: This discussion concerns a subtle bug in the binutils linker's handling
  of PDB (Program Database) files, specifically within the `ld/pdb.c` module. The
  issue arises from an improperly terminated string list in S_ENVBLOCK symbols, which
  can cause tools like `llvm-pdbutil` to misinterpret the data. The core of the problem
  is the lack of a definitive PDB specification, forcing reliance on observed behavior
  in tools like LLVM's implementation and Microsoft's `cvdump.exe`.
primer_glossary:
- term: PDB
  definition: Program Database, a file format used by Microsoft development tools
    to store information about program symbols and debugging data.
- term: S_ENVBLOCK
  definition: A specific type of CodeView symbol record used to store environment
    block information.
- term: ld/pdb.c
  definition: The source file within binutils responsible for handling the creation
    and manipulation of PDB files during the linking process.
- term: llvm-pdbutil
  definition: A utility from the LLVM project for inspecting and manipulating PDB
    files.
- term: cvdump.exe
  definition: A Microsoft utility for dumping and analyzing CodeView debug information,
    often considered a de facto reference for PDB structure.
- term: CodeView
  definition: Microsoft's debugging information format, often stored in PDB files.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/6602570a-365e-4df1-a92e-e9476a9186cd@harmstone.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

Mark Harmstone is reviewing patches related to terminating string lists in S_ENVBLOCK symbols within the PDB format. Oleg Tolmatcev has provided an explanation and a link to LLVM's implementation, which explicitly terminates the list with a zero byte. Harmstone points out the lack of a formal PDB specification and asks Tolmatcev to confirm if the observed behavior is also present in Microsoft's `cvdump.exe` to ensure the fix is correct and not specific to LLVM's implementation.
