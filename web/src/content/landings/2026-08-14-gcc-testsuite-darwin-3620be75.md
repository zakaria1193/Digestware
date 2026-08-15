---
project: gcc
subsystem: gcc/testsuite/darwin
patch_id: null
tags:
- testsuite
- darwin
- linker
commit_hash: 3620be7514366af9ffe8af26082c3a87113fad01
source_type: github
author: Iain Sandoe
headline: Update Darwin cfstring tests for linker-visible labels
tldr: Adjusts Darwin cfstring tests to handle linker-visible string labels.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The test files `g++.dg/torture/darwin-cfstring-3.C` and `gcc.dg/torture/darwin-cfstring-3.c`
  have been updated to account for the fix in PR126723, which affects how string labels
  are made visible to the linker on Darwin. Previously, these tests might have assumed
  a certain linking behavior for strings used in `cfstring` constructs. The update
  ensures that the tests correctly recognize and handle string labels that are now
  explicitly marked as linker-visible, aligning the test suite with the corrected
  compiler behavior.
primer_glossary:
- term: cfstring
  definition: A programming construct often used in Objective-C and Cocoa frameworks
    for efficient handling of string constants.
- term: linker-visible
  definition: A symbol (like a label or variable) that is made available to the linker,
    allowing it to be referenced by other object files or libraries during the final
    linking stage.
- term: string label
  definition: A symbolic name assigned to a string literal or a memory location containing
    a string, used by the assembler and linker.
- term: Darwin
  definition: The open-source Unix-based operating system foundation of macOS, iOS,
    and other Apple operating systems. GCC includes specific support for Darwin targets.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/3620be7514366af9ffe8af26082c3a87113fad01
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

This commit updates Darwin-specific test cases for `cfstring` to accommodate changes related to linker-visible string labels, which were introduced in PR126723. The tests now correctly handle these linker-visible labels, ensuring their continued functionality and correctness on Darwin targets.
