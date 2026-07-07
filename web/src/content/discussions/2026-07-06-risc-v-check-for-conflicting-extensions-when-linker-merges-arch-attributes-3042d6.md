---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- linker
- architecture
- memory leak
- conflict detection
discussion_id: 20260706114428.3967240-1-ycl669@andestech.com
source_type: public_inbox
title: '[PATCH 0/2] RISC-V: Check for conflicting extensions when the linker merges
  arch attributes'
headline: 'RISC-V: Check for conflicting extensions when linker merges arch attributes'
tldr: Ethan Liang proposes a two-part patch series to fix memory leaks and add checks
  for conflicting RISC-V extensions during linker arch attribute merges.
proposer: '"Ethan Y. C. Liang" <ycl669@andestech.com>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: '"Ethan Y. C. Liang" <ycl669@andestech.com>'
  role: proposer
  position: Submits a two-patch series to fix memory leaks and add conflict checking
    for RISC-V architecture attributes during linking.
  quote: 'Patch 1 is preparatory: riscv_merge_arch_attr_info leaked the subset

    lists on its error paths, and the new error path added by patch 2

    would make this worse, so route all error paths through a single

    cleanup exit first.


    Patch 2 adds the check: after merging the input archs, re-derive the

    implicit extensions on the merged arch and run the conflict checks on

    it, rejecting the merge if any conflict…'
- author: Nelson Chu <nelson.chu@sifive.com>
  role: reviewer
  position: Approves the first patch, noting that it looks okay.
  quote: null
primer_expert: 'This series introduces two changes to `bfd/elfxx-riscv.c`. Patch 1
  fixes memory leaks in `riscv_merge_arch_attr_info` by ensuring subset lists are
  cleaned up on all error paths. Patch 2 adds a new check within the same function:
  after merging RISC-V ISA strings from multiple object files, it re-parses the merged
  string to detect and reject conflicting implicit extensions, a behavior previously
  not enforced by the linker.'
primer_glossary:
- term: arch attributes
  definition: Attributes that specify the processor architecture and supported instruction
    set extensions, such as `Tag_RISCV_arch` in ELF files.
- term: linker
  definition: A program that combines object files and libraries into an executable.
    In this context, it's `ld` within binutils.
- term: RISC-V ISA string
  definition: A string defining the RISC-V instruction set extensions, e.g., 'rv32ic'
    or 'rv64imafdc_zifencei'.
- term: implicit extensions
  definition: Instruction set extensions that are implied by the presence of other
    extensions (e.g., 'zcd' might be implied by 'c' and 'd' extensions).
- term: error paths
  definition: Branches of code execution that handle erroneous conditions or failures.
- term: subset lists
  definition: Data structures used to manage parsed RISC-V ISA extensions.
series_id: 'binutils:risc-v: check for conflicting extensions when the linker merges
  arch attributes'
series_role: cover
series_parts:
- title: 'RISC-V: Check for conflicting extensions when the linker merges arch attributes'
  url: https://inbox.sourceware.org/binutils/akxe1X8wwdItOqQj@atctlc04
  n: 2
  total: 2
- title: 'RISC-V: Check for conflicting extensions when the linker merges arch attributes'
  url: https://inbox.sourceware.org/binutils/CAOvetVBXAbVe47w3wjOe7N8OGw=8yOzPYyDN+uyLKVnNPe5wFw@mail.gmail.com
  n: 2
  total: 2
- title: 'RISC-V: Check for conflicting extensions when the linker merges arch attributes'
  url: https://inbox.sourceware.org/binutils/CAOvetVD7==e2hm3CwR31yRKWTjTMCWDAu8cxKz08g8G2pAMEfw@mail.gmail.com
  n: 2
  total: 2
- title: 'RISC-V: Check for conflicting extensions when the linker merges arch attributes'
  url: https://inbox.sourceware.org/binutils/CAOvetVBT=ZA_8Zg4cd1k1X_TDqzgvEL5uFrJnOD2NKT3r8Z0YQ@mail.gmail.com
  n: 2
  total: 2
- title: 'RISC-V: Check for conflicting extensions when the linker merges arch attributes'
  url: https://inbox.sourceware.org/binutils/6ec74d05-50c8-4427-9fcd-e26c1cedf246@iscas.ac.cn
  n: 2
  total: 2
- title: 'RISC-V: Check for conflicting extensions when the linker merges arch attributes'
  url: https://inbox.sourceware.org/binutils/20260706114428.3967240-3-ycl669@andestech.com
  n: 2
  total: 2
url: https://inbox.sourceware.org/binutils/20260706114428.3967240-1-ycl669@andestech.com
bugzilla_url: null
date: '2026-07-06'
is_stub: false
stub_reason: ''
---

Ethan Y. C. Liang introduces a two-patch series to address issues in the RISC-V linker's handling of architecture attributes. The first patch cleans up memory leaks in error paths of `riscv_merge_arch_attr_info`. The second patch implements a crucial check: after merging input architecture strings, it re-evaluates the implicit extensions and verifies for conflicts, preventing silent failures like merging 'rv32ic' with 'rv32id_zcmp' which implies 'zcd' that conflicts with 'zcmp'. The series also includes new test cases.
