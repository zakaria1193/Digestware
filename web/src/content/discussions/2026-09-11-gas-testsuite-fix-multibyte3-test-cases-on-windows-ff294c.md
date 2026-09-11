---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- testsuite
- Windows
- cross-platform
- regular expressions
discussion_id: 20260911022233.502927-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH] gas: testsuite: Fix multibyte3 test cases on Windows.'
headline: 'gas: testsuite: Fix multibyte3 test cases on Windows.'
tldr: Fixes Windows test failures in gas's multibyte3 test cases by adjusting regex
  matching.
proposer: Jan Dubiec
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Improves cross-platform compatibility of the test suite.
- Slightly broadens regex matching, which could theoretically have unintended consequences
  if not carefully applied, though unlikely in this specific context.
exchanges:
- author: Jan Dubiec
  role: proposer
  position: Submits a patch to fix gas testsuite failures on Windows by adjusting
    regular expression matching for file paths.
  quote: 'These two test cases fail on Windows: [...] This is because the [^:] part
    of the regular expressions prevents them from matching the full file path on Windows'
primer_expert: The gas assembler's test suite includes tests for handling multibyte
  characters in file paths. On Windows, paths are typically represented with drive
  letters and backslashes (though forward slashes are often accepted), and can contain
  characters that might be misinterpreted by regular expressions designed for Unix-like
  path structures. This patch specifically targets the `multibyte3` test case, modifying
  the regex to correctly parse Windows paths, which include a drive letter and colon,
  preventing the test from failing due to incorrect path matching.
primer_glossary:
- term: gas
  definition: The GNU Assembler, a component of the binutils package responsible for
    converting assembly language code into machine code.
- term: testsuite
  definition: A collection of tests designed to verify the correct functionality of
    a software component or program.
- term: Windows
  definition: Microsoft's widely used family of graphical operating systems.
- term: regular expression
  definition: A sequence of characters that defines a search pattern, used for pattern
    matching within strings.
- term: multibyte character
  definition: A character that requires more than one byte to represent in a character
    encoding, often used for non-ASCII characters.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260911022233.502927-1-jdx@o2.pl
bugzilla_url: null
date: '2026-09-11'
is_stub: false
stub_reason: ''
---

This patch addresses failures in the `multibyte3` test cases for the gas assembler on Windows. The failures occur because the regular expression `[^:]` used for matching file paths prevents correct recognition of Windows-style paths (e.g., `D:/Works/...`). The patch aims to correct the regular expressions within the test suite to properly handle these paths, ensuring the tests pass on Windows.
