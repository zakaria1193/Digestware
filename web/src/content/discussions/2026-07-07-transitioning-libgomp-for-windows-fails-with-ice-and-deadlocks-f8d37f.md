---
project: gcc
subsystem: gcc
patch_id: null
tags:
- windows
- mingw
- libgomp
- threading
- runtime
discussion_id: d9817db4-4d9b-4b71-ba43-0e9d98fba873@126.com
source_type: public_inbox
title: 'Re: Transitioning libgomp from C to C++ implementation: Windows (''*-*-mingw32*'')'
headline: Transitioning libgomp for Windows fails with ICE and deadlocks
tldr: Porting libgomp to Windows using mingw-w64 without winpthreads leads to ICEs
  and deadlocks, with remaining test failures.
proposer: LIU Hao <lh_mouse@126.com>
consensus: Proposed
outcome: needs_revision
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Switching libgomp to C++ might offer better abstraction but introduces C++/Windows
  integration challenges.
- Avoiding winpthreads for mingw-w64 targets simplifies dependencies but requires
  careful handling of Windows-native threading primitives.
exchanges:
- author: LIU Hao <lh_mouse@126.com>
  role: proposer
  position: Reports that after porting libgomp to C++ and applying patches for win32/mcf
    thread models, a build on GCC master resulted in an ICE, necessitating backporting
    to GCC 16. Further issues include deadlocks upon exiting programs linked against
    libgomp DLLs.
  quote: "This allows building libgomp with win32 or mcf thread model. When yesterday\
    \ I tried to build GCC master \nit ICE'd, so I had to backport the patches to\
    \ GCC 16, and everything built successfully.\n\nHowever, it turns out that any\
    \ program that is linked against libgomp DLL deadlocks upon exit; the reason \n\
    is complex but tl;dr; mingw-w64 CRT has to be patched as well (which I'll push\
    \ later today):"
- author: LIU Hao <lh_mouse@126.com>
  role: proposer
  position: Updates on the Windows port of libgomp, noting the ICE is gone after mingw-w46
    CRT update, but ~20 test failures remain, including missing functions and use
    of pthread functions, along with Fortran test failures.
  quote: "With https://sourceforge.net/p/mingw-w64/mingw-w64/ci/0fad182ff178044ee442b05e1913aa16cde8efcf/\
    \ \ncommitted, I tried updating mingw-w64 CRT and rebuilding GCC with win32 thread\
    \ model.\n\nThe ICE was gone, so I went ahead and ran libgomp tests. There were\
    \ ~20 failures in C and C++ tests; some \nof them didn't compile, for example,\
    \ libgomp/testsuite/libgomp.c-c++-common/cancel-taskgroup-1.c contains \na…"
primer_expert: This discussion on transitioning libgomp (GCC's OpenMP runtime) to
  C++ for Windows targets ('*-*-mingw32*') highlights cross-platform build and runtime
  issues. The core problem appears to be integrating libgomp with the mingw-w64 CRT
  and its threading model (win32 thread) as a replacement for winpthreads, which is
  standard on POSIX systems. Failures include compiler Internal Compiler Errors (ICEs)
  and runtime deadlocks, indicating fundamental incompatibilities or missing pieces
  in the mingw-w64 environment for libgomp's threading primitives.
primer_glossary:
- term: libgomp
  definition: The GNU Offloading Manager, providing the runtime support for OpenMP
    in the GCC compiler.
- term: OpenMP
  definition: An API for supporting shared-memory parallel programming in C, C++,
    and Fortran.
- term: mingw-w64
  definition: A development environment for creating Windows applications. It provides
    GCC toolchains and Windows API headers/libraries.
- term: winpthreads
  definition: A POSIX threads-compatible implementation for Windows, often used by
    libraries compiled with mingw-w64.
- term: CRT
  definition: C Runtime library. Provides essential functions for C programs, including
    memory management, I/O, and process control.
- term: ICE
  definition: Internal Compiler Error, a fatal error within the compiler itself, often
    indicating a bug in the compiler.
- term: libgomp DLL
  definition: Dynamic Link Library version of libgomp, allowing it to be loaded at
    runtime by applications.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/d9817db4-4d9b-4b71-ba43-0e9d98fba873@126.com
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

Following a successful backport of libgomp C++ transition patches to GCC 16, issues arose on Windows where linking against the libgomp DLL caused deadlocks. Despite patching mingw-w64 CRT and attempting a rebuild with the win32 thread model, an ICE was resolved but test failures persist, including missing functions and use of pthread equivalents.
