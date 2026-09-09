---
project: binutils
subsystem: bpf
patch_id: null
tags:
- BPF
- gas
- assembler
- diagnostics
- ISA
discussion_id: 20260908062940.2734221-5-vineet.gupta@linux.dev
source_type: public_inbox
title: 'bpf: diagnose instructions above the selected ISA spec'
headline: 'BPF gas: Diagnose instructions above selected ISA spec'
tldr: BPF gas now provides clearer diagnostics for instructions requiring a higher
  ISA spec than selected.
proposer: Vineet Gupta <vineet.gupta@linux.dev>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Provides much clearer error messages for ISA version mismatches.
- Increases the complexity of the `md_assemble` function.
- Ensures that valid instructions within the selected ISA are still correctly assembled.
exchanges:
- author: Jose E. Marchesi
  role: reviewer
  position: Approves the patch for the master branch, acknowledging the improved diagnostics
    for ISA spec mismatches.
  quote: 'OK for master.

    Thanks!'
- author: Vineet Gupta
  role: proposer
  position: Introduces improved diagnostics for BPF instructions that require an ISA
    spec higher than the one currently selected.
  quote: 'Attempt those templates too, but only for the diagnostic: if

    one matches the whole statement, remember it and keep scanning, since a

    template within the ISA spec may still match.'
primer_expert: This patch refactors the BPF assembler's `md_assemble` function to
  improve diagnostics when an instruction requires a higher ISA specification than
  currently selected. Previously, such attempts resulted in generic errors like 'unrecognized
  instruction'. The change now allows `md_assemble` to temporarily consider templates
  from future ISA specs. If an instruction matches such a template, the assembler
  remembers it and continues parsing. Only if no valid template within the current
  ISA spec is found does it emit a specific error message indicating the required
  ISA version (e.g., 'requires ISA s…
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter, a technology that allows sandboxed programs
    to safely execute code in the Linux kernel, often used for networking and tracing.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    converting assembly language code into machine code.
- term: ISA spec
  definition: Instruction Set Architecture specification. Refers to a particular version
    or feature set of the BPF instruction set that the assembler is targeting.
- term: md_assemble
  definition: A function within the gas assembler responsible for parsing and assembling
    machine instructions based on the target architecture's specification.
- term: diagnostic
  definition: An error or warning message produced by a compiler or assembler to inform
    the user about issues in the source code.
series_id: 'binutils:bpf: diagnose instructions above the selected isa spec'
series_role: reply
series_parts:
- title: 'bpf: diagnose instructions above the selected ISA spec'
  url: https://inbox.sourceware.org/binutils/20260907091102.2595057-6-vineet.gupta@linux.dev
  n: 5
  total: 5
url: https://inbox.sourceware.org/binutils/20260908062940.2734221-5-vineet.gupta@linux.dev
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

This patch enhances the BPF assembler's error reporting. Previously, using an instruction not available in the selected ISA spec resulted in misleading errors, such as 'unrecognized instruction' or 'expected white space'. The updated `md_assemble` function now attempts to match templates above the current ISA spec for diagnostic purposes. If a match is found, it reports the specific ISA spec required (e.g., 'requires ISA spec v4 or later'), providing much clearer feedback to the user.
