---
project: binutils
subsystem: binutils
patch_id: null
tags:
- infrastructure
- Git
- scalability
- performance
discussion_id: 272e308a-a703-4824-b823-cd8e5266f00b@redhat.com
source_type: public_inbox
title: '[RFC] Provide horizontally scaled git pull mirrors for the GNU Toolchain,
  starting with glibc.'
headline: 'RFC: Horizontally scaled Git pull mirrors for GNU Toolchain'
tldr: Proposes horizontally scaled, read-only Git mirrors for the GNU Toolchain to
  alleviate bottlenecks on sourceware.org.
proposer: Carlos O'Donell <carlos@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Implementing mirrors adds infrastructure complexity and requires managing eventual
  consistency.
- Read-only mirrors reduce load on the primary server but require careful security
  considerations for write operations.
exchanges:
- author: Carlos O'Donell <carlos@redhat.com>
  role: proposer
  position: Proposes horizontally scaled Git mirrors to address current bottlenecks
    and improve access to toolchain sources.
  quote: This has resulted in a bottleneck at the host, that at times resulted in
    developers being unable to access sources due to IP deny lists, or the disabling
    of HTTPS [1] for secure access.
primer_expert: This RFC addresses scalability issues with the current monolithic git.sourceware.org
  instance serving all read traffic for projects like glibc and binutils-gdb. It suggests
  a horizontally scaled mirror system to improve availability and performance, especially
  for anonymous Git operations (clones, fetches) which are CPU/IO intensive due to
  `git-upload-pack`.
primer_glossary:
- term: GNU Toolchain
  definition: A collection of programming tools developed by the GNU Project, essential
    for software development, including compilers (GCC), assemblers, linkers (Binutils),
    and debuggers (GDB).
- term: Git
  definition: A distributed version control system used for tracking changes in source
    code.
- term: Mirror
  definition: A copy of a repository or server that provides redundancy and can distribute
    load.
- term: RFC
  definition: Request For Comments, a document or process used to solicit feedback
    on a proposed change or idea.
- term: git-upload-pack
  definition: A Git server-side process that handles 'git fetch' and 'git pull' operations,
    responsible for packaging objects to be sent to the client.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/272e308a-a703-4824-b823-cd8e5266f00b@redhat.com
bugzilla_url: null
date: '2026-11-07'
is_stub: false
stub_reason: ''
---

This RFC proposes implementing horizontally scaled, read-only Git mirrors for the GNU Toolchain, starting with glibc. The current single-host setup for Git read traffic has led to bottlenecks, impacting developer access and reliability. By offloading anonymous read traffic to mirrors, the project aims to improve availability and performance for clone and fetch operations, especially from geographically diverse locations or high-traffic CI/CD systems.
