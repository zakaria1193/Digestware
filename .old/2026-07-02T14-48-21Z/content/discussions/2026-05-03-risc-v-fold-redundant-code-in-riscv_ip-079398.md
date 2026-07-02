---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- bugfix
- review
discussion_id: 531aa2c8-9442-49eb-90e9-0bf066181673@suse.com
source_type: public_inbox
title: 'Re: [02/19] RISC-V: fold redundant code in riscv_ip()'
headline: 'RISC-V: fold redundant code in riscv_ip()'
tldr: Jan Beulich acknowledges and will correct an issue in the RISC-V instruction
  parsing code identified by Jiawei.
proposer: Jiawei
consensus: Needs Revision
outcome: needs_revision
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- The original patch simplified the code but introduced a bug.
- The corrected patch will maintain the original behavior while improving code readability.
exchanges:
- author: Jiawei
  role: reviewer
  position: Identifies that the patch changed the accepted range of values for the
    O2 operand, which may be unintentional.
  quote: 'Before this change, O2 rejected values >= 3, so the accepted range was

    0...2. With the new common check based on 1U << regno, O2 now accepts

    0...3.


    Is this intended?'
- author: Jan Beulich <jbeulich@suse.com>
  role: other
  position: Acknowledges the issue and states that they will correct it.
  quote: No, I will need to correct that. Thanks for spotting.
primer_expert: This thread discusses a refactoring of the RISC-V instruction parsing
  in the GNU assembler.  The specific issue is within the `riscv_ip()` function, which
  handles instruction pseudo-ops. The concern is an unintended change to the allowed
  range of an operand due to the refactoring.
primer_general: This discussion revolves around improvements to the RISC-V assembler
  in the GNU binutils.  The assembler translates human-readable assembly code into
  machine code that the processor can execute. The patch in question aimed to simplify
  the code that parses RISC-V instructions, but a reviewer noticed that it inadvertently
  changed the valid range of values for one part of an instruction, potentially leading
  to incorrect code generation.
series_id: 'binutils:risc-v: fold redundant code in riscv_ip()'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/531aa2c8-9442-49eb-90e9-0bf066181673@suse.com
bugzilla_url: null
date: '2026-05-03'
---

Jan Beulich responds to a review by Jiawei regarding a patch that folds redundant code in the `riscv_ip()` function. Jiawei pointed out that the patch inadvertently changed the accepted range of values for the 'O2' operand. Jan acknowledges the issue and indicates that they will correct it.
