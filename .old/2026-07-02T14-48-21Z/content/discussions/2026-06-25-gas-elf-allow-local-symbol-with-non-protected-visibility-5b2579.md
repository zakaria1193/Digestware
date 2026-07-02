---
project: binutils
subsystem: gas/elf
patch_id: null
tags:
- ELF
- gas
- symbols
- visibility
- ABI
discussion_id: e43bc9d8-260e-46f1-9afc-c52eacd4ac60@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] gas/ELF: Allow local symbol with non-protected visibility'
headline: 'Gas/ELF: Allow local symbol with non-protected visibility'
tldr: This patch re-enables assigning non-default visibility to local symbols in gas/ELF,
  partially reverting a previous change that warned against this practice.
proposer: Alan Modra <amodra@gmail.com>
consensus: Under Review
outcome: under_review
impact_score: 5
sentiment_score: 8
technical_tradeoffs:
- Restores flexibility in assigning non-default visibility to local symbols, potentially
  simplifying certain low-level coding patterns.
- Removes a warning that previously flagged potentially unusual or unintended symbol
  visibility settings, which could hide subtle issues if misused.
- Requires careful testing across various architectures to ensure the change does
  not introduce linking or loading regressions.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes a partial revert to allow local symbols to have non-protected
    visibility without warning, asking for confirmation of broad target testing.
  quote: OK if this has been tested over a reasonable set of targets, ie. not just
    x86.
- author: H.J. Lu <hjl.tools@gmail.com>
  role: reviewer
  position: Agrees with the proposed change and its partial revert of a previous commit
    which warned about local symbols with non-protected visibility.
  quote: null
primer_expert: In ELF (Executable and Linkable Format) binaries, symbols represent
  functions or data. Each symbol has a 'visibility' attribute that controls how it
  behaves during linking and loading. 'Local' symbols are typically not visible outside
  their compilation unit, while 'protected' visibility marks a symbol as visible externally
  but not subject to dynamic linking interposition. This patch touches `gas/ELF`,
  the GNU Assembler's backend for ELF, and specifically concerns how it handles symbol
  visibility for local symbols within `elf_adjust_symtab`.
primer_general: When a computer program is built, different parts are compiled separately
  and then linked together. 'Symbols' are like named markers for functions or data
  within these parts. Each symbol has a 'visibility' setting that tells the linker
  how it can be accessed or shared. Normally, 'local' symbols are meant to be confined
  to the part of the code they are in. This proposal is about a change in how the
  assembler (a tool that turns human-readable assembly code into machine code) handles
  the 'visibility' of these local symbols, specifically allowing them to be marked
  with a non-default visibility without triggering a warning. The impact is on the
  flexibility of how developers can define and manage symbols in their assembly code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ajyEmjX6pTQ8n-gz@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This patch partially reverts a previous commit that introduced a warning for local symbols with non-default visibility in the `gas/ELF` backend. The proposed change specifically allows local symbols to have non-protected visibility without generating a warning. The reviewer expresses a desire for broader testing across various target architectures to ensure the change does not introduce regressions.
