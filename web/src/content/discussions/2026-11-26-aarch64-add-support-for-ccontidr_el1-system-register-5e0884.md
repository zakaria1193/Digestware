---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- gas
- opcode
- register
discussion_id: d6598ab2-a663-362c-e302-b099aadce9a3@e124511.cambridge.arm.com
source_type: public_inbox
title: 'Re: [PATCH] aarch64: Add support for ccontidr_el1 system register'
headline: 'aarch64: Add support for ccontidr_el1 system register'
tldr: Adds support for the read-only aarch64 ccontidr_el1 system register.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Ready to Land
outcome: ready
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adds new definitions for `ccontidr_el1` in `opcodes/aarch64-sys-regs.def`.
- Introduces new test cases (`sysreg-13.s` and `sysreg-13.d`) for basic read operations.
- Modifies `sysreg-diagnostic.s` and `sysreg-diagnostic.d` to test write attempts
  to the read-only register.
exchanges:
- author: Muhammad Kamran
  role: proposer
  position: Submitted a patch to add support for the `ccontidr_el1` system register
    on aarch64, including a new test case for reading it and an extension to a diagnostic
    test for writing attempts.
  quote: null
- author: Alice Carlotti
  role: reviewer
  position: LGTMs the patch, indicating approval and thanking the proposer.
  quote: LGTM, thanks.
primer_expert: This patch adds a new system register, `ccontidr_el1`, to the binutils
  assembler (`gas`) and disassembler (`objdump`) for the AArch64 architecture. This
  register is part of the AArch64 architecture's control and identification registers,
  specifically related to context identification. The changes involve updating `opcodes/aarch64-sys-regs.def`
  to recognize the new register and adding new test cases in `gas/testsuite/gas/aarch64/sysreg/`
  to ensure it can be correctly assembled/disassembled and that write attempts to
  this read-only register are diagnosed.
primer_glossary:
- term: aarch64
  definition: The 64-bit ARM architecture.
- term: system register
  definition: Special-purpose registers in ARM architectures used for controlling
    system behavior, memory management, and processor state.
- term: ccontidr_el1
  definition: A specific read-only AArch64 system register that provides identification
    information related to the execution context.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: objdump
  definition: A utility in GNU Binutils that displays information from object files,
    including disassembly.
- term: sysreg
  definition: Abbreviation for system register.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/d6598ab2-a663-362c-e302-b099aadce9a3@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

This patch adds support for the `ccontidr_el1` system register to the aarch64 assembler and disassembler. The register is read-only. The changes include adding the register definition and a new test case to verify its correct reading, as well as extending an existing diagnostic test to confirm that attempts to write to this read-only register are flagged.
