---
project: binutils
subsystem: configure
patch_id: null
tags:
- build
- configure
- zstd
- patch
discussion_id: 20260928053309.1949979-1-torbjorn.svensson@foss.st.com
source_type: public_inbox
title: '[PATCH v2] configure: Support --with-zstd=PATH'
headline: 'configure: Support --with-zstd=PATH'
tldr: Adds support to the configure scripts for specifying a custom path for zstd
  library installation.
proposer: Torbjörn SVENSSON <torbjorn.svensson@foss.st.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensures zstd version 1.4.0 or newer is used, potentially increasing build dependencies.
- Aligns binutils configuration with GCC's zstd handling.
exchanges: []
primer_expert: This patch enhances the configure scripts across several binutils components
  (bfd, gas, gdb, gold, ld) to correctly interpret the PATH argument for the --with-zstd
  option. Previously, the provided path was ignored, causing the build system to fall
  back to system defaults or fail if zstd was not in a standard location. This change
  aligns binutils' behavior with GCC's handling of this option, ensuring that zstd
  libraries and headers from a specified prefix are used.
primer_glossary:
- term: configure
  definition: A build script that automatically adapts software to a specific operating
    system or environment by checking for necessary components and setting up build
    parameters.
- term: zstd
  definition: A fast lossless compression algorithm, often used for compressing data
    streams or files. In this context, it's used for compressing debug sections.
- term: PATH
  definition: In this context, it refers to a file system path specifying the directory
    where the zstd library and its headers are installed.
- term: Makefile.am
  definition: A file used by Automake to generate Makefiles, defining build rules
    and dependencies.
- term: Makefile.in
  definition: A template file used by the configure script to generate a Makefile.
series_id: 20260928053309.1949979-1-torbjorn.svensson@foss.st.com
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260928053309.1949979-1-torbjorn.svensson@foss.st.com
bugzilla_url: null
date: '2026-09-28'
is_stub: false
stub_reason: ''
---

This patch updates the configure scripts to allow users to specify a PATH for the zstd library using the --with-zstd=PATH option. It ensures that the specified zstd version is 1.4.0 or newer and includes necessary changes in various binutils sub-projects' configure scripts and Makefiles. This addresses the issue where the path provided to --with-zstd was not being utilized, unlike in GCC.
