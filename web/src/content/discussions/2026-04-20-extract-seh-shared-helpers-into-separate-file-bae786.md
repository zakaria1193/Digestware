---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- seh
- coff
- refactoring
- copyright
discussion_id: 9f4c08db-358a-4a3b-902f-77b139e937b0@suse.com
source_type: public_inbox
title: 'Re: [PATCH v7 2/3] Extract SEH shared helpers into separate file.'
headline: Extract SEH shared helpers into separate file.
tldr: Reviewer requests updates to copyright year and code consistency in the extracted
  SEH helper file.
stakes: Correct copyright information and code consistency improve maintainability
  and avoid legal issues.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improved code organization and reusability.
- Potential for introducing errors during the extraction process.
- Increased complexity in build system due to the addition of a new file.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Requests that the copyright year range be copied, a blank line be added,
    and points out what appears to be inconsistencies.
  quote: 'I think the year range from the original file needs copying here. You move
    code rather than introducing in anew.


    Nit: Blank line between these two please.


    Yet then - I can''t spot the original of the latter of the two lines.

    You''re only moving code, aren''t you? Otherwise you would have mentioned

    changes you make along the road?'
primer_expert: This patch refactors the binutils codebase by extracting shared helper
  functions for SEH (Structured Exception Handling) related to COFF object file format
  into a separate file (`obj-coff-seh-shared.c`). This aims to improve code organization
  and reusability across different architectures. The reviewer is focusing on copyright
  and code consistency issues related to the extraction process.
primer_general: Binutils is a collection of tools for working with binary files, such
  as executables and object code. SEH (Structured Exception Handling) is a mechanism
  used by Windows to handle exceptions. COFF (Common Object File Format) is a file
  format for object code and executables. The patch reorganizes the binutils code
  related to SEH in COFF files and the review focuses on ensuring the reorganization
  is done correctly from a copyright and code consistency perspective.
series_id: binutils:extract seh shared helpers into separate file
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9f4c08db-358a-4a3b-902f-77b139e937b0@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This patch extracts shared helpers for SEH (Structured Exception Handling) into a separate file. The reviewer notes that the copyright year range needs to be copied from the original file, requests a blank line for readability, and points out inconsistencies where code seems to be added rather than moved.
