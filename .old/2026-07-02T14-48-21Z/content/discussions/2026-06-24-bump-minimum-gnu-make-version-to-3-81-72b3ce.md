---
project: gcc
subsystem: gcc
patch_id: null
tags:
- build system
- GNU Make
- libstdc++
- toolchain policy
- developer experience
discussion_id: CAH6eHdRuOhrEEYp6jmGZgq6QXUsMe4kr66LY62uk59MpYnTauw@mail.gmail.com
source_type: public_inbox
title: 'RFC: Bump minimum GNU Make version to 3.81'
headline: Bump minimum GNU Make version to 3.81
tldr: This RFC proposes to bump GCC's minimum required GNU Make version from 3.80
  to 3.81, enabling the use of newer Make functions and aligning with existing libstd…
proposer: Jonathan Wakely <jwakely.gcc@gmail.com>
consensus: Under Review
outcome: under_review
impact_score: 6
sentiment_score: 7
technical_tradeoffs:
- Enables the use of newer GNU Make features, simplifying build scripts and improving
  readability.
- Requires all GCC developers and build systems to upgrade to at least GNU Make 3.81,
  which may impact older or more conservative environments.
- Addresses a discrepancy where libstdc++ is already using newer Make features not
  supported by the currently documented minimum version.
exchanges:
- author: Jonathan Wakely <jwakely.gcc@gmail.com>
  role: proposer
  position: Proposes to raise the minimum GNU Make version to 3.81, citing the widespread
    availability of this 2006 release and the desire to use newer Make functions that
    improve maintainability and enable desired build system features.
  quote: Bumping the requirement to 3.81 would allow us to use the $(abspath ...)
    function, which we already started using in libstdc++, not realising that it relies
    on a newer version than our docs require.
- author: Andrea Pinski <andrew.pinski@oss.qualcomm.com>
  role: reviewer
  position: Acknowledges the benefits of using newer Make features and the long release
    history of Make 3.81.
  quote: null
- author: Jeffrey Law <jeffreyalaw@gmail.com>
  role: reviewer
  position: Acknowledges the proposal and the ongoing discussion.
  quote: null
- author: Eric Gallager <egall@gwmail.gwu.edu>
  role: reviewer
  position: Acknowledges the thread and the merits of the proposal.
  quote: null
primer_expert: The GCC build system uses GNU Makefiles to coordinate the compilation
  of its various components, including the compiler proper, its runtime libraries
  (like libstdc++), and associated tools. This proposal concerns the minimum feature
  set available in these Makefiles. The `$(abspath ...)` function, for example, is
  a text function introduced in GNU Make 3.81 that resolves a file name to an absolute
  path, which can simplify complex build rules by making paths canonical.
primer_general: Compilers like GCC are complex software projects that are built using
  a "build system." This system, often driven by a tool called 'Make,' reads special
  files (Makefiles) that describe how all parts of the compiler should be put together
  from their source code. The proposal is about updating the minimum version of the
  'Make' tool that someone needs to have installed to build GCC. A newer version of
  Make (3.81, released in 2006) offers new features that can simplify the Makefiles
  and make the build process more robust, particularly for handling file paths correctly.
  This change would allow GCC developers to use these newer, more convenient features
  in the build system.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAH6eHdRuOhrEEYp6jmGZgq6QXUsMe4kr66LY62uk59MpYnTauw@mail.gmail.com
bugzilla_url: null
date: '2026-06-24'
is_stub: false
stub_reason: ''
---

Jonathan Wakely proposes updating the minimum GNU Make version required to build GCC from 3.80 to 3.81. This change would allow the use of functions like `$(abspath ...)` and `$(lastword ...)`, which are already in use in `libstdc++` but are not supported by the currently documented minimum version. The proposal argues that Make 3.81, released in 2006, is sufficiently widespread after 20 years.
