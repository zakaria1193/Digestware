---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- assembler
- ELF
- relocation
- symbol table
discussion_id: 88097170-c97c-4388-81bc-a2b5e53a89ef@suse.com
source_type: public_inbox
title: 'Re: [PATCH v3] gas: add --reloc-section-sym={all, internal, none} option for
  ELF'
headline: 'gas: add --reloc-section-sym={all, internal, none} option for ELF'
tldr: Adds a new assembler option to control the conversion of local symbols to section
  symbols in relocation entries.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Reduced symbol table size when converting local symbols to section symbols.
- Potential loss of information about individual local symbols in the symbol table,
  which may complicate debugging.
- Increased complexity in the assembler code to support the new option.
exchanges:
- author: Fangrui Song <maskray@sourceware.org>
  role: proposer
  position: Proposes a new assembler option `--reloc-section-sym` to control the conversion
    of local symbols to section symbols in relocation entries.
  quote: 'Add --reloc-section-sym to control this conversion:


    - all (default): convert all eligible local symbols

    - internal: only convert compiler-generated locals (.L prefix)

    - none: never convert; keep all symbols as-is in relocations'
- author: Jan Beulich <jbeulich@suse.com>
  role: maintainer
  position: Acknowledges the proposal and requests verification of the new tests across
    multiple target architectures.
  quote: Okay, provided you checked the new tests pass for a wide range of targets.
    In particular ...
primer_expert: When generating relocations, `gas` can convert local symbols to section
  symbols (STT_SECTION) to reduce the size of the `.symtab`.  This optimization is
  controlled by the `--reloc-section-sym` option. The relevant code resides in `gas/config/tc-*.c`
  files and the ELF backend. This feature interacts with symbol table generation and
  relocation processing.
primer_general: The GNU assembler (`gas`) translates assembly code into object files.
  Relocations are adjustments that the linker makes to the code and data sections
  when combining object files.  Symbols represent memory locations, functions, or
  variables.  Local symbols are typically only visible within a single object file.  This
  patch allows users to control how the assembler represents local symbols within
  relocation entries, potentially affecting the size and debuggability of the final
  executable.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/88097170-c97c-4388-81bc-a2b5e53a89ef@suse.com
bugzilla_url: null
date: '2026-05-15'
is_stub: false
---

This patch (in reply to the original proposal) introduces the `--reloc-section-sym` option to the GNU assembler for ELF targets. This option controls how the assembler handles local symbols in relocations, allowing users to convert all eligible local symbols to section symbols (`all`), only compiler-generated locals (`internal`), or keep all symbols as is (`none`). The change can be useful for debugging and tools relying on preserved symbol names. A maintainer has requested confirmation that the new tests pass for a wide range of targets.
