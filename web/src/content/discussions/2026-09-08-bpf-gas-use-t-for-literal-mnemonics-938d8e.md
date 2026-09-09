---
project: binutils
subsystem: bpf
patch_id: null
tags:
- BPF
- gas
- assembler
- parsing
- opcode table
discussion_id: 87jyovsy9j.fsf@gnu.org
source_type: public_inbox
title: 'Re: [PATCH v4 2/4] bpf: use %t after the remaining mnemonics in the opcode
  table'
headline: 'BPF gas: Use %t for literal mnemonics'
tldr: BPF gas mnemonics now use %t specifier for precise parsing, preventing accidental
  instruction extension.
proposer: '"Jose E. Marchesi" <jemarch@gnu.org>'
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Improves parsing robustness and prevents future bugs related to mnemonic ambiguity.
- Introduces stricter parsing, potentially breaking existing assembly files that relied
  on the previous flexible spacing (though mitigated by test cases).
- Increases accuracy in distinguishing mnemonics from immediate operands.
exchanges:
- author: Jose E. Marchesi
  role: reviewer
  position: Approves the patch for the master branch, acknowledging its fix for a
    latent parsing problem.
  quote: 'OK for master.

    Thanks!'
- author: Vineet Gupta
  role: proposer
  position: Submitted a patch to use the `%t` specifier for remaining BPF literal
    mnemonics in the opcode table.
  quote: 'Convert the remaining 65 sites: `if'', `lock'', `gotol'', `call'', `callx'',

    `may_goto'', `le16''/`le32''/`le64'', `be16''/`be32''/`be64'' and

    `bswap16''/`bswap32''/`bswap64''.'
primer_expert: This patch refactors the BPF assembler's `tc-bpf.c` and `bpf-opc.c`
  to use the `%t` (token boundary) specifier after literal mnemonics in the opcode
  table. Previously, `%w` was used, which allowed mnemonics to be extended by immediately
  following characters (e.g., `goto` followed by `l` in `gotol`). The `%t` specifier
  enforces a stricter token boundary, preventing such ambiguities and aligning with
  the fix for PR gas/34558. This change affects 65 sites and adds new test cases to
  verify spacing rules.
primer_glossary:
- term: BPF
  definition: Berkeley Packet Filter, a technology that allows sandboxed programs
    to safely execute code in the Linux kernel, often used for networking and tracing.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    converting assembly language code into machine code.
- term: opcode table
  definition: A data structure used by an assembler or compiler that maps instruction
    mnemonics and operands to their corresponding machine code representations.
- term: '%t specifier'
  definition: A format specifier in the gas opcode table that signifies a token boundary,
    ensuring that the preceding text is treated as a complete mnemonic and not extended
    by subsequent characters.
- term: PR gas/34558
  definition: A bug report filed against the GNU Assembler, specifically concerning
    incorrect parsing of BPF instructions due to ambiguous mnemonic boundaries.
series_id: 'binutils:bpf: use %t after the remaining mnemonics in the opcode table'
series_role: reply
series_parts:
- title: 'bpf: use %t after the remaining mnemonics in the opcode table'
  url: https://inbox.sourceware.org/binutils/20260908062940.2734221-3-vineet.gupta@linux.dev
  n: 2
  total: 4
- title: 'bpf: use %t after the remaining mnemonics in the opcode table'
  url: https://inbox.sourceware.org/binutils/20260907091102.2595057-4-vineet.gupta@linux.dev
  n: 3
  total: 5
url: https://inbox.sourceware.org/binutils/87jyovsy9j.fsf@gnu.org
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

This patch modifies the BPF assembler's opcode table to use the `%t` specifier after literal mnemonics. This change, prompted by a previous bug (PR gas/34558), ensures that mnemonics like `if`, `lock`, `call`, etc., are treated as distinct tokens and prevent subsequent tokens from being misinterpreted as part of the mnemonic. This improves parsing accuracy and future-proofs the opcode table against new instruction additions.
