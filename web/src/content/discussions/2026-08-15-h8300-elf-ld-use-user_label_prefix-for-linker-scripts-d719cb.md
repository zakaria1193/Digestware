---
project: binutils
subsystem: h8300-elf
patch_id: null
tags:
- linker
- embedded
- symbol naming
- binutils
- gcc
discussion_id: 20260815073659.709410-1-jdx@o2.pl
source_type: public_inbox
title: '[PATCH] h8300-elf: ld: Use USER_LABEL_PREFIX when generating linker scripts.'
headline: 'h8300-elf ld: Use USER_LABEL_PREFIX for linker scripts'
tldr: Ensures the h8300-elf linker uses the USER_LABEL_PREFIX, aligning with GCC's
  convention for symbol names and preventing potential weak symbol issues.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensuring consistent symbol naming between GCC and ld for the h8300-elf target vs.
  adherence to a specific prefix convention.
exchanges:
- author: Jan Dubiec
  role: proposer
  position: Proposed using USER_LABEL_PREFIX in h8300-elf linker scripts to resolve
    a discrepancy with GCC's symbol naming conventions, which can lead to bugs with
    weak symbols.
  quote: 'Gcc sets USER_LABEL_PREFIX: https://gcc.gnu.org/git/?p=gcc.git;a=blob;f=gcc/config/h8300/elf.h;hb=HEAD
    .

    Strangely, ld does not. As a result, ld exports a symbol without a leading

    underscore, while gcc expects the symbol to have one. For example:


    This can lead to sneaky bugs when the symbol is declared as weak. It also

    creates maintenance issues when the C code is intended to be multiplatform.'
primer_expert: This patch for the h8300-elf target in binutils' ld corrects a naming
  inconsistency between the compiler (GCC) and the linker. GCC defines `USER_LABEL_PREFIX`
  (e.g., '_') for symbols, but the h8300-elf linker scripts were not respecting this.
  Consequently, symbols like `__preinit_array_start` would be exported by `ld` without
  the leading underscore, while C code compiled by GCC expects it. This patch adds
  `USER_LABEL_PREFIX=_` to `ld/emulparams/h8300elf.sh` to align the linker's output
  with GCC's expectations, mitigating potential issues with weak symbols and improving
  cross-platform compatib…
primer_glossary:
- term: USER_LABEL_PREFIX
  definition: A compiler or linker configuration option that specifies a prefix to
    be added to user-defined labels (symbols) to ensure unique naming or conform to
    specific conventions.
- term: h8300-elf
  definition: A target architecture and ABI combination, specifically the Renesas
    H8/300 microcontroller family used with the ELF object file format and standard
    C calling conventions.
- term: linker script
  definition: A file used by the linker to control how sections of object files are
    placed in the final executable or library, defining memory layout and symbol resolution.
- term: weak symbol
  definition: A symbol that can be overridden by a non-weak symbol of the same name.
    If multiple weak symbols exist, the linker typically chooses one, or an error
    occurs if none is found.
- term: PROVIDE_HIDDEN
  definition: A linker script directive that defines a symbol and makes it hidden,
    meaning it is not visible to other object files unless explicitly resolved.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20260815073659.709410-1-jdx@o2.pl
bugzilla_url: null
date: '2026-08-15'
is_stub: false
stub_reason: ''
---

This patch modifies the h8300-elf linker script generation to use the `USER_LABEL_PREFIX`. GCC for h8300-elf sets this prefix (typically '_'), but the linker was not using it, leading to mismatches between expected and actual symbol names. This inconsistency can cause subtle bugs, especially with weak symbols, and complicates multiplatform development. By applying the prefix in the linker scripts, the symbol naming becomes consistent between the compiler and the linker.
