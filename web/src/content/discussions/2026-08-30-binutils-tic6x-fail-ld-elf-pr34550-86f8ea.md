---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- tic6x
- elf
- testcase
discussion_id: apSsUx-lhw2ktfAp@squeak.grove.modra.org
source_type: public_inbox
title: 'tic6x FAIL: ld-elf/pr3455'
headline: 'binutils: tic6x FAIL: ld-elf/pr34550'
tldr: Fixes a test case failure for tic6x by relaxing conditions for creating dynamic
  sections.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 8
technical_tradeoffs:
- Relaxing the `compatible_format` check might allow linking of less compatible object
  files, potentially leading to runtime issues if not fully tested.
- The underlying reason for the differing default target formats between `tic6x-ld`
  and `tic6x-as` remains unaddressed.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch to fix a test case failure related to dynamic section
    creation for the tic6x target.
  quote: 'This fixes a fail for a recently added testcase, the underlying cause

    being that tic6x-ld target defaults to "elf32-tic6x-elf-le", while

    tic6x-as target defaults to "elf32-tic6x-le".  I don''t know why that

    is the case, so rather than reconciling the difference I decided to

    tackle the reason why tic6x-ld --shared doesn''t create dynamic sections

    unless an input object contains relocations.'
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Corrects the subject line for the patch.
  quote: 'Oops, subject should have been "tic6x FAIL: ld-elf/pr34550".'
primer_expert: The tic6x toolchain has differing default target formats for the assembler
  (`tic6x-as`) and linker (`tic6x-ld`). More importantly, `ld --shared` on tic6x requires
  input objects to have relocations to trigger the creation of dynamic sections. This
  patch modifies `elf_link_add_object_symbols` in `bfd/elflink.c` to use `compatible_format`
  instead of an exact target match when determining if dynamic sections should be
  created, resolving a test case failure (`pr34550`) and improving the linker's behavior
  for shared library creation on this target.
primer_glossary:
- term: tic6x
  definition: Refers to the toolchain (assembler and linker) targets for Texas Instruments
    C6000 series DSPs.
- term: ld-elf/pr34550
  definition: A specific test case within the binutils testsuite, identified by the
    prefix 'ld-elf/' and the bug report number 'pr34550'.
- term: default target
  definition: The configuration or format automatically assumed by a tool (like an
    assembler or linker) when not explicitly specified by the user.
- term: relocations
  definition: Information in an object file that specifies how addresses and references
    need to be adjusted by the linker to create the final executable or shared library.
- term: dynamic sections
  definition: Special sections in an ELF file (e.g., .dynamic, .dynsym, .dynstr) that
    contain information necessary for dynamic linking at runtime.
- term: shared library
  definition: A library that can be linked into multiple programs at runtime, allowing
    code and data sharing.
- term: compatible_format
  definition: A function or check within BFD that determines if two different ELF
    target formats are compatible for linking purposes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/apSsUx-lhw2ktfAp@squeak.grove.modra.org
bugzilla_url: null
date: '2026-08-30'
is_stub: false
stub_reason: ''
---

This patch addresses a failure in the `ld-elf/pr34550` test case specific to the tic6x target. The issue arises because tic6x-ld defaults to 'elf32-tic6x-elf-le' while tic6x-as defaults to 'elf32-tic6x-le'. More critically, tic6x-ld's handling of `--shared` fails to create dynamic sections unless an input object contains relocations. The fix relaxes this condition to align with other targets, thereby resolving the test failure.
