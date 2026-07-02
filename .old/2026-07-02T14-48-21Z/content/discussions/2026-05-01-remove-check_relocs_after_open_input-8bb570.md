---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- relocation
- code removal
- cleanup
discussion_id: afSgoPLa-UtUb1_j@squeak.grove.modra.org
source_type: public_inbox
title: Remove check_relocs_after_open_input
headline: Remove check_relocs_after_open_input
tldr: Removes the `check_relocs_after_open_input` flag and related code, as it's no
  longer needed after commit 5c3261b0e834.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Simplifies the codebase by removing an unused flag.
- No functional change, as the flag was already unused.
exchanges: []
primer_expert: The `check_relocs_after_open_input` flag controlled when relocations
  were checked during linking. This patch removes the flag and related code from the
  linker's core and emulation templates, indicating a change in how relocation processing
  is handled. This simplifies the linker's internal state.
primer_general: This patch simplifies the binutils linker by removing a flag that
  controlled when relocation checks were performed. Relocations are adjustments made
  to code and data addresses when a program is linked or loaded into memory. The removal
  of this flag suggests a change in the linker's internal workings, potentially improving
  efficiency or simplifying the code.  This cleanup removes complexity without changing
  functionality.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/afSgoPLa-UtUb1_j@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-01'
---

Alan Modra proposes removing the `check_relocs_after_open_input` flag from the binutils linker, along with associated code. This flag became obsolete after commit 5c3261b0e834. The patch removes the flag from the `bfd_link_info` structure and cleans up code in several linker emulation templates.
