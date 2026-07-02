---
project: gcc
subsystem: lra
patch_id: null
tags:
- lra
- register-allocation
- performance
- gcc
discussion_id: ajuBckDkxUIVXvyu@li-819a89cc-2401-11b2-a85c-cca1ce6aa768.ibm.com
source_type: public_inbox
title: '[RFC] LRA: Carrying hard registers around'
headline: LRA needs to split live ranges for hard register assignments
tldr: The Live Range Allocator should split live ranges for hard registers that GCC
  assigns to pseudos, to prevent unsatisfiable allocations.
proposer: Stefan Schulze Frielinghaus <stefansf@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Increased instruction count due to potentially suboptimal reload placement if 'in-between'
  reloads are not optimized.
- Complexity in liveness analysis during `curr_insn_transform()` due to the lack of
  upfront liveness information.
exchanges:
- author: Stefan Schulze Frielinghaus <stefansf@linux.ibm.com>
  role: proposer
  position: Proposes a mechanism for the Live Range Allocator (LRA) to split live
    ranges of hard registers when they are temporarily assigned due to constraints,
    preventing allocation failures.
  quote: However, before diving into those missed optimizations, I would rather like
    to fix the place where such reloads should be introduced. At the moment I decided
    to check during curr_insn_transform() whether the currently selected alternative
    makes use of a hard register constraint and whether this particular hard register
    is live. If so, then create a new reload and emit moves before/after.
primer_expert: GCC's Live Range Allocator (LRA) aims to simplify register allocation
  by building on register-transfer language (RTL) and handling pseudo-registers efficiently.
  This proposal focuses on a specific challenge within LRA related to hard registers.
  When hard registers are constrained (e.g., due to specific instruction requirements),
  their live ranges can overlap in ways that LRA currently struggles to resolve, particularly
  when no liveness information is available at the point where moves might need to
  be emitted. The current implementation tries to address this by checking during
  `curr_insn_tran…
primer_general: Compilers like GCC translate source code into low-level instructions
  that a computer's processor can understand. A critical step in this process is 'register
  allocation,' where the compiler decides which pieces of data should reside in the
  processor's limited set of high-speed storage locations called 'registers.' The
  Live Range Allocator (LRA) is a module within GCC responsible for this. When a program
  needs to use a specific hardware register (a 'hard register') for a short period,
  it can create conflicts if that register is already in use by another part of the
  program. Currently, LRA can fail to manage these conflicts effectively, leading
  to errors or inefficient code. This proposal seeks to improve LRA's ability to temporarily
  free up and restore hard registers when needed, ensuring that the compiled program
  runs correctly and efficiently, especially on architectures with complex register
  usage rules.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/ajuBckDkxUIVXvyu@li-819a89cc-2401-11b2-a85c-cca1ce6aa768.ibm.com
bugzilla_url: null
date: '2026-06-24'
is_stub: false
---

This RFC proposes a change to GCC's Live Range Allocator (LRA) to handle live ranges of hard registers that become live due to hard register assignments. Currently, the LRA doesn't split these live ranges, which can lead to allocation failures. The proposed solution involves introducing temporary reloads around instructions that constrain hard registers, ensuring that those registers are available when needed.
