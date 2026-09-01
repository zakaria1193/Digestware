---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- ifunc
- pic
- relocation
discussion_id: 20260901023318.3503991-6-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 05/11] alpha: emit R_ALPHA_IRELATIVE in PIC links'
headline: 'alpha: emit R_ALPHA_IRELATIVE in PIC links'
tldr: Use R_ALPHA_IRELATIVE for IFUNC references in PIC alpha links to correctly store
  resolver addresses.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Correctly handles IFUNCs in PIC executables.
- Leverages existing memory space for RELATIVE relocations.
exchanges: []
primer_expert: This patch updates the alpha ELF backend to use R_ALPHA_IRELATIVE instead
  of R_ALPHA_RELATIVE for IFUNC references within PIC (Position-Independent Code)
  executables. In a PIC context, an IFUNC reference resolved by the linker would normally
  receive the address of the resolver function. This patch ensures that the correct
  mechanism, R_ALPHA_IRELATIVE, is used to store the actual address returned by the
  IFUNC resolver, leveraging existing space reserved for RELATIVE relocations.
primer_glossary:
- term: PIC
  definition: Position-Independent Code. Code that can be loaded and run at any memory
    address without modification. Essential for shared libraries and modern executable
    security.
- term: IFUNC
  definition: Indirect Function. A mechanism allowing a symbol to resolve to different
    function implementations at runtime, typically chosen by a resolver function.
    Similar to a function pointer but resolved at link or load time.
- term: R_ALPHA_IRELATIVE
  definition: An Alpha ELF relocation type used in dynamic linking to calculate the
    final address of a symbol by adding the load address of the shared object to the
    symbol's addend. For IFUNCs, it stores the address returned by the resolver.
- term: R_ALPHA_RELATIVE
  definition: An Alpha ELF relocation type used in dynamic linking to calculate the
    final address of a symbol by adding the load address of the shared object to the
    symbol's addend. For non-IFUNCs, it typically stores the base address of the GOT
    entry.
series_id: 'binutils:alpha: emit r_alpha_irelative in pic links'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-6-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch modifies the alpha ELF linker to emit R_ALPHA_IRELATIVE relocations for IFUNC references in Position-Independent Code (PIC) links. In PIC, references to IFUNCs previously used R_ALPHA_RELATIVE, which stored the resolver's address. The new R_ALPHA_IRELATIVE relocation correctly stores the address returned by the IFUNC's resolver. This change ensures proper handling of IFUNCs in PIC environments without altering memory layout for existing RELATIVE relocations.
