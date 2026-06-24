---
project: binutils
subsystem: gas/elf
patch_id: null
tags:
- elf
- binutils
- gas
- symbols
- linking
discussion_id: bcd40b22-b90f-4334-8ab4-e8afeea2a6a9@suse.com
source_type: public_inbox
title: '[PATCH] gas/ELF: Allow local symbol with hidden visibility'
headline: ELF allows local symbols with hidden visibility, clarifies spec interpretation
tldr: This patch clarifies that ELF permits local symbols to have hidden visibility,
  correcting a misinterpretation of the ELF specification regarding protected and…
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 5
technical_tradeoffs:
- Clarifying the interpretation of ELF symbol visibility might expose existing code
  that implicitly relied on the previous, stricter interpretation, potentially requiring
  adjustments.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Asserts that ELF local symbols can have hidden visibility, distinct from
    the `STB_LOCAL` and `STV_PROTECTED` prohibition, based on a careful reading of
    the ELF specification.
  quote: A symbol defined in the current component is hidden if its name is not visible
    to other components. Such a symbol is necessarily protected.
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Questions the rationale of allowing `STB_LOCAL` with `STV_HIDDEN` while
    disallowing it for `STV_PROTECTED`, suggesting a potential inconsistency.
  quote: IOW what you're suggesting as interpretation is that while STV_PROTECTED
    and STB_LOCAL may not combine, the visibility-wise more restricting STV_HIDDEN
    may combine with STB_LOCAL? Make no sense
primer_expert: The ELF (Executable and Linkable Format) specification defines various
  attributes for symbols, including `Binding` (e.g., `STB_LOCAL`, `STB_GLOBAL`) and
  `Visibility` (e.g., `STV_DEFAULT`, `STV_HIDDEN`, `STV_PROTECTED`). This discussion
  revolves around the interaction between `STB_LOCAL` binding and `STV_HIDDEN` visibility.
  The ELF specification explicitly states that `STB_LOCAL` symbols cannot have `STV_PROTECTED`
  visibility. However, `STV_HIDDEN` symbols are defined as 'necessarily protected.'
  The core debate is whether the `STB_LOCAL` restriction for `STV_PROTECTED` implicitly
  applies to `S…
primer_general: When you compile a program, the compiler generates a list of "symbols"
  that represent functions and variables. The way these symbols can be seen and used
  by other parts of the program or other programs is controlled by their "binding"
  and "visibility." A `local` symbol (`STB_LOCAL`) is only visible within its own
  compiled file. `Hidden` visibility (`STV_HIDDEN`) means a symbol is not visible
  to other components (like shared libraries) and cannot be replaced by another symbol
  with the same name. `Protected` visibility (`STV_PROTECTED`) means a symbol *is*
  visible to others but cannot be replaced. The ELF specification (a standard for
  executable files) says that `local` symbols cannot be `protected`. This discussion
  is about whether a `local` symbol can also be `hidden`. Because `hidden` symbols
  are described as being "necessarily protected," there's an ambiguity in the spec.
  This patch argues that `local` and `hidden` should be allowed together, as it provides
  useful control for develo…
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOrdHFXyxhZhfmzrBnJFWW6ji+Mam0SPjoqASxufpX2LaA@mail.gmail.com
bugzilla_url: null
date: '2026-06-24'
is_stub: false
---

This discussion clarifies an interpretation of the ELF specification regarding symbol visibility, specifically asserting that local (`STB_LOCAL`) symbols *can* have hidden (`STV_HIDDEN`) visibility. The proposer argues that the spec's disallowance of `STB_LOCAL` with `STV_PROTECTED` does not extend to `STV_HIDDEN`, as `STV_HIDDEN` implies protection. This patch intends to reflect this understanding in the GNU Assembler (`gas`).
