---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- deprecation
- documentation
discussion_id: 20261027034041.1667435-6-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH 5/5] RISC-V: Add NEWS entries for the privileged spec deprecation'
headline: 'RISC-V: Add NEWS entries for the privileged spec deprecation'
tldr: Adds NEWS entries in binutils, gas, and ld to document the deprecation of RISC-V
  privileged spec options and attributes.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Simplifies binutils code by removing support for a deprecated feature.
- May require users to update toolchains if they relied on selecting older privileged
  spec versions.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Adds NEWS entries to binutils, gas, and ld to document the deprecation
    of RISC-V privileged spec options and attributes, informing users that these are
    deprecated and have no effect.
  quote: 'Describe the deprecated privileged spec options and attributes in the

    gas, binutils and ld NEWS files.'
primer_expert: This series removes the explicit selection of RISC-V privileged specification
  versions (e.g., via -M priv-spec, --with-priv-spec, or ELF attributes). Historically,
  binutils supported multiple privileged spec versions, but this mechanism is being
  deprecated in favor of the Ss extension version. These patches remove the code that
  handled these old versions, deprecate the related options, and update NEWS files
  to reflect these changes.
primer_glossary:
- term: RISC-V privileged spec
  definition: Defines the base instruction set and extensions related to system-level
    privileges in RISC-V architecture, including aspects like Control and Status Registers
    (CSRs) and memory management.
- term: psABI
  definition: The Application Binary Interface for the RISC-V architecture, defining
    conventions for how software components interact at the binary level, including
    object file formats and system calls.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps, used by many Unix-like systems.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project, responsible for
    translating assembly language code into machine code.
- term: ld
  definition: The GNU linker, also part of GNU Binutils, responsible for combining
    object files and libraries into an executable or library.
series_id: 'binutils:risc-v: add news entries for the privileged spec deprecation'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261027034041.1667435-6-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

This patch series introduces NEWS entries for binutils, gas, and ld to announce the deprecation of RISC-V privileged spec version selection options and related attributes. The changes aim to align with the evolving RISC-V ISA spec, where the concept of a privileged spec version is replaced by the Ss extension version. Developers are advised to use binutils 2.47 or earlier for older privileged spec versions.
