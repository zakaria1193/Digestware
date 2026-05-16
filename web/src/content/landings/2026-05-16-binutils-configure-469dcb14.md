---
project: binutils
subsystem: binutils/configure
patch_id: null
tags:
- build
- configure
- msgpack
commit_hash: 469dcb143c6d19cd741fbf904188534e7696658b
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: 'configure: Look for msgpack-c.pc in addition to msgpack.pc.'
tldr: The binutils configure script now checks for `msgpack-c.pc` as well as `msgpack.pc`
  to find the msgpack library.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The configure script in binutils uses `PKG_CHECK_MODULES` to detect
  dependencies. This commit modifies `configure.ac` to check for `msgpack-c` before
  `msgpack`, ensuring that the configure process correctly identifies the presence
  of either library. The change involves updating `PKG_CHECK_MODULES` in `configure.ac`
  and regenerating the `configure` script.
primer_general: The `configure` script in binutils checks for the presence of required
  libraries and tools before building the project. `pkg-config` is a utility that
  provides information about installed libraries. This commit ensures that the configure
  script correctly detects the `msgpack` library, used for serialization, whether
  it's installed as `msgpack` or `msgpack-c`.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260516010850.18B3B409F30E@sourceware.org
date: '2026-05-16'
is_stub: false
---

The binutils configure script now checks for both `msgpack-c.pc` and `msgpack.pc` when searching for the msgpack library. This resolves an issue where the configure script would error out if only `msgpack-c` was installed. The configure script is updated to handle missing msgpack packages more gracefully.
