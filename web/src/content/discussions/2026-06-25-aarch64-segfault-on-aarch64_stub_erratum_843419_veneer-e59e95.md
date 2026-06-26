---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- linker
- bugfix
- errata
discussion_id: aj29SHF5KAEEtbR1@squeak.grove.modra.org
source_type: public_inbox
title: 'aarch64: segv on aarch64_stub_erratum_843419_veneer'
headline: 'Aarch64: Segfault on aarch64_stub_erratum_843419_veneer'
tldr: A patch is proposed to fix a segmentation fault in the AArch64 linker when handling
  specific erratum stubs by adding a check for NULL stub sections.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Fixes a segmentation fault, improving linker stability for AArch64 erratum handling.
- Ensures consistent handling of erratum stubs across linker phases.
- Reduces potential for undefined behavior in BFD stub generation.
exchanges: []
primer_expert: This discussion concerns a bug in the AArch64 BFD (Binary File Descriptor)
  library, specifically within the linker's stub generation for handling processor
  errata. The `aarch64_stub_erratum_843419_veneer` relates to a known hardware bug
  (erratum 843419) that requires specific code sequences (stubs) to work around. The
  segfault occurs in `aarch64_build_one_stub` because certain erratum stubs, generated
  by `_bfd_aarch64_add_stub_entry_after`, lack an associated `stub_sec` (stub section),
  leading to a `NULL` pointer dereference. The fix ensures `aarch64_build_one_stub`
  does not attempt to proces…
primer_general: When a computer program is compiled, it's turned into machine code
  that the processor can understand. Sometimes, processors have tiny bugs, called
  'errata,' that need special workarounds in the software. The linker, part of the
  Binutils toolchain, is responsible for combining different pieces of compiled code
  and sometimes inserts these workarounds, called 'stubs.' This discussion is about
  a bug in the AArch64 linker where it crashes (a 'segmentation fault') when trying
  to create these workarounds for a specific processor bug. The crash happens because
  the linker tries to use information about a part of the stub that doesn't exist,
  leading to an error. The proposed fix adds a check to prevent the linker from trying
  to access this missing information, preventing the crash.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aj29SHF5KAEEtbR1@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-25'
is_stub: false
stub_reason: ''
---

This patch addresses a segmentation fault in the AArch64 linker (`ld`) when processing specific erratum stubs, particularly `aarch64_stub_erratum_843419_veneer`. The fault occurs because `aarch64_build_one_stub` attempts to dereference a `NULL` stub section (`stub_sec`), which can happen when `_bfd_aarch64_add_stub_entry_after` creates stub entries for certain errata without an associated section. The proposed solution introduces a check to prevent processing stubs with a `NULL` `stub_sec` in `aarch64_build_one_stub` and aligns this check with existing logic in `aarch64_size_one_stub`.
