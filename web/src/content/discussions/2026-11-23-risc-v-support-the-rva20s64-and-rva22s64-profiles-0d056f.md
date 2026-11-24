---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- architecture
- embedded
discussion_id: CA+yXCZC20WxjA1RpwBJYdid1AGqgXh2J-PKnocQ2E3ygOEyn=g@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Support the RVA20S64 and RVA22S64 profiles'
headline: 'RISC-V: Support the RVA20S64 and RVA22S64 profiles'
tldr: Patch to support RVA20S64 and RVA22S64 profiles in binutils' RISC-V support
  has been pushed.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Committed
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Kito Cheng <kito.cheng@gmail.com>
  role: maintainer
  position: Announces that the patch supporting RVA20S64 and RVA22S64 profiles for
    RISC-V has been pushed.
  quote: pushed :)
- author: Jiawei <jiawei@iscas.ac.cn>
  role: proposer
  position: Submitted the original patch to accept RVA20S64 and RVA22S64 profiles
    for RISC-V, including necessary supervisor ISA versions and extensions.
  quote: 'Accept rva20s64 and rva22s64 in -march [1, 2]. Include the required

    single supervisor ISA versions, Ss 1.11 and 1.12 respectively, and Zifencei

    in both profiles. RVA22S64 also requires Zihpm, Sscounterenw, Svpbmt

    and Svinval. Add readelf tests for the complete ISA attributes.'
primer_expert: This confirms the acceptance and merging of a patch that enhances binutils'
  support for RISC-V. Specifically, it adds the RVA20S64 and RVA22S64 profiles to
  the `-march` option. These profiles are defined by specific combinations of base
  ISA, supervisor extensions (like 'S' with versions 1.11/1.12), and other standard
  extensions (Zifencei, Zihpm, etc.). The patch also adds corresponding tests for
  `readelf` to verify these new profiles.
primer_glossary:
- term: RISC-V
  definition: An open-standard Instruction Set Architecture (ISA) based on reduced
    instruction set computer principles, designed for flexibility and extensibility.
- term: RVA20S64
  definition: A specific profile of the RISC-V architecture, indicating a 64-bit system
    intended for embedded applications, including supervisor-level features.
- term: RVA22S64
  definition: A specific profile of the RISC-V architecture, indicating a 64-bit system
    intended for embedded applications, including supervisor-level features, with
    a later revision than RVA20S64.
- term: profile
  definition: In the context of RISC-V, a predefined set of mandatory extensions and
    features that guarantee a certain level of functionality for specific application
    domains.
- term: supervisor ISA versions
  definition: Refers to specific versions of the supervisor-level instruction set
    for RISC-V, which manage operating system-level tasks and memory management.
- term: Zifencei
  definition: A standard RISC-V extension that provides fence instructions for memory
    ordering.
- term: readelf
  definition: A utility program that displays information about ELF (Executable and
    Linkable Format) files, including details about sections, symbols, and ISA attributes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZC20WxjA1RpwBJYdid1AGqgXh2J-PKnocQ2E3ygOEyn=g@mail.gmail.com
bugzilla_url: null
date: '2026-11-23'
is_stub: false
stub_reason: ''
---

Kito Cheng announces that the patch for adding support for the RISC-V RVA20S64 and RVA22S64 profiles has been accepted and pushed. These profiles include specific supervisor ISA versions (Ss 1.11 and 1.12 respectively) and extensions like Zifencei, Zihpm, Sscounterenw, Svpbmt, and Svinval, as defined in the RVA specifications. The change also includes adding `readelf` tests for these new attributes.
