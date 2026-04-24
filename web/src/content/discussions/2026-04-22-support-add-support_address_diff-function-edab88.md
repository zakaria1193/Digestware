---
project: glibc
subsystem: support
patch_id: null
tags:
- glibc
- AArch64
- pointer arithmetic
- MTE
- address comparison
discussion_id: PAWPR08MB8982A758528AC0F6E68A57D9832D2@PAWPR08MB8982.eurprd08.prod.outlook.com
source_type: public_inbox
title: 'Re: [PATCH v2] support: add support_address_diff function'
headline: 'support: add support_address_diff function'
tldr: Wilco Dijkstra reviews and approves a patch adding `support_address_diff` for
  AArch64 to handle pointer metadata.
proposer: Wilco Dijkstra
consensus: Ready to Land
outcome: ready
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Wilco Dijkstra <Wilco.Dijkstra@arm.com>
  role: reviewer
  position: Approves the patch.
  quote: 'LGTM.


    Reviewed-by: Wilco Dijkstra <Wilco.Dijkstra@arm.com>'
primer_expert: This patch adds a new support function to glibc to handle pointer arithmetic
  on AArch64, specifically in the presence of Memory Tagging Extensions (MTE). MTE
  adds metadata to pointers, which needs to be masked out when comparing addresses.
  The `support_address_diff` function uses the SUBP instruction when available to
  ignore this metadata.
primer_general: Pointers are memory addresses that programs use to access data. On
  some architectures, like AArch64 with Memory Tagging Extensions (MTE), pointers
  can contain additional metadata beyond the raw memory address. This metadata can
  interfere with simple pointer comparisons. This patch introduces a new function,
  `support_address_diff`, to correctly calculate the difference between two addresses,
  taking into account any potential metadata.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/libc-alpha/PAWPR08MB8982A758528AC0F6E68A57D9832D2@PAWPR08MB8982.eurprd08.prod.outlook.com
bugzilla_url: null
date: '2026-04-22'
---

This patch introduces the `support_address_diff` function to correctly compare addresses on AArch64, which may contain metadata in the 64-bit pointer value.  The function uses the SUBP instruction when available, ignoring top-byte metadata. Wilco Dijkstra has reviewed and approved the patch.
