---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- RISC-V
- Zvabd
- binutils
- assembler
- linker
discussion_id: 202605270114.64R1Et1P078332@mse-fl2.zte.com.cn
source_type: public_inbox
title: 'Re: [PATCH] RISC-V: Add experimental support for Zvabd extension'
headline: 'RISC-V: Add experimental support for Zvabd extension'
tldr: The RISC-V Zvabd extension is ready; the author asks for the binutils patch
  to land so the GCC patch isn't blocked.
proposer: chen.zhongyao@zte.com.cn
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Adding support for new instructions increases the complexity of binutils.
- Supporting experimental extensions may require changes as the extension evolves.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: maintainer
  position: Agrees to pick up the patch and update it based on the current specification.
  quote: "Sure, I can help pick this up.\n\nThanks for the updated status and spec\
    \ links. Since Zvabd is now in \nFreeze and\nthe only remaining change appears\
    \ to be the mnemonic rename, I will \nrefresh my\nearlier binutils patch and update\
    \ it against the current spec."
primer_expert: This thread discusses adding support for the RISC-V Zvabd extension
  to binutils. The Zvabd extension adds instructions for vector absolute difference
  operations.  Binutils support is necessary for assemblers and linkers to handle
  the new instructions. GCC support depends on binutils support.
primer_general: This discussion concerns adding support for a new set of instructions
  (the Zvabd extension) to the RISC-V architecture.  The binutils project provides
  tools like assemblers and linkers that translate human-readable code into machine
  code.  For the compiler (GCC) to use these new instructions, binutils needs to understand
  them first.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/202605270114.64R1Et1P078332@mse-fl2.zte.com.cn
bugzilla_url: null
date: '2026-05-27'
is_stub: false
---

Chen Zhongyao notes that the RISC-V Zvabd extension is now in the "Freeze" state and asks Jiawei to pick up the binutils patch. The corresponding GCC patch is ready but blocked, pending the binutils changes.
