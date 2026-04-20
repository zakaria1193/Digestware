---
project: glibc
subsystem: glibc
patch_id: null
tags:
- glibc
- linker
- configure
- build system
- optimization
discussion_id: PAWPR08MB8982C365D3FBB2440AF45143832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] Check if linker supports -z separate-code'
headline: Check if linker supports `-z separate-code`.
tldr: Questioning the necessity of a patch that checks for linker support for `-z
  separate-code` when the minimum binutils version already guarantees it.
stakes: Potentially simplifies the configuration process by removing an unnecessary
  check.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
sentiment_rationale: ''
technical_tradeoffs:
- Potential simplification of the configuration process.
- Removal of a potentially redundant check.
- Reliance on the minimum binutils version for `-z separate-code` support.
primer_expert: This patch likely modifies `configure.ac` to check for linker support
  for `-z separate-code`. The minimum binutils version ensures that this option is
  supported, so this check is redundant. The discussion questions the purpose of this
  configure check if it's always true. This relies on `AC_LINK_IFELSE` or similar
  macros.
primer_general: When building software, the configuration step checks for the presence
  of necessary tools and libraries.  This discussion revolves around a check for a
  specific feature in the linker, a program that combines compiled code into an executable.
  The `-z separate-code` option tells the linker to put code in a separate segment,
  which can improve security. The question is whether this check is still needed,
  given the minimum required version of the linker toolchain.
series_id: glibc:check if linker supports -z separate-code
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982C365D3FBB2440AF45143832F2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-20'
---

This email questions the purpose of a patch that checks if the linker supports the `-z separate-code` option. The author argues that the minimum binutils version required by glibc already ensures that this option is available, making the check redundant. It seeks clarification on the problem that this patch is intended to solve.
