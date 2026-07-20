---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- vector-instructions
- encoding
discussion_id: CAHT-pJyXr_TnBxZGSy6EFqo2aEB5C2y4uW9CvHJTh9ZNA2cyfA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v3 01/13] RISC-V: add dedicated vector arithmetic .insn forms'
headline: 'RISC-V: add dedicated vector arithmetic .insn forms'
tldr: A reviewer LGTMs a patch adding vector arithmetic instruction forms for RISC-V
  but suggests clarifying magic numbers with masks.
proposer: Nelson Chu <nelson.chu1990@gmail.com>
consensus: Ready to Land
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Using raw values for opcode fields is concise but less readable; using named constants
  (MASK/MATCH) improves readability at the cost of slightly more verbose definitions.
exchanges:
- author: Nelson Chu <nelson.chu1990@gmail.com>
  role: reviewer
  position: LGTMs the patch but suggests defining extra MASK/MATCH for funct3 to improve
    clarity over using raw values.
  quote: LGTM +1.  A minor thing (this patch is already good enough to me without
    any change) is do you think we need to define extra MASK/MATCH for funct3 to represent
    bits 10-12 rather than use 0x7000 directly? So that might make it immediately
    clear to understand what these values represent.
- author: Jiawei <jiawei@iscas.ac.cn>
  role: proposer
  position: Proposed adding dedicated `.insn` forms for RISC-V vector arithmetic instructions
    to simplify their encoding, with v3 clarifying operand order.
  quote: null
primer_expert: This patch for binutils' RISC-V support adds new `.insn` directives,
  which are assembler constructs for encoding machine instructions. Specifically,
  it targets vector arithmetic instructions, providing specialized forms to make encoding
  easier than general-purpose ones. The discussion revolves around whether to use
  symbolic constants (MASK/MATCH) for opcode fields or literal values.
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer principles.
- term: .insn
  definition: An assembler directive used in some toolchains (like GNU AS) to explicitly
    encode machine instructions, often used for variable-length or custom instruction
    sets.
- term: funct3
  definition: A 3-bit field in RISC-V instructions used to discriminate between different
    operations within a given opcode class.
- term: LGTM
  definition: Acronym for 'Looks Good To Me', a common affirmative response in code
    reviews indicating approval.
- term: opcode
  definition: The part of a machine language instruction that specifies the operation
    to be performed.
series_id: 'binutils:risc-v: add dedicated vector arithmetic .insn forms'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/CAHT-pJyXr_TnBxZGSy6EFqo2aEB5C2y4uW9CvHJTh9ZNA2cyfA@mail.gmail.com
bugzilla_url: null
date: '2026-07-19'
is_stub: false
stub_reason: ''
---

A reviewer has provided a positive 'Looks Good To Me' (LGTM) on a patch series introducing dedicated `.insn` forms for RISC-V vector arithmetic instructions. While the patch is considered good enough to merge, the reviewer suggests a minor improvement: defining separate masks and matches for the `funct3` field instead of using raw hexadecimal values (0x7000), which would enhance code readability and understanding.
