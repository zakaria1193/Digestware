---
project: binutils
subsystem: bfd
patch_id: null
tags:
- bfd
- btf
- debugging
- bpf
discussion_id: 874if6vb73.fsf@gnu.org
source_type: public_inbox
title: 'Re: [PATCH 1/2] bfd: add basic support for BTF debug info'
headline: 'bfd: add basic support for BTF debug info'
tldr: Adds basic support for BPF Type Format (BTF) debugging information to BFD, including
  data structures and decoding functions.
proposer: David Faust <david.faust@oss.qualcomm.com>
consensus: Ready to Land
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Includes new source and header files, increasing codebase size.
exchanges:
- author: Jose E. Marchesi
  role: maintainer
  position: LGTMs the patch, contingent on no objections from global maintainers regarding
    BTF's relation to BPF.
  quote: 'The patch LGTM.


    Assuming that BTF falls within the BPF realm (which I think it is a fair

    assumption, but please wait for a day or so in case some global

    maintainer has some objection) this patch is OK.'
- author: David Faust
  role: proposer
  position: Submits a patch to add basic BTF support to BFD, including data structures
    and helper functions, based on GCC's BTF definitions.
  quote: 'This patch adds basic support for the BPF Type Format (BTF) to BFD.

    This includes definitions for data structures and helper functions for

    decoding the format.


    The added include/btf.h is copied from gcc and extended with prototypes

    for helper functions implemented in BFD.  The intent is to keep the data

    structure names, definitions, macros, etc in sync with that of gcc''s

    btf.h (which in turn is…'
primer_expert: This patch adds BTF (BPF Type Format) support to BFD, the binary file
  descriptor library used by binutils. BTF is a compact DWARF-like metadata format
  used primarily for eBPF programs and increasingly for general kernel and userspace
  debugging. This change involves adding new source and header files to BFD, mirroring
  definitions from GCC's BTF implementation, and integrating them into BFD's build
  system.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a layer of abstraction in GNU binutils
    for handling various object file formats.
- term: BTF
  definition: BPF Type Format, a compact debugging data format used for eBPF programs
    and increasingly in the Linux kernel and userspace.
- term: eBPF
  definition: Extended Berkeley Packet Filter, a technology that allows running sandboxed
    programs in the Linux kernel without changing kernel source code or loading modules.
series_id: 'binutils:bfd: add basic support for btf debug info'
series_role: reply
series_parts:
- title: 'bfd: add basic support for BTF debug info'
  url: https://inbox.sourceware.org/binutils/20260930182209.212167-1-david.faust@oss.qualcomm.com
  n: 1
  total: 2
url: https://inbox.sourceware.org/binutils/874if6vb73.fsf@gnu.org
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch introduces initial support for BTF debug info into BFD. It includes necessary header files and C source code for handling BTF data structures and decoding functions. The changes are intended to align with GCC's BTF definitions, which are based on Linux kernel specifications, enabling BFD to work with BTF-formatted debug information.
