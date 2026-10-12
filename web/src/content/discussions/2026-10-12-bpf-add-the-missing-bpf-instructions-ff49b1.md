---
project: binutils
subsystem: bpf
patch_id: null
tags:
- BPF
- assembler
- GCC
- kernel
discussion_id: 91241ad8-cf54-4162-9746-6a402328f469@linux.dev
source_type: public_inbox
title: 'Re: [PATCH v3 0/6] bpf: add the missing BPF instructions'
headline: 'bpf: add the missing BPF instructions'
tldr: Series of patches adding missing BPF instructions to gas, enabling GCC support.
proposer: Vineet Gupta <vineet.gupta@linux.dev>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Completes support for newer BPF instructions, enabling GCC.
- Requires changes across assembler configuration, documentation, and test suites.
exchanges:
- author: Vineet Gupta <vineet.gupta@linux.dev>
  role: proposer
  position: Submits a series of patches to add missing BPF instructions to gas, explaining
    the need and summarizing the changes in v3.
  quote: 'gas lacks BPF instructions that clang emits (and the kernel accepts).

    This showed up recently with callx and gotol support. So instead of

    playing whack-a-mole address all the current gaps so GCC side can

    proceed.'
primer_expert: This series of six patches addresses gaps in `gas`'s BPF instruction
  support, specifically for instructions used by `clang` and the Linux kernel that
  `GCC` also needs to support. Patches include `addr_space_cast` (for arenas), `load-acquire`/`store-release`,
  `gotox` (indirect jump), and `r11` as a stack argument register. The changes are
  primarily in `gas/config/tc-bpf.c` and `gas/doc/c-bpf.texi`, with accompanying test
  cases, and are designed to align `gas` with newer BPF features.
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter, a technology that allows programs to be run
    in the Linux kernel without altering kernel source code. It's often used for network
    packet filtering and more general in-kernel computation.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project, responsible for
    converting assembly language code into machine code.
- term: addr_space_cast
  definition: A BPF instruction used to cast between different address spaces, specifically
    generic and arena address spaces.
- term: ISA
  definition: Instruction Set Architecture, the set of commands a CPU understands.
series_id: 'binutils:bpf: add the missing bpf instructions'
series_role: cover
series_parts:
- title: 'bpf: add the missing BPF instructions'
  url: https://inbox.sourceware.org/binutils/20261012081159.2015930-1-vineet.gupta@linux.dev
  n: 0
  total: 6
url: https://inbox.sourceware.org/binutils/91241ad8-cf54-4162-9746-6a402328f469@linux.dev
bugzilla_url: null
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

This is the cover letter for a series of patches aimed at adding several missing BPF instructions to the GNU Assembler (gas). These instructions, such as `addr_space_cast`, `load-acquire`/`store-release`, `gotox`, and `r11` as a stack argument register, are emitted by `clang` and accepted by the kernel, but were not supported by `gas`. Adding them is crucial for enabling GCC to generate code for these features. The series has been updated to v3, incorporating feedback and adding new patches.
