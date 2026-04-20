---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gas
- SEH
- COFF
- exception handling
discussion_id: 9f4c08db-358a-4a3b-902f-77b139e937b0@suse.com
source_type: public_inbox
title: 'Re: [PATCH v7 2/3] Extract SEH shared helpers into separate file.'
headline: Extract SEH shared helpers into separate file.
tldr: This patch extracts shared SEH helpers into a separate file, with minor issues
  concerning copyright year and code style being addressed.
stakes: This change improves code organization and maintainability within the binutils
  project. Developers working on exception handling or COFF object format may be interested.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Extracting code into a separate file improves modularity and reusability.
- Incorrectly handling copyright notices could lead to legal issues.
- Minor code style issues can impact readability and maintainability.
primer: Structured Exception Handling (SEH) is a mechanism used by Windows to handle
  exceptions. COFF (Common Object File Format) is a file format used for executables,
  object code, and shared libraries. gas is the GNU Assembler, part of binutils.
series_id: binutils:extract seh shared helpers into separate file
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9f4c08db-358a-4a3b-902f-77b139e937b0@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This patch extracts shared Structured Exception Handling (SEH) helpers into a separate file named `obj-coff-seh-shared.c`. The reviewer noted that the copyright year range from the original file needs to be copied, and a blank line is missing. These minor adjustments may be made during commit.
