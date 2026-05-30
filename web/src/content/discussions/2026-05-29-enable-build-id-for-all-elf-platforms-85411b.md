---
project: binutils
subsystem: ld/testsuite
patch_id: null
tags:
- linker
- build-id
- ELF
- testsuite
discussion_id: 20260529133254.1429717-1-chigot@adacore.com
source_type: public_inbox
title: '[PATCH] ld/testsuite: enable build-id for ELF platforms'
headline: Enable --build-id for All ELF Platforms
tldr: The patch enables the --build-id option for all ELF platforms in the ld testsuite
  by removing target-specific restrictions.
proposer: Clément Chigot <chigot@adacore.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Enabling --build-id for all ELF platforms may expose issues on platforms where it
  was previously disabled.
- The patch assumes that all ELF targets support --build-id, which may not be the
  case.
exchanges:
- author: Clément Chigot
  role: proposer
  position: Removes target-specific restrictions in the ld testsuite, enabling the
    `--build-id` option for all ELF platforms.
  quote: '--build-id is defined within elf.em and thus should be available for

    all platforms matching "is_elf_format".'
- author: Clément Chigot
  role: other
  position: Asks how to trigger the test for all ELF emulations and states that they
    will adjust if some ELF targets don't support it.
  quote: 'I don''t know if there is a way to trigger this test for all ELF

    emulations ? `--enable-targets=all` doesn''t seem to be enough.

    Otherwise, I''ll adjust if some ELF targets don''t support it.'
primer_expert: This patch modifies the linker testsuite (`ld/testsuite`) to enable
  `--build-id` support for all ELF targets. The `build-id` is a unique identifier
  embedded in the linked binary, and the patch removes checks that limited its availability
  to specific architectures. The change relies on the fact that the `--build-id` functionality
  is defined in `elf.em`, which is common to all ELF targets.
primer_general: This patch enables a feature called `--build-id` for all ELF (Executable
  and Linkable Format) platforms in the Binutils linker.  A build-id is a unique identifier
  embedded in a compiled program, which can be useful for debugging and identifying
  the exact version of the code.  The patch removes restrictions that previously limited
  this feature to certain platforms, making it available more broadly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260529133254.1429717-1-chigot@adacore.com
bugzilla_url: null
date: '2026-05-29'
is_stub: false
---

This patch removes target-specific restrictions in the ld testsuite, enabling the `--build-id` option for all ELF platforms. The `--build-id` option is defined within `elf.em` and should be available for all platforms matching `is_elf_format`.
