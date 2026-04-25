---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- ld
- linker script
- LTO
- glibc
discussion_id: CAMe9rOrRatiGHzffCBX8NVmT__9G-Aq_kPtpS0gDsQ9doY66-A@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3] ld: Maintain the input file order'
headline: 'ld: Maintain the input file order'
tldr: Jan Beulich reviews v3 of the patch to maintain input file order in the linker,
  but Alan Modra raises concerns about linker script reordering.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Under Review
outcome: proposed
sentiment_score: 5
technical_tradeoffs:
- Maintaining input file order might introduce performance overhead.
- The test case depends on a specific glibc configuration, limiting its general applicability.
- Correctly reordering linker script data structures is complex and prone to errors.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Acknowledges the updated patch (v3) and asks whether the behavior is independent
    of the glibc version.
  quote: 'And that behavior is independent of glibc version (and other factors

    which may influence its behavior)?'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: other
  position: States that the original test case triggers a crash on glibc targets.
  quote: 'Add a static LTO test to reference feclearexcept which is a compiler

    builtin function and isn''t in the LTO symbol table when GCC is used.

    It triggers the run-time crash on glibc targets of a linker script

    libm.a without this fix when GCC 13 or above is used'
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Suggests the patch might be incorrect due to not reordering the header.next
    list in linker scripts.
  quote: 'The linker traverses the linker script for different purposes using

    three pointers in a lang_input_statement_type: next_real_file, next

    and header.next.  I suspect you may find this patch is incorrect due

    to not reordering the header.next list.  See insert_input_file.'
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Notes that the test relies on a glibc installation with a specific libm.a
    script and suggests limiting the test to specific architectures.
  quote: 'The test relies on having a glibc installed with a script libm.a.  As

    far as I can see that means the test is only useful on x68_64 and

    aarch64 with a newish glibc.  Please limit it, or write a more

    generally useful test.'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: other
  position: Explains the lists used in linker script handling.
  quote: 'There are more than one lang_statement_list.  statement_list is

    traversed by header.next.   input_file_chain is traversed by

    next_real_file for the reordering.'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: other
  position: Acknowledges the issue with the test setup and potentially limiting its
    scope.
  quote: 'OK.  I will limit the PR ld/34088 test to Linux/x86-64 and

    Linux/aarch64 in next version.'
primer_expert: This patch relates to the linker's handling of input file order, particularly
  in the context of LTO and linker scripts. The core issue arises when LTO-generated
  symbols are not present in the initial symbol table, leading to runtime crashes
  with specific glibc configurations.  The patch aims to resolve this by ensuring
  files are processed in the order specified in the linker script, but there are concerns
  about how this interacts with internal linker script data structures.
primer_general: The linker (`ld`) combines multiple object files and libraries into
  a single executable.  Linker scripts control how this combination happens, including
  the order in which files are processed.  This patch addresses a problem where the
  linker was not preserving the order of input files as specified in the linker script,
  which could lead to crashes, particularly when using link-time optimization (LTO)
  and certain versions of the glibc standard library.  Maintaining the correct input
  order is crucial for ensuring that symbols are resolved correctly and that the resulting
  executable functions as intended.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/090ee32f-fb52-4093-a505-853ce6a15773@suse.com
bugzilla_url: null
date: '2026-04-22'
---

This thread discusses version 3 of a patch that aims to maintain the input file order in the linker. The patch addresses a runtime crash on glibc targets related to a linker script and a compiler built-in function. Jan Beulich acknowledges the patch, while Alan Modra raises concerns about potential issues with reordering of linker script elements and the test's reliance on a specific glibc setup.
