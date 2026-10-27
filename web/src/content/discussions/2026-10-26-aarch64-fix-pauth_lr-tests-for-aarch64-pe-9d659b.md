---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- aarch64
- binutils
- testing
- PE/COFF
- assembler
discussion_id: 39e7c5f2-7517-46eb-93f2-8e8106f5e955@arm.com
source_type: public_inbox
title: 'Re: [PATCH] aarch64: Fix PAuth_LR tests for aarch4-pe'
headline: 'aarch64: Fix PAuth_LR tests for aarch64-pe'
tldr: Patch to fix aarch64-pe PAuth_LR tests due to a non-representable section alignment.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Replaces a direct alignment directive with `.org`-based padding, which might be
  slightly less direct but resolves the alignment issue.
- Relaxes disassembly expectations to accommodate PE/COFF symbol spelling, ensuring
  test stability.
exchanges:
- author: Muhammad Kamran
  role: proposer
  position: Presents a patch to fix aarch64-pe PAuth_LR test failures, which were
    caused by an unrepresentable section alignment, by using .org padding and relaxing
    disassembly expectations.
  quote: It addresses the aarch64-pe failure reported by Alan [1], where the PAuth_LR
    tests used .balign 0x40000 and caused a non-representable 2**18 .text section
    alignment for PE/COFF objects.
primer_expert: The patch modifies aarch64 test cases for PE/COFF object files. Specifically,
  it addresses an issue where the `.balign 0x40000` directive in PAuth_LR tests caused
  an alignment value (2^18) that is not representable in PE/COFF object files. The
  fix involves replacing `.balign` with `.org` for padding and adjusting the expected
  disassembly output to account for PE/COFF symbol naming conventions.
primer_glossary:
- term: aarch64
  definition: The 64-bit ARM architecture.
- term: PE/COFF
  definition: Portable Executable/Common Object File Format, a file format used for
    executables, object code, and DLLs on 32-bit and 64-bit versions of Windows operating
    systems. Sourceware uses this for some cross-compilation targets.
- term: PAuth_LR
  definition: Pointer Authentication for Link Register. A security feature on ARM
    architectures that uses cryptographic techniques to protect the Link Register
    from unauthorized modification.
- term: .balign
  definition: An assembler directive used to align the next piece of code or data
    to a specified boundary.
- term: .org
  definition: An assembler directive that sets the current assembly position to a
    specific address. It can be used for padding by specifying an address beyond the
    current position.
- term: symbol spelling
  definition: The specific way a symbol (like a function or variable name) is represented
    or named in an object file. Different formats or conventions can lead to variations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/39e7c5f2-7517-46eb-93f2-8e8106f5e955@arm.com
bugzilla_url: null
date: '2026-10-26'
is_stub: false
stub_reason: ''
---

This patch addresses a failure in aarch64-pe PAuth_LR tests caused by an excessively large section alignment (.balign 0x40000). The proposed fix replaces the alignment directive with '.org'-based padding and adjusts the expected disassembly to accommodate PE/COFF symbol spelling differences. This aims to resolve test failures and ensure correct object file generation for the aarch64 architecture on PE/COFF systems.
