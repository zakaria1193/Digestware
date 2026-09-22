---
project: gcc
subsystem: gcc
patch_id: null
tags:
- GCC
- AI
- Machine Learning
- Optimization
- Code Generation
discussion_id: f1cd0a2f-3015-44d4-9a09-5717217ca904@embecosm.com
source_type: public_inbox
title: 'GNU Cauldron BoF: GCC for AI - topics wanted'
headline: 'GNU Cauldron BoF: GCC for AI - topics wanted'
tldr: Call for topics for the 'GCC for AI' Birds-of-a-Feather session at GNU Cauldron.
proposer: Pietra Ferreira <pietra.ferreira@embecosm.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Pietra Ferreira <pietra.ferreira@embecosm.com>
  role: proposer
  position: Soliciting community input for topics to be covered in the 'GCC for AI'
    Birds-of-a-Feather session at GNU Cauldron.
  quote: 'Some topics I''m already considering:

    - ML-guided optimization passes and heuristics (e.g. inlining, register

    allocation)

    - Codegen and vectorization for AI/ML workloads (matmul, tensor ops)

    - Target-specific codegen for AI accelerators

    - Where GCC fits relative to MLIR-based toolchains for AI workloads'
primer_expert: This is a call for participation in a Birds-of-a-Feather (BoF) session
  at the GNU Cauldron conference, focusing on the intersection of GCC and Artificial
  Intelligence development. The organizer is seeking community input on specific areas
  like machine learning for compiler optimizations (e.g., guiding pass selection or
  heuristics), specialized code generation for AI/ML hardware accelerators and workloads
  (like tensor operations), and how GCC compares to alternative toolchains, particularly
  those based on MLIR, for AI development.
primer_glossary:
- term: GNU Cauldron
  definition: An annual conference for GNU project developers and users.
- term: BoF
  definition: Birds-of-a-Feather session, an informal meeting at a conference for
    people with a common interest.
- term: AI
  definition: Artificial Intelligence, the field of computer science dedicated to
    creating systems that can perform tasks typically requiring human intelligence.
- term: ML
  definition: Machine Learning, a subset of AI that focuses on algorithms that allow
    systems to learn from data.
- term: optimization passes
  definition: Individual stages within a compiler that analyze and transform the intermediate
    representation of the code to improve its performance or size.
- term: codegen
  definition: Code generation, the process of producing machine code or assembly code
    from an intermediate representation.
- term: MLIR
  definition: Multi-Level Intermediate Representation, a compiler infrastructure project
    designed to represent code at various levels of abstraction.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/f1cd0a2f-3015-44d4-9a09-5717217ca904@embecosm.com
bugzilla_url: null
date: '2026-09-21'
is_stub: false
stub_reason: ''
---

Pietra Ferreira is organizing a Birds-of-a-Feather (BoF) session on 'GCC for AI' at the upcoming GNU Cauldron and is soliciting topic suggestions from the community. Potential areas include ML-guided optimizations, codegen for AI workloads, and GCC's positioning relative to MLIR-based toolchains.
