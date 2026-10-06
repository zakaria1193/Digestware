---
project: binutils
subsystem: ld/pdb
patch_id: null
tags:
- binutils
- linker
- pdb
- windows
- memory safety
discussion_id: 57848e11-bb0a-439b-b603-96651f1cb847@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2] ld/pdb: Avoid double-free on malformed symbol data'
headline: 'ld/pdb: Avoid double-free on malformed symbol data'
tldr: Fixes a double-free bug in linker's PDB generation when handling malformed symbol
  data.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Addresses a critical memory safety issue.
- Minor change to error handling logic.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Acknowledges and accepts the proposed fix.
  quote: Okay.
- author: Oleg Tolmatcev
  role: proposer
  position: Explains that the current module's file array was being freed twice upon
    failure and proposes to leave its cleanup to the caller.
  quote: 'When handle_debugs_section fails, create_module_info_substream frees

    the file arrays for all modules, including the current one. Do not free

    the current array in populate_module_stream as well.'
primer_expert: This patch addresses a memory corruption bug (double-free) in the linker's
  PDB generation for Windows executables. The defect arises in `ld/pdb.c` within the
  `populate_module_stream` function. If `handle_debugs_section` encounters an error,
  `create_module_info_substream` frees the `mod_source->files` array. `populate_module_stream`
  would then also attempt to free this same array, causing a double-free. The fix
  modifies `populate_module_stream` to avoid this redundant free, relying on the caller
  to manage the memory.
primer_glossary:
- term: PDB
  definition: Program Database. A file format used by Microsoft Windows to store information
    about executable files, used by debuggers and other tools.
- term: linker
  definition: A program that combines object code from multiple sources into a single
    executable or library.
- term: double-free
  definition: A memory corruption error that occurs when memory is freed more than
    once.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/57848e11-bb0a-439b-b603-96651f1cb847@suse.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

This patch corrects a double-free error in the linker's PDB (Program Database) generation. The issue occurred when `handle_debugs_section` failed, causing `create_module_info_substream` to free file arrays for all modules, including the current one. Subsequently, `populate_module_stream` would also attempt to free the same array, leading to the double-free. The fix ensures that the cleanup of the current module's file array is handled only once by the caller.
