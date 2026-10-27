---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- elf
- linker
- assembler
discussion_id: 20261027034041.1667435-4-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH 3/5] RISC-V: Ignore the deprecated privileged spec attributes'
headline: 'RISC-V: Ignore the deprecated privileged spec attributes'
tldr: Removes assembler emission and linker processing of deprecated RISC-V privileged
  spec ELF attributes.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Removes code complexity associated with deprecated ELF attributes.
- Ensures compliance with the latest RISC-V psABI.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Removes the emission of deprecated RISC-V privileged spec ELF attributes
    by the assembler and stops the linker from processing them, simplifying code and
    tests.
  quote: 'The assembler no longer emits them when CSR or privileged instructions

    are used, so riscv_is_priv_insn and explicit_priv_attr are removed.


    The linker ignores them in the input and does not output them, so the

    1.9.1 conflict warning is gone too.  The attr-merge-priv-spec tests are

    reduced to one test that checks the attributes are dropped, and the gas

    tests that checked the emitted attributes are…'
primer_expert: This patch removes the code that emits and processes RISC-V specific
  ELF tags related to privileged specification versions (Tag_RISCV_priv_spec, etc.).
  The RISC-V psABI has deprecated these, and this change stops gas from emitting them
  and ld from interpreting them. Test cases are adjusted to reflect this removal,
  ensuring no regressions while cleaning up obsolete functionality.
primer_glossary:
- term: RISC-V psABI
  definition: The Application Binary Interface for the RISC-V architecture, defining
    conventions for how software components interact at the binary level, including
    object file formats and system calls.
- term: ELF
  definition: Executable and Linkable Format, a common standard file format for executables,
    object code, shared libraries, and core dumps, used by many Unix-like systems.
- term: Tag_RISCV_priv_spec
  definition: An ELF tag specifically for RISC-V that denotes the privileged specification
    version used by the code.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project, responsible for
    translating assembly language code into machine code.
- term: ld
  definition: The GNU linker, also part of GNU Binutils, responsible for combining
    object files and libraries into an executable or library.
series_id: 'binutils:risc-v: ignore the deprecated privileged spec attributes'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261027034041.1667435-4-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-10-27'
is_stub: false
stub_reason: ''
---

This patch modifies the RISC-V assembler and linker to ignore deprecated privileged spec ELF attributes (Tag_RISCV_priv_spec, Tag_RISCV_priv_spec_minor, Tag_RISCV_priv_spec_revision). The assembler will no longer emit these attributes, and the linker will not process them, thus removing the associated conflict warnings and simplifying tests. This change aligns with the RISC-V psABI's deprecation of these attributes.
