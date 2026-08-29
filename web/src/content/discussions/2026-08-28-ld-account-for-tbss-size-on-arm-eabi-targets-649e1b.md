---
project: binutils
subsystem: binutils
patch_id: null
tags:
- linker
- binutils
- ARM
- TLS
- bare-metal
discussion_id: 20260818093446.3434913-1-torbjorn.svensson@foss.st.com
source_type: public_inbox
title: '[PING]: [PATCH] ld: Account for .tbss size on ARM EABI targets'
headline: 'ld: Account for .tbss size on ARM EABI targets'
tldr: A patch to the GNU linker (ld) ensures correct accounting for .tbss section
  size on ARM EABI targets, aligning behavior with LLVM's lld.
proposer: Torbjorn SVENSSON <torbjorn.svensson@foss.st.com>
consensus: Under Review
outcome: under_review
impact_score: 6
sentiment_score: 5
technical_tradeoffs:
- Aligns binutils behavior with LLVM lld for consistency.
- Introduces a new linker configuration option (`tls_nobits_occupies_vma`).
exchanges:
- author: Torbjorn SVENSSON
  role: proposer
  position: Pings for review of a patch that ensures .tbss size is accounted for on
    ARM EABI targets.
  quote: Gentle ping! :)
- author: Torbjorn SVENSSON
  role: proposer
  position: Submits a patch to correctly handle .tbss section size on ARM EABI targets,
    aligning with LLVM lld.
  quote: 'Bare-metal ARM EABI programs allocate TLS storage directly, so if .tdata

    consumses VMA, then .tbss must also do so.  Otherwise, a following

    section such as .bss can overlap it.


    Keep the existing behavior for non-EABI targets, and add tests for

    static, executable, PIE, and dynamic links.


    This change aligns with LLVM lld behavior for .tbss.'
- author: Alan Modra
  role: reviewer
  position: Questions the patch's premise, implying it might be addressing a problem
    in the loader rather than the linker itself, and asks why the linker should be
    altered.
  quote: 'In other words, the loader is broken for TLS.  Why break the linker as

    well?'
- author: Torbjorn SVENSSON
  role: proposer
  position: Clarifies that the context is bare-metal execution where no loader is
    involved, and the issue pertains to the linker's behavior.
  quote: 'What loader?

    I''m taking about bare-metal, i.e. there is nothing doing any loading.

    The CPU is executing straight'
primer_expert: This patch addresses an issue in the GNU linker (`ld`) concerning Thread-Local
  Storage (TLS) on ARM EABI targets, specifically for bare-metal environments. The
  problem arises because the `.tbss` section (uninitialized TLS data) needs to occupy
  virtual memory space if the `.tdata` section (initialized TLS data) does, to prevent
  subsequent sections like `.bss` from overlapping. The proposed solution adds a new
  build-time property `tls_nobits_occupies_vma` to `ld.h` and conditionally enables
  this behavior for ARM EABI targets in `armelf.em`, aligning with LLVM's `lld` behavior.
  It also includes…
primer_glossary:
- term: .tbss
  definition: A section in an executable file that typically contains uninitialized
    Thread-Local Storage (TLS) data. Its size is accounted for but it does not occupy
    memory in the final image.
- term: ARM EABI
  definition: The Application Binary Interface for the ARM architecture, defining
    conventions for program execution, data representation, and system calls.
- term: TLS
  definition: Thread-Local Storage. A mechanism that provides data that is local to
    a thread. Each thread in a process gets its own copy of the data.
- term: VMA
  definition: Virtual Memory Address. The address of a location in a computer's virtual
    memory space.
- term: bare-metal
  definition: Refers to running code directly on hardware without an underlying operating
    system or loader, typically in embedded systems or low-level development.
- term: LLVM lld
  definition: A fast, new linker from the LLVM project, designed to be a modern replacement
    for existing linkers.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/8e3a4f2f-26ff-470d-b676-2b9eca4cd83f@foss.st.com
bugzilla_url: null
date: '2026-08-28'
is_stub: false
stub_reason: ''
---

Torbjörn Svensson is pinging for feedback on a patch that addresses how the GNU linker accounts for the size of the .tbss section on ARM EABI targets. The patch ensures that .tbss occupies virtual memory address space if .tdata does, preventing potential overlaps with subsequent sections like .bss. This change aims to align binutils behavior with LLVM's lld and includes new test cases for various linking scenarios.
