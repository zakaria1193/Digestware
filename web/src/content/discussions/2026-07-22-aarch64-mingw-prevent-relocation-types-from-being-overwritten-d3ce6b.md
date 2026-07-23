---
project: binutils
subsystem: aarch64
patch_id: null
tags:
- binutils
- aarch64
- mingw
- linker
- relocations
discussion_id: 20260722110400.62027-1-evgeny.karpov@arm.com
source_type: public_inbox
title: '[PATCH v3 0/1] aarch64: mingw: Prevent relocation types from being overwritten'
headline: 'aarch64: mingw: Prevent relocation types from being overwritten'
tldr: Binutils patch changes how relocation types are handled for aarch64 targets
  to avoid overwriting and breaking other relocation logic.
proposer: Evgeny Karpov <evgeny.karpov@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 6
technical_tradeoffs:
- Using a magic value (-1) for r_vaddr may be fragile if that value becomes valid.
- The change aims to provide a cleaner solution than overwriting relocation types,
  but requires discussion on its robustness.
exchanges:
- author: Evgeny Karpov <evgeny.karpov@arm.com>
  role: proposer
  position: Proposes to replace the use of rel->r_type = IMAGE_REL_ARM64_ABSOLUTE
    with rel->r_vaddr = -1 to avoid impacting other relocation logic.
  quote: 'However, it impacts another relocation logic, as the initial relocation
    type

    is no longer known.

    To avoid extra processing, rel->r_type = IMAGE_REL_ARM64_ABSOLUTE has been

    replaced with rel->r_vaddr = -1, and a condition to skip relocation processing

    has been added to _bfd_coff_generic_relocate_section.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Expresses reservations about using a specific value like -1 as a flag,
    questioning if it's strictly excluded by the specification.
  quote: 'I have to admit that I have reservations against such a(n) (ab)use of a

    particular value. Yes, -1 may be very unlikely to occur in this field, but is
    it excluded by the spec?'
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Questions the necessity of the change and asks for clarification on what
    exactly goes wrong with the current code before committing.
  quote: Firstly, is it really necessary? What exactly goes wrong with the current
    code?
primer_expert: This patch touches `coff-aarch64.c` and `cofflink.c` within GNU Binutils.
  It addresses how linker relocations are processed for the aarch64 Windows (mingw)
  target. Specifically, it modifies the handling of `IMAGE_REL_ARM64_PAGEBASE_REL21`
  and related logic by using a magic value (`-1`) in `r_vaddr` to signal that a relocation
  should be skipped, avoiding issues caused by the previous method of overwriting
  `r_type`.
primer_glossary:
- term: Relocation
  definition: A modification applied to code or data by the linker to resolve symbol
    references. It ensures that addresses and references are correct in the final
    executable or shared library.
- term: aarch64
  definition: The 64-bit ARM architecture, commonly used in mobile devices and increasingly
    in servers and desktops.
- term: mingw
  definition: Minimalist GNU for Windows, a development environment that provides
    a Windows port of the GNU Compiler Collection (GCC) and related tools, enabling
    compilation of native Windows applications.
- term: IMAGE_REL_ARM64_ABSOLUTE
  definition: A specific relocation type used for the ARM64 architecture in the PE/COFF
    object file format, indicating an absolute address.
- term: r_vaddr
  definition: In COFF relocation entries, this field typically stores a virtual address
    related to the relocation.
- term: cofflink.c
  definition: A source file within binutils that handles the linking process for COFF
    (Common Object File Format) binaries.
series_id: 'binutils:aarch64: mingw: prevent relocation types from being overwritten'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/20260722110400.62027-1-evgeny.karpov@arm.com
bugzilla_url: null
date: '2026-07-22'
is_stub: false
stub_reason: ''
---

This patch series for binutils addresses an issue with relocation types on aarch64 targets using the mingw toolchain. The original approach of setting relocation types to IMAGE_REL_ARM64_ABSOLUTE to bypass certain processing has been found to interfere with other relocation logic. The proposed solution replaces this with a less invasive method of marking the relocation for skipping, aiming to preserve the initial relocation type.
