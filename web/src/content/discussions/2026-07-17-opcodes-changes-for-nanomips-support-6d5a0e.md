---
project: binutils
subsystem: binutils
patch_id: null
tags:
- opcodes
- disassembler
- nanomips
discussion_id: 20260717103858.199743-4-lei.wang@oss.cipunited.com
source_type: public_inbox
title: '[PATCH 3/6] Opcodes changes for nanoMIPS support.'
headline: Opcodes changes for nanoMIPS support.
tldr: Adds nanoMIPS instruction set handling to the opcodes library.
proposer: Tsing <lei.wang@oss.cipunited.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Extends the binutils opcodes library for nanoMIPS. This involves adding
  new header files (opcode/nanomips.h), new source files for disassembly (nanomips-dis.c),
  instruction formats (nanomips-formats.h), and opcodes (nanomips-opc.c). Configuration
  files and disassemble.c are updated to incorporate nanoMIPS support.
primer_glossary:
- term: opcodes library
  definition: A component of binutils that defines and handles instruction set architectures
    (ISAs), including their mnemonics, operands, and encoding.
- term: disassembler
  definition: A tool that translates machine code back into human-readable assembly
    language.
series_id: binutils:opcodes changes for nanomips support
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260717103858.199743-4-lei.wang@oss.cipunited.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This patch enhances the binutils opcodes library to support the nanoMIPS architecture. It introduces new header files, updates Makefiles and configuration scripts to recognize the nanoMIPS target, and adds new C source files for nanoMIPS disassembly, formats, and operation codes. Disassembler functions are also modified to include nanoMIPS.
