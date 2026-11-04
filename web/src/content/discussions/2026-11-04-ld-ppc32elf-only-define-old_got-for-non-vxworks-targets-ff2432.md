---
project: binutils
subsystem: ld/ppc32elf
patch_id: null
tags:
- binutils
- linker
- ppc32
- VxWorks
- code cleanup
discussion_id: 3399679d-0271-491b-8a50-341b986537f8@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH] ld/ppc32elf: only define old_got for non-VxWorks targets'
headline: 'ld/ppc32elf: only define old_got for non-VxWorks targets'
tldr: Patch cleans up unused 'old_got' variable for VxWorks targets in ppc32elf ld,
  now marked as ready.
proposer: Surya Kumari Jangala <jskumari@linux.ibm.com>
consensus: Proposed
outcome: ready
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Removes a compiler warning and simplifies code by removing unused variables for
  specific targets.
exchanges:
- author: Simon Marchi
  role: proposer
  position: Submitted a patch to move the definition of `old_got` and its handling
    inside non-VxWorks conditionals to fix a compiler warning.
  quote: 'Building ld with a recent clang fails with:  eelf32ppcvxworks.c:68:12: error:
    variable ''old_got'' set but not used [-Werror,-Wunused-but-set-global]


    old_got is only read in ppc_after_check_relocs, which is not generated for VxWorks.
    The --sdata-got option that sets it is not registered for VxWorks either.  Move
    the variable and the handling of OPTION_OLD_GOT inside the existing non-VxWorks
    condit…'
- author: Surya Kumari Jangala <jskumari@linux.ibm.com>
  role: reviewer
  position: Approved the patch and confirmed it is ready for upstreaming.
  quote: LGTM, ok for upstreaming.
primer_expert: This patch cleans up the `ld/ppc32elf.em` template by conditionally
  defining the `old_got` variable and its associated option parsing. Previously, `old_got`
  was globally defined but only used in code paths not taken on VxWorks targets, leading
  to a compiler warning with `-Wunused-but-set-global`. The change scopes `old_got`
  to non-VxWorks builds, resolving the warning and simplifying the template.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or library.
- term: ppc32elf
  definition: Refers to the 32-bit PowerPC architecture using the ELF object file
    format.
- term: VxWorks
  definition: A real-time operating system developed by Wind River Systems.
- term: old_got
  definition: A variable likely related to the management of the Global Offset Table
    (GOT) in older linking schemes for PPC32 ELF targets.
- term: Global Offset Table (GOT)
  definition: A data structure used in position-independent code (PIC) to store addresses
    of external symbols or functions, allowing indirect access.
- term: sdata-got
  definition: A linker option that influences how small data sections are handled,
    potentially interacting with the GOT.
- term: upstreaming
  definition: The process of submitting code changes to the official, main development
    branch of an open-source project.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/3399679d-0271-491b-8a50-341b986537f8@linux.ibm.com
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch addresses an unused variable warning ('old_got') on VxWorks targets by conditionally defining it only for non-VxWorks builds. The variable was only used in `ppc_after_check_relocs`, which is not generated for VxWorks, and the `--sdata-got` option is also not registered for VxWorks. The reviewer (Surya Kumari Jangala) has approved it, marking it as ready for upstreaming.
