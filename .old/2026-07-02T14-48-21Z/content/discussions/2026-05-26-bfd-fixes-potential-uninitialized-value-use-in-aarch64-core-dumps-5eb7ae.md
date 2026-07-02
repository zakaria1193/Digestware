---
project: binutils
subsystem: binutils
patch_id: null
tags:
- bfd
- aarch64
- core dump
- memory allocation
- bugfix
discussion_id: ahVq6shyddPt4gaM@squeak.grove.modra.org
source_type: public_inbox
title: 'aarch64 core: use of uninitialised value'
headline: 'BFD: Fixes potential uninitialized value use in aarch64 core dumps'
tldr: Avoids allocating excessive memory for aarch64 core sections by ignoring `rawsize`
  in bfd_core, preventing potential uninitialized value usage and OOM errors.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- By ignoring rawsize in bfd_core, the tool relies solely on the 'size' field, which
  might be insufficient in some edge cases (though none are mentioned).
- The fix avoids excessive memory allocation, improving performance and stability
  when dealing with core files.
exchanges: []
primer_expert: This patch modifies `bfd/bfd.c` to address a potential issue in how
  the BFD library handles section sizes when reading AArch64 core files, specifically
  those using memory tagging extensions (MTE). The `rawsize` field of a section is
  being populated with `p_memsz` from the program header, which may be significantly
  larger than the actual data size (`p_filesz`). This can lead to excessive memory
  allocation and potential use of uninitialized data when `objdump -s` is used on
  core files. The fix ignores `rawsize` for core files, using `size` instead.
primer_general: The Binary File Descriptor (BFD) library provides a generic interface
  for accessing different object file formats. Core files are memory dumps of a running
  process, often used for debugging. This patch fixes a bug in how BFD handles AArch64
  core files that utilize memory tagging extensions. The bug could cause the tool
  to allocate an excessive amount of memory when processing the core file, leading
  to either the use of uninitialized data or an out-of-memory error. The patch modifies
  the logic to correctly determine the necessary memory allocation size.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ahVq6shyddPt4gaM@squeak.grove.modra.org
bugzilla_url: null
date: '2026-05-26'
is_stub: false
---

A recent commit added support for PT_AARCH64_MEMTAG_MTE, which stores `p_memsz` (memory range) in `rawsize` and `p_filesz` in `size` within a section. When reading core files, `bfd` allocates memory based on the larger of `rawsize` and `size`. Since `p_memsz` can be much larger than `p_filesz`, this leads to excessive memory allocation, potentially using uninitialized values or causing OOM errors with fuzzed inputs. This patch avoids these issues by ignoring `rawsize` in `bfd_core` to calculate memory allocation.
