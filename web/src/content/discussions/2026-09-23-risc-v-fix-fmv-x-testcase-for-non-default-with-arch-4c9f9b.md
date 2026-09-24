---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- gas
- testsuite
- regression
discussion_id: CA+yXCZBg+HbM+TODOVsYfuV0_o8g841p38ePt39NLVowm0AbZA@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Fix fmv.x testcase for non-default --with-arch'
headline: 'RISC-V: Fix fmv.x testcase for non-default --with-arch'
tldr: RISC-V testcase for fmv.x instruction fixed to explicitly use -march=rv32i.
proposer: Kito Cheng <kito.cheng@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Hardcodes a specific architecture flag in a testcase, reducing its flexibility but
  increasing its reliability.
- Ensures consistent test results across different build configurations.
exchanges:
- author: Kito Cheng <kito.cheng@gmail.com>
  role: proposer
  position: Confirms the patch has been pushed to the trunk.
  quote: Thanks, pushed to trunk :)
- author: Ethan Y. C. Liang via Binutils
  role: contributor
  position: Acknowledges a reminder to Cc maintainers for patches.
  quote: Okay, thanks for the reminder.
- author: Jan Beulich
  role: reviewer
  position: Advises Cc'ing relevant maintainers for better patch visibility.
  quote: 'Btw, when you send patches, you may want to Cc all respective maintainers,
    to

    have an overall better chance of getting an approval indication back.'
- author: Ethan Y. C. Liang via Binutils
  role: proposer
  position: Explains that the testcase fails with non-default -march configurations.
  quote: 'The testcase doesn''t pass -march, so it inherits the configured default

    architecture, and fails with e.g. --with-arch=rv32e* (no a6) or

    --with-arch=rv32i_zfinx (".option arch, +f" conflicts).  It only checks

    that fmv.x.s/fmv.s.x are aliases of fmv.x.w/fmv.w.x, which doesn''t

    depend on the base ISA.'
primer_expert: The `gas/testsuite/gas/riscv/fmv.x.d` testcase was failing when compiled
  with specific `--with-arch` configurations because it relied on the default architecture.
  This patch hardcodes `-march=rv32i` to ensure the test only checks the instruction
  aliasing (`fmv.x.s` to `fmv.x.w`) and not architecture-specific behavior.
primer_glossary:
- term: fmv.x
  definition: A RISC-V instruction for moving a value between integer and floating-point
    registers. The testcase checks aliases for this instruction.
- term: -march
  definition: A compiler flag used to specify the target RISC-V architecture and extensions.
    The testcase previously did not specify this, leading to variations in behavior.
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is modular and
    extensible, widely used in embedded systems and high-performance computing.
- term: Testcase
  definition: A specific scenario or input designed to verify the correct behavior
    of a piece of software, in this case, the assembler.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZBg+HbM+TODOVsYfuV0_o8g841p38ePt39NLVowm0AbZA@mail.gmail.com
bugzilla_url: null
date: '2026-09-23'
is_stub: false
stub_reason: ''
---

A RISC-V testcase for the `fmv.x` instruction has been fixed by explicitly setting the `-march=rv32i` flag. Previously, the testcase did not specify `-march`, causing it to inherit the configured default architecture. This led to failures when using `--with-arch` configurations that lacked the necessary extensions, such as `rv32e` or `rv32i_zfinx`. The fix ensures the testcase correctly checks the aliasing of `fmv.x.s/fmv.s.x` to `fmv.x.w/fmv.w.x` regardless of the base ISA.
