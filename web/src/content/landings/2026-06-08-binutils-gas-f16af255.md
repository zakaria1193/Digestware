---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- arm
- assembler
- toolchain
- extension
commit_hash: f16af255e66e91ff38cef38e2c49b6092cbeebd6
source_type: public_inbox
author: Sivan Shani <sivan.shani@arm.com>
headline: GAS ARM supports CPU features with -mcpu
tldr: GAS for ARM now supports enabling and disabling CPU-specific architectural extensions
  using `+ext` and `+noext` modifiers with the `-mcpu` flag.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: This commit enhances `tc-arm.c` to extend the parsing logic for the
  `-mcpu` option in `gas`. Previously, similar functionality for enabling/disabling
  extensions existed for `-march`, but not for `-mcpu`. The change introduces new
  extension tables and updates relevant CPU feature definition structs within GAS
  to support the `+ext` and `+noext` syntax. This allows for more precise control
  over the instruction set features available for a given ARM CPU model, ensuring
  better compatibility and optimization when targeting specific hardware variants,
  aligning GAS's capabilities more closely with GC…
primer_general: When you compile or assemble code for a computer chip, you often need
  to tell the tools what specific features your chip has. On ARM processors, there
  are many variations, and each might have slightly different capabilities or 'extensions.'
  Previously, you could tell the assembler about broad architectural features using
  `-march`. This change introduces a similar, but more precise, way to specify these
  extensions when you tell the assembler which specific CPU model (`-mcpu`) you are
  targeting. You can now add or remove individual features using `+ext` (to enable)
  or `+noext` (to disable) alongside the `-mcpu` option, giving you finer control
  over the generated code. This ensures the assembler understands the exact capabilities
  of your ARM processor, leading to more efficient and correct code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260608154830.4209351A4304@sourceware.org
date: '2026-06-08'
is_stub: false
---

The GNU Assembler (GAS) for ARM architecture now allows developers to specify CPU-specific extensions using the `-mcpu` command-line option. Similar to how `-march` handles architecture features, this change introduces extension tables for `-mcpu`, enabling fine-grained control over features with `+ext` and `+noext` modifiers. This enhancement updates ARM CPU feature definitions to align with GCC CPU baselines and includes new tests for validating CPU extension modifiers and feature availability.
