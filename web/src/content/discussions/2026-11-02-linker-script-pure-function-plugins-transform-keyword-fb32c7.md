---
project: binutils
subsystem: binutils
patch_id: null
tags:
- linker
- plugins
- linker-scripts
- build-system
discussion_id: CAN30aBF5p8+fZ3KkcG7G=NNjtK+5VeMavy7oMDk2E_MkVzxMzw@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] Linker script pure function plugins - TRANSFORM keyword'
headline: Linker script pure function plugins - TRANSFORM keyword
tldr: Proposes adding a TRANSFORM directive to linker scripts to allow plugins to
  transform section data.
proposer: Fangrui Song <i@maskray.me>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Extending the linker script language adds complexity but enables more sophisticated
  build-time transformations.
- Coordinating with LLVM lld for ABI and syntax compatibility requires ongoing effort.
- Ensuring plugin functions are pure and deterministic is crucial for correctness.
exchanges:
- author: Fangrui Song <i@maskray.me>
  role: proposer
  position: Proposes adding a TRANSFORM directive to linker scripts to allow plugins
    to transform section data, referencing an RFC by Xiangfei Ding.
  quote: 'We propose extending GNU ld and the shared plugin interface in include/plugin-api.h
    to support link-time data transformations in linker scripts via a new output section
    directive, `TRANSFORM`.


    We will coordinate this design with LLVM lld developers so that both linkers share
    an identical C ABI and matching linker script syntax.


    Linker scripts today cannot transform section data. When a build sy…'
primer_expert: This RFC introduces a `TRANSFORM` directive for GNU ld linker scripts,
  allowing plugins to perform data transformations on sections. This feature aims
  to integrate tasks like compression or integrity checking directly into the link-time
  process, reducing the need for external tooling and improving debugging information
  preservation, as seen in kernel and firmware build flows.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAN30aBF5p8+fZ3KkcG7G=NNjtK+5VeMavy7oMDk2E_MkVzxMzw@mail.gmail.com
bugzilla_url: null
date: '2026-11-02'
is_stub: false
stub_reason: ''
---

This RFC proposes extending GNU ld and its plugin interface with a `TRANSFORM` directive. This directive would allow linker scripts to invoke pure, side-effect-free functions provided by plugins to manipulate section data. The goal is to enable use cases like firmware compression and integrity digests directly within the linker, avoiding complex out-of-band scripting and potential loss of debug information.
