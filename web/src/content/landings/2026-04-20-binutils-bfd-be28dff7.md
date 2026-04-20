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
headline: M32R hi/lo reloc offset sanity checks improve security.
tldr: The bfd library gains sanity checks for M32R relocations to prevent out-of-bounds
  memory access, mitigating potential fuzzer attacks.
why_it_matters: These checks prevent the toolchain from crashing or, worse, from miscompiling
  code when faced with malformed object files, improving overall toolchain robustness.
impact_score: 7
impact_rationale: Improves security by preventing potential out-of-bounds memory access
  during relocation.
performance_win: false
breaking_change: false
outcome: committed
primer: BFD (Binary File Descriptor) is a library for working with different object
  file formats in a uniform way. Relocations are adjustments made to addresses in
  object code when linking to create an executable. The M32R is a 32-bit RISC architecture.
  ELF (Executable and Linkable Format) is a common object file format. Fuzzing is
  a testing technique that involves feeding a program with invalid or random data
  to find vulnerabilities.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260420061649.2C9A44BAD14A@sourceware.org
date: '2026-04-20'
---

This commit adds sanity checks for relocation offsets in the M32R ELF backend of the bfd library. It checks that the relocation offset is within the bounds of the input section before accessing the section's contents. This prevents out-of-bounds memory access and fixes a potential security vulnerability exposed by fuzzing. The code for sign extension is also simplified.
