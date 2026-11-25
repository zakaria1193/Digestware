---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- LoongArch
- linker
- relocation
- PIE
- PLT
discussion_id: 20261125023911.58268-1-zhaozhou@loongson.cn
source_type: public_inbox
title: '[PATCH] LoongArch: Use canonical PLT entries for read-only function pointers'
headline: 'LoongArch: Use canonical PLT entries for read-only function pointers'
tldr: Enables successful linking with `-z text` for non-PIE executables using read-only
  function pointers to shared library functions.
proposer: zhaozhou <zhaozhou@loongson.cn>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Slightly increases the complexity of the `loongarch_elf_check_relocs` function to
  handle the specific case of read-only function pointers.
exchanges:
- author: zhaozhou <zhaozhou@loongson.cn>
  role: proposer
  position: Submits a patch to resolve linker errors with `-z text` on non-PIE executables
    by using canonical PLT entries for read-only function pointers to shared library
    functions.
  quote: When a non-PIE executable stores the address of a shared library function
    in read-only data, the relocation scan increments the PLT reference count but
    does not set needs_plt. If the function is only referenced through the pointer,
    the linker leaves an R_LARCH_64 dynamic relocation in .rodata and the link fails
    with -z text.
primer_expert: This patch modifies `bfd/elfnn-loongarch.c` and adds test cases to
  address PR ld/35006. For non-PIE executables, if a function pointer in read-only
  data (`.rodata`) points to a shared library function, the existing logic incorrectly
  handles the PLT (Procedure Linkage Table) reference. Specifically, `needs_plt` is
  not set, leading to a dynamic relocation (`R_LARCH_64`) in `.rodata`. This causes
  a failure when linking with `-z text` (which prohibits writable text segments).
  The fix adds a condition to set `h->needs_plt = 1` when a function entry (`h->type
  == STT_FUNC`) is dynamic, regular, non-…
primer_glossary:
- term: PLT
  definition: Procedure Linkage Table. A table used in dynamically linked executables
    to resolve addresses of functions in shared libraries at runtime.
- term: non-PIE executable
  definition: An executable file that is not position-independent. Its code is loaded
    at a fixed address in memory.
- term: -z text
  definition: A linker option that prohibits writable segments in the output, enforcing
    that the text (code) section remains read-only.
- term: dynamic relocation
  definition: A relocation entry that needs to be processed by the dynamic linker
    at runtime, typically for shared library symbol resolution.
- term: canonical PLT entries
  definition: Standard or pre-defined entries within the Procedure Linkage Table that
    are used for resolving function calls.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261125023911.58268-1-zhaozhou@loongson.cn
bugzilla_url: null
date: '2026-11-25'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where non-PIE executables storing shared library function addresses in read-only data caused linker failures with `-z text`. The relocation scan would increment the PLT reference count but not set `needs_plt`, leaving a dynamic relocation in `.rodata`. The fix resolves this by making the linker use canonical PLT entries for such read-only function pointers, allowing `-z text` links to succeed while maintaining proper dynamic relocation behavior.
