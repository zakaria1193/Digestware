---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- autofdo
- gcov
- optimization
- gnu poke
discussion_id: 87mrynhszh.fsf@gnu.org
source_type: public_inbox
title: 'Re: RFC: AutoFDO GCOV Profile Format Version 4'
headline: 'RFC: AutoFDO GCOV Profile Format Version 4'
tldr: Reviewer requests a sample data file to create a GNU poke pickle for the proposed
  AutoFDO GCOV profile format.
proposer: '"Jose E. Marchesi" <jemarch@gnu.org>'
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jose E. Marchesi
  role: proposer
  position: Requests a sample data file to create a GNU poke pickle for the proposed
    AutoFDO GCOV profile format.
  quote: I intend to review the proposed format by writing a GNU poke pickle for it,
    as complete as possible, including constraints etc.
primer_expert: This exchange concerns AutoFDO, a feedback-directed optimization technique.  GCOV
  profiles are used to guide the compiler's optimization decisions. GNU poke is an
  interactive, extensible editor for binary data.
primer_general: This discussion is about a new format for storing code coverage data
  used to optimize programs.  AutoFDO uses this data to improve the performance of
  compiled code.  GNU poke is a tool for inspecting and manipulating binary files.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/87mrynhszh.fsf@gnu.org
bugzilla_url: null
date: '2026-04-28'
---

Jose Marchesi requests a sample data file for the proposed AutoFDO GCOV profile format version 4. He intends to create a GNU poke pickle to review the format, check for potential pitfalls, and facilitate testing and data manipulation.  A pickle file will allow poking at data and dumping to textual representation.
