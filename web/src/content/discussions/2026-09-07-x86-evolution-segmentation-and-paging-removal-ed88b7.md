---
project: binutils
subsystem: binutils
patch_id: null
tags:
- x86
- segmentation
- paging
- architecture evolution
- binutils
discussion_id: CAKSQd8XJVf3jq8boOJcOE_GzcNvcqMUHeW-whbw3uGnVE2iN_w@mail.gmail.com
source_type: public_inbox
title: x86 evolution for segmentation and paging
headline: 'x86 evolution: segmentation and paging removal'
tldr: Proposal to drop x86 segmentation and compatibility modes for a new PM64-only
  world.
proposer: Christian Ludloff <ludloff@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 8
sentiment_score: null
technical_tradeoffs:
- Simplifies assembler and linker code by removing support for legacy modes.
- Removes support for older x86 processors and operating systems that rely on segmentation.
- Requires new tooling and compiler support to target the simplified architecture.
exchanges: []
primer_expert: This proposal targets the removal of legacy x86 segmentation and compatibility
  modes, including segment registers (CS, SS, DS, ES, FS, GS), descriptor tables (GDT,
  IDT, LDT, TSS), and related instructions. This is driven by new architectural features
  like FRED (Flexible Return and Event Delivery) and APX, enabling a cleaner, "PM64-only"
  execution environment. The changes aim to simplify the assembler's and linker's
  handling of x86 code generation.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAKSQd8XJVf3jq8boOJcOE_GzcNvcqMUHeW-whbw3uGnVE2iN_w@mail.gmail.com
bugzilla_url: null
date: '2026-09-07'
is_stub: false
stub_reason: ''
---

This discussion proposes a significant shift in x86 architecture support within binutils, aiming to remove legacy segmentation and compatibility modes. The changes are motivated by the advent of Intel's FRED and APX specifications, and a new "PM64-only" operating mode. The proposal details the removal of numerous segment registers, table registers, and associated instructions, effectively simplifying the x86 architecture for future processors.
