---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- AVX
- CPU extensions
- naming conventions
discussion_id: SJ5PPF77D28E3C21A8084B3CB97F8194B52ECC62@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
source_type: public_inbox
title: 'RE: [PATCH] x86: separate AVX10.1-aux from AVX10.2'
headline: 'x86: separate AVX10.1-aux from AVX10.2'
tldr: Discussion on naming conventions for AVX10.1-aux and AVX10.2-aux feature bits
  in the assembler, seeking AMD's opinion.
proposer: '"Jiang, Haochen" <haochen.jiang@intel.com>'
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Choosing `avx10.1aux` over `avx10_v1_aux` might be simpler for direct use but less
  aligned with potential documentation standards.
- Ensuring naming consistency across related extensions is important for usability
  but may require waiting for external input (from AMD).
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Suggested potentially aligning the name with documentation, e.g., 'avx10_v1_aux'.
  quote: Maybe avx10_v1_aux instead of avx10.1aux to align with documentation?
- author: Jiang, Haochen
  role: proposer
  position: Prefers 'avx10.1aux' if 'v1' is not used and seeks AMD's opinion on naming
    for consistency.
  quote: 'If we do not want to use v1, then the current name is definitely a win.


    This is an AMD proposed feature bit actually, while Intel will emulate that bit

    to avoid break on HW. So, let''s wait AMD folks to share their opinion on option

    names. We also need to make sure that it is the same naming convention as

    AVX10_V2_AUX.'
- author: Jiang, Haochen
  role: proposer
  position: Pings for an update on AMD's opinion regarding naming conventions for
    AVX10 auxiliary extensions.
  quote: 'Ping for this discussion, Ganesh, what is AMD''s opinion on this? Do you
    want

    to keep the "v" in name? Whatever it is, we need to keep the naming convention

    same between AVX10_V1_AUX and AVX10_V2_AUX.'
primer_expert: This is an iterative discussion concerning the naming of new CPU feature
  bits within the GNU Assembler (`gas`) support for x86 processors. Specifically,
  it relates to the AVX10 instruction set extensions. The patch introduces `AVX10_1_AUX`.
  The debate is about whether to name this feature bit `avx10.1aux` (as proposed)
  or `avx10_v1_aux` (suggested for better alignment with documentation). The crucial
  point is that this is an AMD-proposed feature, and clarity is needed on AMD's preferred
  naming convention to ensure consistency with other AVX10 variants (like `AVX10_V2_AUX`)
  and to avoid regres…
primer_glossary:
- term: x86
  definition: A family of instruction set architectures for computer processors, widely
    used in desktop and server computers.
- term: AVX10
  definition: A proposed instruction set extension for x86 processors, extending AVX-512
    capabilities.
- term: AVX10.1-aux
  definition: A specific auxiliary capability related to the AVX10.1 instruction set.
- term: AVX10.2
  definition: Another iteration or variant of the AVX10 instruction set extensions.
- term: feature bit
  definition: A flag or bit in a CPU's status register or architectural definition
    that indicates the presence or availability of a particular instruction set extension
    or capability.
- term: GNU Assembler (gas)
  definition: The assembler component of the GNU Binutils, responsible for converting
    assembly language code into machine code.
- term: naming convention
  definition: A set of rules to follow when naming entities such as variables, functions,
    classes, etc., in programming.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/SJ5PPF77D28E3C21A8084B3CB97F8194B52ECC62@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

This email is a follow-up to a discussion about naming conventions for new x86 instruction set extensions in the GNU assembler. The core of the discussion is the naming of `AVX10.1-aux` feature bits. Jiang, Haochen, references a previous exchange where Jan Beulich suggested aligning the name with documentation, potentially using `avx10_v1_aux`. Haochen leans towards `avx10.1aux` if `v1` is not preferred, but notes that this is an AMD-proposed feature and they need to confirm their naming preference to ensure consistency with `AVX10_V2_AUX`.
