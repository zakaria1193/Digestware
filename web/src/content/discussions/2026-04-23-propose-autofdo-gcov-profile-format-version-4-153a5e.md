---
project: gcc
subsystem: rfc
patch_id: null
tags:
- AutoFDO
- GCOV
- profiling
- optimization
discussion_id: 60ca9a58-3a23-46b1-8e7d-0e5649e72f45@nvidia.com
source_type: public_inbox
title: 'RFC: AutoFDO GCOV Profile Format Version 4'
headline: Propose AutoFDO GCOV Profile Format Version 4
tldr: A redesigned GCOV profile format enables partial reads, forward compatibility,
  reduced file size, and a textual format for inspection.
proposer: Dhruv Chawla <dhruvc@nvidia.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Increased complexity of the format.
- Potential overhead of the new encoding schemes.
- Need to update existing tools to support the new format.
exchanges:
- author: Dhruv Chawla
  role: proposer
  position: Proposes a new version of the AutoFDO GCOV profile format that is backwards-compatible
    and extensible.
  quote: Per prior discussions, here is the specification we are proposing for version
    4 of the AutoFDO GCOV profile format. This is a complete re-design focused around
    being a backwards-compatible and extensible format which can be partially read
    by the compiler.
- author: Jose E. Marchesi
  role: other
  position: Asks for a sample data file.
  quote: Could you please send me (off list) a sample data file, as complete as possible?  Thanks!
- author: Andrew Pinski
  role: other
  position: Suggests that the sample data file be shared on the mailing list.
  quote: Or maybe it is a good idea to
primer_expert: AutoFDO uses profile information to guide compiler optimizations.  GCOV
  is a code coverage tool that can generate data used by AutoFDO. The proposal focuses
  on the format of the profile data that passes between GCOV and AutoFDO. A more flexible
  format allows for future extensions such as branch profiling.
primer_general: AutoFDO (Automatic Feedback-Directed Optimization) uses runtime information
  to guide compiler optimizations, improving performance. GCOV is a code coverage
  tool that can generate data used by AutoFDO. This proposal concerns the format of
  the data files that pass between those two tools.  By making the format more flexible,
  the developers can add new features in the future without breaking compatibility.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/60ca9a58-3a23-46b1-8e7d-0e5649e72f45@nvidia.com
bugzilla_url: null
date: '2026-04-23'
---

Dhruv Chawla proposes a new version of the AutoFDO GCOV profile format. Version 4 is a redesign focused on being backwards-compatible and extensible. It will also be partially readable by the compiler.
