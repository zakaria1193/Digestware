---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- binutils
- testing
- relaxation
discussion_id: 20261127135554.306692-1-harshit7kr@gmail.com
source_type: public_inbox
title: '[PATCH] ld: run the relax-underflow tests only on their own targets'
headline: 'ld: restrict relax-underflow tests to specific targets'
tldr: Patch ensures that relax-underflow tests in binutils ld are only run on their
  intended targets.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Harshit Kumar
  role: proposer
  position: Submits a patch to restrict relax-underflow tests to their own targets.
  quote: 'The crx, h8300 and rl78 *-relax-underflow.exp files have no target

    check, so every target''s check-ld sources them.

    ld_relax_underflow_test returns when the emulation is missing, so they

    do not fail elsewhere, but like the other .exp files in these

    directories they should return early on other targets.'
primer_expert: This patch refines the test suite for the GNU linker (ld), specifically
  targeting tests related to relaxation underflow conditions. It addresses an issue
  where tests for specific architectures (crx, h8300, rl78) were being inadvertently
  run on unrelated targets due to a lack of explicit target checks in the test scripts.
  The fix ensures these tests are only executed in the environments they are designed
  for, improving test suite robustness.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or another object file.
- term: relaxation
  definition: A linker optimization technique where the linker adjusts branch offsets
    and other relative addressing information to produce smaller or more efficient
    code, often by overwriting placeholder instructions.
- term: underflow
  definition: In this context, likely refers to a situation where a calculated offset
    during relaxation is too small or negative, potentially leading to incorrect code
    generation or errors.
- term: .exp files
  definition: Test case description files used in the DejaGnu testing framework, commonly
    employed by GNU projects like Binutils.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261127135554.306692-1-harshit7kr@gmail.com
bugzilla_url: null
date: '2026-11-27'
is_stub: false
stub_reason: ''
---

This patch modifies the linker test suite to ensure that relax-underflow tests are executed exclusively on their designated targets. Previously, files lacking explicit target checks were sourced by every target's check-ld, leading to unnecessary checks even if the emulation was missing. The change adds target-specific checks to the relevant test files.
