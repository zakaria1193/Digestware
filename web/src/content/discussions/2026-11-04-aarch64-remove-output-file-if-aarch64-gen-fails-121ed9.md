---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- build system
- makefile
- code generation
discussion_id: 87c38e44-de79-b716-a2d7-e6de5f29047c@e124511.cambridge.arm.com
source_type: public_inbox
title: '[PATCH 01/28] aarch64: Remove output file if aarch64-gen fails'
headline: 'aarch64: Remove output file if aarch64-gen fails'
tldr: Ensures AArch64 generated opcode files are removed if generation fails, preventing
  stale files from causing build issues.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Prevents build failures caused by incomplete generated files.
- Improves robustness of the build process.
exchanges: []
primer_expert: This patch adjusts the `Makefile.am` and `Makefile.in` in `opcodes/`
  to add error handling to the generation rules for AArch64 opcode-related C and header
  files. Specifically, it appends `|| ( rm $@ && false )` to the commands that invoke
  `aarch64-gen`. This ensures that if `aarch64-gen` fails (returns non-zero exit status),
  the incomplete output file (`$@`) is removed, and the `make` command itself fails,
  preventing stale generated files from being used in subsequent build steps.
primer_glossary:
- term: aarch64-gen
  definition: A code generator tool used within binutils to produce AArch64 assembly,
    disassembly, and opcode table source files based on definitions.
- term: Makefile
  definition: A file that contains instructions for the `make` utility, used to automate
    the build process of software projects.
- term: stale file
  definition: A file that is outdated and no longer accurately reflects the current
    state of the source code or build process. In this context, it refers to an incomplete
    or incorrect generated file.
- term: Link error
  definition: An error that occurs during the linking phase of compilation, where
    the linker cannot resolve references between different object files or libraries,
    often due to missing symbols or incompatible code.
series_id: 'binutils:aarch64: remove output file if aarch64-gen fails'
series_role: reply
series_parts: []
url: https://inbox.source87c38e44-de79-b716-a2d7-e6de5f29047c@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch modifies the AArch64 build process to ensure that generated opcode files (like `aarch64-asm-2.c`, `aarch64-dis-2.c`, etc.) are removed if the `aarch64-gen` tool fails. Previously, incomplete or erroneous output files could be left behind, potentially causing subsequent build steps to succeed with outdated or incorrect code, leading to subtle errors later in the build or link phase.
