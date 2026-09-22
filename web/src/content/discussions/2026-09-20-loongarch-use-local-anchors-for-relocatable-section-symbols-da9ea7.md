---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- linker
- relocation
- relaxation
- RFC
discussion_id: arBsgyYMkLUw4ReL@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [RFC PATCH] LoongArch: Use local anchors for relocatable section symbols'
headline: 'LoongArch: Use local anchors for relocatable section symbols'
tldr: Alan Modra questions the necessity of using local anchors for relocatable section
  symbols in LoongArch, suggesting the relaxation code should be fixed instead.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Working around linker limitations with local anchors might be simpler but could
  obscure the root cause and potentially limit future optimizations.
- Fixing the core relaxation mechanism is more complex but leads to a cleaner and
  more robust solution.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: reviewer
  position: Questions the approach of using local anchors for LoongArch section symbols,
    suggesting the relaxation code should be fixed instead.
  quote: 'I''m inclined to say, "well, fix your loongarch relaxation code then",

    unless you can convincingly explain why that is not possible.'
- author: mengqinggang
  role: proposer
  position: Proposed using local anchors for relocatable section symbols in LoongArch
    due to limitations in its relaxation code.
  quote: 'For ld -r, when an input STT_SECTION symbol is redirected to the

    output section symbol, elf_link_input_bfd() folds sec->output_offset

    into the RELA addend.  LoongArch relaxation does not allow symbols to

    be optimized into section symbol plus offset form.'
primer_expert: This exchange pertains to the LoongArch architecture's handling of
  relocatable section symbols within the GNU linker (`ld`). The proposer's RFC patch
  suggests using 'local anchors' to address a limitation where the linker's `elf_link_input_bfd()`
  function folds `sec->output_offset` into the RELA addend for section symbols. The
  problem is that LoongArch's relaxation mechanism does not support optimizing symbols
  into a 'section symbol + offset' form. Alan Modra, a reviewer, counters by suggesting
  that the fundamental issue lies within the LoongArch relaxation implementation itself
  and that fixi…
primer_glossary:
- term: LoongArch
  definition: A RISC instruction set architecture developed in China, used in processors
    like the Loongson series.
- term: relocatable section symbols
  definition: Symbols that represent sections within an object file and are used during
    the linking process to resolve addresses in a position-independent manner.
- term: RFC
  definition: Request For Comments, indicating a proposal or discussion document seeking
    feedback from the community.
- term: ld
  definition: The GNU linker, responsible for combining object files into executables
    or libraries.
- term: relaxation
  definition: A linker optimization technique where instructions or addresses are
    adjusted after initial linking to improve code density or performance, often by
    using PC-relative addressing or symbol stubs.
- term: RELA
  definition: Relocation entry with explicit addend, a type of relocation record used
    in ELF object files.
- term: STT_SECTION
  definition: A symbol type in ELF that specifically refers to a section.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/arBsgyYMkLUw4ReL@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-20'
is_stub: false
stub_reason: ''
---

Alan Modra responds to an RFC patch for LoongArch concerning relocatable section symbols. He questions the approach of using local anchors, suggesting that the underlying issue might be within the LoongArch relaxation code itself, which apparently does not permit symbols to be optimized into a section symbol plus offset form. Modra implies that fixing the relaxation code would be a more appropriate solution unless it can be convincingly demonstrated that this is not possible.
