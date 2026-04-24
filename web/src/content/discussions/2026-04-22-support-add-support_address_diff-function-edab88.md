---
project: glibc
subsystem: support
patch_id: null
tags:
- aarch64
- address comparison
- pointer arithmetic
- mte
- ifunc
discussion_id: PAWPR08MB8982A758528AC0F6E68A57D9832D2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH v2] support: add support_address_diff function'
headline: 'Support: Add support_address_diff function'
tldr: A new function, support_address_diff, is added to correctly compare addresses
  on AArch64, using the SUBP instruction to ignore top-byte metadata when available.
proposer: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
consensus: Ready to Land
outcome: ready
sentiment_score: null
technical_tradeoffs:
- The `SUBP` instruction may not be available on all AArch64 processors.
- The ifunc resolver adds some runtime overhead.
- Using top byte as metadata might be incompatible with older architectures
exchanges:
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: reviewer
  position: Reviewed and approved the patch.
  quote: 'LGTM. Reviewed-by: Wilco Dijkstra'
primer_expert: This patch introduces `support_address_diff`, an ifunc-resolved function
  for AArch64 that uses the `SUBP` instruction to accurately calculate the difference
  between addresses, ignoring metadata in the upper byte. This is relevant for memory
  management and pointer arithmetic within glibc, particularly when Memory Tagging
  Extension (MTE) is used.
primer_general: When comparing memory addresses in C programs, especially on AArch64
  systems, the raw pointer values might contain extra information in the upper bytes
  (metadata). This can lead to incorrect comparisons if you only care about the actual
  memory location. This patch introduces a new function that correctly calculates
  the difference between two memory addresses by ignoring this extra metadata. This
  is important for functions like malloc that need to compare addresses.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982A758528AC0F6E68A57D9832D2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-22'
---

A new function, `support_address_diff`, is added to glibc to correctly compare addresses on AArch64. It leverages the `SUBP` instruction when available to ignore top-byte metadata, which can be present in 64-bit pointer values. The best implementation is selected using an ifunc resolver. Wilco Dijkstra reviewed and approved the code.
