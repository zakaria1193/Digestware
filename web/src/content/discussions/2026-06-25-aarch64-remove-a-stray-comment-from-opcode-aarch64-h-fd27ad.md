---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- cleanup
- code-quality
discussion_id: 20260625143639.3909071-2-rearnsha@arm.com
source_type: public_inbox
title: '[PATCH 1/3] aarch64: Remove a stray comment from opcode/aarch64.h'
headline: 'Aarch64: Remove a stray comment from opcode/aarch64.h'
tldr: A patch cleans up `opcode/aarch64.h` by removing a lingering comment associated
  with a previously removed flag bit.
proposer: Richard Earnshaw <rearnsha@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Improves code readability and maintainability.
- Ensures comments accurately reflect the current code state.
- No functional impact or performance changes.
exchanges: []
primer_expert: This patch makes a trivial, non-functional change to `include/opcode/aarch64.h`.
  This header file defines various constants and macros used by the AArch64 opcode
  parsing and generation logic within Binutils, including flag bits that represent
  specific instruction properties. The change removes a comment referencing an instruction
  flag bit (bit 28) that was previously eliminated from the AArch64 instruction set
  definitions. This is a code hygiene operation to maintain consistency between code
  and comments.
primer_general: This discussion is about a very small and simple change to the AArch64
  part of the Binutils software. Binutils includes tools that help turn human-written
  code into machine code. Inside these tools, there are header files that contain
  definitions and notes for various parts of the ARM 64-bit architecture. This patch
  just removes an old note (a 'comment') from one of these files that described a
  specific internal flag. That flag was removed in an earlier update, so this change
  simply cleans up the code by taking out the now-irrelevant comment.
series_id: 'binutils:aarch64: remove a stray comment from opcode/aarch64.h'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260625143639.3909071-2-rearnsha@arm.com
bugzilla_url: null
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This patch provides a minor cleanup to the `aarch64.h` header file within the Binutils project. It removes a comment that described flag bit 28, a bit which was previously removed in an earlier patch. This change is purely for code hygiene, ensuring that the comments accurately reflect the current state of the code and removing outdated information.
