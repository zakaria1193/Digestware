---
project: glibc
subsystem: elf
patch_id: null
tags:
- glibc
- elf
- thp
- loader
- memory management
discussion_id: CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
source_type: public_inbox
title: '[PATCH v4] elf: Support THP segment load with madvise enabled THP'
headline: 'elf: Support THP segment load with madvise enabled THP'
tldr: This patch modifies glibc's ELF loader to properly handle THP when THP is enabled
  with madvise in the kernel.
stakes: Improves performance for applications using THP by ensuring correct segment
  alignment and madvise calls, especially when THP is enabled with madvise.
proposer: H.J. Lu <hjl.tools@gmail.com>
consensus: Under Review
outcome: proposed
sentiment_score: 7
sentiment_rationale: The patch has been through several revisions and has been acknowledged.
  No negative feedback is apparent.
technical_tradeoffs:
- Increased complexity in the ELF loader.
- Potential for regressions if alignment is not handled correctly.
- Dependence on kernel configuration (THP enabled with madvise).
- Possible performance regressions if madvise calls introduce overhead.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Proposes a patch to support THP segment loading when THP is enabled with
    madvise, involving changes to segment alignment and calls to `madvise`.
  quote: 'If THP is enabled with madvise in the

    kernel, to enable THP segment load in an application, madvise should

    be called with MADV_HUGEPAGE on all THP eligible PT_LOAD segments'
- author: Carlos O'Donell <carlos@redhat.com>
  role: reviewer
  position: Acknowledged the patch and quoted the changes from previous versions.
  quote: "On 4/18/26 11:15 PM, H.J. Lu wrote:\n> Changes from v3:\n> \n> 1. Fold the\
    \ -z separate-code linker option check.\n> 2. Move DL_MAP_DEFAULT_THP_PAGESIZE\
    \ to <hugepages.h>\n> and default it to 0.\n> 3. Don't run strace tests for cross-compiling.\n\
    > 4. Remove return after FAIL_UNSUPPORTED in THP test."
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Quoted Carlos O'Donell's acknowledgement of the patch.
  quote: 'On Mon, Apr 20, 2026 at 9:15 PM Carlos O''Donell <carlos@redhat.com> wrote:

    >

    > On 4/18/26 11:15 PM, H.J. Lu wrote:

    > > Changes from v3:'
primer_expert: This patch focuses on glibc's ELF loader (`_dl_map_segment_align`,
  `_dl_executable_postprocess`, `_dl_postprocess_loadcmd_extra`) to ensure proper
  alignment and `madvise` calls for THP-eligible PT_LOAD segments when THP is enabled
  with `madvise` in the kernel. It addresses issues related to dynamic and static
  executables, as well as shared objects. The patch introduces `DL_MAP_DEFAULT_THP_PAGESIZE`
  in `hugepages.h`.
primer_general: This patch addresses how glibc, the standard C library, loads programs
  and shared libraries into memory. It specifically deals with Transparent Huge Pages
  (THP), a kernel feature that uses larger memory pages for performance gains. When
  THP is enabled in 'madvise' mode, applications must explicitly request THP for specific
  memory regions. This patch ensures that glibc correctly aligns memory segments and
  requests THP when loading programs and libraries, potentially improving performance.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/CAMe9rOqKfFXMDY07GRuppudP3V9fsCDXoyxDesPMNQLDrRhzvg@mail.gmail.com
bugzilla_url: null
date: '2026-04-19'
---

H.J. Lu proposes a patch to enable THP segment load when THP is enabled with madvise in the kernel. The patch updates segment alignment, calls `madvise` with `MADV_HUGEPAGE` on THP-eligible segments, and adds tests to verify correct alignment. Carlos O'Donell acknowledged the patch.
