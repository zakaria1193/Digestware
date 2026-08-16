---
project: binutils
subsystem: ld/makefile.am
patch_id: null
tags:
- build system
- makefile
- linker
- binutils
- race condition
discussion_id: CACtFPF0gq-TtGy1fAOQnZE=auqP-w3mn2uT=ebLBStV928ZCdg@mail.gmail.com
source_type: public_inbox
title: '[PATCH/BUG] ld/Makefile.am: missing dependency on ldscripts/stamp for e%.c
  target'
headline: 'ld/Makefile.am: missing dependency for e%.c target'
tldr: Fixes a build issue in ld/Makefile.am where genscripts.sh runs before the ldscripts/
  directory is created, causing build failures.
proposer: A B C <ddupard68@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensuring build correctness and robustness against parallel build environments vs.
  potentially adding minor overhead to the build process due to an extra dependency
  check.
exchanges:
- author: A B C
  role: proposer
  position: Identified a build issue where `genscripts.sh` fails due to the `ldscripts/`
    directory not existing when the `e%.c` target is processed, and proposed adding
    a dependency to fix it.
  quote: 'The failure happens because the ldscripts/ directory does not exist at the
    time genscripts.sh is executed. Because the output files cannot be created in
    ldscripts/, the resulting C variables in e${EMULATION_NAME}.c end up empty/corrupted
    (e.g. generating broken statements like return ; instead of returning the script
    string), which subsequently fails during C compilation.


    Proposed Fix: Adding $(…'
primer_expert: This patch addresses a build-time race condition in binutils' ld/Makefile.am.
  The `e%.c` target, which generates C source files for emulation scripts using `genscripts.sh`,
  lacks a dependency on the creation of the `ldscripts/` directory. This can lead
  to `genscripts.sh` executing before its output directory is ready, causing build
  failures, especially with parallel builds (`make -j`). The fix adds a dependency
  on `$(GEN_DEPENDS)` or `ldscripts/stamp` to ensure the directory exists prior to
  script generation.
primer_glossary:
- term: ldscripts/
  definition: A directory within the binutils source tree that contains linker script
    templates and related files used to configure the behavior of the GNU linker (ld).
- term: genscripts.sh
  definition: A shell script used by GNU ld to generate C source files from linker
    script templates, embedding script logic into the linker executable.
- term: e%.c
  definition: A pattern rule in Makefile.am for generating C source files (e.g., 'eelf32ppc.c')
    that define emulation-specific linker behavior.
- term: Makefile.am
  definition: A file used by the Autotools build system (specifically Automake) to
    describe how to build the project's targets.
- term: make -j
  definition: A command-line option for the `make` utility that allows parallel execution
    of build rules, potentially leading to race conditions if dependencies are not
    correctly specified.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CACtFPF0gq-TtGy1fAOQnZE=auqP-w3mn2uT=ebLBStV928ZCdg@mail.gmail.com
bugzilla_url: null
date: '2026-08-15'
is_stub: false
stub_reason: ''
---

A bug in ld/Makefile.am prevents the correct generation of emulation C sources (e%.c). The rule for creating these files runs `genscripts.sh` before the `ldscripts/` directory and its stamp file are created, leading to build failures with missing file errors. This patch proposes adding `$(GEN_DEPENDS)` or `ldscripts/stamp` as a prerequisite to the `e%.c` target to ensure the directory exists before `genscripts.sh` is executed.
