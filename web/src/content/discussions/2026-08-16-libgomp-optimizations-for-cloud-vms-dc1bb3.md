---
project: gcc
subsystem: gcc/omp
patch_id: null
tags:
- OpenMP
- libgomp
- virtualization
- eBPF
- performance
discussion_id: CAAk=M9dfX6RigVJXPxiLMVauRfipJEBPrQ9pn1A2O2d8vv4JtA@mail.gmail.com
source_type: public_inbox
title: '[Progress Report] libgomp Optimizations for Scheduler Guided OpenMP Execution
  in Cloud VMs'
headline: libgomp Optimizations for Cloud VMs
tldr: Progress report on libgomp optimizations for OpenMP execution in cloud VMs,
  involving eBPF, IVSHMEM, and new environment variables for scheduler guidance.
proposer: Roy Fru <royfru44@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Increased kernel-level instrumentation (eBPF) might introduce minor performance
  overhead.
- Reliance on specific IVSHMEM drivers may limit compatibility across different virtualization
  platforms.
- New environment variables can add complexity for users managing OpenMP applications.
exchanges:
- author: Roy Fru
  role: proposer
  position: Details progress on libgomp optimizations for cloud VMs, including eBPF
    cleanup, IVSHMEM driver integration, and new environment variable support.
  quote: I added tests to verify the interaction between the modified libgomp and
    Phantom Track
primer_expert: This progress report details enhancements to GCC's libgomp for OpenMP
  execution within cloud VMs. The work involves kernel-level eBPF programs and IVSHMEM
  drivers for host-guest communication, allowing the host to detect phantom vCPUs
  running OpenMP threads. A new `GOMP_WAIT_POLICY=pvsched` option aims to improve
  barrier synchronization by utilizing this information, reducing latency in paravirtualized
  environments.
primer_glossary:
- term: libgomp
  definition: GCC's implementation of OpenMP, providing runtime support for parallel
    execution.
- term: OpenMP
  definition: An API for supporting shared-memory parallel programming in C, C++,
    and Fortran.
- term: eBPF
  definition: Extended Berkeley Packet Filter, a technology that allows safe, efficient
    execution of sandboxed programs in the Linux kernel.
- term: IVSHMEM
  definition: Inter-Virtual Machine Shared Memory, a mechanism for efficient communication
    between virtual machines or between a guest and host.
- term: vCPU
  definition: Virtual Central Processing Unit, a software-based emulation of a physical
    CPU core provided to a virtual machine.
- term: Phantom vCPU
  definition: A virtual CPU that is not actively running on a physical core but is
    being tracked by the host for scheduling or performance analysis purposes.
- term: Paravirtualization
  definition: A virtualization technique where the guest operating system is aware
    it's running in a virtualized environment and makes specific calls to the hypervisor
    for optimized performance.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAAk=M9dfX6RigVJXPxiLMVauRfipJEBPrQ9pn1A2O2d8vv4JtA@mail.gmail.com
bugzilla_url: null
date: '2026-08-16'
is_stub: false
stub_reason: ''
---

Roy Fru reports progress on optimizing libgomp for cloud VMs by integrating eBPF and IVSHMEM to monitor and guide OpenMP thread scheduling. This involves cleaning up TIDs, enabling host-guest communication for vCPU states, and introducing a new GOMP_WAIT_POLICY environment variable with a 'pvsched' option for paravirtualized barrier synchronization. The goal is to improve OpenMP performance in virtualized environments by reacting to phantom vCPUs.
