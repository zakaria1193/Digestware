---
project: binutils
subsystem: binutils/gas
patch_id: null
tags:
- binutils
- bpf
- assembler
- diagnostics
commit_hash: 81ba621ff9d59e294b86ccc2c3a980e3f10b0a07
source_type: public_inbox
author: Vineet Gupta <vineetg@sourceware.org>
headline: Diagnose BPF instructions exceeding the selected ISA spec
tldr: BPF assembler now provides better error messages for instructions not supported
  by the target ISA version.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `md_assemble` function in `tc-bpf.c` is updated to attempt matching
  templates that are defined for ISA versions beyond the current `isa_spec`. If such
  a template matches the entire input statement, it's stored as a potential error
  candidate. The assembler continues to scan for templates within the `isa_spec`.
  Only if no valid template is found does the stored candidate drive the error message,
  now indicating the required ISA version. This prevents misleading diagnostics caused
  by version mismatches.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261012140323.2CF1B4BA2E14@sourceware.org
date: '2026-10-12'
is_stub: false
stub_reason: ''
---

The GNU assembler's BPF backend now offers more informative diagnostics when an instruction is used that exists but is not available in the currently selected ISA specification. Previously, such cases would result in a generic 'unrecognized instruction' error. This change allows the assembler to identify and report the required ISA version for the problematic instruction, improving the developer experience.
