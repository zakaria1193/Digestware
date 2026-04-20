---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- linker
- -z separate-code
- build configuration
discussion_id: PAWPR08MB8982C365D3FBB2440AF45143832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] Check if linker supports -z separate-code'
headline: Check if linker supports -z separate-code
tldr: This patch checks if the linker supports the `-z separate-code` option, but
  its necessity is questioned since the minimum binutils requirement should guarantee…
stakes: Potentially impacts build configuration and optimization. Developers might
  need to care if the `-z separate-code` flag is crucial for their builds and the
  check introduces unnecessary complexity.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Potentially adds unnecessary complexity to the build process.
- Could provide a more robust check for linker capabilities.
- May enable the use of `-z separate-code` in subsequent tests and optimizations.
exchanges:
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: proposer
  position: Proposes a patch to check for `-z separate-code` linker support.
  quote: Set have-separate-code to yes if linker supports -z separate-code.
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: reviewer
  position: Questions the necessity of the patch, suggesting it might be redundant.
  quote: Sure, but why do we need this patch at all? What problem does it solve?
primer_expert: The patch probes for linker support of `-z separate-code`, which segregates
  code into separate segments. This can improve security by enabling finer-grained
  memory permissions (e.g., marking code segments read-only). `configure.ac` decides
  the build environment. The minimum binutils requirement in glibc influences which
  linker features are assumed present.
primer_general: The GNU C Library (glibc) provides essential functions for programs.
  Part of building glibc is figuring out what the system's compiler and linker can
  do. This patch is about testing if the linker supports a specific feature (`-z separate-code`).
  This feature helps improve security by separating code from other data in memory,
  making it harder for attackers to inject malicious code. The discussion questions
  if the test is even needed, given the assumed capabilities of the system's toolset.
series_id: glibc:check if linker supports -z separate-code
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982C365D3FBB2440AF45143832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

A patch is proposed to check if the linker supports the `-z separate-code` option, setting `have-separate-code` accordingly.  However, a reviewer questions the patch's purpose, suggesting it might be redundant given the minimum binutils version requirement.  The proposer intends to utilize the `-z separate-code` option in subsequent tests.
