---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- xcoff
- security
- fuzzing
commit_hash: 86a70c3fe7d5d629732cadf00b1f79c55f0782c8
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Fix XCOFF armap traversal to prevent out-of-bounds reads
tldr: Corrects XCOFF armap processing in binutils to prevent memory errors.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `xcoff_write_armap_big` function in `bfd/coff-rs6000.c` processes
  XCOFF armap symbol names. An OSS-Fuzz report indicated that the loop condition for
  iterating through the `map` array was insufficient, allowing `i` to exceed `orl_count`
  in certain cases. This patch corrects the loop conditions to ensure that `i` is
  always less than `orl_count` before accessing `map[i]`, preventing potential uninitialized
  reads or buffer overflows.
primer_glossary:
- term: XCOFF
  definition: Extended Common Object File Format, a variant of COFF used on IBM RS/6000
    and other systems.
- term: armap
  definition: A symbol table extension in XCOFF that maps archive member names to
    their BFD structures.
- term: BFD
  definition: Binary File Descriptor library, a low-level library used by binutils
    to read and write object file formats.
- term: OSS-Fuzz
  definition: A free fuzzing-as-a-service for open-source projects provided by Google.
- term: buffer overflow
  definition: A condition where a program attempts to write more data to a buffer
    than it can hold, potentially overwriting adjacent memory.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261109225244.CA6224B920C5@sourceware.org
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This commit fixes a bug in binutils' handling of XCOFF armap symbol names that could lead to out-of-bounds reads or buffer overflows. The `xcoff_write_armap_big` function in `coff-rs6000.c` has been modified to correctly check the `armap` count within its loops, ensuring that it does not read past the allocated buffer when matching symbol names against BFD archives.
