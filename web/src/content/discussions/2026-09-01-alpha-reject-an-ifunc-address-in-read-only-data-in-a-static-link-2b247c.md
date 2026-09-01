---
project: binutils
subsystem: alpha
patch_id: null
tags:
- alpha
- linker
- ifunc
- relocation
- static executable
discussion_id: 20260901023318.3503991-9-mattst88@gmail.com
source_type: public_inbox
title: '[PATCH 08/11] alpha: reject an IFUNC address in read-only data in a static
  link'
headline: 'alpha: reject an IFUNC address in read-only data in a static link'
tldr: Prevent linker errors by rejecting IFUNC addresses in read-only data for static
  alpha executables.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Rejects potentially problematic configurations instead of attempting to work around
  them.
- Requires a user-level change if IFUNCs are needed in read-only static data.
exchanges: []
primer_expert: This patch modifies the alpha ELF linker to reject IFUNC references
  within read-only data sections when creating a static executable. IFUNCs require
  an R_ALPHA_IRELATIVE relocation, which effectively attempts to relocate read-only
  memory. This conflicts with the execution environment of static binaries where the
  C library's startup code cannot modify read-only segments. The proposed solution
  is to emit an error, similar to how other targets might provide a PLT stub address.
primer_glossary: []
series_id: 'binutils:alpha: reject an ifunc address in read-only data in a static
  link'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901023318.3503991-9-mattst88@gmail.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where IFUNC addresses in read-only data can cause problems in statically linked alpha executables. The relocation of a read-only page for such an address is problematic because the C library's startup code cannot make it writable after the kernel has mapped the segment. Instead of relying on other targets that provide a PLT stub address, this patch proposes reporting an error for the alpha architecture, which lacks a PLT entry for non-dynamic functions.
