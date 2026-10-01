---
project: binutils
subsystem: x86-64
patch_id: null
tags:
- optimization
- x86-64
- performance
- plt
discussion_id: CAMe9rOoFbPvk27h+qnGu9xCfQ5z8LAkrr5L-5HPGR8PDD0XM5g@mail.gmail.com
source_type: public_inbox
title: '[PATCH] x86-64: Use UD0/UD2 after indirect jump in PLT entries'
headline: 'x86-64: Use UD0/UD2 after indirect jump in PLT entries'
tldr: Optimize indirect jumps in PLT entries by replacing NOPs with UD0/UD2 instructions.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: under_review
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- The change introduces a specific instruction (UD0/UD2) that halts decoding, potentially
  impacting performance if branch prediction was already effective.
exchanges:
- author: H.J. Lu
  role: proposer
  position: Proposes replacing NOPs with UD0 or UD2 after indirect branches in PLT
    entries to prevent processor decoding down the fall-through path, based on Intel
    optimization guidelines.
  quote: 'Replace NOP with UD0 or UD2 after indirect branch in PLT entries to

    implement optimization guide from Intel optimization manual:


    Assembly/Compiler Coding Rule 13. (M impact, L generality)


    When indirect branches are present, try to put the most likely target

    of an indirect branch immediately following the indirect branch.

    Alternatively, if indirect branches are common but they cannot be

    predicte…'
- author: Jan Beulich
  role: reviewer
  position: Acknowledges the proposed change and quotes the relevant part of the commit
    message, indicating review of the patch.
  quote: 'Replace NOP with UD0 or UD2 after indirect branch in PLT entries to

    implement optimization guide from Intel optimization manual:


    Assembly/Compiler Coding Rule 13. (M impact, L generality)


    When indirect branches are present, try to put the most likely target

    of an indirect branch immediately following the indirect branch.

    Alternatively, if indirect branches are common but they cannot be

    predicte…'
primer_expert: This patch modifies the generation of Procedure Linkage Table (PLT)
  entries for indirect jumps on x86-64. It replaces the standard NOP instructions
  with UD0 or UD2, which are intended to halt instruction decoding. This aims to optimize
  scenarios where branch prediction is unreliable, as per Intel's guidance.
primer_glossary:
- term: PLT
  definition: Procedure Linkage Table. A table used in ELF executables to resolve
    dynamic library function calls at runtime.
- term: x86-64
  definition: A 64-bit-based assembly language and related computer architecture.
- term: UD0/UD2
  definition: Undefined instruction opcodes that can be used to halt instruction decoding
    or signal an error.
- term: NOP
  definition: No Operation. An instruction that does nothing.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOoFbPvk27h+qnGu9xCfQ5z8LAkrr5L-5HPGR8PDD0XM5g@mail.gmail.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch replaces NOP instructions after indirect jumps in PLT entries with UD0 or UD2 on x86-64. This change aligns with Intel's optimization manual, aiming to improve performance by preventing the processor from decoding unintended fall-through paths. The changes affect the BFD library's ELF object file handling and include test suite adjustments.
