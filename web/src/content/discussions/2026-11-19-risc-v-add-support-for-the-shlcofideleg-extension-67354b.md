---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- extension
- interrupts
- virtualization
- assembler
discussion_id: CA+yXCZCtfnP4Kva17ENwEKew2pHWQ+KTk3+8vYM0sCQwZKWVwA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] RISC-V: Add support for the Shlcofideleg extension'
headline: 'RISC-V: Add support for the Shlcofideleg extension'
tldr: Adds assembler and linker support for the RISC-V Shlcofideleg extension.
proposer: Kito Cheng <kito.cheng@gmail.com>
consensus: Ready to Land
outcome: committed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Extends the toolchain's capabilities to support a new RISC-V hardware feature.
- Requires updates to the assembler and linker, along with new test cases.
exchanges:
- author: Jiawei
  role: proposer
  position: Proposes adding support for the Shlcofideleg extension, which enables
    delegation of local counter-overflow interrupts to VS-mode.
  quote: "Add Shlcofideleg 1.0, which permits delegation of local counter-overflow\n\
    interrupts to VS-mode.  Record its dependency on H and cover extension\nrecognition\
    \ and implication in the assembler testsuite.\n\nbfd/ChangeLog:\n\n        * elfxx-riscv.c\
    \ (riscv_implicit_subsets): Add Shlcofideleg.\n        (riscv_supported_std_s_ext):\
    \ Ditto.\n\ngas/ChangeLog:\n\n        * NEWS: Mention Shlcofideleg.\n        *\
    \ tests…"
- author: Kito Cheng
  role: reviewer
  position: Acknowledges the patch and confirms it has been pushed to the trunk.
  quote: pushed, thanks :)
primer_expert: This patch integrates support for the `shlcofideleg` extension into
  the RISC-V toolchain. This extension, dependent on the 'H' extension, modifies interrupt
  handling by allowing delegation of local counter-overflow interrupts to VS-mode.
  The changes affect `bfd/elfxx-riscv.c` for implicit subset recognition and supported
  extensions, and `gas/` for NEWS updates and testsuite additions.
primer_glossary:
- term: Shlcofideleg
  definition: A RISC-V extension that allows delegation of local counter-overflow
    interrupts to VS-mode. It depends on the 'H' extension.
- term: VS-mode
  definition: Virtualization mode in RISC-V architecture, enabling hypervisors to
    manage guest operating systems.
- term: H extension
  definition: The RISC-V 'H' extension provides basic hardware support for virtualization.
- term: assembler
  definition: A program that translates assembly language into machine code.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    component or system.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZCtfnP4Kva17ENwEKew2pHWQ+KTk3+8vYM0sCQwZKWVwA@mail.gmail.com
bugzilla_url: null
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This patch adds support for the RISC-V Shlcofideleg extension to binutils. The Shlcofideleg extension allows delegation of local counter-overflow interrupts to VS-mode and has a dependency on the 'H' extension. The changes include recognition and implication testing in the assembler.
