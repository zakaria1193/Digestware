---
project: binutils
subsystem: microblaze
patch_id: null
tags:
- microblaze
- assembler
- relocation
commit_hash: ee6b7f5bb8e8aad1694f0c85c47d9a05417d86dd
source_type: public_inbox
author: Michael Eager <eager@sourceware.org>
headline: 'MicroBlaze: Handle BFD_RELOC_8 and BFD_RELOC_16 relocations'
tldr: MicroBlaze assembler now correctly handles 8-bit and 16-bit relocations, fixing
  incorrect zeroing of data.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `md_apply_fix` function in `tc-microblaze.c` handles MicroBlaze
  relocations. Previously, it only had explicit cases for BFD_RELOC_32 and BFD_RELOC_64,
  and MicroBlaze-specific relocations. BFD_RELOC_8 and BFD_RELOC_16 would fall through
  to a default handler that wrote nothing, leading to zeroed data when these relocations
  were present. This change ensures these smaller relocations are handled similarly
  to other architectures like aarch64, mips, and sparc by using `md_number_to_chars`
  to write the value, preventing data loss and fixing testsuite failures.
primer_glossary:
- term: BFD_RELOC_8
  definition: A relocation type in the Binary File Descriptor (BFD) library representing
    an 8-bit data field that needs to be resolved at link time.
- term: BFD_RELOC_16
  definition: A relocation type in the Binary File Descriptor (BFD) library representing
    a 16-bit data field that needs to be resolved at link time.
- term: fixup time
  definition: The stage in the assembly or compilation process where symbolic addresses
    or values are replaced with their final, resolved numerical values. This typically
    happens before or during linking.
- term: md_apply_fix
  definition: A function within the BFD library's machine-dependent code for a specific
    architecture (here, MicroBlaze) that applies relocation information to the output
    object file.
- term: md_number_to_chars
  definition: A BFD library function that converts a numerical value into a sequence
    of bytes in the target's endianness, used for writing data into object files.
- term: BFD_RELOC_NONE
  definition: A relocation type indicating that no further relocation processing is
    needed for a particular symbol or address.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project. It translates assembly
    language code into machine code.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260924153052.9FDBD4BA9000@sourceware.org
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

The MicroBlaze assembler's `md_apply_fix` function previously lacked specific cases for BFD_RELOC_8 and BFD_RELOC_16 relocations. This caused byte or halfword data, whose values were only known at fixup time, to be assembled as zero, with no relocation information surviving for the linker. This commit adds these cases, ensuring values are written correctly and fixing issues in the gas testsuite.
