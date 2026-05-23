---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- documentation
- section
discussion_id: 20260522100809.829774-1-hawkinsw@obs.cr
source_type: public_inbox
title: '[PATCH v2] gas: Clarify documentation about @ and % usage in .section'
headline: 'Gas: Clarify documentation about @ and % usage in .section'
tldr: The documentation for the .section assembler directive is clarified regarding
  the use of @ and % to avoid confusion related to comment characters.
proposer: Will Hawkins <hawkinsw@obs.cr>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- The change is purely documentation and does not affect the functionality of the
  assembler.
- Correct documentation is crucial for usability.
exchanges:
- author: Will Hawkins <hawkinsw@obs.cr>
  role: proposer
  position: Proposes clarifying the documentation for the .section directive regarding
    the use of @ and %.
  quote: 'In the documentation for the .section Assembler Directive for the ELF

    format, clarify the instances where @ and % can be used.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the patch and asks if it needs committing on his behalf.
  quote: Okay, and thanks. I take that this will need committing on your behalf?
- author: Will Hawkins <hawkinsw@obs.cr>
  role: other
  position: Confirms that Jan will be committing the documentation patch.
  quote: null
primer_expert: The `.section` directive in gas is used to define custom sections in
  the output object file.  Assembler directives provide control over the assembly
  process. The ARM assembler uses `@` as the comment character, which necessitates
  a different character for other purposes in specific contexts, such as the `.section`
  directive.
primer_general: An assembler translates human-readable assembly code into machine
  code. Assembly code often uses directives, which are special instructions to the
  assembler itself, rather than instructions that will be executed by the processor.
  The `.section` directive allows developers to define custom sections in the output
  file to organize code and data.  Different architectures and assemblers might use
  different symbols for comments and other special purposes, requiring careful attention
  to syntax.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260522100809.829774-1-hawkinsw@obs.cr
bugzilla_url: null
date: '2026-05-22'
is_stub: false
---

This patch clarifies the documentation for the `.section` assembler directive in the GNU assembler (gas). It explains when to use `@` or `%` characters, especially on targets like ARM where `@` signifies the start of a comment. On such platform, `%` is used instead. It aims to prevent confusion about how to specify section attributes.
