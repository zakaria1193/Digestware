---
project: gcc
subsystem: unknown
patch_id: null
discussion_id: CAFULd4a1_CR=NGZUU1X+EfuT0=Ge5d_32R4dNHN8S0mVPBe8dg@mail.gmail.com
source_type: public_inbox
title: 'RFC: Another pass_late_combine after pass_reorder_blocks?'
proposer: Uros Bizjak <ubizjak@gmail.com>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/gcc/CAFULd4a1_CR=NGZUU1X+EfuT0=Ge5d_32R4dNHN8S0mVPBe8dg@mail.gmail.com
bugzilla_url: null
date: '2026-04-16'
---

Hello!

After pass_reorder_blocks, there remain some propagating opportunities
for late_combine.  Looking at gcc.target/i386/pr90178.c, we get a
trivial sequence of:

gcc -O2 -mavx -mvzeroupper -m32:

