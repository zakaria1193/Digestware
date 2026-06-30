---
project: binutils
subsystem: binutils
patch_id: null
tags:
- x86
- ISA
- ACE
- naming
- dependencies
discussion_id: fd28114f-f3b1-4219-924a-3cdee31d4551@suse.com
source_type: public_inbox
title: 'Re: [PATCH v1 2/2] Support x86 ACE ISA'
headline: Support x86 ACE ISA
tldr: Discussion on naming and dependencies for the x86 ACE ISA support.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Suggests using "ace_v1" as a counterpart to "avx10.1" and "avx10.2", finding
    "acev1" less appealing due to the lack of a separator.
  quote: 'Perhaps. We have "avx10.1" and "avx10.2" as .arch specifiers as well. So

    perhaps "ace_v1" as counterpart ("acev1" being a little odd without

    separator)?'
- author: Jiang, Haochen
  role: reviewer
  position: Questions using "ACE" and suggests "ACEV1" based on documentation, and
    later agrees that "AVX10_V2_AUX" is a more appropriate dependency than "AVX512F|64".
  quote: 'Should we call it as ACEV1 instead of ACE? Documentation mentioned

    it as ACEv1.

    I have different opinion on this implication. I suppose it should

    directly use AVX10_V2_AUX according to documentation CPUID

    emulation part. That part clearly showed AVX10_V2_AUX is a must.'
- author: Ganesh Gopalasubramanian <Ganesh.Gopalasubramanian@amd.com>
  role: contributor
  position: Submitted the initial patch which added 'ace' as a new architecture entry,
    and noted documentation referred to it as ACEv1.
  quote: '+  SUBARCH (ace, ACE, ACE, false),

    '
primer_expert: Discusses the naming and dependencies for the x86 ACE ISA support in
  binutils. Specifically, it debates using "ACE" vs "ACEv1" as the arch specifier,
  with a preference for "ace_v1" to match "avx10.1" and "avx10.2". It also corrects
  the ISA dependency from "AVX512F|64" to "AVX10_V2_AUX".
primer_general: This discussion centers on how to correctly add support for a new
  set of x86 instructions called the ACE ISA to the binutils software. Developers
  are debating the exact name to use for this instruction set (e.g., 'ACE' or 'ACEv1')
  and which other instruction sets it depends on to function properly. This ensures
  the assembler accurately recognizes and handles these new instructions.
series_id: binutils:support x86 ace isa
series_role: reply
series_parts:
- title: Support x86 ACE ISA
  url: https://inbox.sourceware.org/binutils/IA4PR11MB900905D3BA7803AEAE7B2EE7ECF72@IA4PR11MB9009.namprd11.prod.outlook.com
  n: 2
  total: 2
- title: Support x86 ACE ISA
  url: https://inbox.sourceware.org/binutils/DS4PPF8140589512BC3BF3700D7EEE3F1FBA6F72@DS4PPF814058951.namprd11.prod.outlook.com
  n: 2
  total: 2
- title: Support x86 ACE ISA
  url: https://inbox.sourceware.org/binutils/44102d0a-4ebc-4b3a-a135-3739d05caf6a@suse.com
  n: 2
  total: 2
- title: Support x86 ACE ISA
  url: https://inbox.sourceware.org/binutils/PH3PPF801A91A7D9BCD052BC2228570C282A6F72@PH3PPF801A91A7D.namprd11.prod.outlook.com
  n: 2
  total: 2
- title: Support x86 ACE ISA
  url: https://inbox.sourceware.org/binutils/196a627b-0727-4ff9-ac35-cf29a8fa1207@suse.com
  n: 2
  total: 2
url: https://inbox.sourceware.org/binutils/fd28114f-f3b1-4219-924a-3cdee31d4551@suse.com
bugzilla_url: null
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

This discussion revolves around the support for the x86 ACE (Advanced Core Enablement) ISA in binutils. Participants are debating the correct naming convention for the ISA (ACE vs. ACEv1) and its dependencies, specifically whether it should infer AVX512F|64 or AVX10_V2_AUX. The goal is to ensure accurate representation of the ISA in the assembler's configuration and opcode definitions.
