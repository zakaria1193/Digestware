---
project: binutils
subsystem: avr
patch_id: null
tags:
- binutils
- AVR
- linker
- code locality
- optimization
discussion_id: amCvYm3-7Yb1BxS3@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [patch] AVR: Sort .text.* input sections by their name.'
headline: 'AVR: Sort .text.* input sections by their name.'
tldr: 'Discussion on sorting .text sections in AVR binutils: maintainer suggests a
  better approach than originally proposed patch.'
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: needs_revision
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- 'Code Locality: Balancing the potential benefits of sorting sections by name against
  the risk of degrading cache performance.'
- 'Linker Script Flexibility vs. Patch Simplicity: Offering a more powerful but complex
  solution (linker scripts) versus a simpler patch.'
- 'Target-Specific Optimization: Tailoring optimization strategies like section ordering
  for specific architectures (AVR) where it might be beneficial.'
exchanges:
- author: Alan Modra
  role: maintainer
  position: Reviews a patch to sort .text sections by name for AVR, expressing concerns
    about potential negative impacts on code locality, and proposes an alternative
    using linker script directives.
  quote: 'While you may have found one particular case where sorting by name

    helps, I suspect this is generally not a good idea. I believe in

    general you will make -ffunction-sections code locality worse by using

    this patch. Consider an object file with lots of small functions, calls mostly
    within that object file. You don''t want to sort them such that functions from
    other object files separate them.


    Yes,…'
- author: Georg-Johann Lay
  role: proposer
  position: Initially proposed sorting .text.* sections by name to improve code locality
    for AVR targets, particularly for libgcc and AVR-LibC, and later suggested an
    alternative approach based on Modra's feedback.
  quote: 'This patch sorts the .text.* input sections by their name

    in order to increase code locality, e.g. for code from

    libgcc and AVR-LibC. For example, libgcc puts their

    multiplications and helpers in .text.libgcc.mul, but

    without SORT the linker may locate functions related by

    their input section far apart, inserting function from

    unrelated input sections in between them.


    Maybe something like this w…'
primer_expert: This discussion evaluates a patch for the AVR target in binutils that
  proposes sorting `.text.*` input sections by name. The maintainer, Alan Modra, voices
  concern that this naive sorting might degrade code locality, especially when combined
  with `-ffunction-sections`, by interspersing functions from unrelated object files.
  He suggests a more refined approach using linker script `SORT_BY_NAME` and `EXCLUDE_FILE`
  directives, which offers finer control over which files and sections are sorted
  and how they are placed relative to each other, thereby potentially achieving better
  code locality.
primer_glossary:
- term: AVR
  definition: A family of microcontrollers developed by Atmel (now Microchip Technology),
    commonly programmed using C.
- term: .text
  definition: The conventional name for the section in an object file that contains
    the executable code.
- term: code locality
  definition: The principle that related code sections should be placed close together
    in memory to improve CPU cache performance and reduce instruction fetch latency.
- term: -ffunction-sections
  definition: A GCC compiler flag that places each function in its own section, allowing
    the linker to discard unused functions and potentially improve code locality.
- term: linker script
  definition: A file used by the linker to control how sections from input object
    files are mapped into the output file, specifying memory layout and symbol placement.
- term: SORT_BY_NAME
  definition: A linker script directive that sorts input sections alphabetically by
    their names.
- term: EXCLUDE_FILE
  definition: A linker script directive used to exclude specific object files from
    being considered for inclusion in certain sections.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/amCvYm3-7Yb1BxS3@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-22'
is_stub: false
stub_reason: ''
---

Alan Modra reviews a patch that sorts `.text.*` input sections by name for the AVR target in binutils, aiming to improve code locality. Modra expresses skepticism, believing this could worsen locality in general cases, especially with `-ffunction-sections`. He suggests an alternative approach using linker script directives like `*(EXCLUDE_FILE(...))` and `SORT(.text.*)` combined with file exclusions to achieve better control over section placement and code locality.
