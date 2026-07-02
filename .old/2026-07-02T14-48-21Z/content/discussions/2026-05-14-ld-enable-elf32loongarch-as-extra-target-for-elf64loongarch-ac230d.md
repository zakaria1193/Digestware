---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- linker
- LoongArch
- multilib
discussion_id: 20260514171358.789613-1-xry111@xry111.site
source_type: public_inbox
title: '[PATCH] ld: enable elf32loongarch as extra target for elf64loongarch and vice
  versa'
headline: 'ld: Enable elf32loongarch as extra target for elf64loongarch'
tldr: The patch allows building GCC with multilib support for LoongArch without needing
  `--enable-targets=all` in the binutils configuration.
proposer: Xi Ruoyao <xry111@xry111.site>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- May increase linker complexity slightly.
- Potentially increases the size of the linker binary.
- Reduces the need for building all targets, saving build time and disk space.
exchanges:
- author: Xi Ruoyao
  role: proposer
  position: Proposes enabling elf32loongarch as an extra target for elf64loongarch
    and vice versa to allow building GCC with multilib support without `--enable-targets=all`.
  quote: 'Allow people to build GCC with multilib support even without

    --enable-targets=all in binutils configuration.'
- author: Alan Modra
  role: other
  position: Acknowledges the patch.
  quote: null
primer_expert: This patch modifies ld's target configuration to allow cross-linking
  between LoongArch's 32-bit (elf32loongarch) and 64-bit (elf64loongarch) ABIs. It
  achieves this by adding each ABI to the other's `targ_extra_libpath`. This avoids
  needing `--enable-targets=all` in binutils, which can be cumbersome. This change
  affects how the linker searches for libraries when building multilib-enabled toolchains.
primer_general: The GNU linker (ld) is a program that combines object files into an
  executable or library.  Binutils is a collection of binary tools, including the
  linker, assembler, and other utilities.  Multilib refers to the ability to build
  a single toolchain that can target multiple ABIs (Application Binary Interfaces),
  such as 32-bit and 64-bit versions of the same architecture.  LoongArch is a RISC
  instruction set architecture.  This patch simplifies the process of building a GCC
  toolchain that can target both 32-bit and 64-bit LoongArch systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260514171358.789613-1-xry111@xry111.site
bugzilla_url: null
date: '2026-05-14'
is_stub: false
---

This patch modifies the linker configuration to allow building GCC with multilib support for LoongArch, even when binutils isn't configured with `--enable-targets=all`.  It adds `elf32loongarch` as an extra target for `elf64loongarch` and vice versa.  This simplifies the build process for developers working with LoongArch multilib configurations by avoiding the need to build all possible targets.
