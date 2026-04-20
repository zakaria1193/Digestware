---
project: glibc
subsystem: io
patch_id: null
tags:
- io
- fts
- gnulib
- compatibility
discussion_id: lhuy0iit5cy.fsf@oldenburg.str.redhat.com
source_type: public_inbox
title: 'Re: [PATCH v5 2/2] io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
headline: 'Io: Use gnulib fts implementation (BZ 22944, BZ 20331)'
tldr: This patch updates glibc to use the gnulib fts implementation, but there are
  concerns about compatibility with existing programs.
stakes: Switching to gnulib's fts implementation could improve code quality and maintainability,
  but it risks breaking compatibility with applications that rely on the old behavior.  Symbol
  versioning may be required.
proposer: Florian Weimer <fweimer@redhat.com>
consensus: Proposed
outcome: proposed
sentiment_score: 6
sentiment_rationale: The discussion expresses concerns about compatibility issues.
technical_tradeoffs:
- Adopting gnulib's fts implementation may introduce subtle behavioral changes.
- Compatibility symbols add complexity but might be necessary to avoid breaking existing
  applications.
- Changes should be confined to glibc to avoid complicating gnulib maintenance.
series_id: 'glibc:io: use gnulib fts implementation (bz 22944, bz 20331)'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/lhuy0iit5cy.fsf@oldenburg.str.redhat.com
bugzilla_url: null
date: '2026-04-20'
---

This patch aims to replace the glibc file tree walking implementation with the one from gnulib.  A concern was raised that the change in behavior of fts_nostat might break existing programs such as dracut. The author suggests adding compatibility symbols that perform post-processing to mitigate the impact, and confining the changes to glibc.
