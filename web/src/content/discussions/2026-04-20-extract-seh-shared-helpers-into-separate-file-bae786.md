---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gas
- assembler
- SEH
- refactoring
discussion_id: 9f4c08db-358a-4a3b-902f-77b139e937b0@suse.com
source_type: public_inbox
title: 'Re: [PATCH v7 2/3] Extract SEH shared helpers into separate file.'
headline: Extract SEH shared helpers into separate file.
tldr: Review comments on a patch extracting SEH shared helpers into a separate file,
  focusing on copyright year and code placement.
stakes: Ensures proper code attribution and maintainability when refactoring.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improved code organization and reusability vs. potential for introducing errors
  during refactoring.
primer_expert: 'This patch refactors the gas assembler by extracting shared SEH (Structured
  Exception Handling) helpers into `obj-coff-seh-shared.c`. The review concerns minor
  details: ensuring correct copyright attribution by carrying over the year range
  from the original code, and verifying the proper placement of code.'
primer_general: The GNU Assembler (gas) translates assembly code into machine code.
  Structured Exception Handling (SEH) is a mechanism for handling errors and exceptions
  in a program. This patch reorganizes the assembler's code by moving SEH-related
  helper functions into a separate file. The review process focuses on ensuring that
  the code is properly attributed and that the changes are made correctly.
series_id: binutils:extract seh shared helpers into separate file
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9f4c08db-358a-4a3b-902f-77b139e937b0@suse.com
bugzilla_url: null
date: '2026-04-20'
---

Jan Beulich reviews a patch that extracts SEH shared helpers into a separate file. The review focuses on ensuring the copyright year range from the original file is copied to the new file. Also the reviewer requests a blank line and seeks clarification of code movement.
