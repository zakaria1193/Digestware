---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- bfd
- elf
- relocation
- code removal
discussion_id: afSgyrFTP_8j0wIy@squeak.grove.modra.org
source_type: public_inbox
title: Delete _bfd_elf_get_dynamic_reloc_section
headline: Delete _bfd_elf_get_dynamic_reloc_section
tldr: Removes the `_bfd_elf_get_dynamic_reloc_section` function as it is no longer
  needed.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Removes dead code, simplifying the codebase.
- No functional change, as the same information is still accessible through a different
  method.
exchanges: []
primer_expert: '`_bfd_elf_get_dynamic_reloc_section` was used to find the dynamic
  relocation section associated with a given section in ELF objects. This patch cleans
  up redundant code after a previous change made the dynamic relocation section directly
  accessible via `elf_section_data`. Affected files include target-specific relocation
  code in the BFD library.'
primer_general: This patch removes a function used to find dynamic relocation information
  in ELF files. ELF files contain code, data, and metadata, including relocation information
  that describes how to update addresses when the file is loaded into memory.  A previous
  change made this information easier to access, so this patch removes the now-unnecessary
  function, simplifying the code and potentially improving performance. BFD is the
  library that handles reading and writing object files.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/afSgyrFTP_8j0wIy@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-01'
---

Alan Modra proposes removing the `_bfd_elf_get_dynamic_reloc_section` function from the binutils library. The function is no longer necessary because `_bfd_elf_make_dynamic_reloc_section` now guarantees that `elf_section_data(sec)->sreloc` is set to the dynamic reloc section. The patch also updates several files to get the dynamic reloc section via `elf_section_data`.
