---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- gas
- aarch64
- PE/COFF
- testing
discussion_id: 20261020131219.47814-1-muhammad.kamran@arm.com
source_type: public_inbox
title: '[PATCH] aarch64: Fix PAuth_LR tests for aarch64-pe'
headline: 'aarch64: Fix PAuth_LR tests for aarch64-pe'
tldr: Fixes alignment issues in aarch64 PAuth_LR tests for the PE/COFF target by using
  `.org` instead of `.balign` and adjusting expected output.
proposer: Muhammad Kamran <muhammad.kamran@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Muhammad Kamran <muhammad.kamran@arm.com>
  role: proposer
  position: Submits a patch to fix alignment issues in aarch64 PAuth_LR tests for
    the PE/COFF target by replacing `.balign` with `.org` and adjusting expected output.
  quote: 'Fix it by using .org directive and modify the test''s expected output

    to match PE/COFF,s .text+... spelling.'
primer_expert: This patch corrects issues in the GAS test suite for the aarch64 architecture,
  specifically concerning Pointer Authentication (PAuth) and the Link Register (LR),
  when targeting the PE/COFF object file format (used on Windows). The original tests
  employed `.balign 0x40000` to pad sections, but this large alignment value is not
  supported on PE targets. The fix replaces `.balign` with `.org` to achieve the correct
  spacing and adjusts the expected disassembly output to conform to the PE/COFF convention
  of representing addresses relative to the section start (`.text+...`).
primer_glossary:
- term: PAuth_LR
  definition: Pointer Authentication for the Link Register. A security feature that
    uses cryptographic hashes to protect the return address stored in the LR register
    from being tampered with.
- term: aarch64
  definition: The 64-bit ARM architecture.
- term: PE/COFF
  definition: Portable Executable/Common Object File Format. The standard file format
    for executables, object code, and DLLs in Windows operating systems.
- term: .balign
  definition: An assembler directive used to pad the current location to a specified
    alignment boundary, inserting NOPs or zero bytes as needed.
- term: .org
  definition: An assembler directive that sets the current location counter to a specified
    value. If the new value is greater than the current location, it is typically
    filled with zeros or NOPs.
- term: Link Register (LR)
  definition: In ARM architectures, the Link Register holds the return address for
    function calls.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261020131219.47814-1-muhammad.kamran@arm.com
bugzilla_url: null
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the aarch64 assembler's tests for PAuth_LR (Pointer Authentication for Link Register). The tests used `.balign 0x40000`, which caused alignment errors on the `aarch64-pe` (PE/COFF) target because the required alignment (2^18) is not representable. The fix replaces `.balign` with `.org` to achieve the desired offset and modifies the test's expected output to match the PE/COFF specific `.text+...` spelling.
