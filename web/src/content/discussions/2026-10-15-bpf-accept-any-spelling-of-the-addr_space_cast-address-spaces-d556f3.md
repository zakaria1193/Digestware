---
project: binutils
subsystem: bpf
patch_id: null
tags:
- bpf
- assembler
- selftests
- hexadecimal
discussion_id: 20261015083524.3948689-1-vineet.gupta@linux.dev
source_type: public_inbox
title: '[PATCH] bpf: accept any spelling of the addr_space_cast address spaces'
headline: 'bpf: accept any spelling of the addr_space_cast address spaces'
tldr: Binutils assembler now accepts hex or decimal spellings for address spaces in
  bpf addr_space_cast instructions, fixing kernel selftests.
proposer: Vineet Gupta <vineet.gupta@linux.dev>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 10
technical_tradeoffs:
- Introducing a new tag (%N) increases assembler complexity but improves flexibility.
- Ensures compatibility with compiler features that use hex for address spaces.
exchanges:
- author: Vineet Gupta <vineet.gupta@linux.dev>
  role: proposer
  position: Submits a patch to fix gas's handling of BPF addr_space_cast by introducing
    a %N tag to parse address spaces as numbers, resolving assembly errors for kernel
    selftests.
  quote: 'gas matches the address space characters as literal `0'' and `1'' and

    trips over the hex form.


    Introduce a %N tag for a constant the opcode already encodes, and parse

    the operand as a number so the two are compared by value.'
- author: Jose E. Marchesi <jemarch@gnu.org>
  role: reviewer
  position: Acknowledges the patch and thanks the author, indicating it is ready for
    merging.
  quote: 'Hi Vineet.

    Thanks for the patch.


    > Building the kernel''s BPF arena selftests fails to assemble:

    > ...

    > gas matches the address space characters as literal `0'' and `1'' and

    > trips over the hex form.'
primer_expert: The bpf subsystem in binutils is being updated to correctly parse hexadecimal
  representations of address spaces within the `addr_space_cast` instruction for BPF
  programs. Previously, the assembler (gas) incorrectly treated hex digits as literal
  characters, causing assembly failures for certain BPF selftests. This patch modifies
  `tc-bpf.c` and related files to introduce a `%N` tag, enabling numerical parsing
  of these operands.
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter, a technology that allows sandboxed programs
    to make direct use of Linux kernel functions, primarily for networking and security.
- term: addr_space_cast
  definition: An instruction in some BPF variants used to cast a value between different
    address spaces.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project, responsible for
    converting assembly language code into machine code.
- term: '%N tag'
  definition: A new format specifier introduced in this patch to instruct the gas
    assembler to parse a subsequent operand as a numerical value, specifically for
    address space values.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261015083524.3948689-1-vineet.gupta@linux.dev
bugzilla_url: null
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

This patch addresses an issue where the Binutils assembler (gas) failed to assemble BPF programs using the 'addr_space_cast' instruction when address spaces were specified in hexadecimal. The kernel's BPF arena selftests were failing because gas was treating hex values as literal characters. The solution introduces a new %N tag to parse these operands as numbers, allowing for correct comparison and assembly. This change ensures compatibility with GCC's 'addr_space_cast()' support.
