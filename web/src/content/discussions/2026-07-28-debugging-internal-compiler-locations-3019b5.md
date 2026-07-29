---
project: gcc
subsystem: gcc
patch_id: null
tags:
- debugging
- compiler internals
- locations
discussion_id: 20260728161449.c71c09ccacbaf2c8c77cd2e5@cobolworx.com
source_type: public_inbox
title: 'Re: in search of squiggles'
headline: Debugging internal compiler locations
tldr: User confirms -fdump-internal-locations helped debug a scanner location difference.
proposer: James K. Lowden <jklowden@cobolworx.com>
consensus: Committed
outcome: committed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Using verbose debugging options like -fdump-internal-locations can generate large
  amounts of output, potentially impacting build times and disk usage.
exchanges:
- author: James K. Lowden <jklowden@cobolworx.com>
  role: proposer
  position: Found the needed debugging option (-fdump-internal-locations) which revealed
    a location difference between branches, leading to a fix.
  quote: "Thank you; that is evidently what I needed.  Comparing the output\nbetween\
    \ dev and our master+cobol branch (m+c) showed a difference.\n\n  location_t interval:\
    \ 3792256 <= loc < 3842560\n\n\t$ printf \"dev: %x\\nm+c: %x\\n\" 3842560 3843328\n\
    \tdev: 3aa200\n\tm+c: 3aa500\n\nTracking back from there, the scanner's location\
    \ (due to recently\nchanges)  varied from what the trailing-context pattern had\
    \ produced. Fix a…"
- author: Lewis Hyatt
  role: other
  position: Suggested using -fdump-internal-locations for debugging line maps.
  quote: 'You may get something from the -fdump-internal-locations option for

    debugging, to confirm that the line maps have been added in the

    expected order after the new changes.'
primer_expert: This discussion centers on debugging a discrepancy in how GCC's scanner
  reports source code locations after recent changes. The `-fdump-internal-locations`
  option is used to inspect internal location mappings within the compiler, helping
  to pinpoint differences that arise during different build configurations or code
  branches.
primer_glossary:
- term: scanner
  definition: A component of a compiler that reads the source code character by character
    and groups them into tokens.
- term: location maps
  definition: Data structures within the compiler that associate intermediate code
    or tokens with their original source code locations (file, line number, column).
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/20260728161449.c71c09ccacbaf2c8c77cd2e5@cobolworx.com
bugzilla_url: null
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

The user received assistance with a debugging issue related to scanner locations. The option `-fdump-internal-locations` proved instrumental in identifying a difference in reported locations between two branches, which was subsequently fixed.
