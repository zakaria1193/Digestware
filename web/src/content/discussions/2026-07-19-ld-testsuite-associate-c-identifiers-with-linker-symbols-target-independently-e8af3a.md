---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- testsuite
- symbol resolution
- target-specific
discussion_id: alxhIzmq0vtgWrbU@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] ld: testsuite: Associate C identifiers with the corresponding
  assembler or linker symbols in a target-independent manner.'
headline: 'ld testsuite: Associate C identifiers with linker symbols target-independently.'
tldr: Patch applied to ld testsuite to associate C identifiers with linker symbols
  in a target-independent way.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra
  role: maintainer
  position: Applied the patch, acknowledging its usefulness for handling target-specific
    symbol naming conventions in the testsuite.
  quote: null
- author: Jan Dubiec
  role: proposer
  position: Proposed a patch to use the `asm` keyword to associate C identifiers with
    assembler/linker symbol names regardless of target-specific underscore prefixes.
  quote: 'Some targets prepend an underscore to C symbol names, while others do not
    (e.g. H8 vs. ARM). This can cause problems in two situations, as shown in the
    log below: 1. when linking C and assembly code; 2. when a symbol name is specified
    on the linker''s command line. This patch resolves both issues by using the asm
    keyword to associate C identifiers with the corresponding assembler/linker symbol
    nam…'
primer_expert: Alan Modra has accepted Jan Dubiec's patch into the ld testsuite. The
  change addresses inconsistencies in how the linker handles C symbol names that may
  or may not be prefixed with an underscore, depending on the target architecture.
  This ensures test cases accurately reflect symbol recognition across different targets.
primer_glossary:
- term: ld
  definition: The GNU linker, a program that combines various object files and libraries
    into a single executable or library.
- term: Testsuite
  definition: A collection of tests designed to verify the correctness of a software
    program.
- term: Symbol name
  definition: An identifier used in object files and executables to refer to functions,
    variables, or other program elements. Some architectures prepend an underscore
    to C symbol names.
- term: Target-independent
  definition: Software design that does not rely on specific characteristics of a
    particular hardware architecture or operating system.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/alxhIzmq0vtgWrbU@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-19'
is_stub: false
stub_reason: ''
---

Jan Dubiec's patch, which addresses issues with leading underscores in C symbol names across different targets, has been applied to the binutils ld testsuite. The change aims to correctly link C identifiers with their corresponding assembler or linker symbols in a manner that is independent of the target architecture's conventions.
