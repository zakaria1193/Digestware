---
project: gcc
subsystem: gcc
patch_id: null
tags:
- repository management
- git
- workflow
- infrastructure
discussion_id: CAH6eHdQOFhEcT5knmeUOgb2Y3edmJxTpE16TwO8k=GSwB2MVfA@mail.gmail.com
source_type: public_inbox
title: 'Re: GCC repo is locked?'
headline: Discourage personal branches in the main GCC repository
tldr: Discussion on discouraging or disallowing personal branches in the main GCC
  repository due to recurring push hook issues.
proposer: Jonathan Wakely <jwakely.gcc@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Potential inconvenience for developers who prefer using the main repository for
  all their work.
- Requires developers to manage separate repositories for personal work, adding a
  small layer of complexity.
- Improved stability and reliability of the main repository's push operations.
exchanges:
- author: H.J. Lu via Gcc
  role: contributor
  position: Reports experiencing push failures due to "Another user is currently pushing
    changes to this repository."
  quote: 'I have been trying to push for the last 15 minutes and getting:


    Enumerating objects: 18, done.

    Counting objects: 100% (18/18), done.

    Delta compression using up to 8 threads

    Compressing objects: 100% (10/10), done.

    Writing objects: 100% (10/10), 2.37 KiB | 485.00 KiB/s, done.

    Total 10 (delta 8), reused 0 (delta 0), pack-reused 0 (from 0)

    remote:

    ---------------------------------------------------…'
- author: Mikael Morin via Gcc
  role: contributor
  position: Takes responsibility for the issue, stating they are "again" the cause
    and mentioning they posted on IRC about it.
  quote: 'I''m afraid I''m (again) the cause of this.

    I posted a message on IRC telling anyone could kill the push hook

    process(es).  I''m not sure it reached the right people (or someone at

    all).'
- author: Jonathan Wakely <jwakely.gcc@gmail.com>
  role: maintainer
  position: Suggests using personal repositories like GitLab/GitHub or forge.sourceware.org
    instead of the main GCC repo for personal branches to avoid such conflicts.
  quote: 'Yes, or forge.sourceware.org


    There''s no good reason to use the main gcc.gnu.org repo for personal

    branches. And since this keeps happening maybe we should discourage or even

    disallow personal branches in the main repo. The server hooks that we want

    in place for the official branches are not suitable for personal branches

    and just cause these problems.'
primer_expert: This discussion addresses recurring issues with push operations on
  the main GCC repository, caused by users pushing personal branches. These pushes
  interfere with server-side hooks that are critical for maintaining official branches.
  The maintainer suggests that personal work should be kept off the main repository
  to prevent these conflicts.
primer_glossary:
- term: push hook
  definition: A server-side script that runs automatically when a user attempts to
    push changes to a Git repository. It can be used to enforce policies, perform
    checks, or reject pushes that do not meet certain criteria.
- term: refs/heads/master
  definition: In Git, 'refs/heads/' is a namespace for symbolic references to the
    tips of local branches. 'master' typically refers to the main development branch
    of a repository.
- term: personal branches
  definition: Branches in a Git repository that are used by individual developers
    for their own work, often experimental or not yet ready for integration into the
    main development line.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAH6eHdQOFhEcT5knmeUOgb2Y3edmJxTpE16TwO8k=GSwB2MVfA@mail.gmail.com
bugzilla_url: null
date: '2026-07-25'
is_stub: false
stub_reason: ''
---

This thread discusses recent issues with the GCC repository being temporarily locked due to users pushing personal branches, which interferes with server hooks intended for official branches. Jonathan Wakely suggests that personal branches should be discouraged or disallowed in the main repository, recommending alternatives like personal gitlab/github repositories or forge.sourceware.org for such work to avoid recurring problems with server hooks.
