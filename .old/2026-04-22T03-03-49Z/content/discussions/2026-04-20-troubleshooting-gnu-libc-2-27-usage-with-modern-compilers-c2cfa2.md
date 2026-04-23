---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- compatibility
- compiler
- GMP
- MPFR
discussion_id: p9u0eckat4vc.fsf@thym
source_type: public_inbox
title: using GNU libc 2.27
headline: Troubleshooting GNU libc 2.27 usage with modern compilers
tldr: Paul Zimmermann is having trouble using GNU libc 2.27 with a modern compiler
  due to missing symbols, and seeks help from the community.
stakes: This discussion highlights the challenges of using older versions of glibc
  with newer compilers. It is relevant for developers who need to maintain compatibility
  with older systems or who are working on software that relies on specific glibc
  versions.
proposer: Paul Zimmermann <Paul.Zimmermann@inria.fr>
consensus: Under Review
outcome: proposed
sentiment_score: 5
sentiment_rationale: The discussion is a neutral exchange of information and suggestions
  to solve a technical problem.
technical_tradeoffs:
- Using an older glibc version may limit access to newer features and optimizations.
- Using a newer compiler may introduce dependencies on symbols not available in older
  glibc versions.
- Using `--sysroot` can help resolve compatibility issues but may require manual adjustments
  to include paths.
exchanges:
- author: Paul Zimmermann <Paul.Zimmermann@inria.fr>
  role: proposer
  position: Describes the problem of using GNU libc 2.27 with a modern compiler due
    to missing `__isoc23_strtol` symbol and asks for help.
  quote: null
- author: Vincent Lefevre <vincent@vinc17.net>
  role: contributor
  position: Provides a suggestion to configure GMP and MPFR with `--sysroot=$ROOT
    in CFLAGS, where $ROOT/usr/{include,lib} contain GNU libc 2.27 include/lib files.`
  quote: null
- author: Arsen Arsenović <aarsenovic@baylibre.com>
  role: contributor
  position: Suggests using `-save-temps` to examine the preprocessed source files
    for incorrect include paths.
  quote: null
- author: Paul Zimmermann <Paul.Zimmermann@inria.fr>
  role: contributor
  position: Reports that `-save-temps` did not produce the expected files.
  quote: null
- author: Arsen Arsenović <aarsenovic@baylibre.com>
  role: contributor
  position: Asks for clarification about the exact command used with `-save-temps`.
  quote: null
- author: Paul Zimmermann <Paul.Zimmermann@inria.fr>
  role: contributor
  position: Reports that the issue was resolved with Vincent's suggestion and manual
    fixes of hardcoded include paths.
  quote: null
primer_expert: This discussion involves using an old glibc version (2.27) with a modern
  compiler. The core issue is the missing `__isoc23_strtol` symbol, which is part
  of the new ISO C23 standard.  The `CORE-MATH` test suite depends on MPFR and GMP,
  which in turn depend on this symbol when compiled with a recent GCC.  The resolution
  involves using `--sysroot` to ensure the correct headers and libraries from the
  older glibc are used, and fixing hardcoded include paths.
primer_general: Glibc (GNU C Library) provides the standard C functions used by most
  programs on Linux. This discussion revolves around using an older version of glibc
  (2.27) with a newer compiler. The problem is that the newer compiler expects some
  functions (`__isoc23_strtol`) that are not available in the older glibc. The solution
  involves telling the compiler to use the header files and libraries from the older
  glibc, and manually fixing any incorrect include paths in the code. This kind of
  problem can arise when trying to build software that needs to run on older systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/p9u0eckat4vc.fsf@thym
bugzilla_url: null
date: '2026-04-20'
---

Paul Zimmermann is attempting to use GNU libc 2.27 with the CORE-MATH test suite and a modern compiler (gcc 15.2.0) but encounters issues due to missing `__isoc23_strtol` symbol. He tried recompiling GMP and MPFR with `-std=c99` but the issue persists, indicating a potential incompatibility between the older glibc version and the newer compiler. He is seeking advice on how to resolve this.
