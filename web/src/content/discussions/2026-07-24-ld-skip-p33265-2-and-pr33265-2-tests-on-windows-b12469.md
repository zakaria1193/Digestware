---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- windows
- testing
- portability
discussion_id: b69464b7-a316-4bda-b664-c56d2cab092e@o2.pl
source_type: public_inbox
title: 'Re: [PATCH] ld: Skip p33265-2 and pr33265-2 tests on Windows'
headline: 'ld: Skip p33265-2 and pr33265-2 tests on Windows'
tldr: Discussion on why tests might fail on Windows, focusing on PATH_MAX differences
  between MinGW and Cygwin.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Skipping tests on certain platforms to ensure stability versus potentially masking
  platform-specific issues.
- Ensuring test compatibility across different build environments (MinGW vs. Cygwin).
exchanges:
- author: Jan Dubiec
  role: proposer
  position: Explained that MinGW applications use WinAPI directly, while Cygwin uses
    a POSIX layer, leading to different PATH_MAX values and thus confidence that the
    test failures are MinGW-specific.
  quote: Applications built with MinGW are native Windows applications and use the
    WinAPI directly. Applications built with Cygwin, on the other hand, rely on the
    POSIX compatibility layer provided by cygwin1.dll. Among other differences, PATH_MAX
    in Cygwin is 4096 bytes. That's why I'm fairly confident this issue does not exist
    there.
- author: Jan Beulich
  role: reviewer
  position: Asked for the basis of Jan Dubiec's confidence regarding Cygwin, suggesting
    that uncertainty should be documented.
  quote: Is this betting of yours backed by any insight you have? (If we're uncertain,
    I think at least the commit message should mention this fact. If later someone
    notices the same issue on Cygwin, they'd know right away what to do about it.)
primer_expert: 'This exchange discusses the applicability of skipping specific linker
  tests (p33265-2, pr33265-2) on Windows. The nuance lies in the behavior of Windows
  environments: MinGW provides native WinAPI access, while Cygwin offers a POSIX compatibility
  layer. Jan Dubiec argues that differences in `PATH_MAX` between these environments
  explain why the tests might fail under MinGW but not Cygwin. He lacks direct testing
  capability on Cygwin to confirm definitively.'
primer_glossary:
- term: PATH_MAX
  definition: A system constant that defines the maximum length, in bytes, of the
    pathname component, including the terminating null byte.
- term: MinGW
  definition: A development environment for native Microsoft Windows applications
    using the GNU Compiler Collection.
- term: Cygwin
  definition: A Linux-like environment for Windows that provides a large collection
    of GNU and Open Source tools which function like a Linux distribution.
- term: WinAPI
  definition: The native application programming interface for Microsoft Windows operating
    systems.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/b69464b7-a316-4bda-b664-c56d2cab092e@o2.pl
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

Jan Dubiec explains that binutils tests related to path limits might fail on Windows due to differences in PATH_MAX between MinGW (native WinAPI) and Cygwin (POSIX layer). He is confident the issue is specific to MinGW due to its direct WinAPI usage. Jan Beulich questioned the certainty of this analysis.
