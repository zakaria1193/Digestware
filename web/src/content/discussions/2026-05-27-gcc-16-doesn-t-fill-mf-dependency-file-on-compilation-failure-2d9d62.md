---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- makefile
- dependencies
- build system
discussion_id: 3d97af6a8549cee2dee2860440dc4954d79aba07.camel@starynkevitch.net
source_type: public_inbox
title: GCC 16, the -MD -MF<file-for-dependencies> is not filled when compilation fails.
headline: GCC 16 doesn't fill -MF dependency file on compilation failure
tldr: GCC 16 with -MD -MF doesn't write dependency files when compilation fails; the
  author seeks a workaround without patching GCC.
proposer: Basile STARYNKEVITCH <basile@starynkevitch.net>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Requires changes to GCC's internal dependency generation logic.
- A workaround might involve post-processing the compiler output to extract dependency
  information.
exchanges:
- author: Basile STARYNKEVITCH <basile@starynkevitch.net>
  role: proposer
  position: Reports that GCC 16.1 doesn't fill the dependency file specified by `-MF`
    when compilation fails and asks for a workaround.
  quote: 'When compiling a source code with GCC 16.1 (on RaspberryPi

    Linux/Debian, using GNU make 4.4 with guile) the file written for

    dependencies with -MF is not filled on compilation failure'
- author: Basile STARYNKEVITCH <basile@starynkevitch.net>
  role: other
  position: Provides a link to a commit demonstrating the issue.
  quote: null
- author: Basile STARYNKEVITCH <basile@starynkevitch.net>
  role: other
  position: Refers to a previous message for context.
  quote: null
primer_expert: The `-MD -MF` flags instruct GCC to generate dependency information
  in a format suitable for Make. This information specifies the header files included
  by a given source file. When compilation fails, GCC might skip writing the dependency
  file, which hinders debugging complex build systems.
primer_general: Compilers often need to work with build systems like Make, which automate
  the process of compiling code and linking it together. To do this efficiently, the
  compiler can generate a list of dependencies, which tell Make which files need to
  be recompiled when a header file changes. The `-MD` and `-MF` flags tell GCC to
  automatically generate these dependencies, but the dependency file might not always
  be created, especially if there are errors during compilation.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/3d97af6a8549cee2dee2860440dc4954d79aba07.camel@starynkevitch.net
bugzilla_url: null
date: '2026-05-27'
is_stub: false
---

Basile Starynkevitch reports that GCC 16.1 doesn't create or update the dependency file specified by the `-MF` option when compilation fails.  He is looking for a way to ensure the file is populated even when compilation errors occur, as this would aid in debugging complex Makefiles.  Without a fix, debugging build systems becomes harder.
