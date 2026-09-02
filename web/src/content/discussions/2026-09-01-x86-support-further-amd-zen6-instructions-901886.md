---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- gas
- x86
- amd
- assembly
discussion_id: 20260901091530.3755450-1-RohanRadhesh.Shenoy@amd.com
source_type: public_inbox
title: '[PATCH] x86: support further AMD Zen6 instructions'
headline: 'x86: support further AMD Zen6 instructions'
tldr: Adds support for RMPOPT and RMPCHKD instructions and enables FRED on AMD Zen6.
proposer: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
consensus: Ready to Land
outcome: ready
impact_score: 6
sentiment_score: 8
technical_tradeoffs:
- Adding new instruction support requires updates across multiple assembler components.
- Ensuring correct documentation and testing for new features.
exchanges:
- author: Rohan Shenoy <RohanRadhesh.Shenoy@amd.com>
  role: proposer
  position: Submits a patch to add support for RMPOPT and RMPCHKD instructions and
    enable FRED on AMD Zen6.
  quote: 'Changes:

    - Add support for RMPOPT and RMPCHKD instructions.

    - Enable FRED on znver6.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the patch and quotes the changes, indicating review.
  quote: null
- author: Haochen Jiang <haochen.jiang@intel.com>
  role: reviewer
  position: LGTMs the patch with minor comments, requesting documentation for the
    new features.
  quote: 'LGTM but with two minor comments.


    Could you show me the documentation for that?'
primer_expert: This patch adds support for new AMD x86 instructions (RMPOPT, RMPCHKD)
  and a microarchitecture feature (FRED) for the Zen6 family to the GNU Assembler.
  This involves modifying assembler configuration files (`tc-i386.c`), documentation
  (`c-i386.texi`), and adding test cases for the new instructions.
primer_glossary:
- term: RMPOPT
  definition: A new x86 instruction related to memory protection or management, likely
    introduced by AMD.
- term: RMPCHKD
  definition: A new x86 instruction, possibly related to memory protection or checking,
    introduced by AMD.
- term: FRED
  definition: Likely an acronym for a feature or instruction set extension related
    to memory management or protection, specific to AMD processors.
- term: Zen6
  definition: The codename for AMD's sixth-generation Zen microarchitecture, indicating
    the target processor family for these new instructions and features.
- term: GNU Assembler (gas)
  definition: The assembler used in the GNU toolchain, responsible for translating
    assembly language code into machine code.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260901091530.3755450-1-RohanRadhesh.Shenoy@amd.com
bugzilla_url: null
date: '2026-09-01'
is_stub: false
stub_reason: ''
---

This patch introduces support for two new x86 instructions, RMPOPT and RMPCHKD, and enables the FRED feature for the AMD Zen6 microarchitecture in the GNU Assembler (gas). The changes involve updates to assembler configuration, documentation, and test suite files.
