---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- mingw
- cross-compiler
- documentation
- release-process
discussion_id: CAFiYyc3qH5LTXZS6kZkFQ8_WpdX094PNBoVL6jZ1-djs39QdsQ@mail.gmail.com
source_type: public_inbox
title: 'Re: Switching from i686-mingw32 to x86_64-w64-mingw32?'
headline: Propose changes to x86_64-w64-mingw32 port via patches
tldr: Propose individual changes to the x86_64-w64-mingw32 port as patches to gcc-17/criteria.html.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Individual patch proposals allow for focused review and easier merging compared
  to monolithic changes.
- Requiring maintainer acknowledgment ensures buy-in from subsystem owners.
exchanges:
- author: Richard Biener
  role: proposer
  position: Requests individual patch proposals for changes to the x86_64-w64-mingw32
    port, submitted to gcc-17/criteria.html. These should be acked by maintainers
    and approved by release managers.
  quote: 'I''d like to see separate proposals for each individual change, proposed
    in patch form to gcc-17/criteria.html, ideally from respective target/OS maintainers,
    but at least acked by them.


    Approval would be from release managers.'
- author: LIU Hao
  role: other
  position: Notes a previous discussion in March that did not result in action and
    points out that GCC 17 is missing from the releases page.
  quote: null
primer_expert: This discussion concerns the process for updating the GCC cross-compiler
  for Windows 64-bit (x86_64-w64-mingw32). Richard Biener clarifies that individual
  changes should be proposed via patches to the wwwdocs repository, specifically targeting
  the criteria documentation for the upcoming GCC 17 release.
primer_glossary:
- term: x86_64-w64-mingw32
  definition: A GCC cross-compiler target triplet specifying a 64-bit x86 architecture,
    using the Win64 API (part of MinGW-w64), and targeting Windows.
- term: cross-compiler
  definition: A compiler that runs on one operating system (the host) but generates
    executable code for a different operating system or architecture (the target).
- term: wwwdocs
  definition: The repository containing the documentation website for GCC, including
    release criteria and other web-facing information.
- term: patch
  definition: A piece of code that modifies a larger codebase. In this context, it
    refers to a diff file that can be applied to the GCC source or documentation to
    introduce a change.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFiYyc3qH5LTXZS6kZkFQ8_WpdX094PNBoVL6jZ1-djs39QdsQ@mail.gmail.com
bugzilla_url: null
date: '2026-08-19'
is_stub: false
stub_reason: ''
---

Richard Biener requests that changes to the x86_64-w64-mingw32 port be submitted as individual patches to gcc-17/criteria.html. These proposals should ideally come from the respective target/OS maintainers, or at least be acknowledged by them. Approval for such changes would be granted by the release managers.
