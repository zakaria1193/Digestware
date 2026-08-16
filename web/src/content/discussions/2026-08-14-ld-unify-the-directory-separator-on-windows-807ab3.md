---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- linker
- Windows
- path handling
- consistency
discussion_id: 8f4fa844-ad98-4056-a9e1-c00e9cf2477b@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] ld: Unify the directory separator on Windows.'
headline: 'ld: Unify the directory separator on Windows.'
tldr: Standardizes on forward slashes for directory separators in Windows paths handled
  by the linker.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Simplifies path handling within the linker on Windows.
- Ensures consistency with common path conventions.
exchanges:
- author: Jan Dubiec
  role: proposer
  position: Proposes to unify directory separators to forward slashes on Windows in
    the linker.
  quote: 'There is no need to use backslashes on Windows, as Windows handles forward

    slashes in paths quite well. Moreover, the linker has been using

    forward slashes on Windows for a long time.'
- author: Jan Beulich
  role: reviewer
  position: Acknowledges the patch with a simple 'Okay.'
  quote: null
primer_expert: The linker (`ld`) on Windows currently handles directory paths. This
  patch standardizes on using forward slashes ('/') as the directory separator, consistent
  with how many Unix-like systems and modern Windows applications function. Previously,
  backslashes ('\') might have been used or handled inconsistently. This change simplifies
  path manipulation within `ld/ldfile.c` and related test cases.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or another library.
- term: directory separator
  definition: The character used in file system paths to separate directory and file
    names (e.g., '/' on Unix-like systems, '\' on Windows).
- term: Windows path handling
  definition: The mechanisms and conventions by which the Windows operating system
    interprets file and directory paths. Modern Windows APIs generally support both
    '/' and '\' as separators, but consistency is preferred.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/8f4fa844-ad98-4056-a9e1-c00e9cf2477b@suse.com
bugzilla_url: null
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This patch, a spin-off from a previous discussion, unifies the directory separator character used by the `ld` (linker) on Windows systems to forward slashes ('/'). The author notes that Windows has good support for forward slashes in paths and that the linker has historically used them. This change aims to simplify path handling and avoid potential inconsistencies by eliminating the use of backslashes ('\').
