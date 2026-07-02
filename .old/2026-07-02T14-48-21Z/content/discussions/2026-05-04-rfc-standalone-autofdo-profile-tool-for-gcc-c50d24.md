---
project: gcc
subsystem: gcc
patch_id: null
tags:
- AutoFDO
- optimization
- profiling
- toolchain
discussion_id: B80EC0EC-AE15-40D9-9F48-A01DE8716639@nvidia.com
source_type: public_inbox
title: 'Re: RFC: Standalone AutoFDO Profile Tool for GCC'
headline: 'RFC: Standalone AutoFDO Profile Tool for GCC'
tldr: An RFC proposes a standalone AutoFDO profile tool for GCC, aiming for simplicity
  and minimal dependencies, sparking discussion on dependency choices.
proposer: Kugan Vivekanandarajah <kvivekananda@nvidia.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- '**Dependency Size:** libdwarf might be larger than libbacktrace.'
- '**Version Support:** libdwarf versioning can be an issue, potentially requiring
  support for newer DWARF standards.'
- '**Functionality:** libbacktrace might require changes or an additional library
  (ibdw) to provide the necessary functionality (discriminator).'
exchanges:
- author: Kugan Vivekanandarajah
  role: proposer
  position: Proposes creating a native, simplified AutoFDO tool for GCC to replace
    the current reliance on external Google tools. The goal is simplicity and minimal
    dependencies, focusing on libraries like libdwarf for DWARF parsing.
  quote: Building on our discussions from the last Cauldron, we propose creating a
    native, simplified AutoFDO tool for GCC to replace our current reliance on external
    Google tools which is not actively maintained.
- author: Jan Hubička
  role: reviewer
  position: Suggests reusing libbacktrace's code instead of requiring libdwarf and
    libelf as dependencies, mentioning potential issues with specific libdwarf versions.
  quote: Could we reuse libbacktrace's code here? Instead of requiring libdwarf and
    libelf as a dependency? Or maybe libiberty/simple-object code?
- author: Kugan Vivekanandarajah
  role: contributor
  position: Responds to the feedback, noting that libbacktrace might require ibdw
    to get the discriminator, but agrees libbacktrace looks like a better solution.
  quote: I tried recreating with libbacktrace. AFIK, we however would need ibdw to
    get the discriminater unless we change libbacktrace. libbacktrace looks to me
    like a better solution given version issues you mentioned.
primer_expert: AutoFDO uses execution profiles to guide compiler optimizations.  This
  proposal outlines a standalone tool to generate these profiles from samples. The
  discussion centers around minimizing dependencies (libdwarf vs. libbacktrace) for
  parsing DWARF debugging information, a common tradeoff in toolchain development.
primer_general: Automatic Feedback-Directed Optimization (AutoFDO) is a compilation
  technique where the compiler uses runtime information to optimize code. A profile
  is generated that indicates how frequently different parts of the code are executed.
  This information then guides the compiler to optimize the most frequently used code
  paths.  This proposal concerns a tool to generate these profiles in a format that
  GCC can use.  The core discussion is on the dependencies of the tool (libraries
  to parse debugging information).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/F5C9AFD6-2FDE-442C-A261-91457ADB6E5F@nvidia.com
bugzilla_url: null
date: '2026-05-04'
---

Kugan Vivekanandarajah proposes a standalone AutoFDO (Automatic Feedback-Directed Optimization) profile tool for GCC, intended to replace reliance on external, unmaintained Google tools. The tool aims to convert samples into AutoFDO profiles readable by the GCC toolchain, with minimal dependencies.  The discussion focuses on whether to use libdwarf or libbacktrace for DWARF parsing, considering factors like version support and dependency size.
