---
project: gcc
subsystem: rfc
patch_id: null
tags:
- AutoFDO
- profile
- optimization
- perf
- tool
discussion_id: B80EC0EC-AE15-40D9-9F48-A01DE8716639@nvidia.com
source_type: public_inbox
title: 'RFC: Standalone AutoFDO Profile Tool for GCC'
headline: Propose Standalone AutoFDO Profile Tool for GCC
tldr: Kugan Vivekanandarajah proposes creating a native, simplified AutoFDO tool for
  GCC, replacing the current reliance on external Google tools.
proposer: Kugan Vivekanandarajah <kvivekananda@nvidia.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Development and maintenance overhead for a new tool.
- Potential duplication of functionality with existing tools.
- Risk of introducing new bugs or performance regressions.
exchanges:
- author: Kugan Vivekanandarajah <kvivekananda@nvidia.com>
  role: proposer
  position: Proposes creating a standalone AutoFDO profile tool for GCC to replace
    existing external tools.
  quote: Building on our discussions from the last Cauldron, we propose creating a
    native, simplified AutoFDO tool for GCC to replace our current reliance on external
    Google tools which is not actively maintained.
- author: Andrew Pinski
  role: other
  position: Acknowledges the proposal.
  quote: '> Hi,

    >

    > Building on our discussions from the last Cauldron, we propose creating a native,
    simplified AutoFDO tool for GCC to replace our current reliance on external Google
    tools which is not actively maintained.

    >

    > Thanks,

    > Kugan'
primer_expert: AutoFDO (Automatic Feedback-Directed Optimization) uses runtime profile
  data to guide compiler optimizations.  perf.data contains performance counter samples.  This
  proposal aims to create a GCC-native tool to process perf data into AutoFDO profiles,
  reducing external dependencies and easing maintenance.
primer_general: Profile-guided optimization (PGO) uses runtime data to improve compiler
  optimization decisions. AutoFDO is a type of PGO that automates the process using
  performance counters. This proposal suggests building a dedicated tool within the
  GCC project to generate the profiles needed for AutoFDO, simplifying the process
  and reducing reliance on external tools.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/B80EC0EC-AE15-40D9-9F48-A01DE8716639@nvidia.com
bugzilla_url: null
date: '2026-04-22'
---

Kugan Vivekanandarajah proposes creating a standalone, minimal tool for generating AutoFDO profiles that can be consumed by the GCC AutoFDO toolchain. The goal is to integrate it into the GCC repository and replace the current reliance on external Google tools. The tool would support reading existing perf.data, direct attach to a process via the PMU, and system-wide perf.data collection.
