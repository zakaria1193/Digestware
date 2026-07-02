---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- assembler
- optimization
- Valgrind
discussion_id: 7d755d49-de39-4c72-9536-7174e8636454@suse.com
source_type: public_inbox
title: 'Re: [PATCH 1/2] x86: optimize XCHG to MOV for same-register forms'
headline: 'x86: Optimize XCHG to MOV for same-register forms'
tldr: Suggests using pseudo-prefix or directives to prevent XCHG to MOV optimization
  for same-register forms.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Disabling optimization may slightly increase code size or reduce performance in
  unaffected cases.
- Using assembler directives adds complexity to the source code.
- Ensures correct behavior for analysis tools that depend on `XCHG` semantics.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Suggests using the {nooptimize} pseudo-prefix, .insn, or .byte directives
    to prevent the XCHG to MOV optimization for same-register forms.
  quote: Use the {nooptimize} pseudo-prefix, or .insn, or (as suggested by Michael)
    .byte? (Since {nooptimize} has been around for quite a bit longer than .insn,
    .insn likely is the poorest of the possible options.)
primer_expert: This RFC addresses an optimization in the x86 assembler (gas) where
  `XCHG reg, reg` is converted to `MOV reg, reg`. This optimization, while generally
  beneficial, can cause issues for tools like Valgrind which rely on the precise semantics
  of `XCHG` for register tracking. The proposed solution involves using assembler
  directives to explicitly disable this transformation for specific code sections.
primer_glossary: []
series_id: 'binutils:x86: optimize xchg to mov for same-register forms'
series_role: reply
series_parts:
- title: 'x86: optimize XCHG to MOV for same-register forms'
  url: https://inbox.sourceware.org/binutils/7bc70e07-22ce-4dcc-ba5a-7e39ebd00964@suse.com
  n: 1
  total: 2
- title: 'x86: optimize XCHG to MOV for same-register forms'
  url: https://inbox.sourceware.org/binutils/7abeeb9e-649f-d33b-8214-47e0aa35613f@suse.de
  n: 1
  total: 2
- title: 'x86: optimize XCHG to MOV for same-register forms'
  url: https://inbox.sourceware.org/binutils/0c43fa1efaee0789c878638e4ccb9cc250bbc2b3.camel@klomp.org
  n: 1
  total: 2
- title: 'x86: optimize XCHG to MOV for same-register forms'
  url: https://inbox.sourceware.org/binutils/87pl15khzc.fsf@gentoo.org
  n: 1
  total: 2
- title: 'x86: optimize XCHG to MOV for same-register forms'
  url: https://inbox.sourceware.org/binutils/e70ae023-b4fa-4e28-a6e0-834336d5d6a3@suse.com
  n: 1
  total: 2
- title: 'x86: optimize XCHG to MOV for same-register forms'
  url: https://inbox.sourceware.org/binutils/87y0fuj56r.fsf@gentoo.org
  n: 1
  total: 2
url: https://inbox.sourceware.org/binutils/7d755d49-de39-4c72-9536-7174e8636454@suse.com
bugzilla_url: null
date: '2026-07-02'
is_stub: false
stub_reason: ''
---

This discussion centers on preventing the x86 assembler from optimizing `XCHG` instructions with identical source and destination registers into `MOV` instructions. Such optimizations can interfere with certain toolchain analyses, like those performed by Valgrind, especially when inline assembly is used in headers. The proposer suggests using `.nooptimize`, `.insn`, or `.byte` directives to disable this specific optimization.
