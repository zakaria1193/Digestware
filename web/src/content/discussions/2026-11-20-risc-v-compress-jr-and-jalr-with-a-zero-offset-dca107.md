---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- binutils
- gas
- compression
- optimization
discussion_id: 20261120142549.3976191-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH] RISC-V: Compress jr and jalr with a zero offset'
headline: 'RISC-V: Compress jr and jalr with a zero offset'
tldr: Enhances RISC-V assembler to compress `jr` and `jalr` instructions when they
  have a zero offset, aligning with LLVM and improving code density.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Improves code density for RISC-V programs.
- Requires careful handling of register constraints and offset values for correct
  compression.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Submits patches to enable compressed encoding for RISC-V `jr` and `jalr`
    instructions with zero offsets and specific register targets, matching LLVM's
    behavior.
  quote: gas compressed "jr a2" and "jalr a2", but not the same jumps written with
    an explicit zero offset or an explicit x0 or ra destination, such as "jalr x0,
    0(a2)". Add Zca aliases for those forms so they become c.jr and c.jalr too, which
    matches LLVM.
primer_expert: This series of patches targets the RISC-V assembler (`gas`) to improve
  the compression of jump instructions (`jr` and `jalr`). It introduces new operand
  types (`r` for `ra`, `z` for `x0`) and associates them with the Zca instruction
  alias. This ensures that jumps with zero offsets or jumps to the zero register (`x0`)
  or return address register (`ra`) are correctly encoded using their compressed forms
  (`c.jr`, `c.jalr`), enhancing code size optimization.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture based on RISC principles.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: jr
  definition: Jump Register, an instruction that jumps to an address specified in
    a register.
- term: jalr
  definition: Jump and Link Register, an instruction that jumps to an address specified
    in a register and saves the return address.
- term: Zca
  definition: A proposed RISC-V extension that provides compressed aliases for `jr`
    and `jalr` instructions.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120142549.3976191-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch modifies the RISC-V assembler in binutils to correctly compress `jr` and `jalr` instructions when they have an explicit zero offset or target specific registers like `x0` or `ra`. Previously, only simpler forms of `jr` and `jalr` were compressed. This update introduces Zca aliases for these forms, allowing them to be encoded as `c.jr` and `c.jalr`, similar to LLVM's behavior, thus improving code density.
