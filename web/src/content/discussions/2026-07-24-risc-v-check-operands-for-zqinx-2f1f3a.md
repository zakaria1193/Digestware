---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- extension
- validation
discussion_id: a51cf9e2-baf6-4fba-bcae-33fb33d22c7e@suse.com
source_type: public_inbox
title: '[PATCH v4 07/12] RISC-V: check operands for Zqinx'
headline: 'RISC-V: check operands for Zqinx'
tldr: Add operand checks for the RISC-V Zqinx extension in RV32 and RV64.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves correctness by enforcing operand constraints for the Zqinx extension.
- Relies on inferred rules due to the lack of formal specification for Zqinx register
  pair encoding.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Introduces register pair operand checks for Zqinx in RV32 and RV64.
  quote: By analogy to Zdinx on RV32, register pair operands are presumably (there
    not being any formal spec afaict) required to be encoded with the low bit clear
    in RV64; in RV32 the low two bits need to be clear. Since match functions don't
    have XLEN available, introduce respective flags, to be used explicitly in assembler
    and disassembler.
- author: Jiawei <jiawei@iscas.ac.cn>
  role: reviewer
  position: Questioned the utility of Zqinx in RV32, noting that it leads to awkward
    function argument passing and that it cannot be enabled with the V extension.
  quote: null
primer_expert: This patch refines the RISC-V assembler's instruction decoding for
  the Zqinx extension. It adds validation for register operands used in pairs, requiring
  specific bit patterns (even for RV64, low bit clear; for RV32, low two bits clear)
  based on perceived common practice due to lack of formal specification. This ensures
  that instructions are correctly assembled according to implied constraints for critical
  extensions.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is gaining popularity
    for its modularity and extensibility.
- term: Zqinx
  definition: A RISC-V extension that provides integer multiplication instructions.
- term: RV32
  definition: The 32-bit variant of the RISC-V architecture.
- term: RV64
  definition: The 64-bit variant of the RISC-V architecture.
- term: XLEN
  definition: The native integer width of a RISC-V processor, either 32 or 64 bits.
series_id: 'binutils:risc-v: check operands for zqinx'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/a51cf9e2-baf6-4fba-bcae-33fb33d22c7e@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch introduces operand checks for the RISC-V Zqinx extension in both RV32 and RV64. It enforces that register pair operands must have specific low bits clear: the least significant bit for RV64 and the two least significant bits for RV32. This validation is crucial for correct instruction encoding, especially since the Zqinx extension's exact specifications for register pairs are not formally defined.
