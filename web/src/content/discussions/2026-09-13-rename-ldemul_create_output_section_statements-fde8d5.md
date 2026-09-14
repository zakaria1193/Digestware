---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- refactoring
- code clarity
- patch
discussion_id: aqYvJRujIhQs78z0@squeak.grove.modra.org
source_type: public_inbox
title: Rename ldemul_create_output_section_statements
headline: Rename ldemul_create_output_section_statements
tldr: Renames `ldemul_create_output_section_statements` to `after_open_output` for
  clarity, as the function does not create sections.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: null
technical_tradeoffs:
- Renaming functions improves code readability and maintainability but requires updating
  all call sites and related documentation.
- Accurate function naming prevents misunderstandings about a function's purpose,
  potentially avoiding future bugs.
- The tradeoff is between the effort of renaming and the long-term benefit of clearer,
  more maintainable code.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes renaming a linker emulation function from `create_output_section_statements`
    to `after_open_output` for clarity.
  quote: This function was poorly named.  As was noted in ldint.texi, now deleted,
    "nobody creates output sections here".  Apart from the ldint.texi change this
    patch simply substitutes all occurences of create_output_section_statements with
    after_open_output, both lower and upper case.
primer_expert: This patch focuses on improving the naming convention within the GNU
  linker's emulation template files (`.em`). The function currently named `ldemul_create_output_section_statements`
  is being renamed to `ldemul_after_open_output`. The rationale is that the function's
  logic executes after the output file has been opened and its basic structure determined,
  but it does not actively create sections itself. This renaming aims to eliminate
  confusion and better align the function name with its actual behavior during the
  linking process, specifically in the context of target-specific linker emulation…
primer_glossary:
- term: ldemul
  definition: Refers to linker emulation, which allows the linker to support various
    target-specific behaviors and object file formats.
- term: emulation template
  definition: A file (often with a `.em` extension) used in the GNU linker to define
    common behaviors for a family of target architectures or object file formats.
- term: Linker
  definition: A program that combines object files and libraries into an executable
    file or a shared library.
- term: Output file
  definition: The final binary file (executable or shared library) produced by the
    linker.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aqYvJRujIhQs78z0@squeak.grove.modra.org
bugzilla_url: null
date: '2026-09-13'
is_stub: false
stub_reason: ''
---

Alan Modra proposes renaming the linker emulation function `ldemul_create_output_section_statements` to `after_open_output`. The change is motivated by the observation that this function's actual purpose is not to create output sections, but rather to perform actions after the output file has been opened. This rename aims to improve code clarity and accuracy by better reflecting the function's role in the linking process. The patch updates multiple emulation files and documentation.
