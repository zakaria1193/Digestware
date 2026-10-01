---
project: binutils
subsystem: s390
patch_id: null
tags:
- s390
- assembler
- testing
- naming
discussion_id: 20260930081834.2948939-24-jremus@linux.ibm.com
source_type: public_inbox
title: '[PATCH 02/20] s390: Add common IBM Z CPU name to assembler test names'
headline: 's390: Add common IBM Z CPU name to assembler test names'
tldr: Standardizes s390 assembler test names to use common IBM Z CPU names.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch modifies the naming of test files within the binutils gas/testsuite/s390
  directory. It replaces architecture version numbers (e.g., 'arch12') with the common
  CPU names (e.g., 'z14') for IBM Z processors. This improves the readability and
  maintainability of the test suite by using more recognizable identifiers for different
  hardware levels.
primer_glossary:
- term: assembler test file
  definition: A file containing assembly language code and expected output, used to
    verify the correctness of the assembler.
- term: CPU name
  definition: A common, user-friendly identifier for a specific processor model, such
    as 'z14', as opposed to a more technical architecture version number.
series_id: 'binutils:s390: add common ibm z cpu name to assembler test names'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260930081834.2948939-24-jremus@linux.ibm.com
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch updates the naming convention for s390 assembler test files to use common IBM Z CPU names (e.g., 'z14', 'z15', 'z16') instead of just architecture version numbers. This change aligns test file names with the widely used CPU names, improving clarity and consistency in the binutils test suite.
