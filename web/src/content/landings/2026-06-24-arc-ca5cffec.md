---
project: gcc
subsystem: arc
patch_id: null
tags:
- arc
- compiler
- backend
- addressing mode
commit_hash: ca5cffec066fb8a7edd13dd12792505739381b42
source_type: github
author: Michiel Derhaeg
headline: 'Arc: Fix invalid register index addressing for uncached stores'
tldr: GCC's Arc backend now correctly handles register-based addressing for uncached
  stores, fixing invalid operand issues.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit addresses PR126157 by modifying Arc's `prepare_move_operands`
  and machine description. The issue stemmed from `-ffuse-ops-with-volatile-access`
  which enabled `(plus (reg) (reg))` as a destination operand for `stdi<mode>`, an
  invalid format. The fix involves using `move_dest_operand` and `non_mod_move_dest_operand`
  predicates, the latter specifically disallowing PRE/POST increment/decrement, to
  ensure the address is a valid register or memory location for uncached stores.
primer_glossary:
- term: Arc
  definition: A family of 32-bit RISC microprocessors developed by Synopsys, often
    used in embedded systems.
- term: uncached store
  definition: A memory write operation that bypasses the CPU's cache, writing directly
    to main memory. This is often used for memory-mapped I/O or specific hardware
    interactions.
- term: register index addressing
  definition: A memory addressing mode where the base address is in one register and
    an offset or second index is in another register.
- term: predicate
  definition: In the context of GCC's machine description, a predicate is a condition
    used to determine if a particular instruction pattern is valid or can be generated
    for a given target.
- term: POST_INC
  definition: A type of addressing mode where the operand register is incremented
    after its value is used as the memory address.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ca5cffec066fb8a7edd13dd12792505739381b42
date: '2026-06-24'
is_stub: false
stub_reason: ''
---

A bug in GCC's Arc backend that allowed invalid register-index addressing for uncached stores has been fixed. The `stdi<mode>` instruction incorrectly used a too-liberal predicate, allowing [reg,reg] operands which are not valid on Arc. This commit corrects the addressing mode by forcing the address into a register when necessary and uses a more restrictive predicate for the destination operand.
