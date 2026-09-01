---
project: binutils
subsystem: gas
patch_id: null
tags:
- gas
- loongarch
- relocation
- bugfix
commit_hash: aadae9fae2695bd989f26c90bc4f7ebdb495f4d5
source_type: public_inbox
author: liu zhensong <liuzhensong@sourceware.org>
headline: Fix PC-relative offset calculation for LoongArch
tldr: Corrects the PC-relative offset calculation in the LoongArch assembler.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `md_pcrel_from` function in `gas/config/tc-loongarch.c` determines
  the base address for calculating PC-relative relocations. On LoongArch, these relocations
  are relative to the instruction's address. The previous implementation incorrectly
  returned 0, implying a fixed base or an error. The fix updates it to calculate the
  correct PC-relative base by adding the fragment's address (`fr_address`) and the
  fixup's offset within the fragment (`fx_where`). This ensures correct relocation
  calculation for PC-relative addressing modes.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project.
- term: LoongArch
  definition: An open-source instruction set architecture developed by Loongson Technology.
- term: PC-relative offset
  definition: An offset calculated with respect to the current Program Counter (PC)
    value. Used for position-independent code.
- term: relocation
  definition: Information in an object file that specifies how to modify code or data
    after linking, typically to resolve symbol addresses or adjust offsets.
- term: fixS
  definition: A structure used internally by the assembler to represent fixups or
    relocation information.
- term: fragment (fx_frag)
  definition: A unit of code or data within the assembler's internal representation,
    often corresponding to a section or a part of a section.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260831081135.12CCF4BA23E2@sourceware.org
date: '2026-08-31'
is_stub: false
stub_reason: ''
---

This commit corrects the calculation of PC-relative offsets for the LoongArch architecture in the GNU assembler. Previously, `md_pcrel_from` incorrectly returned 0, which is not the correct base address for PC-relative jumps on LoongArch (which are relative to the start of the current instruction). The function has been updated to return `fixP->fx_frag->fr_address + fixP->fx_where`, providing the correct offset.
