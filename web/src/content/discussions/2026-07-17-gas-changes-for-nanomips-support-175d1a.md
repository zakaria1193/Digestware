---
project: binutils
subsystem: binutils
patch_id: null
tags:
- assembler
- nanomips
- build system
discussion_id: 20260717103858.199743-2-lei.wang@oss.cipunited.com
source_type: public_inbox
title: '[PATCH 1/6] Gas changes for nanoMIPS support.'
headline: Gas changes for nanoMIPS support.
tldr: Adds nanoMIPS target support to the GNU Assembler (Gas).
proposer: Tsing <lei.wang@oss.cipunited.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: Integrates the nanoMIPS architecture into the Gas assembler. This involves
  updating build system configuration files (configure.ac, config.sub, configure.tgt)
  to recognize new target triplets like 'nanomips*-*-elf*' and 'nanomips*-*-linux*'.
  It also introduces new assembler-specific configuration files for nanoMIPS.
primer_glossary: []
series_id: binutils:gas changes for nanomips support
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20260717103858.199743-2-lei.wang@oss.cipunited.com
bugzilla_url: null
date: '2026-07-17'
is_stub: false
stub_reason: ''
---

These patches introduce support for the nanoMIPS architecture in the Gas assembler. Changes include modifying configuration files like configure.ac and config.sub to recognize the nanoMIPS target, regenerating configure scripts, and adding new files for nanoMIPS-specific assembler configurations (tc-nanomips.c, tc-nanomips.h).
