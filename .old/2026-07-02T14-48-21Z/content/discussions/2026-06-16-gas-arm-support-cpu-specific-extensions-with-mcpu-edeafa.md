---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- arm
- toolchain
- cpu-extensions
- assembler
discussion_id: 2846ac09-3590-409d-8ecf-cc385c8929e8@arm.com
source_type: public_inbox
title: 'Re: [PATCH v3] gas: arm - support CPU-specific extensions with -mcpu'
headline: 'gas: arm - support CPU-specific extensions with -mcpu'
tldr: This patch adds support to `gas` for enabling and disabling ARM CPU-specific
  extensions using `+ext` and `-noext` modifiers with the `-mcpu` option, aligning
  w…
proposer: Richard Earnshaw (foss) <Richard.Earnshaw@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increased complexity in `gas/config/tc-arm.c` for managing CPU-specific extensions.
- Improved consistency with GCC's CPU feature definitions.
- More granular control over instruction set features for ARM CPUs.
exchanges:
- author: Sivan Shani
  role: proposer
  position: Proposes adding support for CPU-specific extensions to `gas` using `-mcpu`
    with `+ext` and `+noext` modifiers, aligning ARM CPU feature definitions with
    GCC.
  quote: Add extension tables for -mcpu, similar to -march, allowing CPU-specific
    extensions to be enabled and disabled using +ext and +noext modifiers. Update
    ARM CPU feature definitions to match GCC CPU baselines and add tests covering
    supported CPU extension modifiers and feature availability.
primer_expert: This proposal for `gas` (the GNU Assembler) on ARM targets focuses
  on enhancing the `-mcpu` command-line option. Currently, `gas` primarily uses `-march`
  for architecture-specific extensions. This patch introduces a mechanism to associate
  CPU-specific extensions directly with `-mcpu`, using `+ext` and `+noext` modifiers
  similar to how `-march` handles them. This involves updating `gas/config/tc-arm.c`
  and introducing new test cases to reflect GCC's CPU feature baselines. This change
  improves consistency across the GNU toolchain and provides finer-grained control
  over instruction set features…
primer_general: When you write code, a compiler (like GCC) translates it into a low-level
  language called assembly, and then an assembler (like `gas`, the GNU Assembler)
  turns that assembly into machine code that the computer's processor can understand.
  Different computer processors (CPUs), even within the same family like ARM, have
  slightly different capabilities or 'extensions'—special instructions they can run.
  This proposal suggests an improvement to `gas` so that when you tell it which specific
  CPU your code is for (using the `-mcpu` option), you can also tell it more precisely
  which extra features or 'extensions' of that CPU to use or avoid. This is done with
  `+ext` (to enable an extension) or `+noext` (to disable one). This change makes
  sure that `gas` understands these CPU features in the same way that the GCC compiler
  does, leading to more accurate and efficient machine code for ARM processors.
series_id: 2846ac09-3590-409d-8ecf-cc385c8929e8
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/2846ac09-3590-409d-8ecf-cc385c8929e8@arm.com
bugzilla_url: null
date: '2026-06-16'
is_stub: false
---

Sivan Shani submitted a third version of a patch that enables `gas` to support CPU-specific extensions with the `-mcpu` option for ARM targets. This patch introduces extension tables, similar to those for `-march`, allowing users to enable or disable features using `+ext` and `+noext` modifiers. The update also synchronizes ARM CPU feature definitions with GCC baselines and includes new tests to verify support for these modifiers and feature availability.
