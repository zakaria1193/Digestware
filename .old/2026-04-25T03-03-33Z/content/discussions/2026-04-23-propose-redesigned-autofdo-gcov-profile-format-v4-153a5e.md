---
project: gcc
subsystem: rfc
patch_id: null
tags:
- AutoFDO
- GCOV
- profile format
- optimization
discussion_id: 60ca9a58-3a23-46b1-8e7d-0e5649e72f45@nvidia.com
source_type: public_inbox
title: 'RFC: AutoFDO GCOV Profile Format Version 4'
headline: Propose redesigned AutoFDO GCOV profile format v4
tldr: A redesigned GCOV profile format (version 4) is proposed for AutoFDO, featuring
  backward compatibility, extensibility, and reduced file size.
proposer: Dhruv Chawla <dhruvc@nvidia.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- The new format may require updates to existing tools that process GCOV profiles.
- Compact encoding may increase the complexity of reading and writing profiles.
- The section-based layout may introduce some overhead compared to the sequential
  layout of previous versions.
exchanges:
- author: Dhruv Chawla <dhruvc@nvidia.com>
  role: proposer
  position: Presents a redesigned GCOV profile format (version 4) for AutoFDO, emphasizing
    backward compatibility, extensibility, and reduced file size.
  quote: Per prior discussions, here is the specification we are proposing for version
    4 of the AutoFDO GCOV profile format. This is a complete re-design focused around
    being a backwards-compatible and extensible format which can be partially read
    by the compiler.
- author: Jose E. Marchesi <jemarch@gnu.org>
  role: other
  position: Requests a sample data file.
  quote: Could you please send me (off list) a sample data file, as complete as possible?  Thanks!
- author: Andrew Pinski <andrew.pinski@oss.qualcomm.com>
  role: other
  position: Suggests sending sample data file to the mailing list.
  quote: Or maybe it is a good idea to
primer_expert: AutoFDO uses GCOV profiles to guide compiler optimizations based on
  runtime feedback.  This RFC proposes a new version of the GCOV profile format, focusing
  on extensibility and reduced file size.  The changes involve a section-based layout,
  trie-compressed string tables and optional compact encoding.
primer_general: AutoFDO (Automatic Feedback-Directed Optimization) is a technique
  that uses runtime information to improve compiler optimizations. GCOV profiles are
  files that contain data about how often different parts of a program are executed.
  This proposal is to change the format of these files to improve them by making them
  smaller and more flexible.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/60ca9a58-3a23-46b1-8e7d-0e5649e72f45@nvidia.com
bugzilla_url: null
date: '2026-04-23'
---

Dhruv Chawla proposes a new version (4) of the AutoFDO GCOV profile format. The redesign focuses on backward compatibility and extensibility through a section-based layout and typed location records. The format also aims to reduce file size using techniques like trie-compressed string tables and compact encoding. The new format includes a human-readable textual representation in addition to the binary format.
