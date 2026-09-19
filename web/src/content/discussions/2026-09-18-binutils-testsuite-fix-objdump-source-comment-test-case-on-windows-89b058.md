---
project: binutils
subsystem: binutils
patch_id: null
tags:
- objdump
- testsuite
- Windows
- MSYS2
- cross-platform
discussion_id: 2f1d1589-5698-432b-8525-d659c01fe288@suse.com
source_type: public_inbox
title: 'Re: [PATCH] binutils: testsuite: Fix "objdump --source-comment" test case
  on Windows.'
headline: 'binutils: testsuite: Fix "objdump --source-comment" test case on Windows.'
tldr: Adjusts objdump test case for Windows to prevent path conversion issues with
  MSYS2.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: needs_revision
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Fixes a specific test case failure on Windows.
- Uses environment variable manipulation, which might be fragile or have unintended
  side effects.
- The reviewer suggests a potentially more robust method of handling environment variables.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Proposes a fix for a Windows-specific test case failure in `objdump --source-comment`
    by excluding the argument from MSYS2 path conversion.
  quote: 'The workaround of course isn''t very nice, and in particular doesn''t scale.

    The page you reference doesn''t address at all whether e.g. some form of

    quoting would also help. That certainly depends on where exactly the

    conversion is being done.'
- author: Jan Beulich
  role: reviewer
  position: Asks if appending to the environment variable would be a better approach
    than fully overwriting and unsetting it.
  quote: 'In case the user has set the env var globally, wouldn''t you better append

    to it (and then restore) rather than fully overwriting (and then deleting)?'
primer_expert: This discussion addresses a test suite failure in `objdump` on Windows
  when using MSYS2. The problem arises from MSYS2's automatic path conversion interfering
  with arguments like `--source-comment=//`, which expects a specific format. The
  proposed solution involves manipulating the `MSYS2_ARG_CONV_EXCL` environment variable
  within the test script.
primer_glossary:
- term: objdump
  definition: A utility that displays information from object files, including disassembled
    code.
- term: MSYS2
  definition: A software distribution and building platform for Windows, providing
    a Unix-like command-line environment.
- term: test case
  definition: A specific set of conditions or variables under which a tester will
    determine whether a system under test satisfies requirements or works correctly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/2f1d1589-5698-432b-8525-d659c01fe288@suse.com
bugzilla_url: null
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

A test case for `objdump --source-comment` fails on Windows due to MSYS2's automatic conversion of Unix-style paths to Windows-style paths, which alters the expected double slash to a single slash. This patch attempts to fix the issue by using `MSYS2_ARG_CONV_EXCL` to prevent this conversion for the `--source-comment=` argument. A reviewer questions the approach, suggesting appending to the environment variable might be more robust.
