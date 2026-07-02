---
project: binutils
subsystem: pr17107
patch_id: null
tags:
- binutils
- avr
- linker-script
- sections
- gnu-extensions
discussion_id: 28685df3-ca1e-4659-8271-baedb8937bfe@gjlay.de
source_type: public_inbox
title: '[patch, avr, applied] PR17107: Add more .gnu.linkonce section patterns to
  avr.sc'
headline: Binutils AVR linker script adds `.gnu.linkonce` patterns for text and BSS
tldr: Binutils linker script for AVR now includes patterns for `.gnu.linkonce.t*`
  and `.gnu.linkonce.b*` sections, mainly for handling text and BSS in relocatable
  ou…
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adding these patterns might have a minor impact on linker script parsing time, though
  negligible in practice.
- While COMDAT is often preferred, including explicit `.gnu.linkonce` patterns ensures
  broader compatibility and correct handling of older or specific toolchain outputs.
exchanges:
- author: Georg-Johann Lay <avr@gjlay.de>
  role: proposer
  position: Proposes to add rules for `.gnu.linkonce.t*` and `.gnu.linkonce.b*` sections
    to the AVR linker script (`avr.sc`) to ensure proper handling of these sections
    during linking.
  quote: This patch adds pattern rules for .gnu.linkonce.t* and .gnu.linkone.b* to
    the .text resp. .bss output sections. Though that's probably not needed any more
    since G++ is using COMDAT today.
primer_expert: The GNU linker (`ld`) uses linker scripts (e.g., `avr.sc` for AVR targets)
  to define how input sections are mapped to output sections in a final executable.
  This patch extends the `avr.sc` script to explicitly recognize `.gnu.linkonce.t*`
  and `.gnu.linkonce.b*` section patterns. `Linkonce` sections are a GCC extension,
  often used for emitting per-function or per-variable sections that the linker can
  then deduplicate (e.g., for inline functions or template instantiations). While
  modern C++ compilers often leverage COMDAT groups (another linking mechanism for
  deduplication) for this purpose, th…
primer_general: When you compile a program, the compiler creates different sections
  for your code and data. For example, all your program's instructions go into a `.text`
  section, and uninitialized global variables go into a `.bss` (Block Started by Symbol)
  section. Sometimes, due to how compilers work, they might generate multiple identical
  copies of certain pieces of code or data across different parts of your program.
  To avoid making the final executable unnecessarily large, a special type of section
  called `.gnu.linkonce` is used. The linker (which combines all the compiled pieces
  into a single program) then automatically removes these duplicate sections. This
  update to the linker's instructions for AVR microcontrollers (a type of small computer
  chip) adds new rules to ensure that any `.gnu.linkonce` sections related to program
  code (`.gnu.linkonce.t*`) or uninitialized data (`.gnu.linkonce.b*`) are correctly
  placed into the final program's `.text` and `.bss` sections, respectively. Even
  though n…
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/28685df3-ca1e-4659-8271-baedb8937bfe@gjlay.de
bugzilla_url: null
date: '2026-06-23'
is_stub: false
---

This patch adds new rules to the AVR linker script (`avr.sc`) to handle additional `.gnu.linkonce` section patterns, specifically `t*` for `.text` and `b*` for `.bss`. While modern C++ compilers often use COMDAT groups for deduplication, these patterns ensure proper handling of these sections when linking AVR binaries.
