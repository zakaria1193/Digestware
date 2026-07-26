---
project: gcc
subsystem: gcc
patch_id: null
tags:
- git
- repository
- push
- hook
- lock
discussion_id: CAMe9rOrW5KaH5Od1dz=v1kuknOONHRQjQWYXRsznsaCUu6saMA@mail.gmail.com
source_type: public_inbox
title: GCC repo is locked?
headline: GCC repo is locked?
tldr: Pushing to GCC repository blocked by hook, but resolved after process termination.
proposer: '"H.J. Lu" <hjl.tools@gmail.com>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 8
technical_tradeoffs:
- The locking mechanism prevents race conditions during pushes but can cause temporary
  unavailability if a process hangs or is misunderstood.
- Manual intervention is required to resolve hook-related deadlocks, highlighting
  a potential need for more robust automated recovery or clearer protocols.
exchanges:
- author: Mark Wielaard <mark@klomp.org>
  role: proposer
  position: Informed the original poster that the blocking push hook process was terminated
    and the lock file removed, allowing pushes again.
  quote: 'Killed the process and removed the git-hooks::update.token.lock.

    So pushed should be possible again.'
- author: Mikael Morin <morin-mikael@orange.fr>
  role: contributor
  position: Acknowledged being the cause of the problem, explaining they tried to
    kill a push hook process and were unsure if it reached the right people.
  quote: 'I''m afraid I''m (again) the cause of this.

    I posted a message on IRC telling anyone could kill the push hook

    process(es). I''m not sure it reached the right people (or someone

    at all).'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: other
  position: Reported the initial problem of being unable to push to the repository
    due to an active hook.
  quote: 'I have been trying to push for the last 15 minutes and getting:


    remote: -- Another user is currently pushing changes to this repository.  --

    remote: -- Please try again in another minute or two.                     --

    remote:

    error: hook declined to update refs/heads/master'
primer_expert: This thread addresses a temporary repository access issue on GCC development
  infrastructure. A push operation was blocked by a server-side hook, specifically
  a lock file mechanism that prevents concurrent pushes. The issue was resolved by
  manually terminating the blocking process and clearing the lock.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAMe9rOrW5KaH5Od1dz=v1kuknOONHRQjQWYXRsznsaCUu6saMA@mail.gmail.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

A developer reported being unable to push to the GCC repository for 15 minutes due to a "Another user is currently pushing" error, indicating a hook declined the update. Another participant confirmed they were the cause, having attempted to kill a push hook process, and subsequently terminated the process and removed the lock file, resolving the issue.
