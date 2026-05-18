---
project: binutils
subsystem: binutils/configure
patch_id: null
tags:
- configure
- msgpack
- build system
discussion_id: SJ5PPF77D28E3C2EDDB3FE9EF2DE4005B0BEC052@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
source_type: public_inbox
title: 'RE: [PATCH] binutils/configure: look for msgpack-c.pc (in addition to msgpack.pc)'
headline: 'binutils/configure: Look for msgpack-c.pc in addition to msgpack.pc'
tldr: Confirms that a patch to look for both `msgpack-c.pc` and `msgpack.pc` fixes
  a reported issue in the binutils configure script.
proposer: '"Jiang, Haochen" <haochen.jiang@intel.com>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Minimal overhead; adds a check for an alternative package name.
exchanges:
- author: Jiang, Haochen <haochen.jiang@intel.com>
  role: other
  position: Confirms that the patch provided by Alan Modra fixed the issue.
  quote: That patch on trunk has fixed my issue. Thx for the help.
primer_expert: This patch modifies the `configure.ac` file to check for both `msgpack.pc`
  and `msgpack-c.pc` when searching for the msgpack library.  This resolves a dependency
  issue caused by a rename.
primer_general: The `configure` script in binutils checks for the presence of external
  libraries required to build the project. This patch updates the script to look for
  both the old and new names of the msgpack library's package configuration file (`.pc`
  file), ensuring that the build process can find the library regardless of which
  name is used.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/SJ5PPF77D28E3C2EDDB3FE9EF2DE4005B0BEC052@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-05-16'
is_stub: false
---

This message confirms that a previously submitted patch, which modifies the binutils configure script to look for both `msgpack-c.pc` and `msgpack.pc`, has resolved an issue. The change allows the configure script to find the msgpack library even after the `.pc` file was renamed.
