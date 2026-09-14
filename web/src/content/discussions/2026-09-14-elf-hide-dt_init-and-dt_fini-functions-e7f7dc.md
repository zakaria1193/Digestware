---
project: binutils
subsystem: elf
patch_id: null
tags:
- ELF
- binutils
- linker
- dynamic linking
- patch
discussion_id: CAN30aBFtFc6dNL3k_-u25hgygYXj4S9fudLsJT6nF=7umz9HrA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] elf: Hide DT_INIT and DT_FINI functions'
headline: 'elf: Hide DT_INIT and DT_FINI functions'
tldr: Discussion regarding a patch to hide DT_INIT and DT_FINI functions in ELF binaries.
proposer: Fangrui Song <i@maskray.me>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Hiding initialization/finalization functions might improve security by obscuring
  critical code paths, but could break existing tools or assumptions that rely on
  these functions being visible.
- Modifying ELF structures requires careful consideration of ABI compatibility and
  potential impacts on different operating systems and architectures.
- The decision to hide these functions involves balancing potential security benefits
  against compatibility concerns and the complexity of dynamic linker behavior.
exchanges:
- author: Fangrui Song <i@maskray.me>
  role: contributor
  position: Replies to a lengthy thread concerning a patch to hide DT_INIT and DT_FINI
    functions in ELF binaries.
  quote: 'On Fri, Sep 11, 2026 at 9:34 PM Matt Rice <ratmice@gmail.com> wrote:

    > ...'
- author: Matt Rice <ratmice@gmail.com>
  role: contributor
  position: Engaged in the discussion about hiding ELF DT_INIT and DT_FINI functions,
    with multiple prior messages in the thread.
  quote: 'On Fri, Sep 11, 2026 at 7:47 PM H.J. Lu <hjl.tools@gmail.com> wrote:

    > ...'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Participates in the ongoing debate about hiding DT_INIT and DT_FINI functions
    in ELF binaries.
  quote: 'On Sat, Sep 12, 2026 at 10:12 AM Matt Rice <ratmice@gmail.com> wrote:

    > ...'
- author: Jan Beulich <jbeulich@suse.com>
  role: contributor
  position: Contributes to the discussion on a patch affecting DT_INIT and DT_FINI
    visibility in ELF files.
  quote: 'On 11.09.2026 14:04, H.J. Lu wrote:

    > ...'
primer_expert: This thread concerns a patch affecting ELF dynamic linking, specifically
  related to the `DT_INIT` and `DT_FINI` entries in the `.dynamic` section. These
  entries typically point to initialization and finalization functions, respectively,
  which are executed by the dynamic linker. The patch aims to 'hide' these functions,
  likely by modifying how the dynamic linker processes them, potentially for security
  or operational reasons. The extensive quoting suggests a detailed, multi-party discussion
  on the correctness and impact of this change on ELF binary loading and execution.
primer_glossary:
- term: ELF
  definition: Executable and Linkable Format. A common standard file format for executable
    files, object code, shared libraries, and core dumps, primarily used on Unix-like
    systems.
- term: DT_INIT
  definition: A dynamic section tag in ELF that indicates the address of a function
    to be executed when a shared object is loaded.
- term: DT_FINI
  definition: A dynamic section tag in ELF that indicates the address of a function
    to be executed when a shared object is unloaded.
- term: Dynamic linker
  definition: A program that runs when a program is executed. It loads shared libraries
    into memory and resolves symbols (e.g., function calls) between the executable
    and the libraries.
- term: Shared object
  definition: A file that contains code and data that can be used by multiple programs
    simultaneously. Also known as a shared library or dynamic library.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAN30aBFtFc6dNL3k_-u25hgygYXj4S9fudLsJT6nF=7umz9HrA@mail.gmail.com
bugzilla_url: null
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

This discussion revolves around a patch intended to hide the `DT_INIT` and `DT_FINI` functions within ELF binaries. The conversation appears to be a long-running thread with multiple participants weighing in on the implications and correctness of the proposed change. The core technical aspect involves manipulating ELF dynamic section tags to control the visibility or behavior of initialization and finalization functions.
