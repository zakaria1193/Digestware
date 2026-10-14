---
project: gcc
subsystem: gcc/rtl-optimization
patch_id: null
tags:
- optimization
- jump
- debugging
- SPARC
commit_hash: 6db085c8b79ff6fc4265bf8e45605b7992eb85d8
source_type: github
author: Yongqiang Tian
headline: Ignore debug instructions in BARRIER checks
tldr: GCC's jump optimization now correctly ignores debug instructions when searching
  for preceding BARRIERs.
impact_score: 4
performance_win: true
breaking_change: false
outcome: committed
primer_expert: In the `jump.cc` pass, `delete_related_insns` searches backwards from
  a deleted `CODE_LABEL` for a `BARRIER` to determine control flow. Previously, a
  `DEBUG_INSN` would halt this backward walk, leading to incorrect code retention
  when debugging. This patch modifies the walk to skip `DEBUG_INSN`s, allowing the
  `BARRIER` to be found correctly and ensuring that unreachable code is removed even
  with `-g` enabled.
primer_glossary:
- term: BARRIER
  definition: An RTL (Register Transfer Language) instruction that signifies a point
    in the code where control flow is guaranteed to be discontinuous. It's used by
    the compiler to understand execution paths and optimize code.
- term: CODE_LABEL
  definition: A label in the RTL representation of code, typically marking the target
    of a jump or branch instruction.
- term: DEBUG_INSN
  definition: An RTL instruction that represents debugging information, such as line
    number information or variable tracking data. These instructions are typically
    only present when the code is compiled with debugging flags.
- term: RTL
  definition: Register Transfer Language, an intermediate representation used by GCC
    internally to represent code. It's a low-level, machine-independent representation
    that facilitates optimization.
- term: COMDAT
  definition: A COMDAT (common object file data) section is a special type of section
    that allows the linker to select only one instance of several identical sections
    from different object files. This is often used for functions or data that are
    defined in multiple translation units but should only appear once in the final
    executable.
- term: linker script
  definition: A file that provides detailed instructions to the linker on how to arrange
    sections in the output file, how to assign addresses, and how to handle symbols.
    It allows fine-grained control over the final executable's layout.
- term: KEEP()
  definition: A directive within a linker script that explicitly tells the linker
    to preserve a specified symbol or section, preventing it from being garbage collected
    even if it appears unused.
- term: garbage collection
  definition: The process by which the linker identifies and removes unused sections
    or symbols from the final executable to reduce its size. This is crucial for embedded
    systems and for optimizing code size.
- term: property tables
  definition: In the context of Xtensa architecture, these are special sections that
    store metadata or properties related to code or data sections. They are essential
    for certain dynamic features or architectural requirements.
- term: resurrected
  definition: In linker terminology, 'resurrected' refers to a section or symbol that
    was intended to be removed by garbage collection but is kept in the final executable
    due to some directive or indirect reference.
discussion_id_link: null
bugzilla_pr: null
series_id: 'gcc:jump: ignore debug insns before barrier [pr127809]'
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/6db085c8b79ff6fc4265bf8e45605b7992eb85d8
date: '2026-10-13'
is_stub: false
stub_reason: ''
---

This commit enhances GCC's jump instruction handling by ensuring that debug instructions are ignored when searching for a BARRIER instruction preceding a deleted label. This prevents unreachable code, particularly when debugging is enabled (`-g`), from being retained incorrectly. The change adds a regression test for SPARC and addresses issues found during related bug investigations.
