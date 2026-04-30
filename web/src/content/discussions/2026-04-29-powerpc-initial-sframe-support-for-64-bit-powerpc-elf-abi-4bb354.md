---
project: binutils
subsystem: powerpc
patch_id: null
tags:
- powerpc
- sframe
- stack unwinding
- profiling
- perf
discussion_id: b6139ccf-74ea-4ce6-b782-686a1ccee8d9@linux.ibm.com
source_type: public_inbox
title: 'Re: [PATCH v2] PowerPC: Initial SFrame support for 64-bit PowerPC ELF ABI'
headline: 'PowerPC: Initial SFrame support for 64-bit PowerPC ELF ABI'
tldr: The patch adds SFrame support for PowerPC64 to resolve issues with stale link
  registers and epilogue races during profiling.
proposer: Abhay Kandpal <abhay@linux.ibm.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Adds complexity to the kernel.
- Requires changes to the PowerPC64 ABI.
- May introduce a performance overhead (though diharapkan kecil).
exchanges:
- author: Abhay Kandpal
  role: proposer
  position: Explains the motivation for SFrame support on PowerPC64 due to issues
    with stale link registers and epilogue races during profiling.
  quote: SFrame in the kernel would allow the unwinder to resolve this directly without
    relying on userspace post-processing.
primer_expert: This patch adds SFrame support for PowerPC64. SFrame provides a more
  reliable way to unwind the stack during profiling, especially in the presence of
  NMIs and epilogue races. .eh_frame based unwinding has limitations in these scenarios.
  This affects perf and other profiling tools.
primer_general: This patch introduces a new mechanism called SFrame for stack unwinding
  on PowerPC64 systems. Stack unwinding is the process of determining the sequence
  of function calls that led to a particular point in the program's execution. Traditional
  methods can fail in certain situations, leading to inaccurate profiling data. SFrame
  provides a more reliable way to walk the stack, improving the accuracy of performance
  analysis tools.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/b6139ccf-74ea-4ce6-b782-686a1ccee8d9@linux.ibm.com
bugzilla_url: null
date: '2026-04-29'
---

Abhay Kandpal clarifies the necessity of SFrame (stack frame) support for PowerPC64, addressing issues with stale link registers at NMI boundaries and epilogue races that lead to missing caller information during profiling.  These problems cannot be reliably solved in userspace, requiring kernel-side unwinding with reliable frame data provided by SFrame.  The patch has been tested on both ppc64le and ppc64 BE.
