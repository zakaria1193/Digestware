---
project: gcc
subsystem: rfc
patch_id: null
tags: []
discussion_id: CALvbMcDw_ZuVew5yPnrZFOhEy43WVCDundgaYDqGMbcmLgnMGA@mail.gmail.com
source_type: public_inbox
title: 'Re: RFC: Standalone AutoFDO Profile Tool for GCC'
headline: 'RFC: Standalone AutoFDO Profile Tool for GCC'
tldr: Kugan Vivekanandarajah proposes creating a standalone AutoFDO tool for GCC to
  replace the current reliance on external Google tools.
proposer: Andrew Pinski <andrew.pinski@oss.qualcomm.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This RFC proposes creating a standalone AutoFDO tool for GCC to replace
  the current reliance on external Google tools.
primer_general: This RFC proposes a standalone, minimal tool for generating AutoFDO
  profiles that can be consumed by the GCC AutoFDO toolchain, with the goal of integrating
  it into the GCC repository. AutoFDO (Automatic Feedback-Directed Optimization) is
  a technique used to improve the performance of compiled code by using profile data
  collected during program execution.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CALvbMcDw_ZuVew5yPnrZFOhEy43WVCDundgaYDqGMbcmLgnMGA@mail.gmail.com
bugzilla_url: null
date: '2026-04-23'
---

Kugan Vivekanandarajah proposes creating a native, simplified AutoFDO tool for GCC to replace the current reliance on external Google tools. The tool would support offline reading of existing perf.data, direct attach to a process via the PMU, and system-wide reading of perf.data. The goal is to integrate it into the GCC repository, make development easier, and dependent only on libraries such as libdwarf.
