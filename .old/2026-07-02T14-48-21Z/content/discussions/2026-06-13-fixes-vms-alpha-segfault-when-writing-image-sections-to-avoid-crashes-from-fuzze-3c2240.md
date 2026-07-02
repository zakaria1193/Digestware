---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- vms-alpha
- fuzzing
- segfault
discussion_id: aiz9Vn-M-AAD-CQo@squeak.grove.modra.org
source_type: public_inbox
title: 'oss-fuzz: vms-alpha segfault in image_write_section'
headline: Fixes vms-alpha segfault when writing image sections to avoid crashes from
  fuzzed object files
tldr: A patch prevents a segfault in vms-alpha support within binutils when processing
  fuzzed object files by adding a NULL check for `image_section`.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Proposes a fix for a segfault in `image_write_section` in `vms-alpha.c`,
    adding a NULL check to prevent crashes caused by fuzzed object files.
  quote: 'Yet another case where a fuzzed object file triggers a crash in the vms-alpha
    support. * vms-alpha.c (image_write_section): Don''t segfault on NULL image_section.'
primer_expert: This fix targets the Binutils BFD (Binary File Descriptor) library,
  specifically the `vms-alpha.c` backend, which handles object file manipulation for
  the VMS-Alpha architecture. The issue arises in `image_write_section`, a function
  responsible for writing a section's contents. `PRIV(image_section)` accesses architecture-specific
  private data within a `bfd` object. A NULL `image_section` indicates an invalid
  or corrupted section descriptor, which, when dereferenced without a prior check,
  leads to a segfault. This highlights general robustness concerns in handling malformed
  inputs within BFD b…
primer_general: Imagine a program that helps computers understand and work with different
  kinds of program files (like `.exe` files on Windows or `.o` files on Linux). This
  program is called Binutils, and it has a component called BFD (Binary File Descriptor).
  BFD's job is to read, write, and manipulate these files. Different computer architectures
  (like ARM or x86, and in this case, VMS-Alpha) have their own specific ways of structuring
  these files, so BFD has different modules (called 'backends') to handle each. This
  particular issue cropped up when a testing tool (fuzzer) gave a VMS-Alpha file that
  was malformed to BFD, which caused the program to crash (a 'segfault'). The fix
  introduces a check to make sure that the program doesn't try to use invalid data
  when processing these files, making it more robust against corrupt or maliciously
  crafted inputs.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/aiz9Vn-M-AAD-CQo@squeak.grove.modra.org
bugzilla_url: null
date: '2026-06-13'
is_stub: false
---

Alan Modra submitted a patch to address a segfault in the `image_write_section` function within the vms-alpha support of binutils' BFD library. This crash occurs when processing malformed or fuzzed object files, specifically when `image_section` is NULL. The proposed fix introduces a NULL check for `sec` (which is `PRIV(image_section)`) at the beginning of the function, ensuring that the process handles invalid inputs gracefully instead of crashing.
