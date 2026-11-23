---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- build system
- windows
- configuration
discussion_id: SL2P216MB227186D00E8902D4C5BA8117EF462@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
source_type: public_inbox
title: '[RFC] Removing --enable-win32-registry or disabling by default?'
headline: Remove --enable-win32-registry or disable by default
tldr: Proposes removing or disabling the --enable-win32-registry configure option
  due to lack of practical use.
proposer: Zhongteng Gui <dragon-archer@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removing the option simplifies the build system but might break a niche use case
  if one exists.
- Disabling by default is safer but maintains dead code.
exchanges:
- author: Zhongteng Gui <dragon-archer@outlook.com>
  role: proposer
  position: Proposes removing or disabling the --enable-win32-registry configure option,
    as it appears to be unused in practice by Windows GCC distributions and vendors.
  quote: Given this, the option appears to be unused in practice. Removing it would
    simplify configuration and avoid maintaining dead code; default-disabling it would
    be a lower-risk alternative, while still allowing anyone with a real use case
    to opt in explicitly.
primer_expert: This RFC targets the GCC build system, specifically the configuration
  options related to Windows. The --enable-win32-registry option, if enabled, allows
  GCC to register itself in the Windows registry, typically for installer purposes.
  The proposal argues this feature is vestigial and likely unused, impacting build
  system maintenance and potentially introducing subtle configuration issues if relied
  upon.
primer_glossary:
- term: configure option
  definition: A flag passed to the configure script during the build process to customize
    how software is compiled and installed.
- term: Windows registry
  definition: A hierarchical database in Windows used for storing configuration settings
    and options for the operating system and installed applications.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/SL2P216MB227186D00E8902D4C5BA8117EF462@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-11-22'
is_stub: false
stub_reason: ''
---

The proposer questions the utility of the --enable-win32-registry configure option in GCC, citing that major Windows distributions either disable it or do not utilize the registry lookup mechanism. Furthermore, searches for real-world usage of custom registry keys (e.g., --enable-win32-registry=VENDOR-VERSION) yield no results beyond GCC's own documentation. The proposal suggests either removing the option to simplify configuration and dead code, or at least disabling it by default as a lower-risk alternative.
