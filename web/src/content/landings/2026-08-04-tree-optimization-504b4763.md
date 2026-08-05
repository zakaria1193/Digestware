---
project: gcc
subsystem: tree-optimization
patch_id: null
tags:
- vectorization
- optimization
- performance
commit_hash: 504b4763fd5080d078f0a7fe55501b003a079206
source_type: github
author: Tamar Christina
headline: 'vect: Move speculative read check for inbound access'
tldr: Improves vectorizer's ability to safely speculate accesses in loops with multiple
  data references.
impact_score: 6
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `DR_SCALAR_KNOWN_BOUNDS` check, which determines if a misaligned
  access can be safely speculated by the vectorizer if all scalar accesses are within
  a known fixed-size array, was previously placed within a loop that could exit prematurely.
  This commit moves the check to its own loop within `vect_enhance_data_refs_alignment`
  to ensure it correctly evaluates all data references for safe speculation, particularly
  in cases with multiple misaligned accesses.
primer_glossary:
- term: vectorizer
  definition: A compiler component that transforms code to perform the same operation
    on multiple data elements simultaneously, typically by utilizing special CPU instructions.
    This can significantly improve performance for data-parallel tasks.
- term: speculative execution
  definition: A performance optimization technique where a processor or compiler may
    execute instructions before they are known to be necessary. If the predicted outcome
    is correct, performance improves; if not, the work is discarded.
- term: misaligned access
  definition: An attempt to access data in memory at an address that is not a multiple
    of the data's size. This can lead to performance penalties or even crashes on
    some architectures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/504b4763fd5080d078f0a7fe55501b003a079206
date: '2026-08-04'
is_stub: false
stub_reason: ''
---

The check for safe speculative reads when data accesses are within known bounds has been moved to a dedicated loop. Previously, this check could exit early after the first misaligned access, preventing other data references within the same loop from being marked as safe for speculation. This change ensures that all accesses are evaluated correctly, allowing for more aggressive vectorization.
