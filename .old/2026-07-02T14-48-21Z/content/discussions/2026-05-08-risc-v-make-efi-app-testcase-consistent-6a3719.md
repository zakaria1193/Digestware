---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- EFI
- testcase
- assembler
- linker
discussion_id: 66b89ff6-c7a8-41cf-8bee-bf1675c89db5@suse.com
source_type: public_inbox
title: '[PATCH] RISC-V: make EFI app testcase consistent'
headline: 'RISC-V: make EFI app testcase consistent'
tldr: The patch makes the RISC-V EFI app testcase consistent by aligning assembler
  and linker options.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Ensuring consistency between assembler and linker options improves test reliability.
- The change is specific to the RISC-V architecture and EFI environment.
exchanges: []
primer_expert: This patch modifies a RISC-V testcase for EFI applications. It ensures
  that the assembler and linker are invoked with consistent options, specifically
  related to endianness.  Inconsistent options can lead to build failures or unexpected
  behavior in test environments. The relevant file is `binutils/testsuite/binutils-all/riscv/pei-riscv64.d`.
primer_general: The binutils project contains a suite of tools used for working with
  binary files, including assemblers, linkers, and other utilities.  Testcases are
  used to ensure that these tools function correctly across different architectures
  and configurations.  This patch modifies a testcase for RISC-V, a modern open-source
  instruction set architecture, specifically for applications targeting the EFI (Extensible
  Firmware Interface) environment.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/66b89ff6-c7a8-41cf-8bee-bf1675c89db5@suse.com
bugzilla_url: null
date: '2026-05-08'
---

Jan Beulich submits a patch to make the RISC-V EFI app testcase consistent. The patch aligns the options passed to the assembler with those passed to the linker, specifically adding `-mlittle-endian` to the assembler flags, mirroring a previous fix that addressed linker crashes due to inconsistent use of options in testcases.
