---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- c++
- warnings
- structured bindings
- unused variables
discussion_id: IwntDp_Q1VxRwhn7aMzNxnY2SVNNCEI8BMw2bMGfoymG74jx1ONjefmAtoNwjrkk2xcpHC7nBhKor_UBDinXr4qGnWi5pbKCkaK4G1RRzfQ=@nicula.xyz
source_type: public_inbox
title: Warnings for partially-unused structured bindings in C++26 mode
headline: Propose warnings for partially-unused structured bindings in C++26.
tldr: In C++26, enable `-Wunused` warnings for unused variables in structured bindings,
  now that unnamed placeholders are available.
proposer: Ionuț Nicula <nicula@nicula.xyz>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Requires C++26 mode to avoid being unergonomic.
- May increase the number of warnings, requiring developers to add `_` placeholders.
exchanges: []
primer_expert: Structured bindings decompose tuples/structs into individual variables.  `-Wunused`
  flags unused local variables, but not if the variable is part of a structured binding.  C++26
  allows `auto [_, x, _] = ...` to explicitly mark elements as unused, which unblocks
  the new warning.
primer_general: Structured bindings in C++ allow you to unpack the elements of a tuple
  or struct into individual variables (e.g., `auto [x, y, z] = my_tuple;`).  GCC's
  `-Wunused` flag warns about unused variables. This proposal suggests extending `-Wunused`
  to detect when only some elements of a structured binding are used, which can indicate
  a programming error.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/IwntDp_Q1VxRwhn7aMzNxnY2SVNNCEI8BMw2bMGfoymG74jx1ONjefmAtoNwjrkk2xcpHC7nBhKor_UBDinXr4qGnWi5pbKCkaK4G1RRzfQ=@nicula.xyz
bugzilla_url: null
date: '2026-05-12'
is_stub: false
---

Ionuț Nicula proposes enabling `-Wunused` warnings for structured bindings in C++26 mode when some sub-objects are unused.  Before C++26, the lack of a placeholder variable (like `_`) made this awkward.  This change could catch errors, particularly in loops where a variable is unintentionally unused due to copy-paste mistakes.
