---
project: binutils
subsystem: alpha
patch_id: null
tags:
- binutils
- alpha
- linker
- IFUNC
- relocation
discussion_id: 20260901023318.3503991-10-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 10/11] alpha: reject a non-zero addend on a reference to an IFUNC'
headline: 'alpha: reject a non-zero addend on a reference to an IFUNC'
tldr: Reject non-zero addends for IFUNC references on Alpha to avoid issues with R_ALPHA_IRELATIVE.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Prevents potential runtime errors by rejecting invalid IFUNC references.
- Adds complexity to relocation handling.
- Introduces new test cases for validation.
exchanges: []
primer_expert: This patch modifies `bfd/elf64-alpha.c` and adds test cases to reject
  linker relocations for IFUNC symbols on Alpha when a non-zero addend is present.
  The `R_ALPHA_IRELATIVE` relocation, which is used to resolve IFUNCs, utilizes its
  addend field to store the address of the dynamic resolver. Consequently, any additional
  offset specified in the relocation (a non-zero addend) cannot be accommodated, leading
  to potential errors. The patch ensures these invalid relocations are diagnosed,
  preventing runtime issues.
primer_glossary:
- term: IFUNC
  definition: Indirect Function. A mechanism allowing functions to be resolved at
    runtime, often used for performance optimization or selecting architecture-specific
    implementations.
- term: addend
  definition: An immediate value added to a symbol's value during relocation processing.
- term: R_ALPHA_IRELATIVE
  definition: A dynamic relocation type specific to the Alpha architecture, used for
    resolving indirect function addresses at runtime.
- term: R_ALPHA_LITERAL
  definition: An Alpha-specific relocation type, likely used for referencing literal
    pools.
- term: R_ALPHA_REFQUAD
  definition: An Alpha-specific relocation type, possibly for referencing 64-bit quantities.
- term: dynamic linker
  definition: A system component that resolves dynamic dependencies (shared libraries)
    when a program is loaded into memory or during runtime.
series_id: 'binutils:alpha: diagnose a reference to an ifunc whose place is deleted'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-10-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch enhances the linker's handling of indirect functions (IFUNCs) on the Alpha architecture by rejecting references that include a non-zero addend. The `R_ALPHA_IRELATIVE` relocation, used for IFUNCs, embeds the resolver's address in its addend field, leaving no room for an additional offset. This change prevents potential errors when such references are encountered, particularly in scenarios involving `R_ALPHA_LITERAL` or `R_ALPHA_REFQUAD`, and adds test cases to verify this behavior.
