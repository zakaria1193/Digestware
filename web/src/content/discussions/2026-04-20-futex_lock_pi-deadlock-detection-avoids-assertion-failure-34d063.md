---
project: glibc
subsystem: nptl
patch_id: null
tags:
- glibc
- nptl
- futex
- deadlock
- mutex
discussion_id: PR3PR06MB688971B81D9DF02440A469A9FF2F2@PR3PR06MB6889.eurprd06.prod.outlook.com
source_type: public_inbox
title: '[PATCH] nptl: futex_lock_pi deadlock detection provides valuable information
  but it is turned into a rather cryptic assertion failure'
headline: futex_lock_pi deadlock detection avoids assertion failure
tldr: The patch proposes to change the deadlock detection in futex_lock_pi to return
  EDEADLK for error-checking PI mutexes and deliberately deadlock in other cases,…
stakes: Impacts the behavior of priority-inheritance mutexes in the face of deadlocks,
  potentially affecting application stability.
proposer: Moritz KLAMMLER (FERCHAU) <Moritz.Klammler@ferchau.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Returning EDEADLK allows the application to handle the deadlock.
- Deliberately deadlocking might make debugging harder but avoids unexpected aborts.
- The change only affects error-checking PI mutexes.
primer_expert: This concerns glibc's NPTL (Native POSIX Thread Library) implementation
  of priority-inheritance (PI) mutexes using futexes. PI mutexes are designed to avoid
  priority inversion. This patch changes error handling in `futex_lock_pi` to return
  `EDEADLK` or deadlock instead of crashing. Interaction with `__futex_abstimed_wait64`
  is mentioned.
primer_general: Glibc's Native POSIX Thread Library (NPTL) provides threading capabilities
  for Linux programs.  A *mutex* is a lock that prevents multiple threads from accessing
  the same data simultaneously, preventing race conditions.  *Priority inheritance*
  is a mechanism to avoid priority inversion, where a high-priority task is blocked
  by a low-priority task holding a mutex. Futexes are a kernel mechanism used to implement
  mutexes. This patch changes how deadlocks are handled in priority-inheritance mutexes,
  potentially affecting application stability.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PR3PR06MB688971B81D9DF02440A469A9FF2F2@PR3PR06MB6889.eurprd06.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

This patch addresses the current behavior of `futex_lock_pi` deadlock detection, which results in an assertion failure. The proposer suggests modifying the patch to propagate `EDEADLK` for error-checking PI mutexes and deliberately deadlock in other cases, deeming the assertion failure the least desirable outcome.
