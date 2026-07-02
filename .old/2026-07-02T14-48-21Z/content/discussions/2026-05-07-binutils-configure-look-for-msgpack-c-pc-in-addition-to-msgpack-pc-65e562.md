---
project: binutils
subsystem: binutils/configure
patch_id: null
tags:
- binutils
- configure
- msgpack
- pkg-config
discussion_id: 20260507192328.692827-1-simon.marchi@efficios.com
source_type: public_inbox
title: '[PATCH] binutils/configure: look for msgpack-c.pc (in addition to msgpack.pc)'
headline: 'Binutils/configure: Look for msgpack-c.pc (in addition to msgpack.pc)'
tldr: The configure script is updated to look for both msgpack.pc and msgpack-c.pc
  to accommodate the msgpack library's filename change.
proposer: Simon Marchi <simon.marchi@efficios.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- The change adds complexity to the configure script.
- There is a small overhead in checking for both files.
- The change avoids breaking builds when msgpack is installed with the new filename.
exchanges: []
primer_expert: This patch updates the configure script to find the msgpack library.
  The msgpack.pc file provides compiler and linker flags for using the msgpack library.  The
  library renamed the file to msgpack-c.pc, so the configure script needs to check
  for both to support older and newer versions.
primer_general: The build process for binutils uses a configure script to detect which
  libraries are installed on your system. This patch modifies that script to correctly
  locate the msgpack library, which is used for serialization. The script now checks
  for both the old and new names of the msgpack configuration file, ensuring that
  the build process can find the library regardless of which version is installed.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260507192328.692827-1-simon.marchi@efficios.com
bugzilla_url: null
date: '2026-05-07'
---

Simon Marchi updates the binutils configure script to check for both `msgpack.pc` and `msgpack-c.pc`. The msgpack library renamed its pkg-config file, and this change ensures that binutils can find the library regardless of which name is used. This allows binutils to build against either version of the msgpack library.
