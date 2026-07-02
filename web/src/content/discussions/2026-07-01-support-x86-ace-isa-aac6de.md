---
project: binutils
subsystem: binutils
patch_id: null
tags:
- x86
- ACE
- ISA
- binutils
- assembler
discussion_id: IA4PR11MB90092AB3598336D7F5DC47E3ECF62@IA4PR11MB9009.namprd11.prod.outlook.com
source_type: public_inbox
title: 'RE: [PATCH v1 2/2] Support x86 ACE ISA'
headline: Support x86 ACE ISA
tldr: Discusses naming convention for the x86 ACE ISA in binutils.
proposer: Jiang, Haochen <haochen.jiang@intel.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Choosing a naming convention that is both officially consistent and clear to users.
- Aligning with existing naming patterns in binutils for processor extensions.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Questions if 'ACEV1' should be used instead of 'ACE' as documentation
    refers to it as 'ACEv1'.
  quote: Should we call it as ACEV1 instead of ACE? Documentation mentioned it as
    ACEv1.
- author: Jiang, Haochen
  role: proposer
  position: Agrees that either 'ace_v1' or 'acev1' would be acceptable names for the
    ACE ISA in binutils.
  quote: I am ok with ace_v1 or acev1 in binutils since both are reasonable.
- author: Jan Beulich
  role: reviewer
  position: Suggests 'ace_v1' as a counterpart to existing naming like 'avx10.1' and
    'avx10.2'.
  quote: Perhaps. We have "avx10.1" and "avx10.2" as .arch specifiers as well. So
    perhaps "ace_v1" as counterpart ("acev1" being a little odd without separator)?
primer_expert: This exchange concerns the naming convention for the Advanced Core
  Extensibility (ACE) Instruction Set Architecture (ISA) within the GNU Assembler
  (gas). Specifically, it debates whether to register the ISA as 'ACE' or 'ACEV1',
  referencing its 'ACEv1' designation in official documentation and drawing parallels
  to other x86 feature naming schemes like 'AVX10'. The goal is to ensure consistent
  and clear labeling within binutils.
primer_glossary:
- term: ACE ISA
  definition: Advanced Core Extensibility Instruction Set Architecture, a set of new
    instructions for x86 processors.
- term: binutils
  definition: A collection of programming tools, including the linker (ld) and assembler
    (gas), used in programming.
- term: gas
  definition: The GNU Assembler, part of the binutils package, which translates assembly
    language code into object files.
- term: ISA
  definition: Instruction Set Architecture, the part of the processor that defines
    its machine language.
series_id: binutils:support x86 ace isa
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/IA4PR11MB90092AB3598336D7F5DC47E3ECF62@IA4PR11MB9009.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-07-01'
is_stub: false
stub_reason: ''
---

This thread discusses the appropriate naming for the x86 ACE ISA within binutils. The core of the discussion is whether to use 'ACE' or 'ACEV1' as the identifier, considering that the official documentation refers to it as 'ACEv1'. The proposer indicates they are amenable to either 'ace_v1' or 'acev1' for binutils.
