---
project: gcc
subsystem: libgomp
patch_id: null
tags:
- libgomp
- OpenMP
- virtualization
- performance
- eBPF
discussion_id: 20261101132739.695681-1-royfru44@gmail.com
source_type: public_inbox
title: '[RFC 0/4] libgomp: Optimizations for Scheduler Guided OpenMP Execution in
  Cloud VMs'
headline: 'libgomp: Optimizations for Scheduler Guided OpenMP Execution in Cloud VMs'
tldr: Introduces paravirtualized runtime policies (pv-barrier-sync, Juunansei) to
  libgomp to optimize OpenMP execution in virtualized cloud environments.
proposer: NchangRoy <royfru44@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Introducing host-aware policies improves performance in specific virtualized environments
  but may add complexity and overhead.
- The reliance on eBPF requires a compatible kernel version and may introduce kernel-specific
  dependencies.
exchanges:
- author: NchangRoy
  role: proposer
  position: Proposes optimizations for libgomp in cloud VMs by introducing virtualization-aware
    policies based on eBPF-monitored host scheduling metrics, addressing performance
    degradation due to independent host/guest scheduling.
  quote: 'Libgomp is virtualization oblivious, which becomes a problem when

    OpenMP applications runs inside an oversubscribed VM (more virtual

    CPUs (vCPUs) than physical CPUs (pCPUs)). Recent research from Inria

    [1] addresses this with the idea of "Phantom vCPUs". [...] The

    same research proposes Phantom Tracker [2], which monitors

    scheduling decisions made by both the host and guest schedulers and

    aggrega…'
primer_expert: This RFC addresses libgomp's lack of awareness regarding host OS scheduling
  in virtualized environments. It introduces a solution based on research into 'Phantom
  vCPUs' and implements a 'Phantom Tracker' using eBPF. The tracker provides `phantom_average`
  and `idle_average` metrics, which are then used by new libgomp policies (`pv-barrier-sync`
  and `Juunansei`) to adapt thread synchronization and degree of parallelism dynamically.
  This aims to improve OpenMP performance on oversubscribed cloud VMs where host scheduling
  can disrupt guest application progress.
primer_glossary:
- term: libgomp
  definition: The GNU implementation of the OpenMP runtime library for GCC.
- term: Oversubscribed VM
  definition: A virtual machine that has been allocated more virtual resources (like
    vCPUs) than the physical resources available on the host, leading to potential
    performance contention.
- term: Phantom vCPUs
  definition: A concept describing virtual CPUs experiencing scheduling delays or
    preemptions from the host OS, which negatively impact the guest application's
    performance.
- term: Phantom Tracker
  definition: A monitoring system that uses eBPF to observe host and guest scheduler
    behavior and quantify performance impacts on VMs.
- term: eBPF
  definition: Extended Berkeley Packet Filter, a technology enabling the execution
    of sandboxed programs within the Linux kernel, often used for monitoring and tracing.
- term: pv-barrier-sync
  definition: A paravirtualized synchronization policy for OpenMP barriers that adapts
    thread spin/block behavior based on host scheduling metrics.
- term: Juunansei
  definition: A policy for dynamically adjusting the degree of parallelism in OpenMP
    applications, informed by host scheduling metrics.
- term: degree of parallelism (DoP)
  definition: The number of threads that can execute concurrently within a parallel
    region.
series_id: 20261101132739-1-royfru44@gmail.com
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/gcc/20261101132739.695681-1-royfru44@gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This RFC proposes making libgomp virtualization-aware to address performance issues in oversubscribed cloud VMs. It introduces the concept of 'Phantom vCPUs' and the 'Phantom Tracker' system, which monitors host scheduling to provide metrics like phantom_average and idle_average. The project reimplements Phantom Tracker using eBPF and proposes two new libgomp policies: 'pv-barrier-sync' for dynamic wait behavior and 'Juunansei' for dynamic degree-of-parallelism adaptation.
