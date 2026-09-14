---
project: gcc
subsystem: rfc
patch_id: null
tags:
- optimization
- profiling
- AutoFDO
- perf
- compiler
discussion_id: D8EE7B98-B161-4822-82C8-733A9AB3763F@nvidia.com
source_type: public_inbox
title: 'Re: RFC: Standalone AutoFDO Profile Tool for GCC'
headline: Standalone AutoFDO Profile Tool for GCC
tldr: Proposal for a standalone AutoFDO profile tool, seeking feedback on perf data
  parsing and potential library reuse.
proposer: Kugan Vivekanandarajah <kvivekananda@nvidia.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Leveraging existing libraries (e.g., libperf) might simplify development but could
  introduce dependencies or interface instability.
- Developing custom parsing offers more control but increases development effort and
  maintenance burden.
- 'Standalone tool vs. integrated approach: Flexibility vs. potential for code duplication
  or integration challenges.'
exchanges:
- author: Kugan Vivekanandarajah <kvivekananda@nvidia.com>
  role: proposer
  position: Seeking input on perf data parsing for a new standalone AutoFDO tool,
    open to using existing libraries or simpler methods.
  quote: We limited the perf parsing to only what we wanted. If there is an easier
    way to seperate this out and use an exiting library, that would be great. I am
    open for suggestions.
- author: Andi Kleen <andi@firstfloor.org>
  role: reviewer
  position: Responds to concerns about perf.data format stability, suggesting that
    while the format is stable, issues might arise from extensions or the perf library's
    handling of unknown ones.
  quote: That perf.data format is stable, but it supports extensions, and the perf
    library that autofdo uses didn't use to ignore unknown ones. I thought that had
    been fixed however. I don't think the format is a problem for a well written reader.
primer_expert: This RFC proposes a new, standalone tool for generating AutoFDO profiles,
  separating it from the existing integrated GCC infrastructure. The core challenge
  discussed is efficient and robust parsing of `perf.data` files, with a focus on
  whether to leverage existing libraries like libperf or implement custom parsing
  logic. The goal is to provide a more flexible profile generation mechanism for compiler-driven
  optimization.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/D8EE7B98-B161-4822-82C8-733A9AB3763F@nvidia.com
bugzilla_url: null
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

Kugan Vivekanandarajah proposes a standalone tool for AutoFDO profiles, distinct from the integrated GCC approach. He is seeking input on how to best handle the parsing of perf.data files and is open to suggestions for using existing libraries or a simpler parsing method. This initiative aims to offer more flexibility in profile data generation for compiler optimizations.
