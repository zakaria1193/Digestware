---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- aarch64
- windows
- alignment
- patch
discussion_id: 20260813171737.3172237-1-oyzawqgcfc@gmail.com
source_type: public_inbox
title: '[PATCH] ld: default the aarch64pe section alignment to 64K'
headline: 'ld: Default aarch64pe section alignment to 64K'
tldr: Patch modifies GNU ld to default section alignment for aarch64pe to 64K, ensuring
  compatibility with 16K page sizes on ARM64 hosts.
proposer: trcrsired <oyzawqgcfc@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increased section alignment may lead to slightly larger file sizes due to padding,
  but improves compatibility on modern hardware.
exchanges: []
primer_expert: A patch for GNU `ld` proposes changing the default section alignment
  for the `aarch64pe` (ARM64 PE/COFF) target from 4K to 64K. This is to accommodate
  modern ARM64 hardware (e.g., Apple Silicon, Android devices) which increasingly
  use 16K memory pages. The current 4K alignment is not a multiple of 16K, preventing
  proper memory mapping by the OS loader or Wine. Increasing the alignment to 64K
  (a multiple of 16K) resolves this.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: aarch64pe
  definition: The target triplet for linking 64-bit ARM (AArch64) executables in the
    PE (Portable Executable) format, typically used for Windows.
- term: section alignment
  definition: The requirement that sections within an executable file start at memory
    addresses that are multiples of a specific value, often related to memory page
    sizes.
- term: ARM64
  definition: The 64-bit architecture for ARM processors.
- term: page size
  definition: The smallest unit of memory that the operating system manages. Common
    sizes are 4KB, 16KB, or 64KB.
- term: Wine
  definition: A compatibility layer that allows Windows applications to run on POSIX-compliant
    operating systems, such as Linux and macOS.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260813171737.3172237-1-oyzawqgcfc@gmail.com
bugzilla_url: null
date: '2026-08-13'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where the default 4K section alignment for `aarch64pe` executables is incompatible with ARM64 hosts using 16K page sizes, such as Apple Silicon or Android devices. The change defaults the section alignment to 64K, ensuring that these executables can be mapped by the loader, even under Wine.
