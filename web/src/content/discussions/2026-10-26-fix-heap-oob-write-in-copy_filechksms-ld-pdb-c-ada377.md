---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- security
- patch
- policy
discussion_id: 457df2fc-2daa-4ec8-b0e3-ab33b0c2c0fa@suse.com
source_type: public_inbox
title: 'Re: [PATCH] Fix heap OOB write in copy_filechksms (ld/pdb.c)'
headline: Fix heap OOB write in copy_filechksms (ld/pdb.c)
tldr: Discussion regarding a patch fixing a heap OOB write, focusing on type usage,
  error reporting, and AI disclosure policies.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Needs Revision
outcome: needs_revision
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Using `uint32_t` accommodates larger counts but requires careful handling of input
  validation to prevent issues when exceeding `0xFFFF`.
- Replacing a direct code fix with stricter error checking and policy adherence might
  delay the patch but ensures compliance and code quality.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Questions the use of `uint32_t` instead of `unsigned int` and requests
    a full patch submission with a `Signed-off-by` line, also noting concerns about
    AI usage disclosure.
  quote: As you're referencing that other commit - any reason you still switch to
    uint32_t here then, rather than unsigned int?
- author: Jan Beulich
  role: reviewer
  position: Further elaborates on concerns regarding the patch, specifically mentioning
    the policy violation related to AI usage and the need for copyright assignment,
    indicating escalation to higher authorities within the project.
  quote: 'Here comes the really difficult part: This violates [1]. Still of course
    we want the bug fixed.


    Both the S-o-b aspect and the AI use are on the edge, as per [2]. [1] overall
    is more strict than [2], and personally I also tend to more strict interpretation
    of such rules. In any event I''ll bring this up with Nick.'
- author: Jan Beulich
  role: reviewer
  position: Requests clarification on the extent of AI use and reiterates the need
    for a resubmission with the author's `Signed-off-by` line, emphasizing copyright
    ownership.
  quote: After consultation we'd like to ask for clarification on the extent of AI
    use here. Independent of that a re-submission with your S-o-b (to indicate that
    you hold the copyright on the patch) would be required.
primer_expert: This thread discusses a patch for binutils' linker (`ld`) that fixes
  a heap out-of-bounds write in `copy_filechksms` when handling `DEBUG_S_FILECHKSMS`
  entries. The core issue is that `num_files` wraps around `0xFFFF`, leading to an
  attempt to write more data than allocated. Reviewers are focused on code quality
  (type choices, error reporting), contribution policy adherence (AI disclosure, copyright
  assignment/Signed-off-by), and are requesting clarification and re-submission.
primer_glossary:
- term: heap
  definition: A region of memory used for dynamic memory allocation during program
    execution.
- term: OOB write
  definition: Out-of-bounds write. Writing data beyond the allocated buffer, which
    can lead to memory corruption and security vulnerabilities.
- term: ld
  definition: The GNU linker, responsible for combining object files into an executable
    or library.
- term: pdb.c
  definition: A source file likely related to processing Program Database (PDB) information,
    often used for debugging symbols, particularly in environments like Windows.
- term: DEBUG_S_FILECHKSMS
  definition: Likely a data structure or type related to debugging symbols, possibly
    for checking checksums or file information within an object file.
- term: uint16_t
  definition: An unsigned integer type that is exactly 16 bits wide.
- term: unsigned int
  definition: An integer type that is guaranteed to be at least 16 bits wide, typically
    32 bits on most modern systems. Its exact size can vary by architecture.
- term: uint32_t
  definition: An unsigned integer type that is exactly 32 bits wide.
- term: Signed-off-by
  definition: A trailer line in a commit message indicating that the author has the
    right to submit the work under the project's license.
- term: ASan
  definition: AddressSanitizer, a memory error detector for C/C++ that finds issues
    like buffer overflows and use-after-free.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/457df2fc-2daa-4ec8-b0e3-ab33b0c2c0fa@suse.com
bugzilla_url: null
date: '2026-10-26'
is_stub: false
stub_reason: ''
---

This discussion revolves around a patch intended to fix a heap out-of-bounds write in the `copy_filechksms` function within `ld/pdb.c`. Reviewers are questioning the choice of `uint32_t` over `unsigned int` for a variable, the clarity of error reporting to the user, and the policy regarding AI-assisted code submissions. The discussion highlights concerns about copyright assignment and adherence to project contribution guidelines.
