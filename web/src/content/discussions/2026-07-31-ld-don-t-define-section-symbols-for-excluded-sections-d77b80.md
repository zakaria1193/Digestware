---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- linker
- sections
- review
discussion_id: e0baca3d-8099-449e-a282-f2d3e8f4c28b@suse.com
source_type: public_inbox
title: 'Re: [PATCH] ld: Don''t define section symbols for excluded sections'
headline: 'ld: Don''t define section symbols for excluded sections'
tldr: Reviewer suggests adding 'only' to clarify a patch's intent and criticizes code
  churn and indentation.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Balancing the definition of section symbols with linker exclusion rules.
- Ensuring clarity and accuracy in commit messages describing code changes.
- Maintaining code quality by minimizing churn and unnecessary complexity.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Reviews a patch on section symbol definition, suggesting phrasing improvements
    and criticizing code churn and indentation.
  quote: 'Feels like there is "only" missing in the sentences, to properly describe

    what the change actually does (introduce an extra constraint rather than

    provide those symbols anew).


    For changes like this I would also wish that they were done with less

    churn, and without needlessly increasing indentation depth:'
primer_expert: This discussion concerns a patch to the GNU linker (`ld`) that alters
  the conditions under which section symbols (like `__start`, `__stop`, `.startof.`,
  `.sizeof.`) are defined. The patch ensures these symbols are only defined for relocatable
  links or if the `SEC_EXCLUDE` bit is not set on a section. Jan Beulich, reviewing
  the patch, suggests improving the commit message's clarity and criticizes the code
  modification for introducing unnecessary churn and increasing indentation.
primer_glossary:
- term: section symbols
  definition: Symbols that mark the beginning or end of a section in an object file
    or executable, often used by linkers and runtime systems.
- term: excluded sections
  definition: Sections within an object file that the linker is instructed to ignore
    or omit from the final output, typically controlled by flags like `SEC_EXCLUDE`.
- term: relocatable link
  definition: A linking process that produces an output file that can be loaded and
    relocated at different memory addresses by the operating system's loader.
- term: SEC_EXCLUDE
  definition: A flag associated with a section in an object file, indicating that
    the section should be excluded by the linker when creating non-relocatable output.
- term: churn
  definition: In software development, refers to the amount of code that is changed,
    added, or deleted over a period, often implying unnecessary or disruptive modifications.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/e0baca3d-8099-449e-a282-f2d3e8f4c28b@suse.com
bugzilla_url: null
date: '2026-07-31'
is_stub: false
stub_reason: ''
---

Jan Beulich reviews a patch that modifies how section symbols (`__start`, `__stop`, etc.) are defined for excluded sections in the `ld` linker. He suggests that the patch's description should explicitly state that it's introducing an *additional constraint* rather than defining symbols anew. Beulich also expresses dissatisfaction with the churn and increased indentation depth in the modified code.
