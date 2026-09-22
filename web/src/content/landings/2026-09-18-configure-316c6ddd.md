---
project: gcc
subsystem: configure
patch_id: null
tags:
- configure
- dwarf
- assembler
commit_hash: 316c6dddbb4858c2c34b58b3bddc6b85923d2799
source_type: github
author: Christophe Lyon
headline: Fix assembler check for --gdwarf-4 option
tldr: Ensures assembler check for DWARF 4 debug info works across architectures.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The configure script's test for DWARF 4 assembler support relied on
  a specific instruction sequence ending in `ret`. This commit generalizes the check
  by using `$insn`, accommodating architectures where `ret` is not the appropriate
  or available instruction for the test's purpose.
primer_glossary:
- term: DWARF
  definition: A standard file format that represents debugging information within
    compiled programs. DWARF 4 is a specific version of this standard.
- term: assembler
  definition: A program that translates assembly language source code into machine
    code (object code).
- term: configure script
  definition: A script run at the beginning of the build process to adapt the source
    code to the specific characteristics of the target system and environment.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/316c6dddbb4858c2c34b58b3bddc6b85923d2799
date: '2026-09-18'
is_stub: false
stub_reason: ''
---

The configuration script's check for assembler support of the `--gdwarf-4` option used a hard-coded `ret` instruction. This instruction is not universally supported across all architectures, such as ARM. The patch replaces `ret` with a generic `$insn` placeholder, making the check more portable and reliable.
