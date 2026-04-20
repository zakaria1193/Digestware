---
project: glibc
subsystem: glibc
patch_id: null
tags:
- linker
- separate-code
- configure
- build
discussion_id: PAWPR08MB8982C365D3FBB2440AF45143832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] Check if linker supports -z separate-code'
headline: Check if linker supports -z separate-code
tldr: A test is being added that uses -z separate-code, and this patch avoids changing
  configure.ac when changing the test patch.
stakes: This change is related to code separation which can have performance and security
  implications. Developers may need to understand how it affects their code.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Adding a configure check adds complexity to the build process.
- Not adding the check might require modifying configure.ac more often during test
  development.
primer: The `-z separate-code` linker option places code in a separate segment, potentially
  improving security by making it harder to overwrite code and data. It can also improve
  performance in some cases by reducing the working set size. The configure.ac file
  is used to configure the build environment for glibc. `binutils` is a collection
  of binary tools, including the linker.
series_id: glibc:check if linker supports -z separate-code
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982C365D3FBB2440AF45143832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

This patch adds a check to see if the linker supports the `-z separate-code` option. This is being done to avoid having to modify configure.ac when the test patch that uses `-z separate-code` is modified. The reviewer is questioning the necessity of this patch, as the minimum binutils requirement already ensures this option is available.
