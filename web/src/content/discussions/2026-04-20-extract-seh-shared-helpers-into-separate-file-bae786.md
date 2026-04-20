---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gas
- seh
- coff
- refactoring
discussion_id: 9f4c08db-358a-4a3b-902f-77b139e937b0@suse.com
source_type: public_inbox
title: 'Re: [PATCH v7 2/3] Extract SEH shared helpers into separate file.'
headline: Extract SEH shared helpers into separate file.
tldr: This patch extracts shared helpers for SEH (Structured Exception Handling) into
  a separate file to avoid code duplication.
stakes: Improves code organization and maintainability by reducing code duplication.  This
  makes it easier to understand and modify the code related to SEH.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Improves code organization and reduces duplication.
- May introduce minor integration issues if not handled carefully.
- Has a small risk of introducing regressions.
primer_expert: This patch refactors the binutils assembler (gas) by extracting SEH-related
  helper functions into `gas/config/obj-coff-seh-shared.c`. SEH is a mechanism for
  handling exceptions in Windows binaries. COFF is a format for object code and executables.
  The change aims to improve code reuse.
primer_general: Structured Exception Handling (SEH) is a mechanism used by Windows
  to handle errors and exceptions during program execution.  The GNU Assembler (`gas`)
  is part of binutils, and it translates assembly code into object files, which are
  often in COFF format on Windows. This patch reorganizes the assembler's code to
  make it more modular.
series_id: binutils:extract seh shared helpers into separate file
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9f4c08db-358a-4a3b-902f-77b139e937b0@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This patch moves shared helpers for SEH (Structured Exception Handling) related to the COFF object file format into a separate file.  The goal is to reduce code duplication and improve maintainability. The reviewer noted a minor issue related to the copyright year range and a missing blank line.
