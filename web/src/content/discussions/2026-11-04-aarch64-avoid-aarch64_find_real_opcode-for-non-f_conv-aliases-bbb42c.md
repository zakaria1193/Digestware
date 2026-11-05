---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- assembler
- opcode
discussion_id: 721699b2-dfde-cad9-6102-45fcd315e758@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 08/28] aarch64: Avoid aarch64_find_real_opcode for non-F_CONV aliases.'
headline: 'aarch64: Avoid aarch64_find_real_opcode for non-F_CONV aliases.'
tldr: Optimizes opcode encoding by only using aliased opcodes when F_CONV is set.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improved encoding efficiency by conditionally using aliases.
- Code simplification by removing unused cases.
exchanges: []
primer_expert: This patch refactors `aarch64-asm-2.c`. In `aarch64_opcode_encode`,
  it now only uses `aarch64_find_real_opcode` for aliases when the `F_CONV` flag is
  set. This simplifies the encoding logic. Consequently, unused mappings in `aarch64_find_real_opcode`
  for non-`F_CONV` cases (including identity mappings) are removed, reducing code
  size and complexity.
primer_glossary:
- term: F_CONV
  definition: A flag indicating a specific type of conversion or alias behavior for
    an opcode, likely related to how it affects the data or its representation during
    encoding or decoding.
series_id: 'binutils:aarch64: avoid aarch64_find_real_opcode for non-f_conv aliases'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/721699b2-dfde-cad9-6102-45fcd315e758@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

In `aarch64_opcode_encode`, this patch optimizes the process by only using aliased opcodes when the `F_CONV` flag is set. The lookup and flag check are reordered for efficiency. Unused non-`F_CONV` cases, including those that mapped opcodes to themselves, have been dropped from `aarch64_find_real_opcode`.
