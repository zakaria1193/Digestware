---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- security
- documentation
discussion_id: 6328c2df-42b9-4065-8ac4-2de6b4dba3aa@suse.com
source_type: public_inbox
title: '[PATCH v2 0/3] x86: coverage of -mlfence-after-load'
headline: 'x86: coverage of -mlfence-after-load'
tldr: A series of patches to improve the accuracy and documentation of the -mlfence-after-load
  option for x86.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves the correctness and security relevance of the `-mlfence-after-load` option.
- Requires careful testing to ensure no regressions in performance or security coverage.
exchanges: []
primer_expert: This is the cover letter for a series of three patches addressing the
  `-mlfence-after-load` option in the x86 assembler. The series aims to fix issues
  where the option's coverage was both too broad and too narrow, and where its documentation
  was inaccurate. The patches refine which instructions trigger an `LFENCE` insertion
  and improve the explanation of this behavior.
primer_glossary:
- term: x86
  definition: A family of instruction set architectures (ISAs) for CPUs, commonly
    used in personal computers and servers.
- term: -mlfence-after-load
  definition: An assembler option that controls the insertion of an LFENCE (load fence)
    instruction after certain load operations.
- term: LFENCE
  definition: A processor instruction that orders memory loads, preventing subsequent
    loads from being reordered before it.
- term: assembler
  definition: A program that translates assembly language code into machine code.
- term: documentation
  definition: Written materials that explain how a piece of software works or how
    to use it.
series_id: 'binutils:x86: coverage of -mlfence-after-load'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/6328c2df-42b9-4065-8ac4-2de6b4dba3aa@suse.com
bugzilla_url: null
date: '2026-10-30'
is_stub: false
stub_reason: ''
---

This series of three patches aims to correct and improve the functionality and documentation of the `-mlfence-after-load` assembler option for x86. The changes include extending the coverage to more instructions that require load fencing for security mitigations, limiting coverage to exclude instructions that don't necessitate it, and clarifying the documentation to accurately reflect the option's scope and behavior.
