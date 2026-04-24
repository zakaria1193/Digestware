---
project: gcc
subsystem: rfc
patch_id: null
tags:
- AutoFDO
- profiling
- optimization
- toolchain
discussion_id: B80EC0EC-AE15-40D9-9F48-A01DE8716639@nvidia.com
source_type: public_inbox
title: 'RFC: Standalone AutoFDO Profile Tool for GCC'
headline: Propose standalone AutoFDO profile tool for GCC
tldr: A standalone AutoFDO profile generation tool is proposed for GCC to replace
  the current reliance on external tools.
proposer: Kugan Vivekanandarajah <kvivekananda@nvidia.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Developing and maintaining a new tool requires resources.
- A standalone tool may duplicate functionality already present in existing tools.
- Integration with GCC may introduce dependencies and compatibility issues.
exchanges:
- author: Kugan Vivekanandarajah <kvivekananda@nvidia.com>
  role: proposer
  position: Proposes a standalone, minimal AutoFDO profile generation tool for GCC
    to replace reliance on external Google tools.
  quote: Building on our discussions from the last Cauldron, we propose creating a
    native, simplified AutoFDO tool for GCC to replace our current reliance on external
    Google tools which is not actively maintained.
- author: Andrew Pinski <andrew.pinski@oss.qualcomm.com>
  role: other
  position: Acknowledges the proposal.
  quote: null
primer_expert: AutoFDO uses runtime profiles to guide compiler optimizations. Currently
  GCC relies on external tools for profile generation. This RFC proposes a standalone,
  in-tree tool for generating these profiles, simplifying the process and reducing
  dependencies. The tool would parse perf.data and DWARF information.
primer_general: AutoFDO (Automatic Feedback-Directed Optimization) is a compiler optimization
  technique that uses information collected during program execution to improve performance.
  This proposal aims to create a dedicated tool within the GCC compiler to generate
  the necessary feedback data. The tool would analyze performance data and generate
  profiles that the compiler can use to optimize the code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/B80EC0EC-AE15-40D9-9F48-A01DE8716639@nvidia.com
bugzilla_url: null
date: '2026-04-22'
---

Kugan Vivekanandarajah proposes creating a standalone, minimal tool for generating AutoFDO profiles for GCC. The goal is to replace the current reliance on external, unmaintained Google tools. The proposed tool would support offline profile generation from perf.data, direct process attachment via PMU, and system-wide profile generation. The tool aims for simplicity and minimal dependencies.
