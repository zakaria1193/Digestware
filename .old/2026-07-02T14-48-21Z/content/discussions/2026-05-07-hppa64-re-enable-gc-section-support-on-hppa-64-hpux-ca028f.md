---
project: binutils
subsystem: hppa64
patch_id: null
tags:
- binutils
- ld
- hppa64
- hpux
- -gc-section
discussion_id: afzhO5PU_mFNt-5V@mx3210.local
source_type: public_inbox
title: '[committed] hppa64: Re-enable -gc-section support on hppa*64*-*-hpux*'
headline: 'Hppa64: Re-enable -gc-section support on hppa*64*-*-hpux*'
tldr: -gc-section support is re-enabled for hppa64-*-hpux targets by allocating space
  in .data to handle invalid relocation offsets.
proposer: John David Anglin <dave.anglin@bell.net>
consensus: Committed
outcome: committed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- The change allocates 16 bytes of space in the .data section, increasing the size
  of the executable slightly.
- The solution is specific to HP-UX and may not be applicable to other platforms.
- The change simplifies the relocation process and enables garbage collection.
exchanges: []
primer_expert: The `-gc-section` flag enables garbage collection of unused sections
  during linking.  This patch re-enables this feature for hppa64-*-hpux targets by
  allocating space to handle invalid relocation offsets. The HP-UX dynamic linker
  requires valid relocation offsets, and this change provides a workaround.
primer_general: The `-gc-section` option tells the linker to remove unused code and
  data from the final executable, reducing its size. This patch fixes a problem that
  prevented this optimization from working correctly on HP-UX systems. The fix involves
  reserving some space in the data section to handle certain types of relocation issues.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/afzhO5PU_mFNt-5V@mx3210.local
bugzilla_url: null
date: '2026-05-07'
---

John David Anglin re-enables `-gc-section` support for hppa64-*-hpux targets. The change allocates 16 bytes at the start of the `.data` section for the linker to handle relocations with invalid offsets. This resolves issues with the HP dynamic linker and allows for garbage collection of unused sections.
