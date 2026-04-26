---
project: glibc
subsystem: readme
patch_id: null
tags:
- readme
- glibc
- bug reporting
- documentation
- url
discussion_id: 767b8851c63dd6552c0323bea3a5c37d0ebef69f.1776980796.git.ashamil435@gmail.com
source_type: public_inbox
title: '[PATCH] README: fix stale bug-reporting URL [BZ #34094]'
headline: 'Readme: Fix stale bug-reporting URL [BZ #34094]'
tldr: Updates the bug reporting URL in the glibc README file to point to the Bugzilla
  Procedures page.
proposer: Shamil Abdulaev <ashamil435@gmail.com>
consensus: Proposed
outcome: ready
sentiment_score: 9
technical_tradeoffs:
- Ensures users are directed to the correct bug reporting information.
- Maintains up-to-date documentation.
exchanges:
- author: Shamil Abdulaev <ashamil435@gmail.com>
  role: proposer
  position: Proposes to point to the glibc wiki Bugzilla Procedures page instead.
  quote: 'The URL https://www.gnu.org/software/libc/bugs.html now redirects to

    a page with no bug-reporting instructions.  Point to the glibc wiki

    Bugzilla Procedures page instead.'
- author: '"H.J. Lu" <hjl.tools@gmail.com>'
  role: reviewer
  position: Reviewed and approved with "OK".
  quote: null
primer_expert: This patch updates the README file in glibc to point to the correct
  URL for bug reporting procedures. The previous URL was stale, leading to a dead
  link.
primer_general: The README file in a software project provides essential information
  for users and developers. This patch updates the glibc README file to provide a
  working link to the bug reporting instructions, ensuring users can properly report
  issues they encounter.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/767b8851c63dd6552c0323bea3a5c37d0ebef69f.1776980796.git.ashamil435@gmail.com
bugzilla_url: null
date: '2026-04-23'
---

Shamil Abdulaev proposes updating the bug reporting URL in the glibc README file. The old URL redirects to a page without bug-reporting instructions, and this patch updates it to point to the glibc wiki Bugzilla Procedures page. H.J. Lu has reviewed and approved the changes.
