---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- stabs
- objcopy
- integer overflow
- security
discussion_id: CAO9RCZVpP-+=gHL3RCN4CwSvSbHXT+yViTQTnJ_C-ih2W5WrzQ@mail.gmail.com
source_type: public_inbox
title: '[PATCH] binutils: fix integer overflow in stabs base class count and objcopy
  padding'
headline: 'binutils: fix integer overflow in stabs base class count and objcopy padding'
tldr: Fixes integer overflows in stabs processing and objcopy padding calculations
  that could lead to incorrect sizes or crashes.
proposer: mustafa <mustafa@medios.digiscrypt.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- The addition of overflow checks introduces a minor performance cost but significantly
  enhances the robustness and security of the affected utilities.
exchanges:
- author: mustafa <mustafa@medios.digiscrypt.com>
  role: proposer
  position: Fixes integer overflows in stabs base class counting and objcopy padding
    calculations.
  quote: 'parse_stab_baseclasses reads the number of base classes with

    parse_number and stores it in an unsigned int.  For a count of

    0xffffffff, "(c + 1) * sizeof (*classes)" wraps to zero, debug_xalloc

    returns an empty block and the loop that follows writes c entries

    into it.'
primer_expert: This PR addresses two distinct integer overflow issues. In `stabs.c`,
  `parse_stab_baseclasses` now uses `size_t` for the base class count and validates
  the resulting allocation size to prevent heap overflows when parsing malformed debug
  information. In `objcopy.c`, arithmetic operations for `--gap-fill` and `--pad-to`
  now use GCC's `__builtin_mul_overflow` and `__builtin_add_overflow` to detect and
  report overflows, preventing incorrect section sizing due to wrap-around.
primer_glossary:
- term: stabs
  definition: A debugging information format used by some Unix compilers, including
    older versions of GCC.
- term: objcopy
  definition: A utility that copies and translates object files; used here for manipulating
    section padding and fill bytes.
- term: integer overflow
  definition: A condition that occurs when an arithmetic operation produces a result
    that exceeds the maximum value that can be stored in a data type.
- term: heap buffer overflow
  definition: A type of security vulnerability where a program writes data beyond
    the allocated buffer in the heap, potentially corrupting other data or executing
    malicious code.
- term: size_t
  definition: An unsigned integer type that is large enough to contain the size of
    any object in bytes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAO9RCZVpP-+=gHL3RCN4CwSvSbHXT+yViTQTnJ_C-ih2W5WrzQ@mail.gmail.com
bugzilla_url: null
date: '2026-11-19'
is_stub: false
stub_reason: ''
---

This patch addresses two integer overflow vulnerabilities. First, it corrects an issue in `stabs.c` where an excessively large base class count could cause memory allocation to wrap around to zero, leading to a heap buffer overflow. The fix uses `size_t` for counts and includes overflow checks. Second, it prevents integer overflows in `objcopy`'s `--gap-fill` and `--pad-to` operations by using compiler builtins for overflow detection, thus avoiding incorrect section sizes or crashes.
