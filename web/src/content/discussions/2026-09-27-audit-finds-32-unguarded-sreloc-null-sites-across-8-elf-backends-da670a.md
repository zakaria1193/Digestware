---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- bugfix
- linker
- ELF
discussion_id: CAMAZx65XphgK7c=i-CTcm-q047VLtHHBH-zfD3pGZyoNzmUbHQ@mail.gmail.com
source_type: public_inbox
title: '[binutils] Companion audit for 0a84e560216 / PR ld/34448: 32 unguarded sreloc-NULL
  sites across 8 backends'
headline: Audit finds 32 unguarded sreloc-NULL sites across 8 ELF backends
tldr: An audit identified 32 potential NULL pointer dereferences related to 'sreloc'
  across multiple ELF backends in binutils, requiring NULL checks similar to a rec…
proposer: Brandon Barrante <aetherai@aethersystems.net>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Adds defensive checks to prevent crashes, potentially with a minor performance overhead.
- Requires careful adaptation of the fix to local control flow at each site.
exchanges: []
primer_expert: This discussion details a security audit following a fix for PR ld/34448.
  The audit identified numerous instances in various ELF backends (x86, arm, ppc,
  s390, riscv, aarch64, tilepro) where `elf_section_data(...)->sreloc` is accessed
  without checking if `sreloc` is NULL. This condition can arise if `elf_link_read_relocs_from_section`
  aborts due to a bad relocation, and subsequent code expects the dynamic relocation
  section to exist. The proposed solution involves generalizing the fix from commit
  0a84e560216 by adding appropriate NULL checks tailored to the control flow at each
  site.
primer_glossary:
- term: sreloc
  definition: Likely refers to 'static relocation' or 'symbol relocation', a data
    structure used during linking to record information about symbol references and
    their memory addresses.
- term: ELF backends
  definition: Specific code within the binutils linker that handles the ELF (Executable
    and Linkable Format) object file format for different processor architectures
    (e.g., x86, ARM, RISC-V).
- term: NULL pointer dereference
  definition: An error that occurs when a program attempts to access memory through
    a pointer that is NULL (points to nothing), often leading to a crash.
- term: dynamic relocation section
  definition: A section within an object file or executable that contains information
    needed to resolve symbol references at runtime. This is crucial for dynamically
    linked executables.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAMAZx65XphgK7c=i-CTcm-q047VLtHHBH-zfD3pGZyoNzmUbHQ@mail.gmail.com
bugzilla_url: null
date: '2026-09-27'
is_stub: false
stub_reason: ''
---

Following a fix for PR ld/34448, an audit has uncovered 32 additional sites across 8 ELF backends in binutils where 'sreloc' is dereferenced without a preceding NULL check. These sites share the same vulnerability as the one already fixed: the linker may skip dynamic relocation section creation upon encountering a relocation error, leading to a NULL pointer dereference if code assumes the section exists. The proposed solution involves adding local NULL checks at each identified site.
