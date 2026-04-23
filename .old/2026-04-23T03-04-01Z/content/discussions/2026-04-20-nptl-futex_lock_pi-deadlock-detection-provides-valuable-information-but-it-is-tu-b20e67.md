---
project: glibc
subsystem: nptl
patch_id: null
tags:
- glibc
- nptl
- futex
- mutex
- deadlock
discussion_id: PR3PR06MB688909B85CF5747F25CF2713FFAAA@PR3PR06MB6889.eurprd06.prod.outlook.com
source_type: public_inbox
title: '[PATCH] nptl: futex_lock_pi deadlock detection provides valuable information
  but it is turned into a rather cryptic assertion failure'
headline: 'nptl: futex_lock_pi deadlock detection provides valuable information but
  it is turned into a rather cryptic assertion failure'
tldr: Asks whether to propagate EDEADLK for error-checking PI mutexes and deliberately
  deadlock in other cases instead of a cryptic assertion.
stakes: Impacts program behavior when deadlocks are detected in priority inheritance
  mutexes, affecting debugging and error handling.
proposer: '"Moritz KLAMMLER (FERCHAU)" <Moritz.Klammler@ferchau.com>'
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Returning EDEADLK allows the program to handle the error, but might mask the underlying
  cause of the deadlock.
- Deliberately deadlocking provides a clear signal of the problem during development
  but prevents the program from recovering.
- Assertion failures provide information but depend on glibc being built with assertions
  enabled.
exchanges:
- author: Moritz KLAMMLER (FERCHAU)
  role: proposer
  position: Asks if the patch should be updated to propagate EDEADLK for error-checking
    PI mutexes and deliberately deadlock in other cases.
  quote: Should I update the patch accordingly to have only error-checking PI mutex
    propagate the EDEADLK and deliberately deadlock in all other cases?  Running into
    the assertion seems to be the least desirable option to me.
- author: Adhemerval Zanella Netto
  role: contributor
  position: The message provides context for the question, referring to previous discussion
    about error-checking semantics and potential regressions.
  quote: null
primer_expert: This patch relates to the `nptl` (Native POSIX Thread Library) subsystem
  in glibc, specifically the `futex_lock_pi` function used for priority inheritance
  mutexes. Deadlock detection is crucial for these mutexes. The discussion is about
  whether to turn the deadlock event into a returnable error or let it abort via assertion
  failure.
primer_general: 'glibc''s Native POSIX Thread Library (nptl) provides the threading
  primitives for POSIX-compliant systems. A mutex (mutual exclusion) is a synchronization
  primitive that prevents multiple threads from accessing a shared resource simultaneously.
  Priority inheritance (PI) is a mechanism to avoid priority inversion, where a high-priority
  thread is blocked by a low-priority thread holding a mutex. Deadlock occurs when
  two or more threads are blocked forever, waiting for each other. This discussion
  is about how glibc should handle deadlock detection in priority inheritance mutexes:
  by returning an error or aborting the program.'
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PR3PR06MB688971B81D9DF02440A469A9FF2F2@PR3PR06MB6889.eurprd06.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

Moritz Klammler is seeking guidance on how to handle deadlock detection in `futex_lock_pi`.  The current implementation results in an assertion failure, which can be less informative than returning an `EDEADLK` error. He asks whether the patch should be updated to propagate `EDEADLK` for error-checking PI mutexes and deliberately deadlock in other cases.
