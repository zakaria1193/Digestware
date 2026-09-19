---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- arm
- encoding
- linker
- security
commit_hash: ed90621b022ea9f508d71d58a2db9b33162ec760
source_type: public_inbox
author: Christophe Lyon <clyon@sourceware.org>
headline: 'ARM: Fix BE8 encoding for Secure Gateway stubs'
tldr: Corrects ARM BE8 encoding for CMSE stubs to match expected output.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The ARM BFD backend's `elf32_arm_final_link` function incorrectly handled
  Secure Gateway stub sections (`.gnu.sgstubs`) in BE8 mode. These sections were not
  included in the regular stub group processing, preventing BE8 encoding. This patch
  adds specific handling for `cmse_stub_sec` to ensure correct BE8 encoding, verified
  by a new test case checking the raw instruction bytes.
primer_glossary:
- term: BE8
  definition: Big-Endian 8-bit mode, a specific endianness configuration for ARM processors
    where data is accessed in 8-bit chunks, with the most significant byte first.
- term: Secure Gateway (SG) stubs
  definition: Code stubs used in ARM's TrustZone technology for secure function calls
    between secure and non-secure worlds.
- term: veneers
  definition: Small pieces of code that act as intermediaries, often used for function
    calls, jumps, or to bridge different code segments or security states.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260918124125.C26E34B9DB4E@sourceware.org
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

This commit fixes an issue with ARM's Big-Endian 8-bit (BE8) encoding for Secure Gateway (SG) stubs. The Secure Gateway veneers were not being correctly processed for BE8 encoding during the final link phase, leading to incorrect byte ordering in the generated code. The fix ensures these stubs are handled properly and includes a new testcase to verify the correct encoding.
