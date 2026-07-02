---
project: binutils
subsystem: libsframe
patch_id: null
tags:
- libsframe
- security
- buffer overflow
- binutils
- objdump
discussion_id: 178207634240.2958.13202347064770017350@digiscrypt.com
source_type: public_inbox
title: '[PATCH] libsframe: validate FDE/FRE subsection bounds in sframe_decode'
headline: 'libsframe: validate FDE/FRE subsection bounds in sframe_decode'
tldr: A patch for `libsframe` prevents out-of-bounds heap reads by validating FDE/FRE
  subsection bounds during `sframe_decode` to fix a security vulnerability.
proposer: Naveed Khan <naveed@digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: null
technical_tradeoffs:
- Increased code complexity in `sframe_decode` due to added bounds checks.
exchanges:
- author: Naveed Khan
  role: proposer
  position: Proposes a patch to `libsframe` to validate FDE/FRE subsection bounds
    during decoding, preventing out-of-bounds heap reads.
  quote: Validate in sframe_decode that the FDE and FRE sub-sections described by
    the header are fully contained in the buffer before they are read.
primer_expert: The `libsframe` library handles SFrame data, a binary format used for
  storing stack unwinding information. This patch targets the `sframe_decode` function,
  which parses the SFrame header (`sfh_fdeoff`, `sfh_freoff`, `sfh_num_fdes`, `sfh_fre_len`)
  and reads Function Descriptor Entries (FDEs) and Function Return Entries (FREs).
  The vulnerability arises because `sframe_header_sanity_check_p` only checks relative
  offsets, not against the total buffer size, allowing crafted SFrame sections to
  cause `sframe_fde_tbl_init` or `memcpy` to read past the end of the input buffer.
  The fix involves explici…
primer_general: This discussion is about a security fix for a library called `libsframe`,
  which is part of the Binutils toolchain (tools like assemblers, linkers, and debuggers).
  `libsframe` helps in understanding how a program's functions are called, which is
  useful for debugging. The problem was that a specially crafted input file could
  trick the library into reading outside of its designated memory area, potentially
  causing a program to crash or become vulnerable to malicious attacks. The proposed
  fix adds checks to ensure that the library only reads data within the allocated
  boundaries, making the software more secure and reliable, especially when handling
  potentially untrusted input files.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/178207634240.2958.13202347064770017350@digiscrypt.com
bugzilla_url: null
date: '2026-06-21'
is_stub: false
---

This patch addresses a security vulnerability in the `libsframe` library by adding robust bounds checking during the decoding of SFrame data. Previously, a malformed SFrame section could lead to out-of-bounds heap reads when processed by tools like `objdump` or `readelf`. The proposed change validates that all Function Descriptor Entries (FDE) and Function Return Entries (FRE) subsections are fully contained within the SFrame buffer before being accessed. This significantly improves the robustness and security of tools processing SFrame data by preventing potential crashes or exploits from crafted input.
