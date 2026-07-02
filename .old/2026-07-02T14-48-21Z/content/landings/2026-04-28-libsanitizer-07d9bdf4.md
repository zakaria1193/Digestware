---
project: gcc
subsystem: libsanitizer
patch_id: null
tags:
- libsanitizer
- risc-v
- hwasan
- memory safety
commit_hash: 07d9bdf429825cc49b241ea81f9a48aac6281dd3
source_type: github
author: Maximilian Ciric
headline: 'Libsanitizer: RISC-V now supports HWASAN.'
tldr: Enables building libsanitizer with HWASAN support for RISC-V targets.
impact_score: 7
performance_win: true
breaking_change: false
outcome: committed
primer_expert: 'This commit modifies `configure.tgt` to enable HWASAN support for
  the RISC-V target. HWASAN is a memory error detector that uses hardware tagging
  to improve performance. Search terms: libsanitizer HWASAN RISC-V.'
primer_general: 'AddressSanitizer (ASan) is a fast memory error detector. HWASAN is
  a variant that uses hardware memory tagging to reduce the performance overhead.
  This commit enables HWASAN for RISC-V, a modern open-source processor architecture.
  This allows developers to more easily find memory errors in their RISC-V code. Search
  terms: libsanitizer HWASAN RISC-V.'
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:libsanitizer: risc-v supports hwasan'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/07d9bdf429825cc49b241ea81f9a48aac6281dd3
date: '2026-04-28'
---

This commit enables Hardware-assisted AddressSanitizer (HWASAN) support for RISC-V targets in libsanitizer.  With both libsanitizer and the RISC-V backend now supporting HWASAN, this change allows building libsanitizer with HWASAN enabled for RISC-V.
