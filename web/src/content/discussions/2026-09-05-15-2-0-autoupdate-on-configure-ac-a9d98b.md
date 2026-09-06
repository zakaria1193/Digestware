---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- autoconf
- buildsystem
- m4
discussion_id: 2a352af6-9853-f54a-6f6b-faba87cd23bc@systella.fr
source_type: public_inbox
title: '[15.2.0 autoupdate on configure.ac'
headline: '[15.2.0 autoupdate on configure.ac'
tldr: User encounters an m4 error when running autoupdate on configure.ac for binutils
  15.2.0, possibly due to autoconf version mismatch.
proposer: BERTRAND Joël <joel.bertrand@systella.fr>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: The user is attempting to run `autoupdate` on `configure.ac` for binutils
  15.2.0, likely to regenerate the build system files after making modifications.
  They are using autoconf 2.73, which seems to be incompatible with the version expected
  by the `configure.ac` script (possibly requiring autoconf 2.72 or earlier). The
  `m4` utility, invoked by `autoupdate`, is failing with an 'end of file in string'
  error during the processing of the GMP version check macro, suggesting a syntax
  or parsing issue possibly related to quoting or macro expansion within that specific
  section of the script.
primer_glossary:
- term: autoupdate
  definition: A tool that updates `configure.ac` and `Makefile.am` files to newer
    versions of autoconf macros and syntax.
- term: configure.ac
  definition: The main input file for Autoconf, which describes how to configure the
    package for a particular system. It's processed by `autoconf` to generate `configure`.
- term: m4
  definition: A macro processor used by Autoconf to preprocess `configure.ac` before
    `autoconf` generates the `configure` script. It handles macro definitions and
    expansions.
- term: GMP
  definition: The GNU Multiple Precision Arithmetic Library, a free library for arbitrary-precision
    arithmetic. Binutils may depend on it for certain operations.
- term: autoconf
  definition: A tool that automatically configures source code packages to adapt to
    nearly any Unix-like operating system. It generates shell scripts to adapt programs
    to local environment.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/2a352af6-9853-f54a-6f6b-faba87cd23bc@systella.fr
bugzilla_url: null
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

A user is patching binutils 15.2.0 and encountered an m4 error when running `autoupdate` on `configure.ac`, citing a version mismatch between their local autoconf (2.73) and the script's requirement (2.72). The error message indicates an 'end of file in string' from m4, possibly related to macro expansion or quoting issues within the GMP version check logic in `configure.ac`.
