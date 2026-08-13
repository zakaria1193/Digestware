---
project: binutils
subsystem: powerpc
patch_id: null
tags:
- powerpc
- binutils
- debugging
- profiling
- dwarf
discussion_id: 8c5f4f61-a550-47f7-b31f-719838b2d246@gmail.com
source_type: public_inbox
title: 'Re: [PATCH v2] PowerPC: Initial SFrame support for 64-bit PowerPC ELF ABI'
headline: 'PowerPC: Initial SFrame support for 64-bit PowerPC ELF ABI'
tldr: Discusses the need for SFrame support in PowerPC64 ELF ABI to address stale
  LR values and missing caller information during profiling.
proposer: Indu Bhagat <ibhagatgnu@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Enables more reliable profiling by providing kernel-level SFrame support.
- Moves away from fragile userspace heuristics for callchain unwinding.
exchanges:
- author: Indu Bhagat <ibhagatgnu@gmail.com>
  role: reviewer
  position: Asks for motivation behind the change and confirms testing on both ppc64le
    and ppc64 BE.
  quote: 'Thanks for the review and for raising the question about motivation. Regarding
    testing: yes, perf report based testing was done on both ppc64le and ppc64 (BE).'
- author: Abhay Kandpal
  role: proposer
  position: Explains that SFrame is needed for PowerPC64 due to stale LR at NMI and
    missing caller frames during profiling, which current heuristics cannot reliably
    fix.
  quote: 'For the summary of why SFrame is necessary for PowerPC64, two root problems
    were identified: 1. Stale Link Register (LR) at NMI boundary ... 2. Epilogue-race
    / missing caller ... No userspace heuristic can recover this lost frame — it requires
    kernel-side unwinding with reliable frame data, which SFrame enables.'
primer_expert: This thread discusses the integration of SFrame (Stack Frame) support
  into the PowerPC64 ELF ABI for binutils. The core issue is the unreliability of
  callchain unwinding during NMI-based profiling, particularly with `perf`. Two specific
  problems, stale Link Register (LR) values and epilogue-race conditions, lead to
  incorrect or missing stack frames. SFrame aims to provide a more robust kernel-level
  unwinding mechanism, moving beyond fragile userspace heuristics that depend on `.eh_frame`
  interpretation.
primer_glossary:
- term: SFrame
  definition: A proposed mechanism to enhance stack frame information, likely for
    improved debugging and profiling accuracy, particularly in kernel contexts.
- term: PowerPC64 ELF ABI
  definition: The Application Binary Interface for the 64-bit PowerPC architecture
    using the Executable and Linkable Format (ELF).
- term: NMI
  definition: Non-Maskable Interrupt. A type of hardware interrupt that cannot be
    ignored by the processor, often used for critical system events like hardware
    errors or profiling timers.
- term: Link Register (LR)
  definition: A special-purpose register in PowerPC architectures that typically holds
    the return address for function calls.
- term: perf
  definition: A performance analysis tool and profiling utility in the Linux kernel,
    used here for callchain analysis.
- term: .eh_frame
  definition: A section in an ELF object file containing DWARF debugging information,
    primarily used for stack unwinding and exception handling.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/8c5f4f61-a550-47f7-b31f-719838b2d246@gmail.com
bugzilla_url: null
date: '2026-08-12'
is_stub: false
stub_reason: ''
---

This discussion delves into the necessity of SFrame support for 64-bit PowerPC ELF ABI, primarily to resolve issues encountered during profiling with `perf`. Two key problems are highlighted: stale Link Register (LR) values at NMI boundaries and an 'epilogue-race' leading to missing caller information. The current reliance on fragile heuristics in `perf` to correct these issues is deemed insufficient, and SFrame is presented as a kernel-side solution for more reliable unwinding and frame data.
