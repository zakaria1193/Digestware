---
project: gcc
subsystem: gcc/build
patch_id: null
tags:
- build
- platform
- Windows
- cross-compilation
- mingw
discussion_id: SL2P216MB22713567DF1A0CC2252CC300EFD82@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
source_type: public_inbox
title: Switching from i686-mingw32 to x86_64-w64-mingw32?
headline: Switching Windows target from i686-mingw32 to x86_64-w64-mingw32
tldr: Proposes replacing the i686-mingw32 GCC secondary target with x86_64-w64-mingw32
  due to i686's deprecation and x86_64's prevalence.
proposer: Zhongteng Gui <dragon-archer@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Removing support for `i686-mingw32` might affect niche users still developing for
  32-bit Windows.
- Updating platform lists requires careful coordination across documentation and build
  system configurations.
exchanges:
- author: Zhongteng Gui
  role: proposer
  position: Suggests updating GCC's secondary platform list to use x86_64-w64-mingw32
    instead of i686-mingw32, citing deprecation and prevalence.
  quote: Considering that i686 devices are very rare compared to x86_64 nowadays,
    I think it would be better to switching from i686-mingw32 to x86_64-w64-mingw32
    as a secondary platform.
primer_expert: This discussion concerns the platform triplets listed as secondary
  targets in GCC's supported configurations. The proposer points out that `i686-mingw32`
  is problematic as a triplet and that its common use case, `i686-w64-mingw32`, is
  being phased out by major distributions like MSYS2 in favor of `x86_64-w64-mingw32`.
  The proposal is to update the GCC documentation and build system to reflect this
  shift towards 64-bit Windows targets.
primer_glossary:
- term: Triplet
  definition: A string format (architecture-vendor-OS) used to identify a target platform
    for cross-compilation, e.g., x86_64-w64-mingw32.
- term: mingw32
  definition: Minimalist GNU for Windows, a development environment that provides
    a Windows port of the GNU Compiler Collection (GCC) and related tools.
- term: MSYS2
  definition: A software distribution and building platform for Windows, providing
    a Unix-like shell environment and package management for GCC and other development
    tools.
- term: UCRT64
  definition: A specific MSYS2 environment targeting Windows using the Universal C
    Runtime, predominantly for 64-bit applications.
- term: Secondary platform
  definition: A target platform that GCC supports but is not considered a primary,
    actively developed target, often with less extensive testing or feature support.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/SL2P216MB22713567DF1A0CC2252CC300EFD82@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-08-16'
is_stub: false
stub_reason: ''
---

Zhongteng Gui questions the continued listing of `i686-mingw32` as a secondary GCC platform, arguing it's an invalid triplet and that its likely intended counterpart, `i686-w64-mingw32`, has been deprecated by MSYS2. Given the dominance of 64-bit systems and the shift in MSYS2 environments to `x86_64-w64-mingw32`, the proposal is to switch the secondary target to the 64-bit version.
