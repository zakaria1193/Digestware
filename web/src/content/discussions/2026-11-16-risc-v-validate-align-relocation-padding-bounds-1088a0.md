---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- linker
- alignment
- RFC
discussion_id: BL1PR11MB5978E4DD0720C4B7EDE9EB0AC9712@BL1PR11MB5978.namprd11.prod.outlook.com
source_type: public_inbox
title: '[RFC] RISC-V: Validate ALIGN relocation padding bounds'
headline: 'RISC-V: Validate ALIGN relocation padding bounds'
tldr: RFC proposes validating padding bounds for RISC-V ALIGN relaxation in the linker.
proposer: Dorian Vail <snozns@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding validation checks may slightly increase linking time.
- 'Deciding whether to implement this validation alongside the fix for Bugzilla #34844
  involves coordinating development efforts.'
exchanges: []
primer_expert: 'This RFC targets the RISC-V linker''s handling of the ALIGN pseudo-instruction,
  specifically during the relaxation phase where padding is added to satisfy alignment
  requirements. The proposal aims to add bounds checking to ensure that the calculated
  padding does not exceed the limits of the section it belongs to. This is motivated
  by potential issues like non-termination or incorrect linking behavior, as referenced
  by Bugzilla #34844.'
primer_glossary:
- term: ALIGN relaxation
  definition: A linker optimization where the linker adjusts the layout of code or
    data to meet specific alignment requirements, potentially adding padding.
- term: RISC-V
  definition: An open-standard instruction set architecture based on RISC principles.
- term: linker
  definition: A program that combines object files and libraries into an executable
    program.
- term: padding
  definition: Unused space inserted to meet alignment or other structural requirements.
- term: Bugzilla
  definition: An open-source web-based bug tracking system used by many projects,
    including the GNU toolchain.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/BL1PR11MB5978E4DD0720C4B7EDE9EB0AC9712@BL1PR11MB5978.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This RFC proposes a change to the RISC-V linker to validate that the padding required by the ALIGN relaxation fits within the input section. If the padding span exceeds the section boundaries, the linker should fail with a diagnostic. The author is seeking feedback and asking if this validation should be addressed concurrently with Bugzilla #34844, which concerns non-termination in the ALIGN path.
