---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- documentation
- assembler
- ELF
- section
discussion_id: 20260516003806.456403-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH] gas: Document @ and % as interchangeable for type argument in .section'
headline: 'gas: Document @ and % as interchangeable for type argument in .section'
tldr: Clarifies that the assembler accepts both `@` and `%` characters when specifying
  section types in the `.section` directive.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Improved documentation clarity at the cost of a small documentation update.
exchanges: []
primer_expert: The GNU assembler (`gas`) uses the `.section` directive to define sections
  in ELF object files. The directive accepts a `type` argument, which can be specified
  using either the `@` or `%` character. This patch clarifies this detail in the `gas`
  documentation (gas/doc/as.texi).
primer_general: The GNU Assembler (`gas`) translates assembly language source code
  into object code.  A key part of this process involves defining sections in the
  output file, such as `.text` for code and `.data` for initialized data.  The `.section`
  directive allows developers to create custom sections and specify their types. This
  type can be represented using either `@` or `%` followed by a numeric value that
  corresponds to an ELF section type. This patch clarifies that the assembler accepts
  both characters, improving usability.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260516003806.456403-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-05-16'
is_stub: false
---

This patch updates the assembler documentation to explicitly state that both the `@` and `%` characters can be used interchangeably when specifying the type argument in the `.section` directive for ELF files. This avoids confusion for users, especially on targets where `@` might be interpreted as the start of a comment. The change improves the clarity of the documentation without altering the assembler's functionality.
