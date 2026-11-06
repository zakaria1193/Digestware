---
project: binutils
subsystem: mips
patch_id: null
tags:
- binutils
- mips
- allegrex
- vfpu
- psp
discussion_id: cover.1793910298.git.dublikunt@gmail.com
source_type: public_inbox
title: '[RFC PATCH 0/3] MIPS: Allegrex VFPU and PSP target support (trunk)'
headline: 'MIPS: Allegrex VFPU and PSP target support (trunk)'
tldr: Yaroslav Solodovnyk proposes adding Allegrex VFPU assembler/disassembler and
  PSP linker support to Binutils trunk, porting it from a downstream tree and fixing…
proposer: Yaroslav Solodovnyk <dublikunt@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 6
technical_tradeoffs:
- Integrating downstream code (PSP/VFPU support) into upstream Binutils vs. ensuring
  code quality, license compliance, and compatibility with the main branch.
- Adding new target support vs. potential increase in build complexity and testing
  burden.
- Fixing assembler macro parsing and instruction encoding for Allegrex vs. maintaining
  stability for existing MIPS support.
exchanges:
- author: Yaroslav Solodovnyk
  role: proposer
  position: Proposes adding Allegrex VFPU and PSP target support to Binutils trunk,
    porting from a downstream tree and fixing related assembler macros and instruction
    encoding.
  quote: "Hello,\n\nThis RFC adds Allegrex VFPU assembler/disassembler support and\
    \ PSP linker\nsupport, together with regression checks for the load-immediate\
    \ macros.\nIt is rebased onto current Binutils trunk as fetched on 2026-11-05:\n\
    \n  2364e17098e63e0af17c5329dec1ca8cd82c6cbb\n  ld: Couple of fixes for Win32\
    \ section of linker manual\n\nUpstream already recognizes scalar Allegrex. The\
    \ VFPU instruction parsing,…"
- author: Yaroslav Solodovnyk
  role: proposer
  position: Provides a summary of the first patch, detailing the porting of PSP/VFPU
    support and adjustments to assembler APIs.
  quote: 'Port the PSP/VFPU implementation from pspdev/binutils-gdb commit a8b53fe2b5825fa86337623c743d21a19aeb0daf
    to Binutils 2.47. Retain upstream Allegrex ELF machine flags and Loongson GS464
    support.


    Adapt the assembler operand initialization and bool API. Repair lvi/lvhi parsing,
    macro IDs, expansion and row/column lane offsets. Parse half-float immediates
    directly as IEEE binary16, diagnose overflo…'
- author: Yaroslav Solodovnyk
  role: proposer
  position: Explains the second patch, focusing on improvements to lvi/lvhi macro
    handling and standalone validation checks.
  quote: "Check all six lvi/lvhi forms using exact lane contents and scalar register\
    \ encodings, including row/column starts, negative values and raw hexadecimal\
    \ bits.\n\nReject 21 malformed operands without internal assembler aborts and\
    \ check half-subnormal disassembly. Run with Python 3.9 or newer:\n\n  python3\
    \ contrib/allegrex-vfpu/check-pseudo.py --tool-prefix /path/to/install/bin/psp-\n\
    \nThese standalone che…"
- author: Yaroslav Solodovnyk
  role: proposer
  position: Describes the third patch, which refines instruction prefix handling and
    adds reserved-encoding checks to prevent misinterpretation of MIPS instructions.
  quote: "Source prefixes have 20 immediate bits, while destination prefixes have\
    \ 12. Mask the unused high bits so unrelated encodings such as the MIPS III ld\
    \ instruction 0xdc820000 are not decoded as vpfxs on Allegrex.\n\nAdd reserved-encoding\
    \ checks for all three prefixes. This also restores the existing Allegrex ISA-override\
    \ GAS test.\n---\n contrib/allegrex-vfpu/check-pseudo.py |  8 ++++++++\n include/opcod…"
primer_expert: This RFC patch series aims to upstream support for the MIPS Allegrex
  core's Vector Floating Point Unit (VFPU) instructions and the PlayStation Portable
  (PSP) target into Binutils. The code is ported from a downstream fork (pspdev/binutils-gdb).
  Key changes include adding VFPU instruction parsing and disassembly, implementing
  PSP-specific linker behavior, and crucially, fixing issues with the load-immediate
  (lvi/lvhi) macros used for scalar and vector data. The series also addresses instruction
  encoding by correctly masking prefix bits to prevent misidentification of instructions
  and adds regr…
primer_glossary:
- term: MIPS
  definition: Microprocessor without Interlocked Pipeline Stages. A popular RISC instruction
    set architecture, historically used in many embedded systems and early workstations.
- term: Allegrex
  definition: A specific MIPS core variant used in the PSP (PlayStation Portable)
    and other embedded systems. It includes specialized instructions.
- term: VFPU
  definition: Vector Floating Point Unit. An extension to a processor's floating-point
    capabilities that allows it to perform operations on multiple floating-point numbers
    (vectors) simultaneously.
- term: PSP
  definition: PlayStation Portable. A handheld game console developed by Sony, which
    used a MIPS-based processor (Allegrex).
- term: Binutils trunk
  definition: The main development branch of the GNU Binutils project, where new features
    and fixes are integrated before official releases.
- term: assembler
  definition: A program that translates assembly language code into machine code that
    the processor can execute.
- term: disassembler
  definition: A program that translates machine code back into assembly language,
    useful for reverse engineering or understanding compiled code.
- term: linker
  definition: A program that combines various pieces of object code and libraries
    into a single executable program or library. It resolves symbol references between
    these pieces.
- term: RFC
  definition: Request For Comments. A type of email or document that proposes a change
    or feature and solicits feedback from the community before implementation.
- term: lvi/lvhi
  definition: Load Immediate instructions (likely variants for different data sizes)
    used in the Allegrex MIPS architecture to load immediate values into registers,
    potentially with vector operations.
series_id: 'binutils:mips: allegrex vfpu and psp target support (trunk)'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/cover.1793910298.git.dublikunt@gmail.com
bugzilla_url: null
date: '2026-11-06'
is_stub: false
stub_reason: ''
---

Yaroslav Solodovnyk is submitting a series of three patches (RFC) to add support for the Allegrex VFPU (Vector Floating Point Unit) instructions and the PSP (PlayStation Portable) target to the main Binutils trunk. This port is based on existing code from the pspdev/binutils-gdb downstream tree. The proposed changes include updating assembler operand initialization, fixing macro parsing for load-immediate instructions (lvi/lvhi), and ensuring correct handling of instruction prefixes to avoid misinterpretations. The series also addresses copyright and license compliance, adapts to Binutils' API, and maintains existing Allegrex ELF machine flags.
