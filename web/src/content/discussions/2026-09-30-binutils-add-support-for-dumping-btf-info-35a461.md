---
project: binutils
subsystem: binutils/objdump
patch_id: null
tags:
- objdump
- btf
- debugging
- bpf
discussion_id: 87zewytwlq.fsf@gnu.org
source_type: public_inbox
title: 'Re: [PATCH 2/2] binutils: add support for dumping BTF info'
headline: 'binutils: add support for dumping BTF info'
tldr: Adds an --btf option to objdump for displaying BTF section contents in a text
  format compatible with bpftool.
proposer: David Faust <david.faust@oss.qualcomm.com>
consensus: Ready to Land
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adds new functionality to objdump, increasing its complexity.
exchanges:
- author: Jose E. Marchesi
  role: maintainer
  position: LGTMs the patch, reiterating the previous comment about BTF's relation
    to BPF.
  quote: 'This patch also LGTM.


    Same remark than about the other email:


    Assuming that BTF falls within the BPF realm (which I think it is a fair

    assumption, but please wait for a day or so in case some global

    maintainer has some objection) this patch is OK.


    Thanks!'
- author: David Faust
  role: proposer
  position: Submits a patch to add an objdump option for dumping BTF section contents.
  quote: "This patch adds a new command line option --btf[=SECTION] to objdump to\n\
    dump a textual representation of the BTF data stored in section SECTION.\nIf no\
    \ section name is given, then the default of .BTF is used.\n\nThe textual representation\
    \ is the same as used by the Linux kernel\n bpftool utility."
primer_expert: This change adds a new command-line option to `objdump` for parsing
  and displaying the contents of BTF (BPF Type Format) sections. BTF is a metadata
  format used by eBPF and increasingly by the kernel, often residing in a `.BTF` section.
  This patch enables `objdump` to decode this section and present it in a human-readable
  text format, aligning with the output of the `bpftool` utility for consistency.
primer_glossary:
- term: objdump
  definition: A common utility in binutils for displaying information from object
    files, including disassembly.
- term: BTF
  definition: BPF Type Format, a compact debugging data format used for eBPF programs
    and increasingly in the Linux kernel and userspace.
- term: bpftool
  definition: A Linux utility used to interact with eBPF programs and related kernel
    features, capable of dumping BTF information.
- term: section
  definition: A part of an object file or executable that contains specific types
    of data, such as code (.text), initialized data (.data), or debugging information
    (.BTF, .debug_info).
series_id: 'binutils:binutils: add support for dumping btf info'
series_role: reply
series_parts:
- title: 'binutils: add support for dumping BTF info'
  url: https://inbox.sourceware.org/binutils/20260930182209.212167-2-david.faust@oss.qualcomm.com
  n: 2
  total: 2
url: https://inbox.sourceware.org/binutils/87zewytwlq.fsf@gnu.org
bugzilla_url: null
date: '2026-09-30'
is_stub: false
stub_reason: ''
---

This patch introduces the `--btf[=SECTION]` option to `objdump`, enabling it to display the contents of a specified BTF section. The output format is designed to be compatible with the Linux kernel's `bpftool` utility. This enhancement allows developers to inspect BTF debug information directly using objdump.
