---
project: binutils
subsystem: binutils
patch_id: null
tags:
- x86
- AMX
- ACE
- binutils
- documentation
discussion_id: CAKSQd8VRpMcV84Sv3=N1kW6w73Q-0spJqO-nc_K-cjyYSiJU2g@mail.gmail.com
source_type: public_inbox
title: x86 AMX/ACE with >8 tiles
headline: x86 AMX/ACE with >8 tiles
tldr: Discusses documentation and implementation considerations for x86 AMX/ACE supporting
  more than 8 tiles.
proposer: Christian Ludloff <ludloff@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Extends support for wider tile configurations in AMX/ACE, potentially increasing
  performance for specific workloads.
- Requires careful handling of instruction encodings and MSRs to ensure compatibility.
- Addresses potential specification oversights regarding memory operand widths.
exchanges:
- author: Christian Ludloff <ludloff@gmail.com>
  role: proposer
  position: Initiates discussion on documenting and supporting x86 AMX/ACE with more
    than 8 tiles, highlighting that existing VEX/EVEX encodings and TILECFG are mostly
    sufficient.
  quote: "I have been asked to document x86 AMX/ACE behavior\nof 16-tile and 32-tile\
    \ implementations.\n\nThe goal of a 16-tile or 32-tile HW implementation\nis to\
    \ achieve extra performance by running SW that\ntakes advantage of the extra tiles.\
    \ In particular,\nsaid SW is expected to mostly run compute kernels, \nminimize\
    \ process switches, and avoid tile usage in\ninterrupt handlers for storage and\
    \ networking. The…"
primer_expert: This discussion concerns the binutils assembler and disassembler's
  support for extended x86 AMX (Advanced Matrix Extensions) and ACE (Advanced Cryptography
  Extensions) instructions, specifically when implementations go beyond the initial
  8 tiles. It delves into the microarchitectural details and instruction encoding
  implications, such as the use of VEX/EVEX prefixes and the TILECFG MSR, to support
  up to 16 or 32 tiles (TMMs). The thread also anticipates potential issues with the
  `LDTILECFG`/`STTILECFG` instruction's memory operand width.
primer_glossary:
- term: AMX
  definition: Advanced Matrix Extensions, an x86 instruction set extension introduced
    with Intel's Ice Lake processors, designed to accelerate matrix operations, particularly
    for AI and machine learning workloads.
- term: ACE
  definition: Advanced Cryptography Extensions, another x86 instruction set extension
    often associated with AMX, providing hardware acceleration for cryptographic operations.
- term: Tiles
  definition: In the context of AMX, tiles are a fundamental unit of data processing,
    typically a 2D array used for matrix computations. Architectures can support a
    varying number of these tiles.
- term: VEX/EVEX
  definition: Vector Extension (VEX) and Enhanced Vector Extension (EVEX) are prefixes
    for x86 instructions that allow for advanced vector processing, including broader
    register access and extended instruction set support like AMX.
- term: TILECFG
  definition: Tile Configuration, a model-specific register (MSR) or similar mechanism
    used to configure the layout and dimensions of tiles used by AMX instructions.
- term: MSR
  definition: Model-Specific Register, special registers used by the CPU to control
    its behavior or report status.
- term: CPUID
  definition: An x86 instruction that returns information about the CPU's capabilities
    and features.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAKSQd8VRpMcV84Sv3=N1kW6w73Q-0spJqO-nc_K-cjyYSiJU2g@mail.gmail.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

Christian Ludloff is seeking to document and discuss the behavior of x86 AMX/ACE implementations that support 16 or 32 tiles. The focus is on how existing hardware and instruction encodings (VEX, EVEX) can accommodate these larger tile configurations, and the implications for software. The discussion touches upon CPUID reporting, TILECFG modifications, and potential oversights in the AMX specification regarding memory operand width.
