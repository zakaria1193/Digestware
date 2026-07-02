---
project: binutils
subsystem: x86/gas
patch_id: null
tags:
- gas
- x86
- debugging
- registers
discussion_id: 2557bc68-e260-4d2f-901f-5a3fadd2b254@suse.com
source_type: public_inbox
title: '[PATCH] x86/gas: add missing RegBND to debugging code'
headline: 'x86/gas: add missing RegBND to debugging code'
tldr: Add RegBND to the type_names array in x86 gas configuration.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The gas assembler's internal representation of x86 register classes,
  defined in tc-i386.c, maps symbolic names to internal types. This patch adds an
  entry for RegBND, which is related to Intel's MPX (Memory Protection Extensions).
primer_general: This change affects the GNU assembler (gas) on x86 systems. It ensures
  that a specific type of register, known as RegBND, is correctly recognized and handled
  by the assembler's debugging code. This is a minor correction to improve the assembler's
  internal data structures.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/2557bc68-e260-4d2f-901f-5a3fadd2b254@suse.com
bugzilla_url: null
date: '2026-06-29'
is_stub: false
stub_reason: ''
---

This patch adds the RegBND register class to the type_names array in gas/config/tc-i386.c. This was likely an oversight when MPX support was initially added, and its inclusion ensures proper debugging information for this register class.
