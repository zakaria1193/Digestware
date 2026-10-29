---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- bugfix
- loongarch
- relocation
discussion_id: 20261029065520.57394-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH v2] LoongArch: Avoid signed overflow when dumping relocation addends'
headline: 'LoongArch: Avoid signed overflow when dumping relocation addends'
tldr: Fixes signed overflow in LoongArch relocation addend dumping by using unsigned
  arithmetic.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- The change ensures correctness and avoids undefined behavior for a specific edge
  case (INT64_MIN addend) at the cost of slightly more complex arithmetic for negative
  addends.
exchanges:
- author: zhaozhou <zhaozhou@loongson.cn>
  role: proposer
  position: Submits a patch to prevent signed overflow when dumping LoongArch relocation
    addends, particularly for INT64_MIN, by using unsigned arithmetic.
  quote: 'When the addend is INT64_MIN, the negation overflows and trigger

    undefined behavior, using bfd_vma subtraction to compute the absolute

    value of addend and print it with PRIu64.'
primer_expert: This patch modifies `bfd/elfnn-loongarch.c` to correct the behavior
  of `loongarch_dump_reloc_record`. When a negative relocation addend is encountered,
  specifically `INT64_MIN`, its negation would overflow. The fix uses unsigned arithmetic
  to calculate the absolute value before printing, preventing undefined behavior and
  ensuring correct output for all addend values.
primer_glossary:
- term: Relocation
  definition: A modification needed in an object file or shared library to resolve
    references to symbols or addresses that are not yet known at link time. This process
    is typically handled by the linker.
- term: Addend
  definition: A constant value added to a symbol's address during relocation processing.
    It's part of the relocation entry itself.
- term: INT64_MIN
  definition: The smallest representable value for a signed 64-bit integer. Its negation
    results in overflow in standard two's complement representation.
- term: Undefined Behavior
  definition: Behavior that results from an implementation using certain C constructs
    that, according to the C standard, the compiler can assume will never occur. This
    can lead to unpredictable results, crashes, or security vulnerabilities.
- term: bfd_vma
  definition: A data type in the BFD library used to represent virtual memory addresses,
    typically an unsigned integer type large enough to hold any address.
- term: PRIu64
  definition: A format specifier for `printf` family functions to print an unsigned
    64-bit integer in hexadecimal format.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261029065520.57394-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-10-29'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the LoongArch ELF object file handling where negating a negative relocation addend, specifically INT64_MIN, results in signed overflow and undefined behavior. The fix replaces direct negation with unsigned arithmetic to correctly compute and print the absolute value of the addend, ensuring proper handling of INT64_MIN and preserving output for other values. This change is linked to bug report PR ld/34808.
