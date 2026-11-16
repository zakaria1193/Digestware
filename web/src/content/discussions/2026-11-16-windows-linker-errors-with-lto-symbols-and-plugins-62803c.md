---
project: binutils
subsystem: windows
patch_id: null
tags:
- binutils
- linker
- windows
- LTO
- plugin
discussion_id: CAP2b4GOx0mO9ws8wPC4QPxKYZ=fJoz=6KsC616Zhb6ybGm6+uQ@mail.gmail.com
source_type: public_inbox
title: 'Windows: Late references to symbols claimed by linker plugin appear to cause
  defined in discarded section errors'
headline: Windows linker errors with LTO symbols and plugins
tldr: Patch addresses linker errors on Windows when using LTO objects with plugins,
  where late symbol references cause 'defined in discarded section' errors.
proposer: Julian Waters <tanksherman27@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Potential complexity in symbol handling logic to accommodate plugin interactions
  and LTO.
- Ensuring correct resolution of symbol definitions regardless of when references
  appear in the linking process.
exchanges: []
primer_expert: This issue concerns the interaction between binutils' linker (ld.exe),
  Link Time Optimization (LTO), and linker plugins on Windows. Specifically, it addresses
  a race condition or incorrect handling of symbol resolution when a linker plugin
  claims symbols as GIMPLE IR. Late references to these symbols, occurring after the
  plugin's initial pass, cause the linker to fail because the symbol's definition
  is found in a section marked for exclusion (SEC_EXCLUDE), which the plugin might
  have used for intermediate storage.
primer_glossary:
- term: Link Time Optimization (LTO)
  definition: A compiler optimization technique where optimization across multiple
    object files is performed during the linking stage, rather than per compilation
    unit.
- term: linker plugin
  definition: An extension mechanism for the GNU linker (ld) that allows third-party
    tools or custom logic to participate in the linking process.
- term: GIMPLE
  definition: GCC's internal representation language used for optimization after parsing.
- term: SEC_EXCLUDE
  definition: A section flag in object files indicating that the section should not
    be included in the final executable.
- term: ld.exe
  definition: The GNU linker executable, commonly used on Windows via MinGW or Cygwin.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAP2b4GOx0mO9ws8wPC4QPxKYZ=fJoz=6KsC616Zhb6ybGm6+uQ@mail.gmail.com
bugzilla_url: null
date: '2026-11-16'
is_stub: false
stub_reason: ''
---

This patch addresses a linker error on Windows occurring when linking objects compiled with Link Time Optimization (LTO). The issue arises when linker plugins claim symbols as GIMPLE, leading to problems with late references. These late references, appearing after the plugin has run, cause the linker to incorrectly report symbols as defined in discarded sections, preventing the link. The proposed solution involves modifying how symbols are handled to prevent this conflict.
