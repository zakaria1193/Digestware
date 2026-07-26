---
project: gcc
subsystem: gcc
patch_id: null
tags:
- git
- repository
- access
- hooks
discussion_id: 89A5A301-A04D-4C36-8226-6CDFCF5BD8B1@gmail.com
source_type: public_inbox
title: 'Re: GCC repo is locked?'
headline: GCC repo is locked?
tldr: Repository push hook issues prompt discussion on using main repo for personal
  branches.
proposer: Richard Biener <richard.guenther@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Centralizing personal branches in the main repository simplifies some workflows
  but increases the risk of such lockouts.
- Using external hosting for personal branches reduces contention on the main repository
  but adds an extra step for developers.
exchanges:
- author: Richard Biener <richard.guenther@gmail.com>
  role: proposer
  position: Suggests evaluating the efficiency of the scripts causing the push hook
    issues, implying they could be optimized.
  quote: Then just don’t run them …. There must be also inefficiencies in the scripts.
- author: Jonathan Wakely <fmtoc@redhat.com>
  role: reviewer
  position: Agrees with discouraging personal branches in the main repo, pointing
    to Forge.sourceware.org as an alternative.
  quote: 'Yes, or forge.sourceware.org


    There''s no good reason to use the main gcc.gnu.org repo for personal branches.
    And since this keeps happening maybe we should discourage or even disallow personal
    branches in the main repo.'
- author: Mikael Morin <morin-mikael@orange.fr>
  role: contributor
  position: Acknowledges causing the issue due to a misunderstanding about killing
    push hook processes.
  quote: 'I''m afraid I''m (again) the cause of this.

    I posted a message on IRC telling anyone could kill the push hook

    process(es). I''m not sure it reached the right people (or someone at all).'
primer_expert: This discussion concerns access issues to the main GCC development
  repository. Specifically, repeated 'push hook declined' errors are hindering developers.
  The core of the problem appears to be contention or issues with server-side hooks,
  possibly related to personal branches being pushed to the main repository.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/89A5A301-A04D-4C36-8226-6CDFCF5BD8B1@gmail.com
bugzilla_url: null
date: '2026-07-25'
is_stub: false
stub_reason: ''
---

A user reported being unable to push to the GCC repository due to a "Another user is currently pushing" message, indicating a lock on the repository. This has recurred, leading to a discussion about discouraging or disallowing personal branches in the main repository, with suggestions to use external hosting like Gitlab or sourceware.org instead.
