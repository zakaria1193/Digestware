---
project: binutils
subsystem: binutils
patch_id: null
tags:
- gas
- makefile
- configuration
discussion_id: aqYudEB1JLD2hBaR@squeak.grove.modra.org
source_type: public_inbox
title: Add te-linux.h and te-linux-fdpic.h to TARG_ENV_HFILES
headline: Add te-linux.h and te-linux-fdpic.h to TARG_ENV_HFILES
tldr: Add Linux-specific header files for assembler target environment configuration.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes old configuration files, potentially simplifying maintenance.
exchanges: []
primer_expert: This change modifies gas's Makefile.am to include `te-linux.h` and
  `te-linux-fdpic.h` in `TARG_ENV_HFILES`. This is done in conjunction with removing
  `config/obj-fdpicelf.[ch]`, suggesting a consolidation or update of target-specific
  assembler environment definitions, likely related to Linux and its specific object
  file formats or features.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aqYudEB1JLD2hBaR@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

This patch adds `te-linux.h` and `te-linux-fdpic.h` to the `TARG_ENV_HFILES` in the gas assembler's Makefile. It also tidies up by removing obsolete configuration files related to `obj-fdpicelf`. The change aims to correctly include Linux-specific environment headers for the assembler.
