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
headline: 'nptl: futex_lock_pi deadlock detection provides valuable information but
  it is turned into a rather cryptic assertion failure'
tldr: The patch proposes to change the deadlock detection in futex_lock_pi to return
  EDEADLK instead of triggering an assertion failure.
stakes: This change affects the behavior of priority inheritance mutexes, potentially
  impacting the robustness of multithreaded applications.
proposer: '"Moritz KLAMMLER (FERCHAU)" <Moritz.Klammler@ferchau.com>'
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Changing the error reporting mechanism from assertion to EDEADLK may affect existing
  debugging workflows.
- Returning EDEADLK provides a more graceful way to handle deadlocks, but may mask
  underlying issues if the error is not properly handled by the application.
exchanges:
- author: Moritz KLAMMLER (FERCHAU) <Moritz.Klammler@ferchau.com>
  role: proposer
  position: Proposes to change the deadlock detection in `futex_lock_pi` to return
    `EDEADLK` instead of an assertion failure, and asks whether it should be limited
    to error-checking PI mutexes.
  quote: Should I update the patch accordingly to have only error-checking PI mutex
    propagate the EDEADLK and deliberately deadlock in all other cases? Running into
    the assertion seems to be the least desirable option to me.
primer_expert: The `nptl` subsystem implements POSIX threads in glibc. `futex_lock_pi`
  is a function related to priority inheritance mutexes.  The patch modifies deadlock
  detection within this function, changing assertion failures to `EDEADLK` returns.
  Knowledge of `nptl` internals is needed to understand the implications. A general
  toolchain dev might not be familiar with the specifics of priority inheritance or
  the `futex_lock_pi` function.
primer_general: The Native POSIX Thread Library (NPTL) in glibc provides the implementation
  for threads in Linux. Priority inheritance is a mechanism to avoid priority inversion,
  where a high-priority thread is blocked indefinitely by a low-priority thread holding
  a mutex. `futex_lock_pi` is a function that handles locking a priority inheritance
  mutex. This patch changes how deadlocks are reported when using priority inheritance
  mutexes, providing a more user-friendly error code (`EDEADLK`) instead of a program-terminating
  assertion failure.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PR3PR06MB688971B81D9DF02440A469A9FF2F2@PR3PR06MB6889.eurprd06.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

This patch modifies the deadlock detection mechanism in `futex_lock_pi`. Currently, a deadlock triggers an assertion failure, which can be difficult to debug. The patch proposes changing this behavior to return `EDEADLK` instead, providing a more informative error code. The author seeks feedback on whether to limit this change to error-checking PI mutexes or apply it more broadly.
