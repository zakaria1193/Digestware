---
project: binutils
subsystem: x86
patch_id: null
tags:
- binutils
- x86
- assembler
- compiler flags
- memory ordering
discussion_id: SJ5PPF77D28E3C2FFB996CDFCC412801AC5EC982@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
source_type: public_inbox
title: 'RE: [PATCH] x86: extend coverage of -mlfence-after-load'
headline: 'x86: extend coverage of -mlfence-after-load'
tldr: Discussion on extending the x86 -mlfence-after-load option to cover more instructions
  that involve memory reads.
proposer: '"Jiang, Haochen" <haochen.jiang@intel.com>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Ensuring correct memory ordering semantics for performance-critical code vs. potentially
  adding overhead with unnecessary fence instructions.
- The complexity of accurately classifying all x86 instructions' memory access behavior.
- Balancing the need for compiler-generated fences with the programmer's explicit
  control over memory ordering.
exchanges:
- author: Jiang, Haochen <haochen.jiang@intel.com>
  role: proposer
  position: Responds to detailed analysis of x86 instructions, indicating a need to
    extend the `-mlfence-after-load` option's coverage to include more memory-accessing
    instructions.
  quote: "Without even considering ISA extensions which appeared only in newer\nhardware,\
    \ there are several issues:\n- PUSH with a memory operand is both a read and a\
    \ write (much like POP\n  is),\n- LTR, LLDT, VERR, and VERW are memory reads (first\
    \ explicit, then\n  implicit),\n- BT{,C,R,S} with register operand aren't any\
    \ different from ones with\n  immediate operand,\n- SHLD/SHRD aren't any different\
    \ from SHL/SH…"
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Provides a comprehensive list of x86 instructions that perform memory
    reads or read-modify-write operations, questioning the current coverage of the
    `-mlfence-after-load` option and suggesting simplifications.
  quote: 'Sadly the Intel page referenced by the original commit doesn''t provide
    any

    technical details, and the onwards reference from there now redirects to

    something generic (i.e. no technical details there either).


    For a few vector insns the situation is unclear: Pretty likely

    MASKMOV{Q,DQU}, V{,P}MASKMOV*, and masked AVX512 stores

    (V{,P}COMPRESS* possibly even when not masked) are read-modify-write op…'
primer_expert: The `-mlfence-after-load` compiler flag aims to insert memory fence
  instructions (like `LFENCE`) after certain memory load instructions to enforce memory
  ordering. This discussion focuses on identifying all x86 instructions that implicitly
  perform memory reads or read-modify-write operations, which should also be candidates
  for having an `LFENCE` inserted after them by the compiler when this flag is enabled.
  The thread analyzes numerous instructions to ensure comprehensive and correct coverage,
  as the documentation for some is unclear.
primer_glossary:
- term: LFENCE
  definition: A specific x86 instruction that acts as a serializing instruction, preventing
    processors from reordering memory reads around it. It ensures that all prior loads
    are completed before any subsequent loads are initiated.
- term: memory ordering
  definition: The rules governing the order in which memory operations (reads and
    writes) appear to execute from the perspective of different processors or cores
    in a multiprocessor system. Compilers and processors may reorder operations for
    performance, but fences are used to enforce specific ordering when necessary.
- term: instruction
  definition: A basic command or operation that a CPU can execute. Examples include
    ADD, MOV, JMP, and LFENCE.
- term: ISA extensions
  definition: Instruction Set Architecture extensions, which add new instructions
    to a processor's capabilities. Examples include SSE, AVX, and AMX for x86.
- term: read-modify-write
  definition: An operation that reads a value from memory, modifies it, and then writes
    the modified value back to memory. Some instructions perform this atomically,
    while others may not.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/SJ5PPF77D28E3C2FFB996CDFCC412801AC5EC982@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-10-19'
is_stub: false
stub_reason: ''
---

This email discusses extending the x86 assembler's `-mlfence-after-load` option to include more instructions that perform memory reads, beyond just explicit loads. The sender, Haochen Jiang, is responding to Jan Beulich's detailed analysis of various x86 instructions (like PUSH, LTR, LLDT, VERR, VERW, BT, SHLD/SHRD, BOUND, ARPL, CMPXCHG, VMXON, VMCLEAR, XSAVE) that involve memory reads or read-modify-write operations. The conversation aims to accurately identify and cover all relevant instructions to ensure correct memory ordering semantics when this option is used.
