---
project: binutils
subsystem: powerpc
patch_id: null
tags:
- powerpc
- core files
- bfd
- readelf
- debugging
discussion_id: 20260622101408.1384811-1-abhay@linux.ibm.com
source_type: public_inbox
title: '[PATCH v1] PowerPC: Add NT_PPC_DMR core file support'
headline: 'PowerPC: Add NT_PPC_DMR core file support'
tldr: This patch adds support for the new NT_PPC_DMR note type, which stores Dense
  Math Register contents in PowerPC core files.
proposer: Abhay Kandpal <abhay@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Increased core file size due to additional register state being saved.
- Potential for compatibility issues with older tools if they encounter the new note
  type and misinterpret or discard it.
exchanges:
- author: Abhay Kandpal <abhay@linux.ibm.com>
  role: proposer
  position: Proposes adding support for a new PowerPC note type to handle Dense Math
    Registers in core files, highlighting its importance for future Power ISA debugging.
    The patch has undergone regression testing.
  quote: Add BFD and readelf support for the new NT_PPC_DMR note type, which carries
    the contents of the Dense Math Registers (DMR) available on a future PowerPC processor.
    The DMR register set consists of eight 1024-bit registers introduced by the Dense
    Math facility in a future Power ISA revision.
primer_expert: The Linux kernel's core file mechanism uses ELF notes (NT_*) to store
  various bits of process state, e.g., thread info (NT_PRSTATUS) or FPU state (NT_FPREGSET).
  This patch introduces a new note type, NT_PPC_DMR, to store the contents of the
  forthcoming Dense Math Registers (DMR). These are a new set of 1024-bit registers
  specific to a future Power ISA revision, requiring updates to bfd/elf.c for parsing
  and writing these notes during core dump analysis, and to readelf for human-readable
  display.
primer_general: When a program crashes, the operating system can create a 'core file'
  — a snapshot of the program's memory and processor state at the time of the crash.
  This file is critical for debugging, allowing developers to inspect variables, register
  values, and the program's execution path. This proposal introduces support for a
  new type of information, called NT_PPC_DMR, to be stored within these core files
  for PowerPC processors. This new note type specifically handles the contents of
  'Dense Math Registers' (DMRs), which are specialized high-performance computing
  registers that will be present in future PowerPC processors. This update ensures
  that debugging tools like `readelf` and `bfd` can correctly interpret and display
  the state of these new registers, which is essential for diagnosing issues in software
  that uses these advanced features.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260622101408.1384811-1-abhay@linux.ibm.com
bugzilla_url: null
date: '2026-06-22'
is_stub: false
---

This proposal introduces BFD and readelf support for the NT_PPC_DMR note type, enabling the storage of Dense Math Register (DMR) contents in PowerPC core files. These new registers are part of a future Power ISA revision and will contain eight 1024-bit registers. GDB support for reading and writing these registers, live and from core files, will follow in a separate patch. This change is crucial for debugging applications that utilize the forthcoming Dense Math facility on PowerPC processors.
