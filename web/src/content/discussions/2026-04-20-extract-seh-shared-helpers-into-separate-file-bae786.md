---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gas
- assembler
- seh
- code organization
discussion_id: 9f4c08db-358a-4a3b-902f-77b139e937b0@suse.com
source_type: public_inbox
title: 'Re: [PATCH v7 2/3] Extract SEH shared helpers into separate file.'
headline: Extract SEH shared helpers into separate file
tldr: The patch extracts SEH shared helpers into a separate file, with review comments
  about copyright year and whitespace.
stakes: Affects the organization of the assembler's code.  General toolchain developers
  may be impacted if they need to modify or understand SEH handling.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improves code organization and maintainability.
- No functional changes.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Suggests copying the year range from the original file and adding a blank
    line for readability.
  quote: I think the year range from the original file needs copying here. You move
    code rather than introducing in anew.
primer_expert: This patch modifies the `gas` assembler, specifically the code dealing
  with SEH (Structured Exception Handling) for COFF object files. SEH is a mechanism
  used on Windows to handle exceptions. The patch extracts shared helper functions
  into `gas/config/obj-coff-seh-shared.c`. This doesn't change functionality but improves
  code organization.
primer_general: The assembler (`gas`) is a tool that translates human-readable assembly
  code into machine code that a computer can understand. This patch is about rearranging
  the assembler's internal code related to exception handling (a way for programs
  to deal with errors). The change makes the code easier to maintain and understand
  by grouping related functions into a separate file.
series_id: binutils:extract seh shared helpers into separate file
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9f4c08db-358a-4a3b-902f-77b139e937b0@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This patch series reorganizes the assembler code by extracting shared helpers for SEH (Structured Exception Handling) into a separate file. A reviewer points out minor issues like missing copyright year and missing blank line.
