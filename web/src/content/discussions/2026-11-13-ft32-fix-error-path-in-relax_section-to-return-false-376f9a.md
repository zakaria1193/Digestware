---
project: binutils
subsystem: binutils/ft32
patch_id: null
tags:
- binutils
- linker
- ft32
- error handling
discussion_id: 11a02b26-243f-4e10-8981-4e1cc6989d07@suse.com
source_type: public_inbox
title: 'Re: [PATCH v3 9/8] ft32: return false from relax_section error path'
headline: 'ft32: Fix error path in relax_section to return false'
tldr: Corrects an error handling bug in the ft32 linker relaxation process.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Fixes a bug in error reporting, improving the robustness of the linker's relaxation
  process for the ft32 target.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Submits a patch to fix an error return value in the ft32 relaxation process.
  quote: 'In ft32_elf_relax_section, the error_return: block returned true, so

    failures to read the section contents, local symbols or relocations, and

    failures from elf32_ft32_relax_delete_bytes, were reported as

    success and relaxation continued with corrupt state.  Correct

    error_return: to return false.


    Signed-off-by: Harshit Kumar <harshit7kr@gmail.com>'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges and accepts the proposed fix.
  quote: Okay.
primer_expert: The ft32 target in binutils has a relaxation function, `ft32_elf_relax_section`,
  where the error handling path was faulty. Specifically, the `error_return` label
  incorrectly returned `true`, indicating success even when underlying operations
  like section content reading, local symbol processing, or relocation handling (including
  `elf32_ft32_relax_delete_bytes`) failed. This led to corrupted state during relaxation.
  This patch corrects the return value in the error path to `false`, aligning it with
  the expected behavior for signaling failure.
primer_glossary:
- term: ft32
  definition: Likely refers to a specific target architecture or instruction set for
    which binutils provides support, possibly related to Fujitsu's FR or similar architectures.
- term: linker relaxation
  definition: A linker optimization process where certain instructions or data references
    are adjusted (e.g., changing absolute addresses to PC-relative offsets) to improve
    code density or enable position-independent execution. This often involves multiple
    passes.
- term: section
  definition: A part of an object file or executable that contains related data, such
    as code (.text), initialized data (.data), or uninitialized data (.bss).
- term: relocations
  definition: Information in an object file that tells the linker how to modify addresses
    when combining object files, for example, to handle position-independent code
    or absolute addressing.
series_id: 'binutils:ft32: return false from relax_section error path'
series_role: reply
series_parts:
- title: 'ft32: return false from relax_section error path'
  url: https://inbox.sourceware.org/binutils/20261113092940.454448-1-harshit7kr@gmail.com
  n: 9
  total: 8
url: https://inbox.sourceware.org/binutils/11a02b26-243f-4e10-8981-4e1cc6989d07@suse.com
bugzilla_url: null
date: '2026-11-13'
is_stub: false
stub_reason: ''
---

This patch corrects an error in the `ft32_elf_relax_section` function within the binutils ft32 target. Previously, the `error_return` block incorrectly returned `true`, masking failures such as read errors, symbol issues, or relocation problems as successes. This allowed relaxation to continue with corrupted state. The fix changes the error return value to `false`, ensuring that errors during relaxation are properly reported.
