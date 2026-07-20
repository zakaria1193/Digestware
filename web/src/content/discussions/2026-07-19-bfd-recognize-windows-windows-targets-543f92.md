---
project: binutils
subsystem: bfd
patch_id: null
tags:
- binutils
- bfd
- ld
- windows
- target-configuration
discussion_id: alpine.DEB.2.21.2607200021490.64835@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: [PATCH] bfd: recognize *-*-windows* Windows targets'
headline: 'bfd: recognize *-*-windows* Windows targets'
tldr: Reviewer questions if a patch to recognize Windows targets in BFD breaks existing
  build configurations for 'ld'.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- The tradeoff is between improving target recognition for Windows and ensuring that
  existing build configurations, particularly for `ld`, are not broken.
exchanges:
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: reviewer
  position: Questions if the patch breaks 'ld' compilation on Windows targets when
    not explicitly disabled, suggesting that unsupported subdirectories should be
    handled by preventing configuration rather than by breaking compilation.
  quote: 'Does it break compilation then where no explicit `--disable-ld'' has been
    given?  If so, then it''s a no-no, cf. commit 58d798318c42 ("AMDGCN: Disable subdirectory
    configuration for unsupported GAS and LD") for the right way to handle it.'
- author: Pedro Alves
  role: other
  position: Indicates that `ld` currently fails with a "does not support target" error
    for these Windows configurations and that users often disable `ld` during configuration.
  quote: null
primer_expert: This discussion concerns the GNU Binutils collection, specifically
  the Binary File Descriptor (BFD) library and the linker (ld). The patch aims to
  improve target configuration for Windows platforms. The core issue is ensuring that
  unrecognized Windows targets within BFD do not inadvertently cause `ld` to be configured
  or built, potentially leading to build failures or incorrect configurations.
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a low-level library used by GNU binutils
    for manipulating object file formats.
- term: ld
  definition: The GNU linker, responsible for combining object files into executables
    or libraries.
- term: configure
  definition: The process of adapting generic source code to a specific operating
    system and hardware environment.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2607200021490.64835@angie.orcam.me.uk
bugzilla_url: null
date: '2026-07-19'
is_stub: false
stub_reason: ''
---

A patch aims to improve BFD's recognition of Windows targets within the GNU toolchain. A reviewer raises concern about potential build breakage for the linker (`ld`), questioning if the proposed change might cause it to be configured or built when it should not be for these targets. The reviewer suggests a proper way to handle unsupported subdirectories if breakage occurs.
