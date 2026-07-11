---
project: binutils
subsystem: binutils
patch_id: null
tags:
- AVX10
- CPU features
- CPUID
- assembler
- instruction set
discussion_id: 71a1d16f-c112-4ed5-97a7-a3f0908b47f5@suse.com
source_type: public_inbox
title: 'Re: [PATCH v1 1/2] Support AVX10_V2_AUX instructions'
headline: Support AVX10_V2_AUX instructions
tldr: Jan Beulich states he is working on a patch to separate AVX10.1-aux from AVX10.2.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Refines AVX10 support by separating variants, potentially leading to more precise
  feature detection and code generation.
- Requires a new CPUID bit to be handled, ensuring compatibility with newer processors.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: States that he is working on a patch to distinguish AVX10.1 auxiliary
    instructions from AVX10.2, which will be available under a new CPUID bit.
  quote: 'Just to mention that I have a patch in the works to separate 10.1-aux from

    10.2.'
primer_expert: This brief exchange appears to be a follow-up to a patch series introducing
  AVX10_V2_AUX instructions. The context is the Intel/AMD CPUID mechanism used to
  enumerate supported instruction set extensions. The query 'What is your plan on
  supporting that bit?' likely refers to a CPUID bit associated with AVX10_V1_AUX
  or a related feature. Jan Beulich's response indicates he is preparing a patch to
  refine the support for these AVX10 variants, specifically isolating AVX10.1-aux
  from AVX10.2 and enabling it via a distinct CPUID bit.
primer_glossary:
- term: AVX10_V2_AUX
  definition: A set of auxiliary instructions related to the AVX10 instruction set
    extension, characterized by version 2.
- term: CPUID
  definition: An x86 instruction that provides information about the processor's capabilities
    and features, including supported instruction sets. Processors use specific bits
    to indicate support for various extensions.
- term: AVX10.1
  definition: An instruction set extension for x86 processors, representing an early
    version of AVX10 features.
- term: AVX10.2
  definition: A later version of the AVX10 instruction set extension, potentially
    including more features or refinements over AVX10.1.
- term: instruction set extension
  definition: An addition to a processor's base instruction set, providing new capabilities
    such as advanced vector operations (e.g., AVX).
series_id: binutils:support avx10_v2_aux instructions
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/71a1d16f-c112-4ed5-97a7-a3f0908b47f5@suse.com
bugzilla_url: null
date: '2026-07-10'
is_stub: false
stub_reason: ''
---

Jan Beulich responds to a question about supporting a specific CPUID bit related to AVX10 instructions. He informs the thread that he is developing a patch to separate the AVX10.1 preliminary auxiliary instructions from the AVX10.2 set, indicating they will be available under a new CPUID bit. This is in response to a query about the plan for supporting that bit.
