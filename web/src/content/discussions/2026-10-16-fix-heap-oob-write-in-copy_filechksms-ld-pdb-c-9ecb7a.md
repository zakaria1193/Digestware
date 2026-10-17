---
project: binutils
subsystem: binutils
patch_id: null
tags:
- linker
- security
- vulnerability
- memory-corruption
- AI-disclosure
discussion_id: 4dc569e0-1a29-44b7-a9a1-22f7c452620f@suse.com
source_type: public_inbox
title: 'Re: [PATCH] Fix heap OOB write in copy_filechksms (ld/pdb.c)'
headline: Fix heap OOB write in copy_filechksms (ld/pdb.c)
tldr: Reviewer questions type choices and error reporting for a heap OOB write fix,
  and raises concerns about AI-generated content.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Fixes a heap OOB write, improving stability and security.
- Potential for improved portability by using `unsigned int` instead of `uint32_t`.
- Enhanced user feedback through more specific error messages.
- Compliance with AI usage policies introduces a process hurdle.
exchanges:
- author: adrimg3196@gmail.com
  role: proposer
  position: Submitted a patch to fix a heap out-of-bounds write in `copy_filechksms`
    by widening a counter and adding input validation.
  quote: 'This patch fixes a heap out-of-bounds write in copy_filechksms()

    (ld/pdb.c:733), a direct sibling of today''s fix 343ab670 (same

    uint16_t pattern, different function).


    uint16_t num_files wraps with more than 65535 DEBUG_S_FILECHKSMS

    entries; the loop then iterates over all entries — with 70000 entries,

    35712 bytes are allocated but 70000 pointers are written. ASan

    confirms: WRITE of size 8 past t…'
- author: Jan Beulich
  role: reviewer
  position: Questions the choice of `uint32_t` over `unsigned int`, suggests improving
    error messages, and raises concerns about the patch author's AI usage disclosure
    and compliance with binutils' LLM content policy.
  quote: 'As you''re referencing that other commit - any reason you still switch to

    uint32_t here then, rather than unsigned int?


    For ease of processing, a full patch (including description and possibly

    tags) would be nice. As to tags: Unless you have a copyright assignment

    in place with the FSF, a Signed-off-by: of yours would be necessary.


    A patch purely as attachment also is harder to comment upon. The…'
primer_expert: This patch targets a heap buffer overflow in the `ld/pdb.c` file, specifically
  within the `copy_filechksms` function. The overflow occurs because `DEBUG_S_FILECHKSMS`
  entries are counted using a `uint16_t` which wraps around when exceeding 65,535.
  The patch proposes widening this counter to `uint32_t` and rejecting inputs with
  more than 65,535 entries. A reviewer, Jan Beulich, questions the choice of `uint32_t`
  over `unsigned int` for better portability and suggests more specific error reporting.
  Crucially, Beulich also raises concerns about the 'AI tool use disclosure' and compliance
  with bi…
primer_glossary:
- term: heap
  definition: A region of a computer's memory that is managed dynamically. Memory
    is allocated and deallocated from the heap at runtime.
- term: OOB write
  definition: Out-of-Bounds write. A memory corruption vulnerability where a program
    writes data beyond the allocated buffer, potentially overwriting adjacent memory
    or corrupting program state.
- term: ld/pdb.c
  definition: A source file within the binutils project, likely related to the linker
    (`ld`) and possibly PDB (Program Database) file handling or debugging information.
- term: ASan
  definition: AddressSanitizer. A memory error detector for C/C++ programs, integrated
    with compilers like GCC and Clang. It helps find buffer overflows, use-after-free,
    and other memory errors.
- term: BFD
  definition: Binutils 'Binary File Descriptor' library. It provides a common interface
    for reading and writing various object file formats.
- term: LLM
  definition: Large Language Model. Refers to AI models trained on vast amounts of
    text data, capable of generating human-like text and code. Binutils has a policy
    regarding the use and disclosure of LLM-generated content.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/4dc569e0-1a29-44b7-a9a1-22f7c452620f@suse.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This discussion revolves around a patch intended to fix a heap out-of-bounds write in the `copy_filechksms` function within `ld/pdb.c`. The issue stems from a `uint16_t` variable wrapping around when the number of entries exceeds 65535, leading to a buffer write beyond allocated memory. The proposed fix widens the variable to `uint32_t` and rejects input exceeding 0xffff. However, the reviewer raises several points: questioning the use of `uint32_t` instead of `unsigned int`, suggesting more informative error reporting than a generic `bfd_error_bad_value`, and importantly, flagging potential issues with the patch's AI-generated content disclosure and compliance with binutils' policy on LLM-generated code.
