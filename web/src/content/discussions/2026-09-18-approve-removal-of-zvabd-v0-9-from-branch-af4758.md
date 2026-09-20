---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- extension
- release
- binutils
discussion_id: 31dddfcd-08a3-4648-9009-c43502408b34@redhat.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Support Zvabd version 0.9'
headline: Approve removal of Zvabd v0.9 from branch
tldr: Nick Clifton approves the removal of the Zvabd v0.9 feature from the binutils-2.47
  branch.
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Removing a potentially useful but unstable feature from a release branch to maintain
  stability.
- Ensures that only finalized or well-understood features are included in stable releases.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: maintainer
  position: Approves the request to remove the Zvabd v0.9 feature from the release
    branch.
  quote: Yes, please do. :-)
- author: Unknown
  role: reviewer
  position: Requested the removal of Zvabd v0.9 from the 2.47 branch due to its instability
    and encoding changes.
  quote: Could we push a patch to remove that on the binutils-2_47-branch branch?
primer_expert: This brief exchange confirms the removal of the RISC-V Zvabd version
  0.9 extension support from the binutils-2.47 branch. The rationale is that the extension
  is not finalized (not 1.0) and has undergone changes, making its inclusion in a
  stable release problematic. This action reflects a common practice of stabilizing
  feature sets before release.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA).
- term: Zvabd
  definition: A specific extension for the RISC-V architecture, likely related to
    vector operations.
- term: binutils-2.47-branch
  definition: A development branch for version 2.47 of the GNU Binutils.
- term: encoding
  definition: The binary representation of an instruction.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/31dddfcd-08a3-4648-9009-c43502408b34@redhat.com
bugzilla_url: null
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

Nick Clifton confirms that the RISC-V Zvabd version 0.9 feature should be removed from the binutils-2.47 branch. This follows a discussion where it was argued that the feature is not yet stable (not 1.0) and has undergone encoding changes, warranting its removal from the release branch.
