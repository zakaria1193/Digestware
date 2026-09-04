---
project: binutils
subsystem: bpf
patch_id: null
tags:
- binutils
- gas
- bpf
- assembler
- regression-test
discussion_id: 7f87eb3f-d970-417b-a1db-5eb72fcdde8d@linux.dev
source_type: public_inbox
title: 'Re: [PATCH v2 0/2] bpf: fix gotol with a signed offset, and run the spacing
  test'
headline: 'bpf: fix gotol with a signed offset, and run the spacing test'
tldr: Fixes BPF assembler misassembly of `gotol` with signed offsets and enables a
  related test case.
proposer: Vineet Gupta <vineet.gupta@linux.dev>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The fix ensures compatibility with libbpf and potentially other tools that rely
  on correct `gotol` instruction assembly, improving the reliability of BPF program
  loading.
- Enabling the `spacing-pseudoc` test case improves test coverage for the BPF assembler,
  helping to catch future regressions.
exchanges:
- author: Vineet Gupta <vineet.gupta@linux.dev>
  role: proposer
  position: Submits patches to fix BPF assembler misassembly of `gotol` with signed
    offsets and to enable a related test case, noting issues with previous suggestions.
  quote: "Ping !\n\nOn 8/25/26 3:11 AM, Vineet Gupta wrote:\n> In the pseudo-C dialect\
    \ `gotol +1' is silently assembled as `goto l+1'\n> leading to libbpf load time\
    \ failures. LLVM obviously supports this so gas\n> needs fixing.\n> \n> Ran into\
    \ this when trying to enable certain selftests which are\n> currently clang built\
    \ only while GCC can build them fine. Moreover those\n> not run tests are declared\
    \ passing too […"
primer_expert: This patch series updates the GNU Assembler's BPF backend. It corrects
  how `gotol` instructions with signed immediate offsets are parsed and assembled,
  resolving an incompatibility with libbpf's handling of these instructions. Additionally,
  it ensures a relevant test case (`spacing-pseudoc.s/.d`) is executed, which previously
  existed but was not run. The fix for `gotol` addresses a subtle interaction between
  operand parsing and assembler directives, particularly when whitespace is involved
  around signed immediates.
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter. A technology that allows sandboxed programs
    to run efficiently in the Linux kernel for network packet filtering, tracing,
    and other tasks.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils project. It translates assembly
    language code into machine code.
- term: libbpf
  definition: A userspace library that helps load and interact with BPF programs running
    in the Linux kernel.
- term: PIE
  definition: Position-Independent Executable. An executable file that can be loaded
    at any address in memory without modification. This is achieved through special
    relocation entries and is crucial for security and flexibility.
- term: ET_DYN
  definition: Executable ELF file type. Indicates a dynamically linked executable
    or a shared object. PIE executables are of this type.
- term: UEFI
  definition: Unified Extensible Firmware Interface. A specification that defines
    the software interface between an operating system and platform firmware. UEFI
    applications are typically loaded and run by the UEFI firmware.
- term: R_RISCV_RELATIVE
  definition: A RISC-V specific relocation type used for position-independent code,
    where the relocation value is determined by adding the image's base address to
    the symbol's offset.
- term: elf32lriscv-defs.sh
  definition: A shell script within Binutils that defines linker emulation parameters
    specific to the 32-bit little-endian RISC-V architecture.
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or library.
- term: gotol
  definition: A BPF assembly instruction that likely represents a jump to a label
    with an offset.
series_id: 'binutils:bpf: fix gotol with a signed offset, and run the spacing test'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/7f87eb3f-d970-417b-a1db-5eb72fcdde8d@linux.dev
bugzilla_url: null
date: '2026-09-03'
is_stub: false
stub_reason: ''
---

This patch series addresses two issues in the BPF backend of the GNU Assembler (gas). First, it fixes a bug where `gotol + imm` was misassembled as `goto label + imm`, leading to runtime failures in libbpf. Second, it enables a previously disabled test case, `spacing-pseudoc.s/.d`, which is relevant to testing jump instructions. The author notes that a proposed solution using `%W` for whitespace did not work due to how gas parses operands.
