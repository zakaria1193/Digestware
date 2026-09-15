---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- testsuite
- windows
- objdump
- msys2
discussion_id: 20260915053021.234582-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH] binutils: testsuite: Fix "objdump --source-comment" test case on Windows.'
headline: Fix objdump --source-comment test on Windows
tldr: Fixes objdump test case failure on Windows due to path argument conversion.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensuring test suite reliability across different operating systems.
- Managing the intricacies of environment-specific argument processing (MSYS2 path
  conversion).
exchanges:
- author: Jan Dubiec <jdx@o2.pl>
  role: proposer
  position: Submits a patch to fix a failing objdump test case on Windows by preventing
    MSYS2 path conversion for the --source-comment argument.
  quote: 'This patch fixes the issue using the method described on the aforementioned

    page.'
primer_expert: This patch addresses a test suite failure in the binutils project on
  Windows, specifically for the `objdump --source-comment` test. The problem stems
  from MSYS2's automatic path conversion, which incorrectly modifies the argument
  intended for `objdump`. The fix involves temporarily disabling this conversion for
  the specific argument using the `MSYS2_ARG_CONV_EXCL` environment variable.
primer_glossary:
- term: objdump
  definition: A GNU binary utilities program that displays information from object
    files, including disassembled code.
- term: testsuite
  definition: A collection of tests designed to verify the correctness of a software
    system.
- term: MSYS2
  definition: A software distribution and building platform for Windows, providing
    a Unix-like shell environment and package management.
- term: path conversion
  definition: The process by which a system automatically modifies file paths, for
    example, converting Unix-style paths (e.g., `/usr/bin`) to Windows-style paths
    (e.g., `C:\msys64\usr\bin`).
- term: MSYS2_ARG_CONV_EXCL
  definition: An environment variable used in MSYS2 to specify arguments that should
    be excluded from automatic path conversion.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260915053021.234582-1-jdx@o2.pl
bugzilla_url: null
date: '2026-09-15'
is_stub: false
stub_reason: ''
---

A test case for `objdump --source-comment` is failing on Windows within the MSYS2 environment. This failure occurs because MSYS2 automatically converts Unix-style paths to Windows-style paths in command-line arguments, resulting in a single slash being passed to objdump instead of the expected double slash. This patch addresses the issue by conditionally excluding `--source-comment=` from this automatic conversion for Windows hosts.
