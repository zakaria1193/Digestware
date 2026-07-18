---
project: gcc
subsystem: gcc
patch_id: null
tags:
- OpenMP
- libgomp
- threading
- performance
- runtime
discussion_id: 7b5f4947850a49419d77b0cb9fa5004b@inf.ufrgs.br
source_type: public_inbox
title: '[gcc,libgomp] Validation for an approach to PR115367'
headline: Validation for an approach to PR115367
tldr: Proposes improving libgomp's OMP_DYNAMIC thread spawning by memoizing load average
  and optimizing when it's fetched.
proposer: Léo Hardt <leom.hardt@inf.ufrgs.br>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Memoizing load average reduces overhead but might lag behind sudden system load
  changes if the memoization window is too long.
- Fetching load average during GOMP_parallel_end instead of start could improve parallel
  region performance but might make the decision lag behind the actual need for threads
  at the beginning of a block.
exchanges: []
primer_expert: This proposal addresses the dynamic thread management within libgomp,
  specifically the OMP_DYNAMIC runtime behavior. It aims to optimize the fetching
  and utilization of system load averages (via getloadavg) to determine the number
  of threads for OpenMP parallel regions. The core issues are the overhead of repeated
  system calls and the suitability of the averaging period for varying workloads.
primer_glossary:
- term: OMP_DYNAMIC
  definition: An OpenMP runtime environment variable that controls whether the number
    of threads used in parallel regions can be dynamically adjusted by the runtime
    library.
- term: libgomp
  definition: GCC's implementation of the OpenMP runtime library.
- term: getloadavg
  definition: A POSIX function that returns the average system load over the last
    1, 5, and 15 minutes.
- term: PR115367
  definition: A bug report (Problem Report) concerning the limitations or desired
    improvements for OMP_DYNAMIC in libgomp.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/7b5f4947850a49419d77b0cb9fa5004b@inf.ufrgs.br
bugzilla_url: null
date: '2026-07-18'
is_stub: false
stub_reason: ''
---

This discussion proposes improvements to the libgomp implementation of OMP_DYNAMIC for thread spawning on Linux. The current approach uses glibc's getloadavg with a 15-minute average, which has been criticized for its potentially too-long or too-short averaging window. The proposer suggests memoizing the load average to reduce overhead on short-lived parallel blocks and fetching it during GOMP_parallel_end instead of GOMP_parallel_start. Additionally, it's suggested that using the 1, 5, and 15-minute averages along with program runtime could lead to a more optimal thread count.
