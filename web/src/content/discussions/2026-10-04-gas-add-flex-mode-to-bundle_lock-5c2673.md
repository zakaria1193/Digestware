---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- assembler
- instruction bundling
- documentation
discussion_id: 7027307a-b1e9-4f76-a576-62f35b5b1341@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH] gas: add flex mode to .bundle_lock'
headline: 'gas: add flex mode to .bundle_lock'
tldr: Reviewer welcomes a patch adding 'flex' mode to .bundle_lock but requests documentation
  and justification for oversized sequences.
proposer: Abhay Kandpal <abhay@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Increased flexibility in instruction sequencing.
- Requires documentation updates and justification for use cases.
exchanges:
- author: Abhay Kandpal
  role: reviewer
  position: Welcomes the patch and reviewer, finds the format acceptable, but requests
    justification for oversized sequences and documentation updates.
  quote: 'Thanks for the patch, and welcome. The format looks fine to me.


    Could you say in the commit message what needs oversized locked sequences?


    gas/doc/as.texi describes a .bundle_lock sequence as staying within the

    same bundle, which flex changes, so the new argument needs documenting

    there. A gas/NEWS entry would probably be good too.'
- author: Sarvesh Chandra
  role: proposer
  position: Proposes a patch to allow `.bundle_lock` flex to accept sequences larger
    than the bundle size, keeping existing alignment handling and strict checks for
    ordinary locks, and adds tests.
  quote: 'Allow .bundle_lock flex to accept sequences larger than the bundle size.

    Keep the existing alignment handling and strict checks for ordinary locks.


    Add tests for straddling, non-straddling, oversized, and nested locks.'
primer_expert: This patch introduces a 'flex' mode to the `.bundle_lock` pseudo-instruction
  in the GNU Assembler (`gas`). This mode relaxes the constraint that sequences locked
  by `.bundle_lock` must entirely fit within a single instruction bundle (typically
  4 instructions on x86). The change, located in `gas/read.c`, allows `.bundle_lock`
  to accommodate sequences that span across bundle boundaries. The discussion centers
  on the justification for this flexibility and the necessary documentation updates.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package. It translates assembly
    language code into machine code.
- term: .bundle_lock
  definition: An assembler directive used to ensure that a sequence of instructions
    is kept together within a single instruction bundle, relevant for architectures
    with instruction bundling.
- term: instruction bundle
  definition: A group of instructions that can be executed in parallel or as a single
    unit on certain architectures, like VLIW or some x86 processors.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/7027307a-b1e9-4f76-a576-62f35b5b1341@linux.ibm.com
bugzilla_url: null
date: '2026-10-04'
is_stub: false
stub_reason: ''
---

Abhay Kandpal welcomes Sarvesh Chandra's first patch to binutils, which adds a 'flex' mode to the `.bundle_lock` directive in the assembler (gas). This mode allows sequences larger than the standard bundle size. The reviewer finds the format acceptable but asks for clarification on why oversized locked sequences are needed and requests documentation updates for `as.texi` and a `gas/NEWS` entry.
