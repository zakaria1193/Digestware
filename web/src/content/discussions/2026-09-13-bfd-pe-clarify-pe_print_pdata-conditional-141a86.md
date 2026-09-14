---
project: binutils
subsystem: bfd
patch_id: null
tags:
- bfd
- pe
- pdata
- clarification
- code quality
discussion_id: 20260913123323.9734-2-jon.turney@dronecode.org.uk
source_type: public_inbox
title: '[PATCH 1/4] bfd: pe: Clarify pe_print_pdata() conditional'
headline: 'bfd: pe: Clarify pe_print_pdata() conditional'
tldr: Clarify and correct the conditional logic in PE .pdata printing.
proposer: Jon Turney <jon.turney@dronecode.org.uk>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves code clarity and documentation.
- Identifies potential bugs and security issues related to `.pdata` handling.
exchanges: []
primer_expert: This patch addresses confusing and potentially incorrect conditional
  logic in `bfd/peXXigen.c`'s `pe_print_pdata` function. The original condition was
  intended to differentiate between PE MIPS and other architectures but is now obsolete.
  The author clarifies comments and points out that the logic for ia64's `.pdata`
  entry size (3*8 bytes) might be incorrect compared to x86_64's (3*4 bytes), and
  that unconstrained reads could occur. This sets the stage for further corrections
  in subsequent patches.
primer_glossary:
- term: pe_print_pdata
  definition: A function within binutils' BFD library responsible for printing the
    contents of the `.pdata` section in PE (Portable Executable) files.
- term: conditional logic
  definition: Code that executes different paths based on whether certain conditions
    are true or false, often implemented using `#if`, `#ifdef`, etc.
- term: unconstrained read
  definition: Reading data from memory without proper bounds checking, which can lead
    to accessing invalid memory or security vulnerabilities.
series_id: 'binutils:bfd: pe: clarify pe_print_pdata() conditional'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260913123323.9734-2-jon.turney@dronecode.org.uk
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

This patch clarifies the conditional logic within the `pe_print_pdata` function in `bfd/peXXigen.c`. It updates comments to reflect the function's intended behavior and identifies that the existing conditional is pointless, as PE MIPS support was removed. The change also highlights potential issues with the `pdata` entry size for ia64 and unconstrained reads, suggesting that the current implementation may be incorrect or unsafe for certain architectures.
