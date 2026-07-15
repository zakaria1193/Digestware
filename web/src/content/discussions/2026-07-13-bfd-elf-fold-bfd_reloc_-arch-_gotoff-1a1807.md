---
project: binutils
subsystem: bfd/elf
patch_id: null
tags:
- binutils
- bfd
- elf
- linker
- relocation
discussion_id: d0ab4a18-0b34-45d9-b500-38bcccd22329@suse.com
source_type: public_inbox
title: 'Re: bfd/ELF: fold BFD_RELOC_<arch>_GOTOFF*'
headline: 'bfd/ELF: fold BFD_RELOC_<arch>_GOTOFF*'
tldr: Fixes build breakage in frv and lm32 by updating relocation types after a previous
  commit refactored GOTOFF relocations.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Consolidating relocation types simplifies the codebase but can lead to temporary
  build or runtime issues if not handled carefully across all affected architectures.
- Maintaining architecture-specific code while striving for generic solutions requires
  careful management of dependencies and abstractions.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Questions a potential layering violation but acknowledges the fix for
    build breakage.
  quote: 'Oh, wow. Isn''t this really a layering violation? Yet then I see there are

    ample other examples of BFD_* and bfd_* used from cpu/, so perhaps that''s

    indeed intentional.'
- author: Alan Modra
  role: other
  position: Original author of the commit that caused the issue, confirms the fix
    is being pushed to the 2.47 branch.
  quote: null
primer_expert: This discussion revolves around a fix for build breakage introduced
  by a previous commit (705b90feb82c) that refactored GOTOFF relocation types. Prior
  to the fix, generated opcode files for the frv and lm32 architectures would break
  if regenerated, due to outdated relocation type references. The fix updates these
  references from architecture-specific types (e.g., `BFD_RELOC_FRV_GOTOFFLO`) to
  more generic, unified types (e.g., `BFD_RELOC_LO16_GOTOFF`). This addresses the
  build issue and aligns with the broader effort to consolidate relocation types.
primer_glossary:
- term: BFD_RELOC_<arch>_GOTOFF*
  definition: Architecture-specific relocation types related to Global Offset Table
    (GOT) entries for offset calculations.
- term: GOT
  definition: Global Offset Table. A data structure used by dynamically linked executables
    and shared libraries to support references to external or global symbols.
- term: layering violation
  definition: In software design, a violation where a component depends on or interacts
    with components at a lower level or in a different abstraction layer than intended.
- term: frv
  definition: Fujitsu Rioch processor architecture.
- term: lm32
  definition: LatticeMico32, a 32-bit soft processor core.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/d0ab4a18-0b34-45d9-b500-38bcccd22329@suse.com
bugzilla_url: null
date: '2026-07-13'
is_stub: false
stub_reason: ''
---

Responding to a fix for build breakage in `cpu/frv.opc` and `cpu/lm32.opc`, Jan Beulich questions if the change represents a layering violation but acknowledges that other similar BFD_* usage from `cpu/` might be intentional. The fix involves updating relocation types from architecture-specific `BFD_RELOC_FRV_GOTOFFLO` and `BFD_RELOC_LM32_GOTOFF_HI16` to more generic `BFD_RELOC_LO16_GOTOFF` and `BFD_RELOC_HI16_GOTOFF`, respectively, ensuring generated files in `opcodes/` can be safely regenerated.
