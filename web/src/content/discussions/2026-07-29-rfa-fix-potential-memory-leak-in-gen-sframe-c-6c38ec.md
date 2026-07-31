---
project: binutils
subsystem: gas
patch_id: null
tags:
- assembler
- memory management
- debugging
- binutils
discussion_id: cec32933-c3b6-4b28-8745-9a3d738a2bed@linux.ibm.com
source_type: public_inbox
title: 'Re: RFA: Fix potential memory leak in gen-sframe.c'
headline: 'RFA: Fix potential memory leak in gen-sframe.c'
tldr: Fixes a memory leak in gas/gen-sframe.c that could lead to a segmentation fault
  by properly cleaning up context structures.
proposer: Jens Remus <jremus@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Fixes a critical bug leading to crashes and data corruption.
- May involve a slight overhead for initializing/clearing structure fields.
exchanges:
- author: Nick Clifton
  role: proposer
  position: Identifies a bug where `sframe_xlate_ctx_cleanup` doesn't zero out fields
    after freeing memory, leading to dangling pointers and a crash.
  quote: "The problem reported looks like this:\n\n    1. sframe_do_fde() (line 2490)\
    \ populates xlate_ctx->first_fre with\n       allocated FRE entries and sets xlate_ctx->num_xlate_fres\
    \ > 0.\n       \n    2. On failure for a signal frame (line 2491-2496),\n    \
    \   sframe_xlate_ctx_cleanup() frees the FRE chain (line 1096) but\n       does\
    \ not null first_fre or reset num_xlate_fres. Then err is\n       forced to SF…"
- author: Jens Remus
  role: contributor
  position: Confirms the described issue causes a segfault and points to his own patch
    series that addresses this and related SFrame issues.
  quote: 'Not Indu, but replying as I was involved in SFrame V3 development:


    I can confirm that above causes a segmentation fault and below fixes it.


    See my just sent "[PATCH 0/2] gas: sframe: Fix for flefible FDE and new test":

    https://inbox.sourceware.org/binutils/20260729163445.2563223-1-jremus@linux.ibm.com/'
primer_expert: This discussion concerns `gas/gen-sframe.c` and potential memory corruption
  when handling SFrame data, specifically during error paths in signal frame processing.
  The issue involves dangling pointers (`xlate_ctx->first_fre`) and stale counts (`xlate_ctx->num_xlate_fres`)
  after cleanup, which are then copied into the final FDE structure, leading to a
  crash. Jens Remus has submitted a patch series to address this and other SFrame-related
  issues.
primer_glossary:
- term: GAS
  definition: The GNU Assembler, part of the GNU Binutils package, which translates
    assembly language code into machine code.
- term: SFrame
  definition: A mechanism used to describe the structure of stack frames, particularly
    for exception handling and debugging information, often used in conjunction with
    DWARF.
- term: FDE
  definition: Frame Description Entry. Part of DWARF debugging information, it describes
    how to unwind the stack for a particular function.
- term: gen-sframe.c
  definition: A source file within GAS that handles the generation and manipulation
    of SFrame data structures.
- term: sframe_xlate_ctx
  definition: A structure used within GAS to manage the translation context for SFrame
    data.
- term: segfault
  definition: A segmentation fault, an error that occurs when a program tries to access
    a memory location that it's not allowed to access.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/cec32933-c3b6-4b28-8745-9a3d738a2bed@linux.ibm.com
bugzilla_url: null
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

This discussion addresses a potential memory leak and subsequent segmentation fault in the SFrame handling within GAS (GNU Assembler). The issue arises when an error occurs during signal frame processing, leading to `sframe_xlate_ctx_cleanup` freeing memory but not resetting pointers and counts. This results in dangling pointers being copied to the output FDE structure, causing a crash when that data is written. A proposed patch and a related series aim to fix this by properly nullifying structure fields during cleanup.
