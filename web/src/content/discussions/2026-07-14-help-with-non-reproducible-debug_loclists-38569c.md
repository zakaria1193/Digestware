---
project: gcc
subsystem: gcc
patch_id: null
tags:
- debugging
- dwarf
- gcc
- compilation
discussion_id: a82afd153187c3fdfa398b241acb3691@codethink.co.uk
source_type: public_inbox
title: Help with non-reproducible .debug_loclists
headline: Help with non-reproducible .debug_loclists
tldr: Developer seeks help debugging non-reproducible DWARF debug info in .debug_loclists,
  with varying addresses and values.
proposer: Nazar Kazakov <nazar.kazakov@codethink.co.uk>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensuring consistent DWARF output across compilations can impact optimization choices,
  as some optimizations might perturb debug information generation.
exchanges: []
primer_expert: The user is observing differences in .debug_loclists, a DWARF section
  detailing location expressions for variables. These differences, affecting start/end
  addresses and operation values (e.g., DW_OP_reg4, DW_OP_stack_value), suggest a
  potential issue in DWARF emission, possibly related to optimization, instruction
  scheduling, or internal compiler state that affects debug information generation
  reproducibility.
primer_glossary:
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers. It stores
    information about source code, such as variable names, types, and memory locations.
- term: .debug_loclists
  definition: A section within DWARF debugging information that stores location lists.
    These lists specify the address ranges where a variable is valid or accessible.
- term: DW_OP_reg4
  definition: A DWARF operation code indicating that a value is held in a specific
    register (register number 4).
- term: DW_OP_stack_value
  definition: A DWARF operation code that signifies the value on top of theDWARF expression
    stack should be considered the actual value of the variable.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/a82afd153187c3fdfa398b241acb3691@codethink.co.uk
bugzilla_url: null
date: '2026-07-14'
is_stub: false
stub_reason: ''
---

Nazar Kazakov is encountering non-reproducible DWARF debug information in the .debug_loclists section when building glslang with GCC. The issue manifests as variations in start/end values or other values within loclists, even when the source code is identical. Nazar is seeking insights into potential bugs or debugging strategies for this DWARF generation problem.
