---
project: binutils
subsystem: binutils
patch_id: null
tags:
- patch
- binutils
- loongarch
- internationalization
- i18n
discussion_id: arRo0w5TSRdmk1sp@squeak.grove.modra.org
source_type: public_inbox
title: '/usr/bin/xgettext: Non-ASCII string at loongarch-dis.c:452.'
headline: Fix non-ASCII string in LoongArch disassembler
tldr: Removes non-ASCII characters from comments in the LoongArch disassembler source
  code.
proposer: Alan Modra
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch cleans up comments in `opcodes/loongarch-dis.c` by replacing
  non-ASCII hyphens with standard ASCII hyphens. The motivation is to resolve issues
  with `xgettext`, a tool used for extracting translatable strings. The affected comments
  describe the layout of the `dbar` instruction's annotation field.
primer_glossary:
- term: xgettext
  definition: A command-line utility that extracts translatable strings from source
    code files, used in the GNU gettext framework for internationalization.
- term: LoongArch
  definition: An instruction set architecture (ISA) developed by Loongson Technology,
    primarily for use in China.
- term: disassembler
  definition: A program that translates machine code (binary instructions) back into
    a human-readable assembly language format.
- term: dbar
  definition: Likely refers to a specific instruction or a type of barrier in the
    LoongArch architecture, possibly related to memory ordering or synchronization.
- term: annotate
  definition: To add explanatory notes or comments to code or data.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/arRo0w5TSRdmk1sp@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

This patch addresses an issue reported by `xgettext` regarding non-ASCII characters in the LoongArch disassembler's source code. Specifically, it fixes two non-ASCII '-' characters within comments in the `loongarch-dis.c` file to ensure proper handling by internationalization tools.
