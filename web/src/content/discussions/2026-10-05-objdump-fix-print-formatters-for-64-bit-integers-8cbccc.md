---
project: binutils
subsystem: objdump
patch_id: null
tags:
- objdump
- btf
- portability
- formatting
discussion_id: 20261005145046.611902-1-david.faust@oss.qualcomm.com
source_type: public_inbox
title: '[pushed] objdump: fix print formatters for 64-bit integers'
headline: 'objdump: fix print formatters for 64-bit integers'
tldr: David Faust committed a fix to objdump to use portable print formatters for
  64-bit integers when dumping BTF info.
proposer: David Faust <david.faust@oss.qualcomm.com>
consensus: Committed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensures correct output across platforms at the cost of slightly more verbose format
  specifiers.
exchanges:
- author: David Faust <david.faust@oss.qualcomm.com>
  role: proposer
  position: Committed a fix to objdump to use portable print formatters for 64-bit
    integers when dumping BTF info, resolving target-specific issues.
  quote: null
primer_expert: This commit addresses a portability issue in the `objdump` utility,
  specifically within the BTF dumping functionality. Commit `071f8a902eb29d29b9306b1425392e9fc73470f3`
  introduced BTF dumping but used non-portable C standard library format specifiers
  for 64-bit integers. This change replaces them with portable ones, ensuring correct
  output on all supported targets.
primer_glossary:
- term: objdump
  definition: A standard utility in the binutils package used to display information
    from object files, including disassembly and symbol tables.
- term: BTF
  definition: Brief Type Format, a compact representation of type information used
    in systems like the Linux kernel for features like eBPF.
- term: print formatters
  definition: Specifiers used in C's `printf`-style functions (like `printf`, `sprintf`)
    to define how different data types should be represented as strings (e.g., `%d`
    for integers, `%s` for strings).
- term: portable
  definition: Code or behavior that works consistently across different operating
    systems, architectures, and compiler versions without modification.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261005145046.611902-1-david.faust@oss.qualcomm.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

David Faust has committed a change to objdump that corrects the formatting of 64-bit integer values when displaying BTF (Basic Type Format) information. The previous implementation used non-portable formatting directives that caused issues on certain targets. This fix ensures that portable print formatters are used, improving compatibility and correctness across different platforms.
