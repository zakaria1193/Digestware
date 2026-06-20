---
project: binutils
subsystem: bfd/risc-v
patch_id: null
tags:
- risc-v
- bfd
- isa extensions
- vector extensions
- implicit dependencies
discussion_id: 0450f2b8-fa5b-4921-b330-d9fe2e2c54b2@suse.com
source_type: public_inbox
title: '[PATCH v3 04/13] bfd/RISC-V: Zv{b,k}* imply Zve32x'
headline: 'BFD/RISC-V: Zv{b,k}* imply Zve32x'
tldr: This patch updates the RISC-V BFD backend to explicitly define that various
  Zv{b,k}* extensions imply Zve32x, aligning with specification.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Explicitly defines implicit dependencies, which reduces the chance of misinterpreting
  ISA extensions during linking.
- Requires careful verification to ensure that all actual implicit dependencies are
  captured and no unintended ones are introduced.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes to explicitly list various Zv{b,k}* vector extensions as implying
    Zve32x in the RISC-V BFD backend, aligning with the specification.
  quote: The specification is quite explicit about this.
primer_expert: In the RISC-V `bfd` library (`bfd/elfxx-riscv.c`), the `riscv_implicit_subset`
  table defines inherent dependencies between RISC-V Instruction Set Architecture
  (ISA) extensions. These implications are crucial for correctly merging object attributes
  during linking. The problem addressed here is that the cryptographic vector extensions
  (those starting with `Zv{b,k}*`, such as `zvbc`, `zvkb`, `zvkg`, etc.) implicitly
  depend on the `Zve32x` base vector extension. This dependency is specified in the
  RISC-V ISA. The patch adds entries like `{"zvbc", "+zve32x", check_implicit_always}`
  to the `riscv_i…
primer_general: This discussion is about how the linker (`bfd`) in the binutils toolchain
  handles specific features for RISC-V processors. RISC-V has various optional extensions
  that add new instructions for specialized tasks, such as cryptography (often denoted
  by `Zv{b,k}*`). These advanced extensions often rely on a more basic set of vector
  (parallel processing) instructions, in this case, `Zve32x`. The RISC-V specification
  states that if you use any of these cryptographic vector extensions, you automatically
  also get the `Zve32x` base vector extension. This patch updates the linker to explicitly
  record these relationships. This ensures that when different parts of a program
  are linked together, the linker correctly understands all the features supported
  by the target RISC-V processor, preventing errors that might arise from misunderstanding
  which instruction sets are available.
series_id: 'binutils:bfd/risc-v: zv{b,k}* imply zve32x'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/0450f2b8-fa5b-4921-b330-d9fe2e2c54b2@suse.com
bugzilla_url: null
date: '2026-06-19'
is_stub: false
---

This proposal updates the RISC-V BFD (`libbfd`) backend to formalize the implicit dependency of cryptographic (`Zv{b,k}*`) vector extensions on the `Zve32x` base vector extension. The RISC-V specification dictates this implication, and this patch explicitly adds these relationships to the `riscv_implicit_subset` structure to ensure correct attribute propagation during linking.
