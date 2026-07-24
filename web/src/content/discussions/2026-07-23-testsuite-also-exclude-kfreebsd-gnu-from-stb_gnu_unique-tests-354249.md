---
project: binutils
subsystem: testsuite
patch_id: null
tags:
- binutils
- testsuite
- ELF
- kfreebsd
- consistency
discussion_id: alpine.DEB.2.21.2607231958460.14485@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [PATCH] testsuite: Also exclude `*-*-kfreebsd*-gnu'' from STB_GNU_UNIQUE
  tests'
headline: 'testsuite: Also exclude `*-*-kfreebsd*-gnu'' from STB_GNU_UNIQUE tests'
tldr: Patch extends exclusion of kfreebsd-gnu targets from STB_GNU_UNIQUE tests to
  improve consistency with BFD target handling.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- 'Test Specificity vs. Consistency: Balancing the need for precise tests with the
  benefit of consistent target handling across the project.'
- 'Maintainability: Simplifying future maintenance by having consistent patterns for
  target exclusions.'
- 'Correctness: Ensuring tests accurately reflect linker behavior without being affected
  by unrelated symbol binding types.'
exchanges:
- author: Maciej W. Rozycki
  role: proposer
  position: Applies a patch to exclude `*-*-kfreebsd*-gnu` targets from STB_GNU_UNIQUE
    tests, emphasizing the value of consistent triplet matching patterns across binutils
    components.
  quote: "I think there's value in having triplet match patterns consistent where\
    \ \nappropriate, as it makes tree-wide changes easier, in particular to avoid\
    \ \ndiscrepancies between components. I've seen too many of them recently.\n\n\
    Change committed now, thank you for your review."
- author: Jan Beulich
  role: reviewer
  position: Discusses the consistency of triplet matching patterns, initially questioning
    the necessity of a wider match in tests compared to BFD configurations but ultimately
    yielding.
  quote: 'Afaict `foo-kfreebsd-bar'' will simply not match anything, hitting the

    "BFD does not support target" case. Therefore I don''t see it as wrong to

    have a wider match here than what bfd/config.bfd has. Yet no, I''m not

    going to insist.'
primer_expert: This patch modifies the binutils test suite to include `*-*-kfreebsd*-gnu`
  triplets in the set of targets excluded from tests related to `STB_GNU_UNIQUE` symbols.
  The rationale, confirmed by the maintainer, is to ensure consistency in target pattern
  matching between different parts of binutils (like the testsuite and BFD). While
  the specific target might not be explicitly handled by BFD's configuration for these
  tests, maintaining consistent exclusion patterns simplifies tree-wide changes and
  avoids potential discrepancies in how targets are treated across the binutils project.
primer_glossary:
- term: testsuite
  definition: A collection of automated tests designed to verify the correct functionality
    of a software system, in this case, the binutils linker.
- term: STB_GNU_UNIQUE
  definition: A symbol binding type in ELF, indicating that a symbol has a unique
    instance within the dynamic symbol table, often used for interpositioning.
- term: kfreebsd-gnu
  definition: A target triplet indicating a FreeBSD kernel combined with GNU userland
    tools, often used in build systems.
- term: BFD
  definition: The Binary File Descriptor library, part of binutils, which provides
    a generic interface for reading and writing various object file formats.
- term: triplet
  definition: A string commonly used to identify a target architecture, vendor, and
    operating system (e.g., `x86_64-linux-gnu`).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2607231958460.14485@angie.orcam.me.uk
bugzilla_url: null
date: '2026-07-23'
is_stub: false
stub_reason: ''
---

This discussion revolves around a patch that extends the exclusion of `*-*-kfreebsd*-gnu` targets from STB_GNU_UNIQUE tests in binutils. Maciej W. Rozycki, the proposer, successfully applied the patch after agreeing with Jan Beulich that maintaining consistency in triplet matching patterns across components is beneficial, even if wider matches in testsuite patterns seem safe. The change aims to prevent discrepancies between different binutils components.
