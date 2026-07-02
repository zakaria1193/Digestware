---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- documentation
- avr
- assembler
- gas
discussion_id: d3e8a57c-da3b-47fb-a0d0-4114fc222803@gjlay.de
source_type: public_inbox
title: '[patch, avr] Overhaul section AVR modifiers and document gs()'
headline: GAS manual update overhauls AVR modifiers and documents `gs()`
tldr: This patch overhauls the AVR modifiers section in the GAS manual and adds documentation
  for the previously undocumented `gs()` modifier.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Georg-Johann Lay <avr@gjlay.de>
  role: proposer
  position: Proposes to overhaul the AVR modifiers section in the GAS manual and add
    documentation for the `gs()` function, addressing PR gas/13129.
  quote: "This patch adds documentation for gs() to the GAS manual, and it overhauls\
    \ the 'AVR modifiers' section. \n\tPR gas/13129"
primer_expert: The GNU Assembler (GAS) for AVR microcontrollers uses various modifiers
  to control assembly directives and symbol resolution. This patch specifically addresses
  the documentation for AVR-specific modifiers, with a particular focus on `gs()`.
  The `gs()` modifier is critical for handling program memory addressing on AVR devices,
  especially those with more than 64KB of flash where word addressing is needed. It
  functions by providing a word address, often by generating a trampoline jump table
  entry for accessing addresses beyond the 16-bit reach, allowing 24-bit program memory
  to be accessed indir…
primer_general: When programming microcontrollers (small, embedded computers, like
  those used in Arduino projects), you often use an assembler (like GNU Assembler,
  or GAS) to write code very close to the hardware. These assemblers have special
  commands, called "modifiers," that help you tell the microcontroller exactly how
  to do things. This proposal updates the user manual for GAS, specifically for AVR
  microcontrollers (a common family of chips). The main improvement is adding clear
  instructions for a special modifier called `gs()`. This `gs()` modifier is important
  for how the microcontroller finds and uses different parts of its own program memory,
  especially when the memory is larger than usual. Without this documentation, it
  was hard for programmers to understand and use this feature correctly, potentially
  leading to errors or inefficient code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/d3e8a57c-da3b-47fb-a0d0-4114fc222803@gjlay.de
bugzilla_url: null
date: '2026-06-23'
is_stub: false
---

This patch overhauls the "AVR modifiers" section of the GNU Assembler (GAS) manual, improving its clarity and completeness. Crucially, it adds long-missing documentation for the `gs()` function, which is used for generating word addresses on AVR microcontrollers.
