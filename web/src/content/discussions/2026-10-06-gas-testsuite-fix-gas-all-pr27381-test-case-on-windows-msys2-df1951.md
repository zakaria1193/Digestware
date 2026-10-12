---
project: binutils
subsystem: gas
patch_id: null
tags:
- assembler
- testing
- Windows
- MSYS2
discussion_id: asV1grlhWgDvy7pJ@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] gas: testsuite: Fix gas/all/pr27381 test case on Windows/MSYS2.'
headline: 'gas: testsuite: Fix gas/all/pr27381 test case on Windows/MSYS2.'
tldr: Test case fix for gas on Windows/MSYS2.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensures test suite portability across different operating systems.
- Minor adjustments to test case files.
exchanges:
- author: Jan Dubiec
  role: proposer
  position: Submitted a patch to fix a gas test case on Windows/MSYS2 by adjusting
    a regular expression and directory path.
  quote: 'This patch fixes the test case by extending the regular expression in

    pr27381.err accordingly. It also replaces the /etc directory, which does

    not exist on Windows, with ./tmpdir.'
- author: Alan Modra <amodra@gmail.com>
  role: maintainer
  position: Applied the patch, confirming its acceptance.
  quote: Applied, thanks.
primer_expert: This patch corrects the `gas/all/pr27381` test case within the GNU
  Binutils test suite to function correctly on Windows environments, particularly
  those using MSYS2. The changes involve modifying `gas/all/pr27381.err` to adjust
  a regular expression that was causing test failures due to platform-specific output
  differences, and updating a hardcoded path from `/etc` to a more appropriate temporary
  directory (`./tmpdir`) for Windows.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project, responsible for
    converting assembly language code into machine code.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    program.
- term: Windows/MSYS2
  definition: MSYS2 is a software distribution and building platform for Windows,
    providing a Unix-like command-line environment and tools, often used for compiling
    open-source software on Windows.
- term: regular expression
  definition: A sequence of characters that defines a search pattern, used for pattern
    matching within strings.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/asV1grlhWgDvy7pJ@squeak.grove.modra.org
bugzilla_url: null
date: '2026-10-06'
is_stub: false
stub_reason: ''
---

This patch addresses an issue with the `gas/all/pr27381` test case on Windows systems using MSYS2. The fix involves updating a regular expression in the `.err` file to correctly match expected output and replacing the non-existent `/etc` directory with `./tmpdir` to accommodate the Windows environment.
