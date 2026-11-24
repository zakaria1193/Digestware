---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- architecture
- deprecation
discussion_id: 20261123142801.1435245-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH] RISC-V: Deprecate -misa-spec and drop the ISA spec classes'
headline: 'RISC-V: Deprecate -misa-spec and drop the ISA spec classes'
tldr: Deprecates the -misa-spec option and removes ISA spec classes in binutils for
  RISC-V, as they do not align with newer ISA specifications.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Removes functionality related to `-misa-spec` which may break build systems relying
  on it, although it is deprecated.
- Simplifies the internal logic for handling RISC-V ISA versions, potentially improving
  maintainability.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Submits a patch to deprecate the `-misa-spec` option and remove RISC-V
    ISA spec classes from binutils.
  quote: 'Only i, a, f, d and q have default versions that depend on the ISA

    spec, and GCC passes -misa-spec=20191213 by default.  The spec classes

    do not fit newer ISA specs either, where each extension has its own

    version, so it is time for this logic to become history.  Remove the

    ISA spec classes, so each extension has a single default version, the

    20191213 one for the base extensions.  The 1.12 and 1.…'
primer_expert: This patch affects binutils' handling of RISC-V architecture specifications.
  It removes the concept of 'ISA spec classes' (e.g., for 20191213, 20190608) used
  in options like `-march` and `-misa-spec`. These classes are being deprecated because
  newer RISC-V specifications define extensions independently, rather than as monolithic
  'specs'. The change simplifies the internal representation by mapping extensions
  directly, deprecates `-misa-spec` to no-op, and updates tests accordingly. The default
  spec remains 20191213 for base extensions.
primer_glossary:
- term: RISC-V
  definition: An open-standard Instruction Set Architecture (ISA) based on reduced
    instruction set computer principles, designed for flexibility and extensibility.
- term: -misa-spec
  definition: A compiler/assembler option that specifies a particular version or standard
    of the RISC-V Instruction Set Architecture.
- term: ISA spec classes
  definition: Internal classifications or groupings within binutils that represent
    specific versions or standards of the RISC-V ISA.
- term: extension
  definition: In RISC-V, optional sets of instructions that add functionality to the
    base ISA (e.g., 'M' for multiplication/division, 'F' for floating-point).
- term: assembler
  definition: A program that translates assembly language into machine code.
- term: configure
  definition: A script used in the build process of many open-source projects to adapt
    the software to a specific system environment.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261123142801.1435245-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

This patch deprecates the `-misa-spec` option and removes the associated ISA specification classes from binutils' RISC-V support. These classes, designed for older ISA specifications where extensions had single versions, are no longer suitable for newer specifications where each extension has its own version. While the `-misa-spec` option is kept for backward compatibility, it will have no effect. The change also updates related tests and warnings.
