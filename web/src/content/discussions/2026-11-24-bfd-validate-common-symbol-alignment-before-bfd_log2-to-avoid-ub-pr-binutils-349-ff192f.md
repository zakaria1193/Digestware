---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- bugfix
- undefined behavior
discussion_id: tencent_982E718519D17BC3786B6301E84CC6C22F08@qq.com
source_type: public_inbox
title: '[PATCH v2] bfd: Validate common symbol alignment before bfd_log2 to avoid
  UB [PR binutils/34996]'
headline: 'bfd: Validate common symbol alignment before bfd_log2 to avoid UB [PR binutils/34996]'
tldr: Patch v2 validates common symbol alignment before using bfd_log2 to prevent
  undefined behavior from large shift counts.
proposer: jelly <762233433@qq.com>
consensus: Needs Revision
outcome: needs_revision
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: jelly <762233433@qq.com>
  role: proposer
  position: Submits version 2 of a patch to cap the alignment value returned by `bfd_log2`
    to prevent undefined behavior when used as a shift count.
  quote: Cap the alignment result of bfd_log2 at 63 (the maximum useful alignment
    for a 64-bit address space) so 64-bit shifts are safe, and cast the left shift
    operands at the use sites to bfd_vma so the cap is effective everywhere the alignment
    is consumed.
primer_expert: This patch targets `elflink.c` within the BFD library. It addresses
  a potential undefined behavior in C stemming from a large shift count. When a common
  symbol's `st_value` (alignment requirement) is excessively large, `bfd_log2(st_value)`
  can return 64. This value, when used as `1 << 64`, causes UB. The fix caps the result
  of `bfd_log2` at 63 and ensures appropriate casting to `bfd_vma` at the shift operation
  sites.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library; a low-level library used by GNU Binutils
    to abstract the details of various object file formats.
- term: common symbol
  definition: A type of symbol in object files that represents uninitialized data.
    The linker resolves all common symbols to a single location.
- term: alignment
  definition: The requirement that data be stored in memory at an address that is
    a multiple of a specified value. This is often related to the size of the data
    type or hardware constraints.
- term: bfd_log2
  definition: A function within the BFD library that likely calculates the base-2
    logarithm of a number, often used to determine the power of 2 for alignment.
- term: UB
  definition: Undefined Behavior; behavior that results from implementations not required
    to diagnose or prevent, and whose absence of specification means that each implementation
    may behave differently.
- term: bfd_vma
  definition: A data type within the BFD library, typically representing a virtual
    memory address or a large unsigned integer type suitable for representing addresses.
- term: PR binutils/34996
  definition: Problem Report number 34996 filed against the binutils project, indicating
    a bug or issue that has been reported.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/tencent_982E718519D17BC3786B6301E84CC6C22F08@qq.com
bugzilla_url: null
date: '2026-11-24'
is_stub: false
stub_reason: ''
---

This patch (v2) addresses an issue in binutils' BFD library where a common symbol with a very large or non-power-of-two alignment value can cause `bfd_log2` to return 64. This large value, when used as a shift count in `elflink.c`, leads to undefined behavior. The patch caps the alignment result at 63 and ensures casts to `bfd_vma` at use sites to maintain safety across different architectures and data types.
