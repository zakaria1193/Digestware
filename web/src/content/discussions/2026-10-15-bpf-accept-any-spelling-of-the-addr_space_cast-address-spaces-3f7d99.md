---
project: binutils
subsystem: bpf
patch_id: null
tags:
- bpf
- assembler
- selftests
- hexadecimal
discussion_id: 20261015121201.3986789-1-vineet.gupta@linux.dev
source_type: public_inbox
title: '[PATCH v2] bpf: accept any spelling of the addr_space_cast address spaces'
headline: 'bpf: accept any spelling of the addr_space_cast address spaces'
tldr: Binutils assembler now accepts hex or decimal spellings for address spaces in
  bpf addr_space_cast instructions, fixing kernel selftests.
proposer: Vineet Gupta <vineet.gupta@linux.dev>
consensus: Proposed
outcome: committed
impact_score: 5
sentiment_score: 10
technical_tradeoffs:
- Introducing a new tag (%DIGIT) increases assembler complexity but improves flexibility.
- Ensures compatibility with newer compiler features that use hex for address spaces.
exchanges:
- author: Vineet Gupta <vineet.gupta@linux.dev>
  role: proposer
  position: Proposes to fix gas's handling of BPF addr_space_cast by introducing a
    %DIGIT tag to parse address spaces as numbers, resolving assembly errors for kernel
    selftests.
  quote: 'gas matches the address space characters as literal `0'' and `1'' and

    trips over the hex form.


    Introduce a %DIGIT tag for a constant the opcode already encodes, and

    parse the operand as a number so the two are compared by value.'
- author: Jose E. Marchesi <jemarch@gnu.org>
  role: reviewer
  position: Approves the patch for merging into the master branch, noting that the
    second version (v2) is accepted.
  quote: 'Hi Vineet.


    Thanks for the new version of the patch.

    OK for master.'
- author: Vineet Gupta <vineet.gupta@linux.dev>
  role: proposer
  position: Confirms that the patch has been pushed to the master branch.
  quote: 'Pushed.


    Thx,

    -Vineet'
primer_expert: The bpf subsystem in binutils is being updated to correctly parse hexadecimal
  representations of address spaces within the `addr_space_cast` instruction for BPF
  programs. Previously, the assembler (gas) incorrectly treated hex digits as literal
  characters, causing assembly failures for certain BPF selftests. This patch modifies
  `tc-bpf.c` and related files to introduce a `%DIGIT` tag, enabling numerical parsing
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
- term: '%DIGIT tag'
  definition: A new format specifier introduced in this patch to instruct the gas
    assembler to parse a subsequent operand as a numerical digit, specifically for
    address space values.
series_id: binutils:bpf:accept any spelling of the addr_space_cast address spaces
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/20261015121201.3986789-1-vineet.gupta@linux.dev
bugzilla_url: null
date: '2026-10-15'
is_stub: false
stub_reason: ''
---

This patch series addresses an issue where the Binutils assembler (gas) failed to assemble BPF programs using the 'addr_space_cast' instruction when address spaces were specified in hexadecimal. The kernel's BPF arena selftests were failing because gas was treating hex values as literal characters. The solution introduces a new %DIGIT tag to parse these operands as numbers, allowing for correct comparison and assembly. This change ensures compatibility with GCC's 'addr_space_cast()' support.
