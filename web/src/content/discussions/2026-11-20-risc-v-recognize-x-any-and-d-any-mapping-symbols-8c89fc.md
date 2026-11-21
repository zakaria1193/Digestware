---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- binutils
- objdump
- disassembly
- symbols
discussion_id: 20261120142608.3976646-1-kito.cheng@sifive.com
source_type: public_inbox
title: '[PATCH] RISC-V: Recognize $x.<any> and $d.<any> mapping symbols'
headline: 'RISC-V: Recognize $x.<any> and $d.<any> mapping symbols'
tldr: Binutils now correctly recognizes RISC-V mapping symbols like $x.<n> and $d.<n>,
  improving objdump's disassembly.
proposer: Kito Cheng <kito.cheng@sifive.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: 8
technical_tradeoffs:
- Improves disassembly accuracy for RISC-V code using specific compiler extensions.
- Ensures better compliance with RISC-V psABI conventions.
exchanges:
- author: Kito Cheng <kito.cheng@sifive.com>
  role: proposer
  position: Submits a patch to binutils to correctly recognize RISC-V mapping symbols
    with suffixes, such as $x.<n> and $d.<n>, which are emitted by clang.
  quote: The psABI allows a ".<any>" suffix on the $x and $d mapping symbols, and
    clang emits $x.<n>. objdump only handled the bare names, so it kept the previous
    ISA or state and printed the symbols as labels.
- author: Jerry Zhang Jian <jerry.zhangjian@sifive.com>
  role: contributor
  position: The original author of the work, whose patch is being submitted by Kito
    Cheng.
  quote: null
- author: Jeff Law <jeffreyalaw@gmail.com>
  role: reviewer
  position: Reviews the patch, suggesting the use of `startswith()` for the checks
    and noting that this change will be committed.
  quote: Use startswith() for these checks, and for the existing $xrv one too.
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Asks a clarifying question about the change, specifically regarding the
    use of `startswith()`.
  quote: "On 20.11.2026 15:26, Kito Cheng wrote:\n\n> From: Jerry Zhang Jian <jerry.zhangjian@sifive.com>\n\
    > \n> The psABI allows a \".<any>\" suffix on the $x and $d mapping symbols, and\
    \ clang emits $x.<n>. objdump only handled the bare names, so it kept the previous\
    \ ISA or state and printed the symbols as labels."
primer_expert: This patch modifies `bfd/cpu-riscv.c` to correctly identify RISC-V
  mapping symbols that include suffixes, such as `$x.rv32` or `$d.lstm`. The psABI
  allows these suffixes, and compilers like clang emit them. The previous implementation
  in objdump (via BFD) only recognized the base symbols `$x` and `$d`, misinterpreting
  suffixed symbols as standard labels. The fix uses `strncmp` (updated to `startswith`
  in a later revision) to handle these suffixed symbols, improving disassembly accuracy.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture based on RISC principles.
- term: psABI
  definition: The Application Binary Interface specific to the Platform, often referring
    to conventions for function calls, data types, and symbol naming.
- term: objdump
  definition: A utility that displays information from object files, including disassembly.
- term: mapping symbols
  definition: Special symbols used in RISC-V to indicate processor ISA extensions
    or modes.
- term: BFD
  definition: Binutils Format Description, a library used by binutils to support various
    object file formats.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/20261120142608.3976646-1-kito.cheng@sifive.com
bugzilla_url: null
date: '2026-11-20'
is_stub: false
stub_reason: ''
---

This patch enhances binutils' handling of RISC-V mapping symbols by recognizing suffixes like '.<any>' appended to $x and $d. Previously, objdump only handled bare '$x' and '$d', leading to incorrect disassembly where these symbols were treated as labels. This change ensures that clang-generated symbols like '$x.<n>' are correctly interpreted.
