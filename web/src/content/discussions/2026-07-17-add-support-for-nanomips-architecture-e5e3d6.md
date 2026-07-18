---
project: binutils
subsystem: binutils
patch_id: null
tags:
- nanomips
- architecture
- assembler
- disassembler
- ELF
discussion_id: 20260717103858.199743-1-lei.wang@oss.cipunited.com
source_type: public_inbox
title: '[PATCH 0/6] Add support for nanoMIPS architecture'
headline: Add support for nanoMIPS architecture
tldr: Introduces support for the nanoMIPS architecture across binutils components.
proposer: Tsing <lei.wang@oss.cipunited.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This is the cover letter for a series adding nanoMIPS support to binutils.
  It touches Gas, BFD, opcodes, readelf, docs, and tests. The series integrates a
  new target architecture into the toolchain, requiring modifications across multiple
  components for proper handling of assembly, disassembly, object file formats, and
  associated toolchain utilities.
primer_glossary:
- term: nanoMIPS
  definition: A variant of the MIPS Reduced Instruction Set Computer (RISC) architecture,
    often optimized for embedded systems.
- term: Gas
  definition: The GNU Assembler, part of the binutils package, responsible for converting
    assembly language into machine code.
- term: BFD
  definition: Binary File Descriptor library. A low-level library used by binutils
    to provide a consistent interface for reading and writing various object file
    formats.
- term: Opcodes
  definition: A component of binutils that defines and handles instruction set architectures
    (ISAs), including their mnemonics, operands, and encoding.
- term: Readelf
  definition: A command-line utility that displays information about ELF (Executable
    and Linkable Format) files.
series_id: binutils:add support for nanomips architecture
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260717103858.199743-1-lei.wang@oss.cipunited.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This patch series introduces comprehensive support for the nanoMIPS architecture within the binutils project. It spans changes to Gas (assembler), BFD (binary file descriptor library), Opcodes, Readelf, documentation, and testing infrastructure. The core goal is to enable binutils to correctly assemble, disassemble, link, and analyze code for the nanoMIPS target.
