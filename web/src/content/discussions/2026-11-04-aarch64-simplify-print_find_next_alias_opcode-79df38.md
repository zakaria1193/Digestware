---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- disassembler
- refactoring
- performance
discussion_id: 451d4ee5-b405-eaf9-214b-57af9f3fa8d1@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 20/28] aarch64: Simplify print_find_next_alias_opcode'
headline: 'aarch64: Simplify print_find_next_alias_opcode'
tldr: Simplifies AArch64 alias opcode resolution by using a bucket sort.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Replaces a complex structure and multiple sorts with a single bucket sort for cleaner
  code and potential performance improvement.
- Slight reordering of alias resolution sequences, but no change in disassembler output.
exchanges: []
primer_expert: Refactors `aarch64_find_next_alias_opcode` in `opcodes/aarch64-dis-2.c`.
  It replaces the previous mechanism of building an `alias_info` structure and then
  using individual bubble sorts with a single bucket sort to order alias opcodes.
  This simplifies the generation of the `switch` statement cases by sorting aliases
  based on their priority in the main opcode table. The output sequence of alias resolutions
  may change, but the functional outcome is identical.
primer_glossary:
- term: alias opcode
  definition: An instruction that is represented by multiple different opcodes or
    encoding patterns, but performs the same operation. The disassembler must correctly
    identify which alias corresponds to the given instruction encoding.
- term: bucket sort
  definition: A sorting algorithm that distributes elements into a number of buckets
    or bins, and then sorts each bucket individually. It's efficient when the input
    data is uniformly distributed.
series_id: 'binutils:aarch64: simplify print_find_next_alias_opcode'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/451d4ee5-b405-eaf9-214b-57af9f3fa8d1@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch simplifies the `aarch64_find_next_alias_opcode` function in `opcodes/aarch64-dis-2.c` by employing a bucket sort for alias opcodes. It creates a sorted list of aliases, prioritizing those earlier in the opcode table. This eliminates the need for the `alias_info` structure and replaces a separate bubble sort for each aliased opcode with a single efficient sort. The disassembler behavior remains unchanged, but the code is cleaner.
