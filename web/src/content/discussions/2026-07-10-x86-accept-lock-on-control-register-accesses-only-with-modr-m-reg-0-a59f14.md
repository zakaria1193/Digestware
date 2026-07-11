---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- assembler
- disassembler
- MOV to CR
- LOCK prefix
discussion_id: CAKSQd8W9qdwvq8gFGPheYJnExeq5yeCUsNLx6doR-OEdmFqtJA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] x86: accept LOCK on control register accesses only with ModR/M.reg
  == 0'
headline: 'x86: accept LOCK on control register accesses only with ModR/M.reg == 0'
tldr: Discussion on MOV to/from control registers, including variants and LOCK prefix
  handling.
proposer: Christian Ludloff <ludloff@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: 5
technical_tradeoffs: []
exchanges:
- author: Christian Ludloff <ludloff@gmail.com>
  role: proposer
  position: Explains the four historical variants of MOV to/from control registers
    (CR0/2/3, CR4, CR0-4/8, CR8D) and their suffixes, noting that some tools support
    a wider range of encoded registers.
  quote: 'If you zoom out, there are four variants of MOV

    from/to CRx, listed here in chronological order:


    1) 32-bit CR0/2/3 (386, !PM64)

    2) 32-bit CR4 (486, !PM64)

    3) 64-bit CR0/2/3/4/8 (x64, PM64)

    4) 32-bit CR8D (LockMovCr0/AltMovCr8, !PM64)


    In theory 1) and 2) are D-suffixed just like 4). As

    they predate x86, the suffix was always omitted.


    Some tools support the entire 0-7/15/31 ranges

    that can be en…'
- author: Jan Beulich <jbeulich@suse.com>
  role: contributor
  position: Adds a fifth variant for 64-bit CR8 (LockMovCr0/AltMovCr8, PM64) and notes
    that gas would not encode CR8 accesses in this manner, though suggests offering
    a way to do so.
  quote: '5) 64-bit CR8 (LockMovCr0/AltMovCr8, PM64)


    gas wouldn''t encode CR8 accesses like this (albeit from an abstract pov

    we probably should offer a way to do so, just that I can''t think of any

    reasonable one),'
primer_expert: Discussion centers on x86 MOV to/from control registers (CR0-CR8).
  The core issue is how the assembler and disassembler interpret LOCK prefixes on
  these instructions, which are historically restricted (e.g., to ModR/M.reg == 0
  for control registers and specific CRs like CR0/CR8). This RFC and follow-up explore
  instruction encoding, feature flags (like `altmovcr8`), and historical nuances across
  different CPU generations and instruction set extensions.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAKSQd8W9qdwvq8gFGPheYJnExeq5yeCUsNLx6doR-OEdmFqtJA@mail.gmail.com
bugzilla_url: null
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

Christian Ludloff clarifies the four variants of MOV from/to CRx instructions, including D-suffixed versions. Jan Beulich adds a fifth variant for 64-bit CR8 and notes that gas wouldn't encode CR8 accesses in a certain way. The thread discusses the nuances of these instructions and potential assembler support.
