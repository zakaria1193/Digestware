---
project: gcc
subsystem: gcc
patch_id: null
tags:
- policy
- LLM
- AI
- bug fixes
discussion_id: 9560964f-9871-4a1e-b56c-4e518bed3543@tugraz.at
source_type: public_inbox
title: 'Re: Policy on use of LLM tools and bug fixes'
headline: Discuss Policy on Use of LLMs for Bug Fixes
tldr: The GCC steering committee is working on a policy for the use of LLMs, similar
  to the Linux kernel's, but possibly more restrictive.
proposer: Jonathan Wakely <jwakely.gcc@gmail.com>
consensus: Proposed
outcome: proposed
sentiment_score: null
technical_tradeoffs:
- Potential for faster bug fixes and code generation with LLMs.
- Legal and ethical concerns surrounding AI-generated code.
- Difficulty in verifying the correctness and security of AI-generated code.
exchanges:
- author: Jonathan Wakely
  role: other
  position: States that the GCC steering committee is working on a policy for the
    use of LLMs in bug fixes and code contributions, similar to the Linux kernel's
    policy, but potentially more restrictive by not accepting AI-generated code.
  quote: null
- author: Jonathan Wakely
  role: other
  position: Corrects the previous message to clarify that the current draft policy
    does not accept AI-generated code.
  quote: null
primer_expert: The thread discusses the use of Large Language Models (LLMs) in the
  GCC development process. The legal status of AI-generated code is unclear. The discussion
  centers around copyright and whether or not the code meets the legal requirements
  for GCC contributions.
primer_general: Large Language Models (LLMs) can be used to generate code. However,
  the legal status of that code is unclear making the toolchain developers wary of
  its use. This thread discusses the policy on using LLMs for bug fixes in GCC, including
  concerns about copyright and legal requirements.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAH6eHdS4_0TczAGKSMWBUrMOrtkEE-6ptqbVTJVC9Vgtbs9fdQ@mail.gmail.com
bugzilla_url: null
date: '2026-04-17'
---

Jonathan Wakely responds to a thread about policy on the use of LLM tools for bug fixes. He mentions that the steering committee is trying to figure out a good policy. He also mentions that a draft policy exists that proposes not accepting AI-generated code, only allowing the use of AI for assistance, idea generation, and testing.
