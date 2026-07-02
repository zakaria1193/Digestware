---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- strchr
- const correctness
- linker
discussion_id: afa6D-vklx2LFqS3@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH 2/2] ld: Fix calls to strchr that discard or use wrong const qualifiers'
headline: 'Ld: Fix calls to strchr that discard or use wrong const qualifiers'
tldr: The linker is updated to avoid discarding const qualifiers when calling strchr
  in several places.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensures const correctness, potentially preventing unintended modifications of constant
  strings.
- Minimal performance impact.
- Increased code clarity and maintainability.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Acknowledges the previous patch and indicates approval.
  quote: OK.
primer_expert: This patch modifies linker scripts and C code to ensure const correctness
  when using `strchr`. Specifically, it addresses cases where the return value of
  `strchr` (a `const char *`) was being assigned to a non-const `char *`, potentially
  leading to undefined behavior. The changes affect files within the `ld/emultempl/`
  directory, which contain emulation templates for different target architectures,
  and `ld/ldelf.c`, which handles ELF-specific linking operations.
primer_general: The `strchr` function searches for the first occurrence of a character
  within a string.  When working with constant strings (strings that shouldn't be
  modified), `strchr` returns a pointer to a constant character (`const char *`).
  This patch ensures that the code correctly handles these constant pointers in the
  linker, a tool that combines compiled code into an executable. Incorrect handling
  can lead to unexpected behavior when the program tries to modify a string that should
  not be changed.
series_id: 'binutils:ld: fix calls to strchr that discard or use wrong const qualifiers'
series_role: reply
series_parts:
- title: 'ld: Fix calls to strchr that discard or use wrong const qualifiers'
  url: https://inbox.sourceware.org/binutils/20260502170132.3303884-3-mark@klomp.org
  n: 2
  total: 2
url: https://inbox.sourceware.org/binutils/afa6D-vklx2LFqS3@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-03'
---

This patch updates the linker (ld) to ensure that the return values of `strchr` are correctly assigned to `const char *` variables, avoiding the discarding of const qualifiers. This change affects multiple files under the `ld/emultempl/` directory and `ld/ldelf.c`. The patch addresses potential issues related to const correctness in the linker code.
