---
project: gcc
subsystem: gcc
patch_id: null
tags: []
discussion_id: 20260528185814.af0333e87a5f285ff4b91a25@schemamania.org
source_type: public_inbox
title: using STANDARD_BINDIR_PREFIX and overrdes
headline: Understanding STANDARD_BINDIR_PREFIX and -B overrides
tldr: A developer seeks to understand how the `-B` flag overrides `STANDARD_BINDIR_PREFIX`
  in GCC to correctly locate COBOL include files.
proposer: '"James K. Lowden" <jklowden@schemamania.org>'
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The user wants to understand how `STANDARD_BINDIR_PREFIX` is used to
  locate the `cobol1` executable, and how the `-B` option and `GCC_EXEC_PREFIX` environment
  variable modify this path.  The goal is to propagate this overridden path to the
  COBOL compiler to locate include files.
primer_general: '`STANDARD_BINDIR_PREFIX` specifies the default location where GCC
  expects to find executables like compilers and linkers. The `-B` option allows users
  to override this default location, specifying a different directory to search for
  these executables.  Understanding how these mechanisms work is crucial for developers
  who need to customize the build environment or use non-standard compiler locations.
  This is relevant when compiling languages like COBOL that rely on external executables
  and include files.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/20260528185814.af0333e87a5f285ff4b91a25@schemamania.org
bugzilla_url: null
date: '2026-05-28'
is_stub: false
---

A developer is seeking clarification on how the `-B` flag interacts with `STANDARD_BINDIR_PREFIX` in GCC, specifically in the context of compiling COBOL. They want to understand how `-B` overrides the default search path for executables like `cobol1` and how to propagate this information to the COBOL compiler to locate include files.  This is important for ensuring that the COBOL compiler can find necessary include files similar to how C++ finds `<algorithm>`.
