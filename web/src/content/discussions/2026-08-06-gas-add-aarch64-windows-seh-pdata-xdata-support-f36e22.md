---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- AArch64
- Windows
- SEH
discussion_id: 9995c4b9-cb2a-47a3-9738-9f37fe27609f@suse.com
source_type: public_inbox
title: 'Re: [PATCH] gas: Add AArch64 Windows SEH (pdata/xdata) support'
headline: 'gas: Add AArch64 Windows SEH (pdata/xdata) support'
tldr: Reviewer questions a resubmitted patch for AArch64 SEH support due to an existing,
  similar patch.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: needs_revision
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Ensures proper SEH support for AArch64 on Windows, crucial for application compatibility.
- The resubmission process and review concerns might delay the integration of this
  important feature.
exchanges:
- author: coshvji cujmlqef
  role: other
  position: Explains that the resubmitted patch addresses different bugs than a previous
    one and was resent due to port issues.
  quote: Hi. The previous patch has other bugs that would break seh on x86_64 so they
    are not the same patch, the first one needs to be discarded + i did not use git
    send-email because the 587 port was blocked so i resubmitted it again. Not deliberately
    try to insult other devs.
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Queries the resubmission of the patch, pointing out an existing similar
    patch and suggesting a need for a Statement of Biography.
  quote: Please can you comment then on that patch? Re-starting from scratch is an
    option if the other one is excessively broken, yet even then comments given there
    on earlier versions would want taking into account in such a full re-do.
primer_expert: Reviewer Jan Beulich expresses concern about a resubmitted patch adding
  AArch64 Windows SEH support to `gas`. The concern stems from a similar, earlier
  patch (v12) and potential requirements for a Statement of Biography (S-o-B). The
  proposer clarifies that the current patch addresses distinct issues and was resent
  due to external factors.
primer_glossary:
- term: gas
  definition: The GNU Assembler, responsible for converting assembly language code
    into machine code.
- term: AArch64
  definition: The 64-bit execution state of the ARM architecture.
- term: SEH
  definition: Structured Exception Handling, a mechanism for handling errors and exceptions
    in Windows operating systems.
- term: pdata/xdata
  definition: Data structures used in Windows exception handling to describe function
    unwind information.
- term: Statement of Biography (S-o-B)
  definition: A declaration by a contributor about their identity and any potential
    conflicts of interest, sometimes required for substantial contributions to open-source
    projects.
- term: patch
  definition: A piece of code that modifies existing software to fix bugs, add features,
    or improve performance.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/9995c4b9-cb2a-47a3-9738-9f37fe27609f@suse.com
bugzilla_url: null
date: '2026-08-06'
is_stub: false
stub_reason: ''
---

Jan Beulich questions a resubmitted patch for AArch64 Windows SEH support in `gas`, noting that similar work is already in progress (v12) and that the author might need to provide a Statement of Biography (S-o-B) if they are not a known contributor. The original author, responding to Beulich's previous comments, explains that the patch was resubmitted due to an unblocked port and that previous bugs were distinct from x86_64 issues.
