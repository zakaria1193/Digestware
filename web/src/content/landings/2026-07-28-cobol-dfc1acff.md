---
project: gcc
subsystem: cobol
patch_id: null
tags:
- cobol
- warning
- lexer
commit_hash: dfc1acffcd52d0ae0fbc155f221ea7091a2f39b9
source_type: github
author: James K. Lowden
headline: 'cobol: Cast assigned 0x8D to char to quell warning'
tldr: Fixes a signed/unsigned char warning in the COBOL lexer by explicitly casting
  a hex value.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In the COBOL frontend's lexer, an assignment of a constant 0x8D to
  a `char` type triggered a signed/unsigned warning. This patch applies a `char()`
  cast to the value to resolve the diagnostic. This change is localized to `cdftext::free_form_reference_format`
  in `lexio.cc`.
primer_glossary:
- term: lexer
  definition: The lexical analyzer, also known as a scanner, is the first phase of
    a compiler. It takes the source code as input and produces a stream of tokens.
- term: signed/unsigned warning
  definition: A compiler diagnostic issued when a value's signedness might not match
    the target type's signedness, potentially leading to unexpected behavior or data
    interpretation.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/dfc1acffcd52d0ae0fbc155f221ea7091a2f39b9
date: '2026-07-28'
is_stub: true
stub_reason: low_score
---

The COBOL compiler's lexer incorrectly issued a warning when assigning the hexadecimal value 0x8D to a character type. This commit resolves the issue by explicitly casting the value to `char`, satisfying the compiler's type checking and suppressing the diagnostic warning, ensuring cleaner build outputs.
