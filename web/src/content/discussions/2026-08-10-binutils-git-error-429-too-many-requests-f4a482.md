---
project: binutils
subsystem: binutils
patch_id: null
tags: []
discussion_id: a05a8ffd-2c84-41f9-b24a-a1526380ad3b@gjlay.de
source_type: public_inbox
title: 'binutils git: error 429 (too many requests)'
headline: 'binutils git: error 429 (too many requests)'
tldr: Georg-Johann Lay encounters '429 Too Many Requests' error when fetching binutils-gdb,
  suspects scraper bots or recent Anubis updates.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Georg-Johann Lay
  role: proposer
  position: Reports receiving '429 Too Many Requests' errors when trying to git pull
    from binutils-gdb repository.
  quote: "I am getting that error when I try to git pull from\n\ngjl@cfarm121:~/gnu/source/binutils-master$\
    \ cat .git/config\n[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n\t\
    bare = false\n\tlogallrefupdates = true\n[remote \"origin\"]\n\turl = https://sourceware.org/git/binutils-gdb.git\n\
    \tfetch = +refs/heads/*:refs/remotes/origin/*\n[branch \"master\"]\n\tremote =\
    \ origin\n\tmerge = refs/heads/master\ngjl@cfarm121:~/gnu/…"
primer_expert: null
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/a05a8ffd-2c84-41f9-b24a-a1526380ad3b@gjlay.de
bugzilla_url: null
date: '2026-08-10'
is_stub: false
stub_reason: ''
---

Georg-Johann Lay is experiencing '429 Too Many Requests' errors when attempting to 'git fetch' from the binutils-gdb repository on sourceware.org. He reports this on a cfarm machine and notes that he has not made an excessive number of requests, suggesting potential issues with scraper bot activity or recent changes to the Anubis service.
