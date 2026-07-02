---
project: binutils
subsystem: gas/elf
patch_id: null
tags:
- binutils
- assembler
- ELF
- symbol visibility
- gas
discussion_id: b4ec2334-1821-4780-9876-f8a12d20dc4b@suse.com
source_type: public_inbox
title: 'Re: [PATCH 2/3] gas/ELF: warn upon non-default visibility of local symbols'
headline: 'Gas/ELF: Warn Upon Non-Default Visibility of Local Symbols'
tldr: The patch proposes a warning when local symbols have non-default visibility,
  which is against ELF spec. The author considers reverting to earlier behavior.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Warning on invalid symbol visibility may break existing builds.
- Silently upgrading visibility to global may introduce unexpected symbol collisions.
- Changing visibility semantics might affect linking behavior.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes a warning for non-default visibility of local symbols in gas/ELF,
    as the ELF spec doesn't allow STB_LOCAL with STV_PROTECTED/HIDDEN/INTERNAL.
  quote: The spec explicitly precludes STB_LOCAL together with STV_PROTECTED (and,
    implicity, STV_HIDDEN or STV_INTERNAL), so we better wouldn't entirely silently
    write out symbols violating this.
- author: Richard Earnshaw (foss)
  role: reviewer
  position: Questions whether the change might cause issues for existing code and
    suggests treating '.hidden' as making the symbol global, but hidden.
  quote: Do we know that this won't cause issues for real code out in the wild?  Might
    it not be better to just treat .hidden as making the symbol global, but hidden?
- author: Jan Beulich <jbeulich@suse.com>
  role: contributor
  position: States that after reconsideration, implying global from hidden feels riskier
    and may stick with the current approach.
  quote: 'Having thought about this more, implying global from hidden (etc) feels
    more risky than keeping things as they are in v1: People suddenly may face dupli'
primer_expert: The GNU Assembler (gas) handles symbol visibility when creating ELF
  objects. STB_LOCAL symbols should not have STV_HIDDEN, STV_PROTECTED, or STV_INTERNAL
  visibility. This patch checks and warns on encountering that invalid combination.
  The concern is whether to silently upgrade such symbols to global scope (but hidden)
  instead of warning.
primer_general: When assembling code, symbols (names for memory locations or functions)
  are defined with specific attributes. One such attribute is visibility, which dictates
  where the symbol can be accessed from. In ELF (Executable and Linkable Format),
  the standard binary format on Linux, symbols can be local (visible only within the
  object file) or global (visible to other object files). This patch deals with the
  assembler's behavior when a symbol is marked as both local and having a visibility
  attribute that implies it should be global. Binutils is the project that hosts the
  assembler, linker and other binary tools.
series_id: 'binutils:gas/elf: warn upon non-default visibility of local symbols'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/b4ec2334-1821-4780-9876-f8a12d20dc4b@suse.com
bugzilla_url: null
date: '2026-05-08'
---

This patch warns when local symbols are declared with non-default visibility (protected/hidden/internal), as the ELF spec forbids mixing STB_LOCAL with those STV_* attributes. The author is now reconsidering whether to instead treat symbols with non-default visibility as global, but hidden. The discussion weighs the risk of introducing unexpected globals against the benefit of adhering to the ELF specification.
