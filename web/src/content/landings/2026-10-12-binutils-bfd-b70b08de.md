---
project: binutils
subsystem: binutils/bfd
patch_id: null
tags:
- binutils
- bfd
- rx
- endianness
- gdb
commit_hash: b70b08de3ca11759dd357aba9d919043eee93673
source_type: public_inbox
author: Alan Modra <amodra@sourceware.org>
headline: Fix destination pointer advancement in RX big-endian section reads
tldr: Corrects out-of-bounds writes in big-endian RX executable section reads on unaligned
  offsets.
impact_score: 6
performance_win: false
breaking_change: false
outcome: committed
primer_expert: In `bfd/elf32-rx.c`, the `rx_get_section_contents` function's destination
  cursor `cloc` was incorrectly advanced by `count` (remaining bytes) instead of `cnt`
  (consumed bytes) after a partial copy. This commit corrects the advancement to `cloc
  += cnt`, preventing buffer overflows when processing unaligned section data on big-endian
  RX targets.
primer_glossary:
- term: big-endian
  definition: A byte order where the most significant byte is stored at the lowest
    memory address. This is in contrast to little-endian, where the least significant
    byte is at the lowest address.
- term: RX
  definition: Renesas RX, a family of 32-bit microcontrollers.
- term: unaligned offset
  definition: An access to memory at an address that is not a multiple of the data's
    size (e.g., accessing a 4-byte integer at an address not divisible by 4). This
    can be less efficient or even cause errors on some architectures.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261012074651.BD2644BA2E0F@sourceware.org
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

A bug in `rx_get_section_contents` for big-endian RX code sections caused incorrect destination pointer advancement when reading at unaligned offsets. The function advanced the pointer by the remaining byte count instead of the number of bytes actually consumed, leading to subsequent out-of-bounds writes during word-swapping. This fix ensures the pointer is advanced by the correct number of consumed bytes, preventing memory corruption, particularly during GDB target memory reads.
