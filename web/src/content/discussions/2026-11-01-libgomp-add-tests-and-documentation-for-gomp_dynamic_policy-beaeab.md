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
discussion_id: 20261101132739.695681-4-royfru44@gmail.com
source_type: public_inbox
title: '[RFC 4/4] libgomp: Add tests and documentation for GOMP_DYNAMIC_POLICY'
headline: 'libgomp: Add tests and documentation for GOMP_DYNAMIC_POLICY'
tldr: Documentation and tests for the new GOMP_DYNAMIC_POLICY environment variable,
  enabling Juunansei's phantom-guided DoP adaptation.
proposer: NchangRoy <royfru44@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding comprehensive tests and documentation improves maintainability and user understanding.
- The Juunansei policy adapts DoP based on host metrics, which could lead to suboptimal
  performance if the metrics are not perfectly representative of the guest workload's
  needs.
exchanges:
- author: NchangRoy
  role: proposer
  position: Submits documentation and test cases for the GOMP_DYNAMIC_POLICY environment
    variable, detailing its behavior and verifying its functionality through DejaGNU
    tests.
  quote: 'This patch adds documentation and DejaGNU test cases for GOMP_DYNAMIC_POLICY,
    a

    new GCC-specific environment variable extending OMP_DYNAMIC to support

    Juunansei''s phantom-guided degree-of-parallelism (DoP) adaptation

    (GOMP_DYNAMIC_POLICY=pvsched), as well as the default online-CPU-count-minus-

    loadavg policy.


    The test cases in libgomp/testsuite/libgomp.c/ verify:

    - GOMP_DYNAMIC_POLICY=pvsched re…'
primer_expert: This RFC provides the necessary documentation and test suite for `GOMP_DYNAMIC_POLICY`,
  a new environment variable for libgomp. It allows OpenMP applications to dynamically
  adjust their degree of parallelism (DoP) based on paravirtualized scheduling metrics
  (`phantom_average`, `idle_average`) gathered from the host via eBPF. The Juunansei
  policy leverages these metrics to mitigate performance issues in oversubscribed
  cloud VMs by reducing thread count during host contention.
primer_glossary:
- term: GOMP_DYNAMIC_POLICY
  definition: A GCC-specific environment variable that controls how libgomp dynamically
    adjusts the number of threads used in parallel regions, influenced by host system
    load.
- term: Juunansei
  definition: A specific policy for GOMP_DYNAMIC_POLICY that uses paravirtualized
    scheduling metrics (phantom_average, idle_average) to adapt the degree of parallelism.
- term: degree of parallelism (DoP)
  definition: The number of threads that can execute simultaneously in a parallel
    region.
- term: phantom_average
  definition: A paravirtualized scheduling metric indicating the extent of host scheduling
    contention affecting guest vCPUs.
- term: idle_average
  definition: A paravirtualized scheduling metric representing the average number
    of idle physical CPUs on the host.
- term: DejaGNU
  definition: A testing framework used for GNU software, providing a way to write
    portable tests that can be run across different platforms and configurations.
series_id: 20261101132739-1-royfru44@gmail.com
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/20261101132739.695681-4-royfru44@gmail.com
bugzilla_url: null
date: '2026-11-01'
is_stub: false
stub_reason: ''
---

This patch adds documentation and DejaGNU test cases for the new GOMP_DYNAMIC_POLICY environment variable. This variable extends OpenMP's dynamic degree-of-parallelism (DoP) adaptation to include the Juunansei policy, which uses host-side scheduling metrics (phantom_average, idle_average) to adjust the number of threads used. The tests cover various scenarios, including case-insensitivity and fallback to default behavior.
