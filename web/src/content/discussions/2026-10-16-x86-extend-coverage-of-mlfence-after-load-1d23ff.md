---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- compiler
- optimization
- memory-ordering
- performance
discussion_id: 71ab0e0c-6961-4d9b-a424-c474e4e0eea3@suse.com
source_type: public_inbox
title: '[PATCH] x86: extend coverage of -mlfence-after-load'
headline: 'x86: extend coverage of -mlfence-after-load'
tldr: Expands compiler support for memory fence instructions after loads on x86.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Improves memory ordering guarantees for a wider range of x86 instructions, potentially
  enhancing correctness and stability in multithreaded or concurrent scenarios.
- Increases the number of instructions that trigger fence insertion, which may incur
  a performance overhead.
- Addresses documentation discrepancies between processor manuals and compiler behavior.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Proposes to extend the `-mlfence-after-load` option's coverage to include
    a wider range of x86 instructions that perform memory reads or read-modify-write
    operations.
  quote: "Without even considering ISA extensions which appeared only in newer\nhardware,\
    \ there are several issues:\n- PUSH with a memory operand is both a read and a\
    \ write (much like POP\n  is),\n- LTR, LLDT, VERR, and VERW are memory reads (first\
    \ explicit, then\n  implicit),\n- BT{,C,R,S} with register operand aren't any\
    \ different from ones with\n  immediate operand,\n- SHLD/SHRD aren't any different\
    \ from SHL/SH…"
primer_expert: This patch modifies the internal handling of memory ordering for the
  x86 backend in binutils, specifically related to the `-mlfence-after-load` flag.
  This flag instructs the compiler to insert LFENCE (or equivalent) instructions after
  load operations. The patch expands the set of instructions recognized as loads or
  read-modify-write operations that should be subject to this fencing. It details
  instructions like PUSH, LTR, LLDT, various BT variants, ARPL, CMPXCHG, VMXON, XSAVE,
  and certain vector instructions, arguing they also require fencing after loads to
  maintain correct memory ordering se…
primer_glossary:
- term: memory fence
  definition: An instruction that synchronizes memory operations, ensuring that memory
    reads and writes complete in a specific order. It prevents the processor or compiler
    from reordering memory operations across the fence, which is crucial for multi-core
    systems and certain hardware interactions.
- term: -mlfence-after-load
  definition: A compiler flag (likely for GCC or Clang) that instructs the compiler
    to insert a memory fence instruction (e.g., LFENCE) after every load instruction.
    This is used to enforce memory ordering constraints.
- term: x86
  definition: A family of instruction set architectures (ISAs) originally developed
    by Intel, widely used in desktop computers, laptops, and servers. Binutils provides
    backends for x86.
- term: ISA extensions
  definition: Additional sets of instructions that augment a base instruction set
    architecture, providing new capabilities or performance improvements (e.g., SSE,
    AVX for x86).
- term: read-modify-write
  definition: A type of memory operation where a value is read from memory, modified,
    and then written back to the same memory location. Some instructions perform this
    atomically, while others might not guarantee ordering relative to other memory
    operations.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/71ab0e0c-6961-4d9b-a424-c474e4e0eea3@suse.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch proposes extending the coverage of the `-mlfence-after-load` compiler option for the x86 architecture. The option aims to insert memory fence instructions after load operations to ensure proper memory ordering, which is critical for certain hardware and instruction sequences. The author identifies several x86 instructions that perform memory reads (e.g., PUSH, LTR, LLDT, BT variants, ARPL, CMPXCHG, VMXON, XSAVE) that were not previously covered by this option. Additionally, the patch suggests code restructuring for clarity and discusses potential ambiguities with newer ISA extensions and documentation updates. The lack of detailed technical documentation for some instructions is noted as a challenge.
