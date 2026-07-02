---
project: binutils
subsystem: x86/intel
patch_id: null
tags:
- binutils
- x86
- infinite recursion
- assembly
- bugfix
discussion_id: 44e7ed68-60fe-4e72-9391-6f124030d975@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] x86/Intel: avoid infinite recursion in i386_intel_simplify_symbol()
  (again)'
headline: Questions loop termination in i386_intel_simplify_symbol()
tldr: Jan Beulich questions the correctness of a patch aiming to prevent infinite
  recursion in `i386_intel_simplify_symbol()`.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: other
  position: Questions the correctness of the proposed patch, suggesting that cutting
    the loop and only looking for `O_symbol` may be insufficient to prevent infinite
    recursion.
  quote: null
primer_expert: This discussion revolves around preventing infinite recursion in `i386_intel_simplify_symbol()`,
  a function in binutils responsible for simplifying symbols in Intel x86 assembly.
  The concern is that the proposed patch may not fully address the issue, potentially
  leading to continued recursion under certain conditions. The discussion hints at
  the need for a more comprehensive expression walking mechanism.
primer_general: Binutils is a collection of tools used for working with binary files,
  such as executables and object code. This discussion concerns a function within
  binutils that simplifies symbol names in x86 assembly code. The goal is to prevent
  the function from getting stuck in an infinite loop when processing complex symbol
  definitions, ensuring that the tools remain stable and reliable.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/44e7ed68-60fe-4e72-9391-6f124030d975@suse.com
bugzilla_url: null
date: '2026-05-18'
is_stub: false
---

Jan Beulich expresses concerns regarding the correctness of a patch designed to prevent infinite recursion within the `i386_intel_simplify_symbol()` function. They suggest that the current approach of cutting the loop and only looking for `O_symbol` might be insufficient. The author acknowledges the lack of a comprehensive solution and points to the need for a more robust expression walking mechanism, similar to what's used for Intel syntax parsing.
