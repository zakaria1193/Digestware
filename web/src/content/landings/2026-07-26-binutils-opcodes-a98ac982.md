---
project: binutils
subsystem: binutils/opcodes
patch_id: null
tags:
- aarch64
- opcodes
- build
commit_hash: a98ac982f160696989cede4b6b43b5a9c2b32c74
source_type: public_inbox
author: Nick Clifton <nickc@sourceware.org>
headline: Fix struct initializer for aarch64-gen.
tldr: Corrects a struct initializer issue in the aarch64 opcode generator.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit refactors the definition of `FLD_CONST_*` macros in `aarch64-gen.c`
  to use a direct struct initializer instead of relying on `AARCH64_FIELD_CONST`.
  This resolves a similar issue to commit `0e89ce812b79` where a cast was applied
  to a struct initializer. The macros were moved from `aarch64-opc.h` to `aarch64-gen.c`
  as they are only used there, avoiding the need for additional `#undef` directives.
primer_glossary:
- term: aarch64-gen.c
  definition: A C source file within the binutils project responsible for generating
    opcode information for the AArch64 architecture.
- term: struct initializer
  definition: A construct used in C to assign initial values to the members of a structure
    at the time of its declaration or creation.
- term: macro
  definition: A fragment of code that is intended to be expanded in place by the C
    preprocessor. Macros can be used to define constants or create shorthand for more
    complex code snippets.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260726071246.9959F4BA2E0B@sourceware.org
date: '2026-07-26'
is_stub: false
stub_reason: ''
---

This commit fixes a similar issue in the aarch64-gen code as a previous commit did for the aarch64 architecture itself. It addresses an incorrect cast within a struct initializer that was affecting the build of the aarch64 opcode generator. Constant definitions were moved to resolve this.
