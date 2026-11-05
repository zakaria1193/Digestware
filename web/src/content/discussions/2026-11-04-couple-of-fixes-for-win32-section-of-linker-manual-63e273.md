---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- documentation
- windows
discussion_id: 2625506.WW41rfXDos@fomalhaut
source_type: public_inbox
title: Couple of fixes for Win32 section of linker manual
headline: Couple of fixes for Win32 section of linker manual
tldr: Patch corrects outdated information in the binutils linker manual regarding
  Win32 pseudo-relocation support.
proposer: Eric Botcazou <botcazou@adacore.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 9
technical_tradeoffs: []
exchanges:
- author: Eric Botcazou <botcazou@adacore.com>
  role: proposer
  position: Submits a patch to fix inaccuracies in the Win32 section of the linker
    manual, correcting a switch name and noting default enablement of pseudo-relocations.
  quote: "The whole section is a little bit outdated, but this fixes at least a couple\
    \ \nof blatant issues in the description of the support for pseudo relocations:\
    \ \nthe name of the switch is misspelled (no terminating 's') and it has been\
    \ \nenabled by default for a while now."
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Agrees with the proposed changes, stating 'Okay'.
  quote: Okay.
primer_expert: This submission updates documentation within the binutils linker manual,
  specifically the section covering Win32 target support. It addresses outdated details
  about pseudo-relocation handling, including a typographical error in a command-line
  switch and the fact that this feature is now enabled by default. This is a documentation-only
  change.
primer_glossary:
- term: pseudo relocation
  definition: A type of relocation that doesn't directly correspond to a machine instruction
    but is used internally by the linker, often for special purposes like symbol resolution
    or address calculation.
- term: linker manual
  definition: Documentation for the GNU linker (ld), explaining its usage, options,
    and features for creating executable programs from object files.
- term: Win32
  definition: Refers to the target architecture and operating system environment for
    Microsoft Windows, specifically the 32-bit version, though often used more broadly.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/2625506.WW41rfXDos@fomalhaut
bugzilla_url: null
date: '2026-11-04'
is_stub: false
stub_reason: ''
---

This patch corrects two inaccuracies in the binutils linker manual's section on Win32 support. Specifically, it fixes a misspelled switch name and updates the information that pseudo-relocation support is now enabled by default. The author tested the changes by building binutils for a Windows cross-compilation target.
