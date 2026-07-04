---
project: binutils
subsystem: binutils/libctf
patch_id: null
tags:
- binutils
- ctf
- memory error
- bugfix
commit_hash: b2ba16132fe4ecdb1ae112e017266b045de9dd80
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Fix double free in ctf_link_deduplicating_per_cu.
tldr: Fixes a double free error in the CTF linking process when an error occurs during
  input processing.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `libctf/ctf-link.c`, the `ctf_link_deduplicating_per_cu` function
  previously had an error path that could lead to a double free of a `ctf_symbol_type`
  if `ctf_link_deduplicating_open_inputs` failed. This was because `ctf_next_destroy`
  was called before the `goto err_open_inputs` which also implicitly handled cleanup.
  The fix removes the redundant call.
primer_glossary:
- term: CTF
  definition: Compact Type Format, a data format for storing type information in object
    files, primarily used by DWARF.
- term: libctf
  definition: The library that implements the Compact Type Format parsing and manipulation.
- term: double free
  definition: A memory corruption error where the same memory block is freed more
    than once, leading to undefined behavior.
discussion_id_link: public_inbox:binutils#34275
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260703235327.687F54BA2E14@sourceware.org
date: '2026-07-03'
is_stub: false
stub_reason: ''
---

This commit corrects a double free error in the `ctf_link_deduplicating_per_cu` function within `libctf/ctf-link.c`. The error occurred on the error path when `ctf_next_destroy` was mistakenly called twice. The fix ensures `ctf_next_destroy` is called only once, resolving the issue.
