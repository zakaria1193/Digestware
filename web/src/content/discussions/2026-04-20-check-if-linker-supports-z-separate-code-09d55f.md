---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- linker
- -z separate-code
- configure
- build system
discussion_id: PAWPR08MB8982C365D3FBB2440AF45143832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] Check if linker supports -z separate-code'
headline: Check if linker supports -z separate-code
tldr: The purpose of a patch to check for linker support for `-z separate-code` is
  questioned, as the minimum binutils requirement already guarantees its availabilit…
stakes: Potentially avoids unnecessary code in the build system.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Unnecessary code in configure script vs. explicit check for feature support.
- Relying on minimum tool version vs. probing for specific features.
primer_expert: This thread discusses a configure check for `-z separate-code` linker
  support. The question is whether this check is redundant given the minimum binutils
  version required by glibc. The configure script determines which features are available
  during the build process. In this case, it seems the feature in question is already
  guaranteed to be present.
primer_general: When building software, the configure script checks for the presence
  of required tools and libraries. The `-z separate-code` linker option separates
  code into its own segment, which can improve security. This discussion questions
  whether a specific check for this linker option is necessary because glibc's minimum
  tool requirements already ensure that the linker supports it, potentially making
  the check redundant.
series_id: glibc:check if linker supports -z separate-code
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982C365D3FBB2440AF45143832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

Wilco Dijkstra questions the necessity of a patch that checks for linker support for the `-z separate-code` option. The option is already guaranteed to be present due to the minimum required version of binutils. The original author, HJ, mentions it's for adding tests using `-z separate-code` but doesn't clarify why the check is needed.
