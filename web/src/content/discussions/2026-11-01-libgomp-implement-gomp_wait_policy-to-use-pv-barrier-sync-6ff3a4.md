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
discussion_id: 20261101132739.695681-2-royfru44@gmail.com
source_type: public_inbox
title: '[RFC 1/4] libgomp: Implement GOMP_WAIT_POLICY to use pv-barrier-sync'
headline: 'libgomp: Implement GOMP_WAIT_POLICY to use pv-barrier-sync'
tldr: Implement GOMP_WAIT_POLICY to enable pv-barrier-sync, which dynamically adjusts
  thread spin/block behavior based on host contention.
proposer: NchangRoy <royfru44@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Dynamically adjusting spin/block behavior can improve performance in virtualized
  environments but adds complexity and potential overhead from metric checks.
- Relying on host metrics means the policy's effectiveness is dependent on the accuracy
  and timeliness of the host monitoring.
exchanges:
- author: NchangRoy
  role: proposer
  position: Introduces the GOMP_WAIT_POLICY environment variable and the 'pv-barrier-sync'
    policy, enabling dynamic spin/block behavior at barriers based on host scheduling
    metrics to improve performance in virtual machines.
  quote: 'This patch introduces phantom_average to libgomp barrier wait policy implemented

    with the help of GOMP_WAIT_POLICY, a new libgomp environment variable, which

    when set to "pvsched" uses phantom_average to dynamically decide whether to spin

    or block on a per-barrier and per-thread basis at runtime.


    The pv-barrier-sync policy changes this behavior by exploiting as many spin

    iterations as possible a…'
primer_expert: This RFC proposes the implementation of `GOMP_WAIT_POLICY` for libgomp,
  focusing on the `pv-barrier-sync` strategy. This policy dynamically tunes the wait
  behavior at OpenMP barriers. Instead of a fixed spin count, it leverages the `phantom_average`
  metric (obtained via eBPF from the host) to decide whether to spin or block. This
  adaptive approach is crucial for performance in oversubscribed virtual machine environments
  where host scheduler preemptions can significantly impact guest application progress.
primer_glossary:
- term: GOMP_WAIT_POLICY
  definition: A new environment variable for libgomp that controls the strategy threads
    use when waiting at synchronization points like barriers.
- term: pv-barrier-sync
  definition: A paravirtualized barrier synchronization policy that dynamically adjusts
    thread waiting behavior based on host scheduling conditions.
- term: phantom_average
  definition: A metric derived from host monitoring (eBPF) indicating the degree of
    scheduling contention experienced by guest vCPUs.
- term: vCPU
  definition: Virtual Central Processing Unit, a software emulation of a physical
    CPU that runs on a host machine's physical CPU.
- term: eBPF
  definition: Extended Berkeley Packet Filter, a technology allowing safe, sandboxed
    execution of code within the Linux kernel, used here for performance monitoring.
- term: shared memory
  definition: Memory that can be accessed by multiple processes or, in this context,
    by the host and guest VM via mechanisms like QEMU's ivshmem.
series_id: 20261101132739-1-royfru44@gmail.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/20261101132739.695681-2-royfru44@gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This patch implements the GOMP_WAIT_POLICY environment variable for libgomp, introducing the 'pv-barrier-sync' policy. This policy leverages the 'phantom_average' metric from host monitoring to dynamically decide whether threads should spin or block at barriers. This aims to optimize performance in virtualized environments by maximizing spinning during low contention and immediately blocking when host-side contention is detected.
