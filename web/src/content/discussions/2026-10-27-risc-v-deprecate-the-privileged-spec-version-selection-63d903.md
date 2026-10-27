---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- deprecation
- isa
- compiler
discussion_id: 20261027034041.1667435-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH 0/5] RISC-V: Deprecate the privileged spec version selection'
headline: 'RISC-V: Deprecate the privileged spec version selection'
tldr: Deprecates RISC-V privileged spec version selection options and related code
  across binutils components.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Simplifies the binutils codebase by removing legacy features.
- Aligns binutils with current RISC-V standards and best practices.
- May require users to adapt if they depended on the old versioning mechanism.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Proposes deprecating the RISC-V privileged spec version selection mechanism
    in binutils, citing its replacement by the Ss extension version and lack of modern
    relevance. The series plans to warn about deprecated options, remove unused CSRs,
    and clean up related code.
  quote: 'In the ISA spec, the idea of the privileged spec version has been

    replaced by the version of the Ss extension.  Also, the old

    compatibility logic is not very useful today.  When I search the web for

    these options, I find almost nothing but the binutils documentation and

    its tests.  On the RISC-V psABI side, we deprecated the related

    attributes a long time ago [1].  So I think it is time to leave…'
primer_expert: This patch series addresses the obsolescence of explicit RISC-V privileged
  specification version selection in binutils. The core idea is that the ISA spec
  has evolved, favoring the Ss extension version, rendering old mechanisms like `-mpriv-spec`
  and associated ELF attributes largely unused and complex. The series systematically
  deprecates these features, removes related code (like N extension CSRs), and updates
  documentation, simplifying the binutils codebase for RISC-V.
primer_glossary:
- term: RISC-V
  definition: A modular and extensible open-standard instruction set architecture
    (ISA) based on Reduced Instruction Set Computer principles.
- term: privileged spec version
  definition: A versioning scheme for the RISC-V privileged architecture specification,
    which defines system-level behavior and features. This mechanism is being superseded
    by newer approaches.
- term: Ss extension
  definition: A specific extension in the RISC-V architecture that relates to system-level
    features and their versioning, replacing older methods of versioning the privileged
    specification.
- term: CSR
  definition: Control and Status Register. Special registers in RISC-V used for system
    control and status information.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project, responsible for
    translating assembly language code into machine code.
- term: ld
  definition: The GNU linker, also part of GNU Binutils, responsible for combining
    object files and libraries into an executable or library.
- term: bfd
  definition: Binary File Descriptor library, part of GNU Binutils, which provides
    a common interface to various object file formats.
series_id: 'binutils:risc-v: deprecate the privileged spec version selection'
series_role: cover
series_parts:
- title: 'RISC-V: Deprecate the privileged spec version selection'
  url: https://inbox.sourceware.org/binutils/20261027034041.1667435-2-kito.cheng@sifive.com
  n: 1
  total: 5
url: https://inbox.sourceware.org/binutils/20261027034041.1667435-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

This patch series aims to deprecate and eventually remove the mechanism for selecting RISC-V privileged spec versions within binutils. The changes include marking options like `-mpriv-spec` and `--with-priv-spec` as deprecated with a default to version 1.13, removing obsolete N extension CSRs, and cleaning up related code in gas, ld, and bfd. The primary motivation is that the RISC-V ISA spec has moved to using the Ss extension version, making the old privileged spec versioning less relevant.
