---
project: gcc
subsystem: libgomp
patch_id: null
tags:
- libgomp
- OpenMP
- virtualization
- eBPF
- GSoC
discussion_id: CAAk=M9f8cfVr-SZCY3vPgxg25A+AeQNfWuces1+-xz-13n5tEQ@mail.gmail.com
source_type: public_inbox
title: '[GSoC Project Submission] libgomp Optimizations for Scheduler Guided OpenMP
  Execution in Cloud VMs'
headline: libgomp Optimizations for Scheduler Guided OpenMP Execution in Cloud VMs
tldr: GSoC submission introduces new environment variables to libgomp for paravirtualized
  OpenMP optimizations using eBPF-based Phantom Tracker.
proposer: Roy Fru <royfru44@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Introducing new environment variables increases configuration complexity but allows
  for finer-grained performance tuning in specific environments.
- Relying on eBPF for monitoring adds a dependency on kernel features and potentially
  increases overhead.
exchanges:
- author: Roy Fru
  role: proposer
  position: Submits GSoC project deliverables, including eBPF-based Phantom Tracker
    and new environment variables for libgomp optimizations. Mentions that performance
    evaluation is forthcoming.
  quote: 'The project had two main deliverables: reimplementing Phantom Tracker using

    eBPF and, building on this new implementation, introducing two new

    environment variables to libgomp, GOMP_WAIT_POLICY and GOMP_DYNAMIC_POLICY,

    to enable paravirtualized OpenMP optimizations guided by Phantom Tracker.


    One thing worth mentioning is that the current patch series does not yet

    include an evaluation section de…'
primer_expert: This submission details a GSoC project aimed at improving libgomp's
  performance within virtualized environments, particularly on oversubscribed cloud
  VMs. It leverages eBPF for host-level monitoring (Phantom Tracker) to inform libgomp's
  runtime decisions regarding thread synchronization (wait policy) and degree of parallelism
  (dynamic policy). This aims to mitigate performance degradation caused by independent
  host and guest OS scheduling.
primer_glossary:
- term: libgomp
  definition: The GNU Offloading and Modular Parallelism (GOMP) library, which implements
    the OpenMP API for GCC.
- term: OpenMP
  definition: An API that supports multi-platform shared-memory parallel programming
    of C, C++, and Fortran in the areas of high performance computing and embedded
    systems.
- term: Cloud VMs
  definition: Virtual Machines running on cloud computing infrastructure, often subject
    to resource oversubscription and dynamic scheduling by the cloud provider.
- term: eBPF
  definition: Extended Berkeley Packet Filter, a technology that allows sandboxed
    programs to be run in the Linux kernel without changing kernel source code or
    loading kernel modules. Used here for monitoring host scheduling.
- term: Phantom Tracker
  definition: A system that monitors host scheduling decisions and vCPU preemption
    to provide paravirtualized scheduling metrics for guest VMs.
- term: GOMP_WAIT_POLICY
  definition: A new environment variable for libgomp that allows customization of
    thread synchronization behavior (e.g., spin vs. block) based on host-side scheduling
    metrics.
- term: GOMP_DYNAMIC_POLICY
  definition: A new environment variable for libgomp that enables dynamic adaptation
    of the degree of parallelism (number of threads) based on host-side scheduling
    metrics.
series_id: 20261101132739.695681-1-royfru44@gmail.com
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/gcc/CAAk=M9f8cfVr-SZCY3vPgxg25A+AeQNfWuces1+-xz-13n5tEQ@mail.gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This is a submission for a GSoC project focused on optimizing libgomp for cloud VMs. The project reimplemented Phantom Tracker using eBPF and introduced two new environment variables, GOMP_WAIT_POLICY and GOMP_DYNAMIC_POLICY, to enable paravirtualized OpenMP optimizations. The proposer plans to add performance evaluation results soon and is committed to addressing review feedback.
