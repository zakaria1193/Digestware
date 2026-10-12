---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- BPF
- assembler
- kernel
discussion_id: 878q43m8x5.fsf@gnu.org
source_type: public_inbox
title: 'Re: [PATCH v3 6/6] gas: bpf: accept r11, the stack argument register'
headline: 'gas: bpf: accept r11, the stack argument register'
tldr: The `gas` assembler now accepts `r11` as a register for BPF stack arguments.
proposer: '"Jose E. Marchesi" <jemarch@gnu.org>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables `gas` to support newer BPF calling conventions.
- Minimal code change, primarily an update to register definitions and documentation.
exchanges:
- author: Vineet Gupta
  role: proposer
  position: Submitted a patch to allow `gas` to recognize `r11` for BPF stack arguments,
    aligning with kernel and `clang` support.
  quote: 'BPF functions with more than five arguments pass the rest on the stack,

    addressed through r11: the kernel has accepted that since 7.2 [1], and

    clang emits it [2].  No new instructions are involved, only 64-bit

    loads and stores with r11 as the base register:'
- author: Jose E. Marchesi
  role: reviewer
  position: Reviewed the patch and approved it for the master branch.
  quote: 'Thanks for the patch.

    OK for master!'
primer_expert: This patch updates `gas/config/tc-bpf.c` and `gas/doc/c-bpf.texi` to
  include `r11` in the list of recognized BPF registers for `gas`. This is necessary
  because the Linux kernel (since 7.2) and `clang` utilize `r11` to handle function
  arguments that exceed the standard register set, passing them via the stack. The
  change ensures that `gas` can correctly parse and assemble BPF code that uses `r11`
  for these stack-based arguments, including adding relevant test cases.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project, responsible for
    converting assembly language code into machine code.
- term: BPF
  definition: Berkeley Packet Filter, a technology that allows programs to be run
    in the Linux kernel without altering kernel source code. It's often used for network
    packet filtering and more general in-kernel computation.
- term: r11
  definition: A register used in the BPF instruction set. In this context, it's used
    for passing arguments beyond the first five via the stack.
- term: stack argument
  definition: A function argument passed via the call stack, typically used when the
    number of arguments exceeds the number of available registers.
series_id: 'binutils:gas: bpf: accept r11, the stack argument register'
series_role: reply
series_parts:
- title: 'gas: bpf: accept r11, the stack argument register'
  url: https://inbox.sourceware.org/binutils/20261012081159.2015930-7-vineet.gupta@linux.dev
  n: 6
  total: 6
url: https://inbox.sourceware.org/binutils/878q43m8x5.fsf@gnu.org
bugzilla_url: null
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

This patch modifies the GNU Assembler (`gas`) for BPF to accept `r11` as a valid register name. The kernel has supported `r11` for passing function arguments beyond the first five since version 7.2, and `clang` also emits code using it. Previously, `gas` only recognized registers `r0` through `r10`. This change enables `gas` to correctly assemble instructions that use `r11` for stack arguments, ensuring compatibility with newer kernel and compiler features.
