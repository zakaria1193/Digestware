---
project: gcc
subsystem: gcc/configure
patch_id: null
tags:
- aarch64
- sve2p3
- sme2p3
commit_hash: e818a48fc88685246852739a969194e24857013f
source_type: github
author: John David Anglin
headline: Disable CFI directives on hppa*-*-hpux* for EH encoding.
tldr: CFI directives are disabled on hppa*-*-hpux* as GCC will generate EH difference
  expressions directly.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `configure.ac` script now sets `gcc_cv_as_cfi_directive` to `no`
  for `hppa*-*-hpux*`. This prevents GCC from emitting CFI directives in `.eh_frame`
  because the target's assembler (gas) does not support them correctly for EH encoding.
  GCC will instead generate the necessary EH difference expressions directly, relying
  on linker support.
primer_glossary:
- term: CFI directives
  definition: Instructions embedded in object files that describe how to unwind the
    call stack. They are crucial for exception handling and debugging.
- term: Difference expressions
  definition: A method for encoding offsets and other values in the `.eh_frame` section.
    They allow for more compact representation of frame data compared to absolute
    values.
- term: .eh_frame
  definition: The DWARF debugging standard section in an object file that stores Call
    Frame Information (CFI) necessary for stack unwinding during exception handling
    or debugging.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e818a48fc88685246852739a969194e24857013f
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

Generation of Call Frame Information (CFI) directives is disabled for hppa*-*-hpux* targets. This is necessary because the assembler on these systems defines CFI_DIFF_EXPR_OK to 0, preventing it from handling difference expressions. GCC will now generate the required difference expressions itself for the .eh_frame section.
