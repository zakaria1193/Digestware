---
project: gcc
subsystem: rfc
patch_id: null
tags: []
discussion_id: 60ca9a58-3a23-46b1-8e7d-0e5649e72f45@nvidia.com
source_type: public_inbox
title: 'RFC: AutoFDO GCOV Profile Format Version 4'
headline: 'RFC: AutoFDO GCOV Profile Format Version 4'
tldr: Dhruv Chawla proposes a redesigned, backwards-compatible, and extensible version
  4 of the AutoFDO GCOV profile format.
proposer: Dhruv Chawla <dhruvc@nvidia.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Dhruv Chawla <dhruvc@nvidia.com>
  role: proposer
  position: Proposes a redesigned, backwards-compatible and extensible version 4 of
    the AutoFDO GCOV profile format which is a section-based one.
  quote: 'Per prior discussions, here is the specification we are proposing for

    version 4 of the AutoFDO GCOV profile format. This is a complete re-design

    focused around being a backwards-compatible and extensible format which

    can be partially read by the compiler.'
- author: '"Jose E. Marchesi" <jemarch@gnu.org>'
  role: other
  position: Asks for a sample data file.
  quote: 'Could you please send me (off list) a sample data file, as complete as

    possible?  Thanks!'
- author: Andrew Pinski <andrew.pinski@oss.qualcomm.com>
  role: other
  position: Suggests sending the sample data file to the list.
  quote: Or maybe it is a good idea to
primer_expert: This RFC proposes a new version of the AutoFDO GCOV profile format.
  The goal is to improve backward compatibility and extensibility.
primer_general: This RFC proposes a new version of the AutoFDO GCOV profile format.
  AutoFDO (Automatic Feedback-Directed Optimization) is a technique used to improve
  the performance of compiled code by using profile data collected during program
  execution. GCOV is a test coverage program and a tool for collecting this data.
  The new format aims to be backwards compatible and extensible.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/60ca9a58-3a23-46b1-8e7d-0e5649e72f45@nvidia.com
bugzilla_url: null
date: '2026-04-23'
---

Dhruv Chawla proposes version 4 of the AutoFDO GCOV profile format. The redesign is section-based, aims for partial reads, forward compatibility, reduced file size, optional compact encoding, and a human-readable textual format. The new format intends to replace the existing fixed, non-extensible tag-length sequential layout used in versions 2 and 3.
