---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- readelf
- dwarf
- debuginfo
- debug_names
discussion_id: 20260522121618.1460707-1-tdevries@suse.de
source_type: public_inbox
title: '[PATCH] [binutils] Handle implicit const in .debug_names'
headline: Handle implicit const in .debug_names
tldr: Readelf now supports DW_FORM_implicit_const in .debug_names sections, fixing
  errors when reading debug info for gdb test cases.
proposer: Tom de Vries <tdevries@suse.de>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Adding support for new DWARF forms increases the complexity of readelf.
- The patch may need to be updated if the DWARF standard evolves further.
exchanges:
- author: Tom de Vries <tdevries@suse.de>
  role: proposer
  position: Proposes adding support for DW_FORM_implicit_const in display_debug_names
    to fix readelf errors.
  quote: "Add support for DW_FORM_implicit_const in display_debug_names, such that\
    \ we\nget the expected:\n...\nSymbol table:\n[  1] #eddb6232 _start: <0><1> DW_TAG_subprogram\
    \ DW_IDX_compile_unit=0\n[  2] #53a2ae86 struct_with_int_member: <0x3><2> DW_TAG_structure_type\
    \ \\\n      DW_IDX_type_unit=0 DW_IDX_GNU_language=2"
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the patch and its fixes.
  quote: 'I tried to use readelf to read the debug info for gdb test-case

    gdb.dwarf2/debug-names-tu-dwarf5.exp, and ran into some trouble reading the

    .debug_names section:

    ...'
primer_expert: The .debug_names section is a DWARF5 construct that provides a faster
  way to locate debug information entries (DIEs) by name. DW_FORM_implicit_const is
  a DWARF form that represents a constant value implicitly, without storing it directly
  in the .debug_names section. Readelf is a binutils utility that displays information
  about ELF files, including debug information.
primer_general: Debug information helps debuggers like GDB map machine code back to
  the original source code.  DWARF is a standard format for representing this debug
  information.  The `.debug_names` section (introduced in DWARF version 5) is an index
  that speeds up the process of finding debug information by name. `readelf` is a
  command-line tool that displays the contents of ELF (Executable and Linkable Format)
  files, the standard format for executables on Linux and other systems; it needs
  to understand the DWARF format to display debug info.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260522121618.1460707-1-tdevries@suse.de
bugzilla_url: null
date: '2026-05-22'
is_stub: false
---

This patch adds support for `DW_FORM_implicit_const` in the `.debug_names` section when using `readelf`. This fixes an issue where `readelf` would fail to read debug information for certain gdb test cases due to encountering this form in the abbreviation table. The patch modifies `binutils/dwarf.c` to handle the `DW_FORM_implicit_const` entry.
