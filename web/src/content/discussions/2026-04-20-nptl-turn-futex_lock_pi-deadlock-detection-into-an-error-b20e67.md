---
project: glibc
subsystem: nptl
patch_id: null
tags:
- glibc
- nptl
- futex
- deadlock
- priority inheritance
discussion_id: PR3PR06MB688909B85CF5747F25CF2713FFAAA@PR3PR06MB6889.eurprd06.prod.outlook.com
source_type: public_inbox
title: '[PATCH] nptl: futex_lock_pi deadlock detection provides valuable information
  but it is turned into a rather cryptic assertion failure'
headline: 'nptl: Turn futex_lock_pi deadlock detection into an error'
tldr: The patch aims to improve deadlock detection for priority inheritance (PI) mutexes
  by reporting an error instead of triggering an assertion failure.
stakes: Improving deadlock detection helps developers identify and resolve concurrency
  issues, leading to more reliable and robust multithreaded applications.  It also
  aligns with error-checking semantics expected when using PI mutexes.
proposer: '"Moritz KLAMMLER (FERCHAU)" <Moritz.Klammler@ferchau.com>'
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Returning EDEADLK allows for more graceful error handling but might mask underlying
  issues.
- Deliberately deadlocking in non-error-checking cases could simplify debugging but
  might be unexpected behavior.
- Changing the behavior for all PI mutexes could introduce regressions.
exchanges:
- author: Moritz KLAMMLER (FERCHAU)
  role: proposer
  position: Asks whether the patch should be updated to only propagate EDEADLK for
    error-checking PI mutexes and deliberately deadlock in other cases, as opposed
    to the current assertion failure.
  quote: Should I update the patch accordingly to have only error-checking PI mutex
    propagate the EDEADLK and deliberately deadlock in all other cases?  Running into
    the assertion seems to be the least desirable option to me.
primer_expert: This patch relates to the nptl (Native POSIX Thread Library) subsystem
  in glibc, specifically the futex_lock_pi function which handles locking of priority
  inheritance mutexes. Priority inheritance is a mechanism to avoid priority inversion,
  where a high-priority thread is blocked by a low-priority thread holding a mutex.
  The patch modifies the deadlock detection logic to return an error code instead
  of triggering an assertion. The discussion revolves around whether to apply this
  change to all PI mutexes or only those configured for error checking.
primer_general: In multithreaded programming, a deadlock occurs when two or more threads
  are blocked indefinitely, waiting for each other to release resources. Priority
  inheritance (PI) is a mechanism used with mutexes (mutual exclusion locks) to prevent
  priority inversion, a situation where a high-priority thread is blocked by a lower-priority
  thread. This patch modifies how glibc's PI mutex implementation handles deadlock
  detection. Instead of causing the program to abort with an assertion failure, the
  patch proposes returning an error code (EDEADLK), allowing the program to handle
  the deadlock more gracefully. Error checking is a standard practice in multithreaded
  programming to prevent undefined behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PR3PR06MB688971B81D9DF02440A469A9FF2F2@PR3PR06MB6889.eurprd06.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

Moritz Klammler proposes modifying the futex_lock_pi function to return EDEADLK when a deadlock is detected, rather than triggering an assertion failure. Adhemerval Zanella Netto suggests only propagating the EDEADLK error for error-checking PI mutexes and deliberately deadlocking in other cases.
