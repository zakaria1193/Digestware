---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gas
- SH4
- build-fix
- compiler
discussion_id: 179518902297.39706.377568521193588250.sendpatchset@1.0.0.127.in-addr.arpa
source_type: public_inbox
title: '[PATCH] Fix build error in gas/config/tc-sh.c'
headline: Fix build error in gas/config/tc-sh.c
tldr: Corrects a build error in the SH target's assembler configuration by changing
  a boolean literal from an integer to a proper boolean type.
proposer: Magnus Damm <magnus.damm@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Corrects a minor type mismatch for improved build stability.
- No functional change, solely a build fix.
exchanges:
- author: Magnus Damm <magnus.damm@gmail.com>
  role: proposer
  position: Submits a patch to fix a build error in `gas/config/tc-sh.c` for the SH4
    target by changing `1` to `true` for a boolean assignment.
  quote: seg_info (now_seg)->tc_segment_info_data.in_code = true;
primer_expert: The change modifies `gas/config/tc-sh.c`, specifically the `seg_info`
  structure, to correct a type mismatch. The `in_code` member, likely a boolean, was
  being assigned an integer `1` instead of the boolean literal `true`, causing a build
  failure in certain configurations like `sh4-unknown-elf`.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: SH4
  definition: A specific microarchitecture from the SuperH RISC architecture family.
- term: tc-sh.c
  definition: Configuration file for the SuperH architecture within the GNU Assembler.
- term: boolean literal
  definition: A value representing true or false, typically written as `true` or `false`
    in C++ and other languages, or `1` and `0` in C.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/179518902297.39706.377568521193588250.sendpatchset@1.0.0.127.in-addr.arpa
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch fixes a build error encountered when compiling binutils for the SH4 target with the `sh4-unknown-elf` configuration. The error occurred in `gas/config/tc-sh.c` due to an incorrect type for a boolean flag, which has been corrected to use `true` instead of `1`.
