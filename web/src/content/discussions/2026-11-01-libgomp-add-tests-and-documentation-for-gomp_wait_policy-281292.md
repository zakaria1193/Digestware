---
project: gcc
subsystem: libgomp
patch_id: null
tags:
- libgomp
- OpenMP
- documentation
- testing
- virtualization
discussion_id: 20261101132739.695681-3-royfru44@gmail.com
source_type: public_inbox
title: '[RFC 2/4] libgomp: Add tests and documentation for GOMP_WAIT_POLICY'
headline: 'libgomp: Add tests and documentation for GOMP_WAIT_POLICY'
tldr: Documentation and tests are added for GOMP_WAIT_POLICY, supporting pv-barrier-sync
  and other wait policies.
proposer: NchangRoy <royfru44@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding new wait policies offers flexibility but increases the complexity of libgomp's
  internal state management.
- The `pv-barrier-sync` policy relies on accurate `phantom_average` metrics; any inaccuracies
  could lead to suboptimal synchronization behavior.
exchanges:
- author: NchangRoy
  role: proposer
  position: Provides documentation and test cases for the GOMP_WAIT_POLICY environment
    variable, ensuring its correct implementation and behavior, including the pv-barrier-sync
    policy.
  quote: 'This patch adds documentation and DejaGNU test cases for GOMP_WAIT_POLICY,
    a new

    GCC-specific environment variable extending OMP_WAIT_POLICY to support the

    paravirtualized pv-barrier-sync policy (GOMP_WAIT_POLICY=pvsched), as well as

    ACTIVE and PASSIVE wait policies.


    The documentation in libgomp.texi describes the behavior of pv-barrier-sync:

    when no phantom vCPUs are detected (phantom_average =…'
primer_expert: This RFC provides documentation and test cases for `GOMP_WAIT_POLICY`,
  a libgomp environment variable designed to optimize thread synchronization in virtualized
  environments. The `pv-barrier-sync` policy, when enabled, dynamically adjusts whether
  threads spin or block at barriers based on `phantom_average` metric from the host,
  aiming to reduce wasted CPU cycles during contention and maximize parallelism when
  contention is absent.
primer_glossary:
- term: GOMP_WAIT_POLICY
  definition: A GCC-specific environment variable that customizes how OpenMP threads
    behave when waiting at synchronization points (e.g., barriers), choosing between
    spinning or blocking.
- term: pv-barrier-sync
  definition: A paravirtualized wait policy for libgomp that uses host-side scheduling
    metrics to dynamically decide whether threads should spin or block at barriers.
- term: phantom vCPUs
  definition: Virtual CPUs experiencing host-side scheduling contention, hindering
    guest application progress.
- term: SystemTap SDT
  definition: SystemTap Static Defined Tracing, a mechanism for instrumenting applications
    to provide probe points for dynamic tracing.
- term: USDT tracing probes
  definition: User-level Statically Defined Tracing probes, allowing userspace applications
    to emit tracepoints that can be captured by tracing tools like SystemTap or DTrace.
series_id: 20261101132739-1-royfru44@gmail.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/20261101132739.695681-3-royfru44@gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This patch introduces documentation and DejaGNU test cases for the new GOMP_WAIT_POLICY environment variable. This variable allows users to specify wait policies for OpenMP threads, including the paravirtualized 'pv-barrier-sync' policy, which adapts spinning behavior based on host contention. The tests cover parsing of different policies and fallback mechanisms.
