---
project: binutils
subsystem: gcc
patch_id: null
tags:
- dwarf
- debugging
- security
- binutils
- patch
discussion_id: ambkVeuxp_ZAFso4@squeak.grove.modra.org
source_type: public_inbox
title: DWARF1 AT_sibling sanity check
headline: DWARF1 AT_sibling sanity check
tldr: Patch to sanity check AT_sibling in DWARF version 1 to prevent infinite loops
  from fuzzed object files.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Potential breakage for very old DWARF v1 files that may have used backward `AT_sibling`
  links.
- Increased robustness against malformed DWARF v1 input, preventing potential crashes
  or infinite loops.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch to add a sanity check for AT_sibling in DWARF v1 to prevent
    potential infinite loops with fuzzed files, noting it might break support for
    some old files.
  quote: 'If backward links are allowed then it is considerably more tedious to

    protect against fuzzed object files that loop forever reading DWARF1.

    So this patch may break addr2line and objdump -dS for some old files.'
primer_expert: This patch modifies `bfd/dwarf1.c` to add a sanity check for the `AT_sibling`
  attribute when parsing DWARF version 1 debug information. The author posits that
  `AT_sibling` pointers in DWARF v1 are generally forward-pointing and that a backward
  pointer could lead to infinite loops during parsing. The change updates `parse_die`
  to use a `stash` pointer and adds a check to ensure `AT_sibling` points within the
  current Debug Information Entry (DIE) unit. This addresses potential vulnerabilities
  in tools like `addr2line` and `objdump` when processing malformed DWARF v1 data,
  while acknowledging it…
primer_glossary:
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to store
    information about variables, types, and code structure.
- term: AT_sibling
  definition: A DWARF attribute tag that points to the next sibling Debugging Information
    Entry (DIE) at the same level in the DIE tree.
- term: DIE
  definition: Debugging Information Entry. A unit of information within DWARF that
    describes a program entity like a function, variable, or type.
- term: addr2line
  definition: A utility that translates addresses into file names and line numbers,
    using debugging information.
- term: objdump
  definition: A utility that displays information from object files, including disassembled
    code and section contents.
- term: fuzzed object files
  definition: Object files that have been intentionally corrupted or malformed (fuzzed)
    to test the robustness and security of the tools that process them.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ambkVeuxp_ZAFso4@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This patch introduces a sanity check for the AT_sibling attribute in DWARF version 1 debugging information. The author believes that AT_sibling usually points forward in DWARF v1, a format largely unsupported since GCC 3.3. Allowing backward AT_sibling links can lead to infinite loops when parsing fuzzed object files, impacting tools like addr2line and objdump. This change aims to prevent such issues and may break support for some older DWARF v1 files if they rely on backward links.
