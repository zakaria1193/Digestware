---
project: binutils
subsystem: binutils/testsuite
patch_id: null
tags: []
commit_hash: ae94fe0664f7801cdf0f485d7632186fa1859719
source_type: public_inbox
author: '"Maciej W. Rozycki" <macro@sourceware.org>'
headline: Exclude kfreebsd targets from STB_GNU_UNIQUE tests
tldr: Adds kfreebsd targets to the exclusion list for STB_GNU_UNIQUE symbol tests.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: Adds `*-*-kfreebsd*-gnu` to the `istarget` check in `supports_gnu_unique`
  within `binutils/testsuite/lib/binutils-common.exp`. This ensures that these targets,
  which share BFD vectors and ELFOSABI with FreeBSD targets, are correctly excluded
  from `STB_GNU_UNIQUE` symbol tests, fixing PR10549 and other visibility-related
  regressions.
primer_glossary:
- term: STB_GNU_UNIQUE
  definition: A symbol binding type in ELF, used for unique symbols that are resolved
    at runtime. It's primarily supported by GNU toolchains.
- term: ELFOSABI_FREEBSD
  definition: An Application Binary Interface (ABI) identifier indicating that the
    ELF object file adheres to the FreeBSD ABI.
- term: BFD vectors
  definition: Internal structures within the Binary File Descriptor (BFD) library
    that define how to handle specific object file formats and target architectures.
- term: PR10549
  definition: A specific bug report number in the Binutils project tracker, indicating
    a reported issue with linker settings and GNU OSABI for STB_GNU_UNIQUE symbols
    on kfreebsd targets.
discussion_id_link: public_inbox:binutils#10549
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260723185834.112874BA2E04@sourceware.org
date: '2026-07-23'
is_stub: false
stub_reason: ''
---

The test suite now excludes `*-*-kfreebsd*-gnu` targets from tests involving `STB_GNU_UNIQUE` symbols. This aligns them with `*-*-freebsd*` targets, which use the same BFD vectors and ELFOSABI, resolving multiple regressions related to symbol visibility and GNU OSABI handling.
