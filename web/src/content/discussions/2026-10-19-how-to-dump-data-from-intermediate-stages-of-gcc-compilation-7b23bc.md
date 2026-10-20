---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- compiler
- intermediate representation
- rtl
- custom target
discussion_id: P4K5PW6--F-9@tutamail.com
source_type: public_inbox
title: How to dump data from intermediate stages of gcc compilation?
headline: How to dump data from intermediate stages of gcc compilation?
tldr: User wants to dump GCC's tree-like intermediate data structure before RTL generation
  for a custom CPU.
proposer: jf84ut@tutamail.com
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 6
technical_tradeoffs:
- Modifying GCC's internal dump mechanisms can be complex and may require deep understanding
  of its pass structure.
- The user's custom intermediate format needs to be decidable and useful for their
  target CPU's backend.
- Balancing the desire for detailed intermediate representation with potential performance
  impacts of new dump mechanisms.
exchanges:
- author: jf84ut@tutamail.com
  role: proposer
  position: Seeks to dump GCC's tree-like intermediate data structure before RTL generation
    for a custom CPU, as existing dump options are insufficient. Asks for pointers
    to relevant source code locations.
  quote: I'd like to modify gcc to target a CPU that I'm designing. The RTL used by
    the intermediate stages of gcc, unfortunately, won't be useful for me. I'd like
    to find a way to dump the tree-like data structure, that consists of the compiled
    program, with symbol resolution, constant folding, etc., having been done, just
    before it's transformed into the linear RTL.
- author: Andrea Pinski <andrew.pinski@oss.qualcomm.com>
  role: reviewer
  position: Acknowledges the request and indicates the need for further investigation
    into GCC's internals.
  quote: null
- author: David Malcolm <dmalcolm@redhat.com>
  role: reviewer
  position: Joins the discussion, indicating interest in the user's query about GCC's
    intermediate representations.
  quote: null
primer_expert: The user wants to instrument GCC's internal representation (GENERIC/GIMPLE
  trees) before the lowercasing to RTL. This likely involves modifying the `tree-dump.c`
  or related passes to output a custom format, potentially by traversing the `tree`
  structures. The challenge is identifying the precise point and structure before
  the final RTL generation.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/P4K5PW6--F-9@tutamail.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

A user designing a custom CPU seeks to extract GCC's intermediate representation before it's converted to RTL. Standard dump options like "-fdump-tree-optimized" are insufficient. The user is asking for guidance on where in the source code to find and potentially modify the data structures for custom dumping.

Replies acknowledge the request and suggest further investigation into GCC's internal representation and dump mechanisms.
