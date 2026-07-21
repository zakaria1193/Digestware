---
project: binutils
subsystem: bfd/risc-v
patch_id: null
tags:
- risc-v
- extensions
- binutils
- specification
- patch
discussion_id: CAHT-pJzSFKGzjFEqypAcAp1YnWMkq6LvGLX+879VxqBQDy8sKA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3 03/13] bfd/RISC-V: Zvfbfwma implies Zvfbfmin'
headline: 'RISC-V: Zvfbfwma implies Zvfbfmin'
tldr: Confirmation and acceptance of a patch clarifying RISC-V extension implications
  in binutils.
proposer: Nelson Chu <nelson.chu1990@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensures specification compliance at the cost of a minor change in established logic.
exchanges:
- author: Nelson Chu
  role: proposer
  position: Acknowledges and accepts the patch, stating 'OK! Thanks for this.'
  quote: OK!  Thanks for this.
- author: Jan Beulich
  role: reviewer
  position: 'Provided the patch and questioned the implication logic, stating ''This
    is pretty clear from the spec.'' and ''While the spec is also explicit there:
    I would have expected Zvfbfmin (not Zvfbfwma) to be what implies Zfbfmin. Is there
    an explanation for this?'''
  quote: null
primer_expert: This patch corrects the binutils implementation of RISC-V extension
  implications. The change ensures that `Zvfbfwma` correctly implies `Zvfbfmin`, aligning
  with the RISC-V specification and addressing a potential misunderstanding about
  the relationship between these vector extensions.
primer_glossary:
- term: RISC-V
  definition: An open-source Instruction Set Architecture (ISA) that is modular and
    extensible.
- term: Extension
  definition: A set of instructions that can be added to the base RISC-V ISA to provide
    additional functionality (e.g., vector processing).
- term: Implication
  definition: In the context of RISC-V extensions, when supporting one extension automatically
    enables support for another.
- term: Zvfbfwma
  definition: A RISC-V vector extension related to floating-point fused multiply-add
    operations.
- term: Zvfbfmin
  definition: A RISC-V vector extension related to floating-point minimum operations.
- term: bfd
  definition: Binary File Descriptor library, part of GNU Binutils, used for handling
    various object file formats.
series_id: 'binutils:bfd/risc-v: zvfbfwma implies zvfbfmin'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAHT-pJzSFKGzjFEqypAcAp1YnWMkq6LvGLX+879VxqBQDy8sKA@mail.gmail.com
bugzilla_url: null
date: '2026-07-21'
is_stub: false
stub_reason: ''
---

Nelson Chu confirms and accepts a patch related to RISC-V extension implications within binutils. The patch corrects an assumption about which extension implies another, specifically concerning `Zvfbfwma` and `Zvfbfmin`. The discussion also touches upon the explicit nature of the RISC-V specification regarding these implications.
