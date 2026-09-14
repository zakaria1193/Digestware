---
project: binutils
subsystem: bfd
patch_id: null
tags:
- bfd
- pe
- refactoring
- maintainability
discussion_id: 20260913123323.9734-5-jon.turney@dronecode.org.uk
source_type: public_inbox
title: '[PATCH 4/4] bfd: pe: Introduce COFF_WITH_pe32plus define'
headline: 'bfd: pe: Introduce COFF_WITH_pe32plus define'
tldr: Define COFF_WITH_pe32plus for PE32+ formats to simplify conditional logic.
proposer: Jon Turney <jon.turney@dronecode.org.uk>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improves code readability and maintainability by centralizing PE32+ format checks.
- Reduces the potential for errors in conditional logic related to PE file formats.
exchanges: []
primer_expert: This patch refactors `bfd/peXXigen.c` by introducing `COFF_WITH_pe32plus`.
  Previously, multiple `COFF_WITH_pe*` defines were used to distinguish PE32+ targets.
  This new macro simplifies conditional logic that differentiates between PE32 and
  PE32+ formats, making code that handles these differences more readable and less
  prone to copy-paste errors. It's a code hygiene improvement.
primer_glossary:
- term: PE32+
  definition: A 64-bit version of the Portable Executable (PE) file format, commonly
    used for executables on Windows.
- term: preprocessor macro
  definition: A directive in C/C++ code that the preprocessor expands before compilation,
    often used for conditional compilation or defining constants.
- term: conditional logic
  definition: Code that executes different paths based on whether certain conditions
    are true or false, often implemented using `#if`, `#ifdef`, etc.
series_id: 'binutils:bfd: pe: introduce coff_with_pe32plus define'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260913123323.9734-5-jon.turney@dronecode.org.uk
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

This patch introduces a new preprocessor macro, `COFF_WITH_pe32plus`, to consolidate checks for PE32+ (64-bit) formats within `bfd/peXXigen.c`. This aims to replace error-prone, long lists of specific format defines with a single, clearer indicator, making the code more maintainable and reducing the likelihood of errors when handling PE32/PE32+ differences.
