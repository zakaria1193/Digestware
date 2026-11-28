---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- riscv
- testing
- emulation
discussion_id: bec2ed59-4dfc-4939-b31c-f717a4d8ea55@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH] ld: RISC-V: Select the matching emulation for Zcmt tests'
headline: 'ld: RISC-V: Zcmt tests emulation selected'
tldr: Patch to select correct emulation for RISC-V Zcmt tests has been merged.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jiawei
  role: maintainer
  position: Merged the patch after positive review and acknowledgment of a reported
    issue.
  quote: Pushed, thanks for the review and report.
- author: Kito Cheng
  role: reviewer
  position: Reviewed and approved the patch.
  quote: LGTM
- author: Jiawei
  role: proposer
  position: Submitted a patch to select the matching emulation for RISC-V Zcmt tests.
  quote: 'Most table-jump tests assemble RV64 objects. On riscv32-elf the

    linker defaults to ELF32 and rejects those objects before the tests

    reach the relaxation or inspect the jump table.


    Select LP64 for this group and use the target byte order for the

    cases that specify their own XLEN. Keep the explicit little- and

    big-endian tests in their respective emulations.


    Use objdump -z in tests that inspect s…'
primer_expert: This merged patch addresses a test suite configuration issue for RISC-V
  within the GNU linker (ld). The Zcmt tests, which focus on table-jump instructions
  and potentially relaxation, were failing on 32-bit RISC-V targets because the linker
  defaulted to an ELF32 emulation instead of the required LP64 (64-bit Linux). The
  fix ensures the correct emulation is selected, allowing these tests to run as intended.
  Additionally, it refines how sparse jump tables are inspected using `objdump -z`
  on big-endian systems.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or another object file.
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on RISC principles,
    increasingly adopted for various computing applications.
- term: emulation
  definition: In this context, refers to the linker's interpretation of the target
    architecture and ABI (Application Binary Interface), which affects how object
    files are processed.
- term: LP64
  definition: A data model where `long` and pointer types are 64 bits, commonly used
    in 64-bit Unix-like systems. Contrasts with ILP32 where `int` is 32 bits and `long`/pointers
    are 64 bits.
- term: ELF32
  definition: The 32-bit version of the Executable and Linkable Format, a common standard
    for object file formats.
- term: relaxation
  definition: A linker optimization technique where the linker adjusts branch offsets
    and other relative addressing information to produce smaller or more efficient
    code.
- term: objdump
  definition: A command-line utility that displays information from object files,
    including disassembled code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/bec2ed59-4dfc-4939-b31c-f717a4d8ea55@iscas.ac.cn
bugzilla_url: null
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

Jiawei has merged a patch that corrects the emulation selection for RISC-V Zcmt tests. The tests, which primarily assemble RV64 objects, previously defaulted to ELF32 on riscv32-elf, causing them to be rejected before reaching the relaxation or jump table inspection stages. The patch sets the emulation to LP64 for this test group and adjusts endianness handling.
