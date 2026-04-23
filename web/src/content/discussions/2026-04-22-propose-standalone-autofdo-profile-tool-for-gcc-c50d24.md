---
project: gcc
subsystem: rfc
patch_id: null
tags:
- AutoFDO
- profiling
- optimization
- perf
discussion_id: B80EC0EC-AE15-40D9-9F48-A01DE8716639@nvidia.com
source_type: public_inbox
title: 'RFC: Standalone AutoFDO Profile Tool for GCC'
headline: Propose Standalone AutoFDO Profile Tool for GCC
tldr: To replace the current reliance on external Google tools, a native, simplified
  AutoFDO tool for GCC will be created and integrated.
proposer: Kugan Vivekanandarajah <kvivekananda@nvidia.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Development and maintenance costs of a new tool.
- Potential for increased complexity in the GCC build process.
- Risk of introducing new bugs or performance regressions.
exchanges:
- author: Kugan Vivekanandarajah
  role: proposer
  position: Proposes creating a native, simplified AutoFDO tool for GCC, with the
    goal of integrating it into the GCC repository.
  quote: Building on our discussions from the last Cauldron, we propose creating a
    native, simplified AutoFDO tool for GCC to replace our current reliance on external
    Google tools which is not actively maintained.
- author: Andrew Pinski
  role: other
  position: Asks whether this tool will replace the existing AutoFDO tools in GCC.
  quote: null
primer_expert: AutoFDO uses profile information to guide compiler optimizations.  The
  proposal is to create a standalone tool that generates the profiles consumed by
  GCC's AutoFDO. Perf is a performance monitoring tool in Linux that captures data
  which this tool would consume.
primer_general: AutoFDO (Automatic Feedback-Directed Optimization) uses runtime information
  to guide compiler optimizations, improving performance. This proposal is for a new
  tool that will generate the data used by AutoFDO. This tool will replace the existing
  tools, which are not well-maintained, with something that is integrated directly
  into GCC.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/B80EC0EC-AE15-40D9-9F48-A01DE8716639@nvidia.com
bugzilla_url: null
date: '2026-04-22'
---

Kugan Vivekanandarajah proposes creating a standalone AutoFDO tool for GCC. The goal is to replace the current reliance on external Google tools. The new tool would support offline reading of perf.data, direct attach to a process via the PMU, and system-wide reading of perf.data.
