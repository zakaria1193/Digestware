---
project: binutils
subsystem: objdump
patch_id: null
tags:
- binutils
- objdump
- pe format
- aarch64
- import table
discussion_id: 17d4f2f8-e520-4c16-91a0-6db4aa75db57@dronecode.org.uk
source_type: public_inbox
title: 'Re: [PATCH] objdump: Fix private header (''-p'') import table output for pe-aarch64'
headline: 'objdump: Fix private header (''-p'') import table output for pe-aarch64'
tldr: Corrects objdump's output for PE import tables on 64-bit ARM and other non-x86_64
  architectures by properly distinguishing PE32 and PE32+ formats.
proposer: Jon Turney <jon.turney@dronecode.org.uk>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Code formatting and maintainability concerns raised by a reviewer.
- Ensuring consistent handling of PE32+ across various 64-bit architectures.
exchanges:
- author: Jon Turney
  role: proposer
  position: Submits a revised patch to fix objdump's PE import table output for pe-aarch64
    and other 64-bit arches, addressing an issue where the distinction between PE32
    and PE32+ was incorrectly implemented.
  quote: I attach a revised patch since I'm not entirely sure of the desired formatting
    and indentation here.
- author: Jan Beulich
  role: reviewer
  position: Approved the fix conceptually but suggested improving code formatting
    by splitting long lines and potentially consolidating conditional checks into
    a single manifest constant for better maintainability.
  quote: Okay, albeit preferably with ... ... this line split for each part to remain
    within 80 columns (no matter that other such long lines exist).
primer_expert: This patch in binutils' `objdump` addresses an issue in `pe_print_idata`
  when processing PE32+ files on architectures other than x86_64 (e.g., AArch64).
  The original code incorrectly used a conditional that did not account for PE32+
  on these platforms, leading to truncated import table output. The fix expands the
  conditional to include specific PE32+ defines for AArch64 and other 64-bit architectures.
primer_general: This change corrects a bug in the `objdump` tool, which is used to
  examine executable files. When inspecting the import table of certain 64-bit Windows
  program files (compiled for architectures like ARM64), `objdump` was cutting off
  the information after the first entry. This fix ensures that `objdump` correctly
  reads and displays the entire import table for these files by properly recognizing
  the file format differences.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/17d4f2f8-e520-4c16-91a0-6db4aa75db57@dronecode.org.uk
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

Jon Turney provides a revised patch for objdump to fix how it displays import table information for PE files on 64-bit ARM and similar architectures. The issue was that the output was truncated for these architectures because the code incorrectly distinguished between 32-bit (PE32) and 64-bit (PE32+) formats. The fix involves updating conditional logic to correctly handle PE32+ on these new architectures.
