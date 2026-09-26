---
project: binutils
subsystem: binutils/testsuite
patch_id: null
tags:
- testsuite
- windows
- bugfix
commit_hash: aea8b82af17261c88ab4e4b8e623903c49fc81c0
source_type: public_inbox
author: Jan Beulich <jbeulich@sourceware.org>
headline: Fix objdump --source-comment test on Windows
tldr: Objdump test case for --source-comment now passes on Windows.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `objdump --source-comment` test case in binutils/testsuite failed
  on Windows hosts. This was due to MSYS2's automatic conversion of Unix-style paths
  to Windows-style paths, resulting in incorrect arguments being passed to objdump.
  The test now accounts for this behavior.
primer_glossary:
- term: objdump
  definition: A command-line utility that displays information from object files,
    such as disassembled code, symbol tables, and section headers.
- term: MSYS2
  definition: A software distribution and building platform for Windows, providing
    a Unix-like command-line environment and tools.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260925121757.700814BB588C@sourceware.org
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

A test case for `objdump --source-comment` failed on Windows due to path conversion issues in the MSYS2 environment. This commit adjusts the test to correctly handle Windows-style paths, ensuring the test passes.
