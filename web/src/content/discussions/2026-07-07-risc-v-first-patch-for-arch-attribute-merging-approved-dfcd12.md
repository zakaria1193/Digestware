---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- memory leak
- patch review
discussion_id: CAOvetVCPXtFsRmBLCdrEiEdpzYfVgp4v=f2N1JuB4OS47bDLfw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] RISC-V: Release subset lists on all paths when the linker
  merges arch attributes'
headline: 'RISC-V: First patch for arch attribute merging approved'
tldr: Nelson Chu approves the first patch in the RISC-V linker arch attribute series,
  which fixes memory leaks.
proposer: Nelson Chu <nelson.chu@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Nelson Chu <nelson.chu@sifive.com>
  role: reviewer
  position: Approves the first patch, stating it looks okay.
  quote: This looks Okay, thanks.
- author: Ethan Y. C. Liang <ycl669@andestech.com>
  role: proposer
  position: Explains that the first patch fixes memory leaks by cleaning up subset
    lists on error paths.
  quote: 'riscv_merge_arch_attr_info returned early on the error paths without

    releasing in_subsets, out_subsets and merged_subsets, so the nodes

    already added to them were leaked.  The leaked nodes of in_subsets

    and out_subsets also carry over into the next merge.'
primer_expert: Nelson Chu has reviewed and approved the first patch (part of a series)
  by Ethan Y. C. Liang. This patch modifies `bfd/elfxx-riscv.c` to fix memory leaks
  within the `riscv_merge_arch_attr_info` function. It ensures that `in_subsets`,
  `out_subsets`, and `merged_subsets` are properly deallocated in all error exit paths,
  preventing resource leaks and their carry-over to subsequent operations.
primer_glossary:
- term: subset lists
  definition: Data structures holding parsed RISC-V ISA extensions relevant to linker
    attribute merging.
- term: error paths
  definition: Code execution pathways taken when an error condition is encountered.
- term: linker
  definition: The tool responsible for combining object files, in this case, `ld`
    from binutils.
- term: RISC-V
  definition: An open standard Instruction Set Architecture (ISA) based on Reduced
    Instruction Set Computing.
series_id: 'binutils:risc-v: release subset lists on all paths when the linker merges
  arch attributes'
series_role: reply
series_parts:
- title: 'RISC-V: Release subset lists on all paths when the linker merges arch attributes'
  url: https://inbox.sourceware.org/binutils/20260706114428.3967240-2-ycl669@andestech.com
  n: 1
  total: 2
url: https://inbox.sourceware.org/binutils/CAOvetVCPXtFsRmBLCdrEiEdpzYfVgp4v=f2N1JuB4OS47bDLfw@mail.gmail.com
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

Nelson Chu approves the first patch in Ethan Y. C. Liang's series, which addresses memory leaks in the RISC-V linker's architecture attribute merging function. The patch ensures that subset lists are properly released on all error paths, preventing memory leaks that could carry over to subsequent merges.
