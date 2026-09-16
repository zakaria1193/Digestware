---
project: binutils
subsystem: elf
patch_id: null
tags:
- binutils
- elf
- dynamic-linking
- linker
- visibility
discussion_id: CACTLOFqnRUxBbtTgNTgx_8U4ejjUaSZ6LEyRtpqx0fd-JnUu7Q@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] elf: Hide DT_INIT and DT_FINI functions'
headline: 'elf: Hide DT_INIT and DT_FINI functions'
tldr: Discussion continues regarding hiding DT_INIT/DT_FINI functions in ELF binaries.
proposer: Matt Rice <ratmice@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Potentially improves security or robustness by hiding internal initialization/finalization
  functions.
- Risk of breaking dynamic linking if not implemented carefully.
- Requires careful consideration of symbol visibility and ELF structure.
exchanges:
- author: Matt Rice <ratmice@gmail.com>
  role: proposer
  position: Engaged in the ongoing discussion about hiding DT_INIT and DT_FINI functions.
  quote: 'On Sun, Sep 13, 2026 at 5:03 PM Fangrui Song <i@maskray.me> wrote:

    >

    > On Fri, Sep 11, 2026 at 9:34 PM Matt Rice <ratmice@gmail.com> wrote:

    > >

    > > On Fri, Sep 11, 2026 at 7:47 PM H.J. Lu <hjl.tools@gmail.com> wrote:

    > > >

    > > > On Sat, Sep 12, 2026 at 10:12 AM Matt Rice <ratmice@gmail.com> wrote:

    > > > >'
primer_expert: This discussion concerns the ELF dynamic linking mechanism, specifically
  the handling of `DT_INIT` and `DT_FINI` entries in the dynamic section (`.dynamic`).
  These entries point to functions that are executed upon dynamic library loading
  (`DT_INIT`) and unloading (`DT_FINI`). The patch aims to hide these functions, likely
  by marking them as local or otherwise reducing their visibility, to prevent unintended
  calls or symbol resolution issues. The complex threading of replies suggests active
  debate over the correct approach and potential side effects on dynamic linking behavior.
primer_glossary:
- term: ELF
  definition: Executable and Linkable Format. A standard file format for executables,
    object code, shared libraries, and core dumps on Unix-like systems.
- term: DT_INIT
  definition: A tag in the ELF dynamic section (`.dynamic`) that specifies the address
    of the initialization function for a shared library. This function is executed
    when the library is loaded.
- term: DT_FINI
  definition: A tag in the ELF dynamic section (`.dynamic`) that specifies the address
    of the finalization function for a shared library. This function is executed when
    the library is unloaded.
- term: dynamic linking
  definition: A process where executable files are linked against shared libraries
    at runtime, rather than at compile time. This allows multiple programs to share
    code and data from a single library.
- term: shared library
  definition: A library whose code can be shared by multiple executable programs simultaneously.
    Also known as a dynamic library.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CACTLOFqnRUxBbtTgNTgx_8U4ejjUaSZ6LEyRtpqx0fd-JnUu7Q@mail.gmail.com
bugzilla_url: null
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

This thread is a continuation of a discussion about hiding `DT_INIT` and `DT_FINI` functions in ELF binaries. The participants are actively debating the implications and correct implementation of such a change, with multiple nested replies indicating a thorough review process. The core issue appears to revolve around ensuring that these initialization and finalization functions are properly managed and possibly hidden from certain visibility contexts without breaking dynamic linking or program startup.
