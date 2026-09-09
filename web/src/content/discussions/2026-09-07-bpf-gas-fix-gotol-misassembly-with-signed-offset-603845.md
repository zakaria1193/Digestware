---
project: binutils
subsystem: bpf
patch_id: null
tags:
- BPF
- gas
- assembler
- parsing
- libbpf
discussion_id: 20260907091102.2595057-1-vineet.gupta@linux.dev
source_type: public_inbox
title: '[PATCH v3 0/5] bpf: fix gotol with a signed offset and fallout'
headline: 'BPF gas: Fix `gotol` misassembly with signed offset'
tldr: BPF gas `gotol` instruction now correctly assembles signed offsets, resolving
  libbpf load-time failures.
proposer: Vineet Gupta <vineet.gupta@linux.dev>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Fixes critical bugs leading to runtime failures in libbpf.
- Improves assembler robustness and accuracy.
- Introduces a new parsing specifier (`%t`) for stricter tokenization.
exchanges:
- author: Jose E. Marchesi
  role: reviewer
  position: Acknowledges the series, approving patches and providing feedback on specific
    issues like the `gotol` test coverage.
  quote: 'OK for master.

    Thanks!'
- author: Vineet Gupta
  role: proposer
  position: Submits a series of patches to fix the misassembly of BPF's `gotol` instruction
    with signed offsets.
  quote: 'In the pseudo-C dialect `gotol +1'' is silently assembled as `goto l+1''

    leading to libbpf load time failures.'
primer_expert: This is the cover letter for a series of patches fixing BPF `gotol`
  instruction assembly issues in GNU gas. The core problem is that `gotol +1` is misassembled
  as `goto l+1` due to ambiguous parsing, causing libbpf load failures. Patch 1 enables
  a never-run test suite (`spacing-pseudoc`) that reveals this and other spacing issues.
  Patch 2 directly fixes the `gotol` misassembly using the `%t` token boundary specifier,
  moving away from previous attempts like specific parser workarounds or opcode reordering.
  Patch 3 generalizes the `%t` usage to 65 other mnemonics for consistency and future-proo…
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter, a technology that allows sandboxed programs
    to safely execute code in the Linux kernel, often used for networking and tracing.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    converting assembly language code into machine code.
- term: gotol
  definition: A BPF assembler instruction, likely a variant of 'goto' with a specific
    operand format or target type.
- term: libbpf
  definition: A library providing helper functions for loading, compiling, and interacting
    with BPF programs in the Linux kernel.
- term: pseudo-C dialect
  definition: A specific assembly syntax or dialect used for BPF, which resembles
    C language constructs for clarity and testing purposes.
- term: '%t specifier'
  definition: A format specifier in the gas opcode table that signifies a token boundary,
    ensuring that the preceding text is treated as a complete mnemonic and not extended
    by subsequent characters.
series_id: 'binutils:bpf: fix gotol with a signed offset and fallout'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260907091102.2595057-1-vineet.gupta@linux.dev
bugzilla_url: null
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

This patch series addresses an issue in the BPF assembler (gas) where the `gotol` instruction was silently misassembled when given a signed offset. This led to errors during libbpf loading. The series introduces a more robust parsing mechanism using the `%t` token boundary specifier to correctly distinguish `gotol` from `goto`, especially in contexts with flexible spacing. It also includes fixes for related issues like testing `gotol` in compound conditional jumps and improving ISA spec diagnostics.
