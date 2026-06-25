---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- architecture extension
- memory management
- PMP
- processor architecture
discussion_id: e6678628-d55a-4ae7-9e95-718ce11f1709@oss.qualcomm.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Add support for Smpmpmt v0.6 extension'
headline: 'RISC-V: Add support for Smpmpmt v0.6 extension'
tldr: Binutils now supports the RISC-V Smpmpmt v0.6 extension, which enables PMP-based
  memory type control for fine-grained memory attribute management.
proposer: Jeffrey Law <jeffrey.law@oss.qualcomm.com>
consensus: Committed
outcome: committed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Enhances memory control capabilities for RISC-V based systems, allowing for more
  precise management of memory attributes.
- Increased complexity in tooling and software for systems using this extension due
  to its advanced nature.
- Improves security and flexibility for embedded and safety-critical applications
  by enabling fine-grained memory protection and behavior control.
exchanges:
- author: Jeffrey Law <jeffrey.law@oss.qualcomm.com>
  role: proposer
  position: Announces that trivial updates to support RISC-V Smpmpmt v1.0, an extension
    for PMP-based memory types, have been applied and pushed.
  quote: I made the trivial updates as this spec has moved to v1.0 and moved the NEWS
    entry and pushed this.
primer_expert: The RISC-V architecture is modular, with a base instruction set and
  various extensions. Smpmpmt (PMP-based Memory Types) is an optional extension that
  enables fine-grained control over memory attributes (e.g., cacheability, writability)
  at the granularity of Physical Memory Protection (PMP) regions. PMPs are typically
  used for memory access control and protection within a system. This extension, which
  operates similarly to Svpbmt (Page-Based Memory Types) but leverages PMPs, is crucial
  for systems requiring advanced memory management capabilities, such as embedded
  systems or systems with stri…
primer_general: Modern computer processors, like those based on the RISC-V architecture,
  need ways to manage how they access different parts of memory. This involves setting
  various "memory attributes" which dictate how the processor behaves when interacting
  with specific memory regions (e.g., whether data can be cached, or if a region is
  read-only). The Smpmpmt extension is an optional add-on to the RISC-V instruction
  set that provides a more granular way to control these memory attributes. Instead
  of using traditional page tables, it leverages "Physical Memory Protection" (PMP)
  regions, which are hardware mechanisms typically used to define protected memory
  areas. This allows for very precise control over memory access and behavior, important
  for system security and performance in specialized applications.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/e6678628-d55a-4ae7-9e95-718ce11f1709@oss.qualcomm.com
bugzilla_url: null
date: '2026-06-24'
is_stub: false
stub_reason: ''
---

This patch adds support for the RISC-V Smpmpmt (PMP-based Memory Types) v0.6 extension to Binutils. The Smpmpmt extension allows control over memory attributes using Physical Memory Protection (PMP) regions, similar to how page tables manage attributes, but with a different mechanism. The extension, currently in a frozen state, was updated to v1.0, and the necessary changes were made and pushed after trivial updates.
