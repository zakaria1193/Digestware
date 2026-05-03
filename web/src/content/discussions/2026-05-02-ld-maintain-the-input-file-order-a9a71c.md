---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- ld
- linker
- LTO
- linker script
discussion_id: CAMe9rOou0Nsz12kg-9ToWVsuO7KcsuLh3ce5X_bHP9=Og-sVRg@mail.gmail.com
source_type: public_inbox
title: '[2.46 PATCH]: ld: Maintain the input file order'
headline: 'Ld: Maintain the input file order.'
tldr: This patch backports a fix to binutils 2.46 to maintain the correct input file
  order during linking with LTO, especially when using linker scripts.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Backporting the patch ensures stability for the 2.46 release, but it may introduce
  unforeseen regressions.
- The fix is limited to Linux/x86-64 and Linux/aarch64 due to test dependencies.
- The patch might increase the complexity of the linker code.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Proposes backporting a fix (PR ld/34088) to the binutils 2.46 branch which
    maintains the input file order during linking, especially with LTO and linker
    scripts.
  quote: OK to backport the PR ld/34088 fix to 2.46 branch?
primer_expert: The binutils linker (`ld`) processes input files in a specific order
  to resolve symbols. When LTO is enabled, the linker may re-scan archive files, potentially
  altering the final input order. This patch addresses a scenario where files included
  via linker scripts (using `GROUP`) are reordered during LTO, leading to incorrect
  symbol resolution. The issue is triggered because compiler builtin functions are
  not added to the LTO symbol table, and ld extracts archive elements during LTO rescan.
primer_general: The linker (`ld`) is a crucial part of the toolchain that combines
  compiled object files and libraries into an executable program.  Link-Time Optimization
  (LTO) is a compilation strategy that optimizes the entire program at link time,
  potentially improving performance.  Linker scripts provide fine-grained control
  over the linking process, including specifying the order of input files and libraries.
  Maintaining the correct input order is essential for resolving symbol dependencies
  and ensuring that the program behaves as expected; reordering can lead to unexpected
  errors or incorrect program behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMe9rOou0Nsz12kg-9ToWVsuO7KcsuLh3ce5X_bHP9=Og-sVRg@mail.gmail.com
bugzilla_url: null
date: '2026-05-02'
---

This patch backports a fix from the master branch to the binutils 2.46 branch to address an issue where the linker (`ld`) reorders input files when linking with Link-Time Optimization (LTO) and linker scripts. Specifically, when libraries are included via the `GROUP` command in a linker script (e.g., `-lm` pulling in `/usr/lib64/libm.a`), the order of archive members can be changed during LTO rescan.  This is important for maintaining the correct symbol resolution order and preventing unexpected linking errors.
