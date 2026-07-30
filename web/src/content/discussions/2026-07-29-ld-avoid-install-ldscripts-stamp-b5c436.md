---
project: binutils
subsystem: ld
patch_id: null
tags:
- binutils
- ld
- build
- makefile
discussion_id: SL2P216MB22712048BFD9787E6B385D59EFCA2@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
source_type: public_inbox
title: '[PATCH] ld: avoid install ldscripts/stamp'
headline: 'ld: avoid install ldscripts/stamp'
tldr: Fixes ld Makefile to correctly exclude 'ldscripts/stamp' from installation.
proposer: Zhongteng Gui <dragon-archer@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs: []
exchanges: []
primer_expert: This patch addresses an installation issue within the GNU linker (ld)
  component of binutils. Specifically, it corrects a Makefile configuration that erroneously
  included a file named 'stamp' within the 'ldscripts' directory during the installation
  process. The fix ensures that this file is now correctly excluded, adhering to the
  intended installation scope.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or library.
- term: ldscripts
  definition: Directory containing linker scripts, which are configuration files that
    control how the linker combines input sections into output sections.
- term: Makefile
  definition: A file containing build instructions for the `make` utility, automating
    the compilation and installation process.
- term: install
  definition: The process of copying built files from the build directory to their
    final destination on the system.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/SL2P216MB22712048BFD9787E6B385D59EFCA2@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-07-29'
is_stub: false
stub_reason: ''
---

This patch corrects an issue in the ld linker's Makefile, ensuring that 'ldscripts/stamp' is properly excluded from being installed. This rectifies a mistake in a previous commit that failed to implement this exclusion, preventing unintended files from being included in the build output.
