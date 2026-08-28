---
project: gcc
subsystem: gcc
patch_id: null
tags:
- optimization
- OpenMP
- libgomp
- virtualization
- tracing
discussion_id: CAAk=M9cNW__YSJUUL4yiG=jW5toR53J3w0TizehtWmmJh=kcfg@mail.gmail.com
source_type: public_inbox
title: '[Progress Report] libgomp Optimizations for Scheduler Guided OpenMP Execution
  in Cloud VMs'
headline: Libgomp optimizations for scheduler-guided OpenMP execution
tldr: Roy Fru reports progress on optimizing libgomp for cloud VMs by replacing read
  operations with mmap, adopting USDT probes, and testing with NPB benchmarks.
proposer: Roy Fru <royfru44@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Replacing read/pread with mmap reduces system call overhead but requires careful
  handling of memory mapping and unmapping.
- Transitioning from uprobes to USDT provides a more stable tracing interface but
  may require changes in how eBPF programs are written and attached.
- Shared metadata and dynamic IVSHMEM allocation add complexity to the runtime but
  could improve scalability and resource utilization.
exchanges: []
primer_expert: This report details progress on optimizing libgomp, the OpenMP runtime
  library within GCC. The work focuses on improving performance for OpenMP applications
  running in virtualized cloud environments, specifically leveraging IVSHMEM for inter-VM
  communication and USDT for stable tracing. The goal is to reduce overhead and enhance
  scalability for parallel workloads.
primer_glossary:
- term: libgomp
  definition: The OpenMP runtime library for GCC. It manages thread creation, work-sharing
    constructs, and synchronization for OpenMP parallel regions.
- term: IVSHMEM
  definition: Interrupt-vectoring shared memory, a mechanism for efficient inter-Virtual
    Machine (VM) communication. It allows VMs to share memory regions directly, bypassing
    hypervisor mediation for faster data exchange.
- term: mmap
  definition: A system call that maps files or devices into memory. It allows a program
    to treat memory-mapped regions as if they were directly in its address space,
    enabling efficient I/O operations.
- term: USDT probes
  definition: Userspace Statically Defined Tracing probes. These are markers embedded
    in user-space applications by developers to enable dynamic tracing by tools like
    eBPF, offering a stable interface for observing internal program behavior.
- term: eBPF
  definition: Extended Berkeley Packet Filter. A technology that allows running sandboxed
    programs in the Linux kernel without changing kernel source code or loading modules.
    It's often used for networking, security, and tracing.
- term: NPB
  definition: NAS Parallel Benchmarks. A suite of benchmark programs designed to evaluate
    the performance of parallel supercomputers, often used to test parallel programming
    libraries like OpenMP.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAAk=M9cNW__YSJUUL4yiG=jW5toR53J3w0TizehtWmmJh=kcfg@mail.gmail.com
bugzilla_url: null
date: '2026-08-27'
is_stub: false
stub_reason: ''
---

Roy Fru provides a progress report on optimizing libgomp for OpenMP execution in cloud VMs. Key advancements include replacing read operations with mmap for IVSHMEM pages to avoid system calls, and transitioning from uprobe-based to USDT probes for more stable tracing. The integration has been tested with NPB benchmarks, and future work may involve a shared metadata section for VMs.
