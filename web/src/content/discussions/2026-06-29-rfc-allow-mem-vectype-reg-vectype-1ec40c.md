---
project: gcc
subsystem: rfc
patch_id: null
tags:
- gcc
- rtl
- vector types
- register allocation
discussion_id: 8c09a3f6-6ac9-4964-8394-8511f966582b@baylibre.com
source_type: public_inbox
title: 'Re: RFC: Allow "(mem:<vectype> (reg:<vectype>))"'
headline: 'RFC: Allow "(mem:<vectype> (reg:<vectype>))"'
tldr: Proposal to allow a new memory operand format for vector types in GCC's RTL.
proposer: Andrew Stubbs <ams@baylibre.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Potential complexity introduced to LRA.
- Ensuring correct handling of vector memory accesses across different architectures.
exchanges:
- author: Andrew Stubbs
  role: proposer
  position: Asks for clarification on why an unspec pattern was reloaded by LRA and
    explains his current approach using a special memory constraint for GCN, noting
    difficulties in understanding LRA's behavior with different address spaces.
  quote: Ideally, LRA would know how to handle the new vectors of addresses, but I'm
    struggling to understand that code. (I feel like it's broken for addresses spaces
    with different sized addresses also, but maybe that's just my lack o
- author: Richard Sandiford
  role: reviewer
  position: Questions why an unspec part of a pattern was reloaded by LRA, as LRA
    typically only reloads match_operands.
  quote: Out of curiosity, how did that happen?  In the pattern above, the unspec
    is a fixed part of the pattern, whereas LRA only reloads match_operands.
primer_expert: This RFC proposes a new RTL expression `(mem:<vectype> (reg:<vectype>))`
  for representing memory accesses with vector types in GCC. The discussion revolves
  around how the Live Register Allocator (LRA) handles such constructs, particularly
  when combined with `define_special_memory_constraint` as seen in GCN, and potential
  issues with address spaces.
primer_general: This discussion proposes a change to the internal representation of
  code within the GCC compiler. Specifically, it concerns how memory accesses involving
  vector data types are described. The current implementation might not fully support
  a new way of expressing these accesses, leading to potential issues with how the
  compiler optimizes register usage. Developers are discussing the nuances of the
  compiler's register allocation logic to ensure the proposed change works correctly
  and efficiently across different hardware architectures.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/8c09a3f6-6ac9-4964-8394-8511f966582b@baylibre.com
bugzilla_url: null
date: '2026-06-29'
is_stub: false
stub_reason: ''
---

Andrew Stubbs proposes allowing a new format for memory operands in GCC's RTL, specifically `(mem:<vectype> (reg:<vectype>))`. This change is related to handling vector types and memory access, with ongoing internal discussion about how the register allocator (LRA) interacts with special memory constraints.
