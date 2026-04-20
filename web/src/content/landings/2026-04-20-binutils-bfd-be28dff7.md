---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- bfd
- m32r
- relocation
- security
- fuzzing
commit_hash: be28dff7f92890b859cf365c4f2c7dd687da6c04
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: 'm32r: Add Offset Sanity Checks for Hi/Lo Relocations.'
tldr: The m32r backend now validates relocation offsets to prevent out-of-bounds memory
  accesses during relocation, improving security.
why_it_matters: This change hardens the toolchain against malicious inputs by preventing
  potential buffer overflows during relocation processing, a common avenue for security
  exploits.
impact_score: 7
impact_rationale: Fixes a security vulnerability found by fuzzing.
performance_win: false
breaking_change: false
outcome: committed
primer: The Binary File Descriptor (BFD) library provides a generic interface for
  manipulating object files in various formats. Relocations adjust addresses within
  object code to account for the actual load address in memory. The m32r is a specific
  target architecture, and its BFD backend handles relocations specific to that architecture.
  Without proper offset validation, a crafted object file could cause BFD to read
  or write to arbitrary memory locations, potentially leading to crashes or security
  vulnerabilities.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260420061649.2C9A44BAD14A@sourceware.org
date: '2026-04-20'
---

The m32r backend was vulnerable to fuzzer attacks due to missing offset validation during HI16 and LO16 relocations. This commit adds sanity checks for relocation offsets before accessing section contents, preventing out-of-bounds memory accesses. It also simplifies sign extension and adjusts function calls.
