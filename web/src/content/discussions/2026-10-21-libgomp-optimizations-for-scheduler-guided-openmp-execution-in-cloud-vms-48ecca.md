---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- libgomp
- OpenMP
- eBPF
- cloud
discussion_id: CAAk=M9dh-SZgz3p2JXqAaUX_FSW2+ZQvozob7ccgmVwDX1bYDQ@mail.gmail.com
source_type: public_inbox
title: 'Progress Report: libgomp Optimizations for Scheduler Guided OpenMP Execution
  in Cloud VMs'
headline: Libgomp optimizations for scheduler-guided OpenMP execution in cloud VMs
tldr: Progress report on libgomp scheduler optimizations, including pv-barrier-sync,
  Degree of Parallelism (DoP) implementation, and eBPF for CPU load monitoring.
proposer: Roy Fru <royfru44@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Roy Fru <royfru44@gmail.com>
  role: proposer
  position: Reports on progress in implementing pv-barrier-sync for libgomp, including
    new tests and documentation, and the ongoing Degree of Parallelism (DoP) implementation.
    Details a refined eBPF approach for host CPU load monitoring using per-CPU runqueue
    data and BPF timers, which resolves previous issues with drift.
  quote: 'I then changed my approach and used bpf_per_cpu_ptr() to directly read the

    nr_running field from each CPU''s runqueue. I sample this value on each

    sched_switch event and calculate a time-weighted average using a BPF timer.

    I then use this average to calculate the idle average which is to be shared

    with the guest.'
primer_expert: This discussion concerns optimizations within libgomp, GCC's OpenMP
  runtime library. The work involves a new pv-barrier-sync implementation and the
  Degree of Parallelism (DoP) for scheduler-guided execution, likely targeting dynamic
  task scheduling. A significant part is the use of eBPF to monitor host CPU load
  by directly accessing per-CPU runqueue information (`nr_running`) via `bpf_per_cpu_ptr`
  and using BPF timers for time-weighted averaging. This data is then exposed to guests,
  possibly for power or performance management.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAAk=M9dh-SZgz3p2JXqAaUX_FSW2+ZQvozob7ccgmVwDX1bYDQ@mail.gmail.com
bugzilla_url: null
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

This is a progress report on ongoing libgomp optimizations for OpenMP execution in cloud VMs. The author has been working on the pv-barrier-sync implementation and the Degree of Parallelism (DoP) implementation, with patches for the former to be posted soon. Additionally, an eBPF-based approach has been developed to monitor host CPU load by sampling the number of runnable tasks on each CPU, addressing previous drift issues.
