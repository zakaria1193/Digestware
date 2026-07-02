---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- objdump
- testsuite
- x86
- disassembly
discussion_id: c705bed3-6713-4fa2-b3e4-9ff10e346b2a@redhat.com
source_type: public_inbox
title: 'Re: RFC: Annotate immediates in x86 disassembly'
headline: Fix test_objdump_M_annotate failure by dropping $(exe).
tldr: Nick Clifton proposes a patch to fix a testsuite failure by removing the need
  for executable file names in test_objdump_M_annotate.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch addresses a testsuite failure in objdump related to immediate
  value annotation in x86 disassembly.  The issue arises from the test's reliance
  on the $(exe) variable, which assumes a host OS executable filename.
primer_general: Objdump is a tool for examining object files, including disassembling
  machine code.  This patch fixes a problem in the objdump testsuite where the tests
  were incorrectly requiring executable filenames, even though the executables were
  not actually run.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/c705bed3-6713-4fa2-b3e4-9ff10e346b2a@redhat.com
bugzilla_url: null
date: '2026-05-12'
is_stub: false
---

Nick Clifton provides a patch to fix a testsuite failure in `test_objdump_M_annotate` by removing the dependency on the host OS's executable filename conventions. The patch drops the use of `$(exe)` as the compiled binary isn't executed.
