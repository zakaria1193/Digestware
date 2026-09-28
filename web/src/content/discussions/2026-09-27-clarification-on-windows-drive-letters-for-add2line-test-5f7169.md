---
project: binutils
subsystem: binutils
patch_id: null
tags:
- test
- windows
- linker
- debugging
discussion_id: 87bda70b-e844-4369-a829-feb0eac0ab3a@o2.pl
source_type: public_inbox
title: 'Re: [PATCH] binutils: testsuite: Fix add2line test cases on Windows.'
headline: Clarification on Windows drive letters for add2line test
tldr: Developer seeks clarification on whether non-letter characters like underscores
  or brackets can function as drive letters on Windows, impacting add2line test c…
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Ensures test cases accurately reflect Windows path conventions.
- Requires understanding of nuanced Windows file system behavior.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Asks for clarification on Windows drive letter concepts.
  quote: No, I meant underscores or square brackets as "drive letters".
- author: Jan Dubiec <jdx@o2.pl>
  role: proposer
  position: Expresses surprise at the suggestion and states they are not a Windows
    expert.
  quote: "Huh? 8) I've never heard of anything like that… Although I'm not a \nWindows\
    \ guru…"
primer_expert: This is a brief exchange within a testsuite maintenance thread for
  binutils. The core of the discussion is a clarification request about Windows path
  handling, specifically whether non-alphabetic characters can be interpreted as drive
  letters by utilities like `add2line`. The participants are trying to ensure test
  cases correctly simulate Windows file system behavior.
primer_glossary:
- term: add2line
  definition: A utility that converts addresses into line numbers and function names,
    typically used for debugging and backtraces.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    program.
- term: Windows drive letters
  definition: In Windows, drive letters (e.g., C:, D:) are used to identify storage
    volumes. The discussion explores whether other characters might also function
    similarly in certain contexts.
- term: MinGW
  definition: Minimalist GNU for Windows, a software development environment for creating
    Windows applications using GNU compilers and tools.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/87bda70b-e844-4369-a829-feb0eac0ab3a@o2.pl
bugzilla_url: null
date: '2026-09-27'
is_stub: false
stub_reason: ''
---

This discussion revolves around fixing test cases for the `add2line` utility on Windows. Following a previous exchange about drive letters, the original author of the fix is seeking clarification from Jan Beulich regarding whether characters other than standard letters (like underscores or square brackets) can act as drive letters on Windows. This clarification is needed to ensure the test cases accurately cover Windows path variations.
