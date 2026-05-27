---
project: binutils
subsystem: gdb/microblaze
patch_id: null
tags:
- gdb
- MicroBlaze
- debugging
- Linux
- native
discussion_id: CAL1P33wvSyEkqa5KC8QH3KRN1hGGn2-H6sE59rRjsrLibprvKg@mail.gmail.com
source_type: public_inbox
title: '[PATCH] gdb/MicroBlaze: Add support for native linux gdb'
headline: 'gdb/MicroBlaze: Add support for native linux gdb'
tldr: Adds native Linux support for GDB for the MicroBlaze architecture, including
  core target support and basic debugger functionality.
proposer: Gopi Kumar Bulusu <gopi@sankhya.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased code complexity in GDB.
- Potential for architecture-specific bugs.
- Requires maintaining the MicroBlaze-specific code within GDB.
exchanges:
- author: Gopi Kumar Bulusu <gopi@sankhya.com>
  role: proposer
  position: Clarifies that the patch includes core target support.
  quote: '[ Please note: the typo, including core target support ]'
primer_expert: This patch provides native Linux support for debugging MicroBlaze targets
  directly from a Linux host using GDB. This eliminates the need for remote debugging
  setups in some scenarios. MicroBlaze is a soft processor core often used in Xilinx/AMD
  FPGAs.
primer_general: GDB (GNU Debugger) is a tool used to debug programs. This patch adds
  the ability to run GDB directly on a Linux computer to debug programs running on
  a MicroBlaze processor (a type of embedded processor often found in FPGAs). This
  simplifies the debugging process compared to using a remote debugger.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAL1P33wvSyEkqa5KC8QH3KRN1hGGn2-H6sE59rRjsrLibprvKg@mail.gmail.com
bugzilla_url: null
date: '2026-05-26'
is_stub: false
---

Gopi Kumar Bulusu proposes a patch to add native Linux support for GDB (GNU Debugger) for the MicroBlaze architecture. This includes core target support and enables commonly used debugger functions such as breakpoints, stepping, and printing. The patch is based on sources from the Xilinx/AMD Yocto git repository and has been tested on a Linux instance running on QEMU.
