---
project: binutils
subsystem: configure
patch_id: null
tags:
- build
- configure
- zstd
- patch
discussion_id: 20260927115704.1214794-1-torbjorn.svensson@foss.st.com
source_type: public_inbox
title: '[PATCH] configure: Support --with-zstd=PATH'
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
- Raises a question about the maintenance of generated configure files.
exchanges: []
primer_expert: This patch modifies the configure scripts in several binutils components
  (bfd, binutils, gas, gdb, gold, ld) to correctly process the PATH argument for the
  --with-zstd option. Previously, this path was ignored, leading to reliance on system-installed
  zstd or build failures. The change aligns binutils' behavior with GCC, which already
  supports this functionality. The author also raises a question about why the checked-in
  configure files differ from what `autoconf2.69` generates, specifically regarding
  the `LARGE_OFF_T` macro definition.
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
- term: autoconf
  definition: A tool that generates scripts to automatically configure source code
    packages.
- term: LARGE_OFF_T
  definition: A macro likely used to define a large integer type for file offsets,
    potentially related to handling large files.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260927115704.1214794-1-torbjorn.svensson@foss.st.com
bugzilla_url: null
date: '2026-09-27'
is_stub: false
stub_reason: ''
---

This patch updates the configure scripts to allow users to specify a PATH for the zstd library using the --with-zstd=PATH option. It ensures that the specified zstd version is 1.4.0 or newer and includes necessary changes in various binutils sub-projects' configure scripts. This addresses the issue where the path provided to --with-zstd was not being utilized, unlike in GCC. The patch also notes discrepancies in configure file content compared to autoconf output.
