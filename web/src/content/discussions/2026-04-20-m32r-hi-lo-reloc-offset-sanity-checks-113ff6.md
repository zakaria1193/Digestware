---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- m32r
- ELF
- relocation
- security
discussion_id: aeXEBvhXwRjo2qaW@squeak.grove.modra.org
source_type: public_inbox
title: m32r hi/lo reloc offset sanity checks
headline: m32r hi/lo reloc offset sanity checks
tldr: This patch adds sanity checks for relocation offsets in the m32r ELF backend
  to prevent crashes due to malicious input.
stakes: Fixes a security vulnerability where crafted input could cause binutils to
  crash, potentially leading to denial of service.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: 9
sentiment_rationale: Addresses a fuzzer-discovered security issue; the fix appears
  straightforward and uncontroversial.
technical_tradeoffs:
- Adds additional checks that may slightly increase linking time.
- No diagnostics are emitted for invalid input.
primer: Binutils is a collection of tools for working with binary files, including
  assemblers, linkers, and debuggers. The ELF (Executable and Linkable Format) is
  a common file format for executables, object code, shared libraries, and core dumps.
  Relocation is the process of adjusting addresses in object code or executable files
  to reflect their actual load addresses in memory. Fuzzers are tools that generate
  random or semi-random inputs to find bugs and vulnerabilities in software.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aeXEBvhXwRjo2qaW@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-20'
---

This patch adds input validation to the m32r ELF backend in binutils. It checks relocation offsets before accessing section contents to prevent out-of-bounds reads. The patch addresses a fuzzer-discovered vulnerability.
