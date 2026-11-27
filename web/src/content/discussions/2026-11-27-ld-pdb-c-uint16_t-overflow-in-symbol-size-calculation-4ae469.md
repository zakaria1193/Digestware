---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- security
- vulnerability
- integer overflow
discussion_id: tencent_1E90FB5F010C5CFC199A9480@qq.com
source_type: public_inbox
title: 'Bug <35058>: uint16_t overflow in ld/pdb.c calculate_symbols_size/parse_symbols'
headline: 'ld/pdb.c: uint16_t overflow in symbol size calculation'
tldr: A uint16_t overflow vulnerability exists in ld/pdb.c's symbol size calculation
  and parsing functions, similar to a previously fixed issue.
proposer: 薛皓琳 <xuehaolin@uniontech.com>
consensus: Proposed
outcome: needs_revision
impact_score: 5
sentiment_score: 8
technical_tradeoffs:
- Fixes a potential integer overflow vulnerability that could lead to security issues.
- Requires careful analysis of integer types and bounds checking in symbol table processing.
exchanges:
- author: 薛皓琳 <xuehaolin@uniontech.com>
  role: proposer
  position: Reported a `uint16_t` overflow vulnerability in `ld/pdb.c` that was not
    caught by a previous fix.
  quote: "I've reported a bug in ld/pdb.c that was not caught by the recent\ncommit\
    \ 147e60cae54 (\"Fix potential integer overflows in ld/pdb.c\"):\n\n https://sourceware.org/bugzilla/show_bug.cgi?id=35058\n\
    \nThe same uint16_t truncation pattern exists in calculate_symbols_size() and\
    \ parse_symbols()."
- author: Jan Beulich <jbeulich@suse.com>
  role: maintainer
  position: Acknowledged the reported bug and its similarity to a previously fixed
    one, noting the specific failure condition of the existing check.
  quote: The same uint16_t truncation pattern exists in calculate_symbols_size() and
    parse_symbols(). calculate_symbols_size() received no bounds check at all, and
    the "if (len > size)" check added to parse_symbols() does not trigger when len
    wraps to 0
primer_expert: This bug report for `binutils` concerns the `ld` linker's PDB (Program
  Database) file handling, specifically within `ld/pdb.c`. It identifies a `uint16_t`
  overflow vulnerability in functions responsible for calculating and parsing symbol
  table sizes. This vulnerability is a regression or an oversight from a prior commit
  intended to fix integer overflows. The issue arises from insufficient bounds checking
  and a condition where a length variable wrapping to zero bypasses existing checks,
  potentially leading to incorrect memory allocation or buffer overflows.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or library.
- term: pdb.c
  definition: A source file likely related to handling Program Database (PDB) files,
    which store debugging information, particularly in environments like Windows.
- term: uint16_t
  definition: An unsigned integer type that is exactly 16 bits wide.
- term: overflow
  definition: A condition where an arithmetic operation attempts to create a numeric
    value that is too large to be represented within the allocated bits.
- term: Bugzilla
  definition: An open-source bug tracking system used by many software projects, including
    Binutils, to manage bug reports and feature requests.
- term: ASan
  definition: AddressSanitizer, a tool that detects memory errors such as buffer overflows.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/tencent_1E90FB5F010C5CFC199A9480@qq.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

This report highlights a `uint16_t` overflow vulnerability in `ld/pdb.c` within the `calculate_symbols_size` and `parse_symbols` functions. This issue is similar to a bug recently addressed by commit `147e60cae54`. `calculate_symbols_size` lacks bounds checking entirely, and the existing check in `parse_symbols` fails when the length variable wraps around to 0. Proof-of-concept files and ASan output are available in the linked Bugzilla report.
