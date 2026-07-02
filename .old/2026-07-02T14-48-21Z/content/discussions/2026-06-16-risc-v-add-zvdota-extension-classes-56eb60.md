---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- binutils
- isa-extensions
- command-line
- dot-product
discussion_id: cd961258-afd2-4726-846f-7b27c8b875c3@iscas.ac.cn
source_type: public_inbox
title: 'Re: [RFC 1/2] RISC-V: Add Zvdota extension classes'
headline: 'RISC-V: Add Zvdota extension classes'
tldr: Jiawei proposes adding shorthand aliases like `zvdota` and `zvbdota` for groups
  of RISC-V dot product extensions to simplify command-line specifications and be…
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Proposed
outcome: needs_revision
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Simplified `-march` command-line specification for RISC-V dot product extensions.
- Requires updating `binutils` to recognize new roll-up aliases.
- Improved alignment with RISC-V ISA specification conventions.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: Suggests introducing shorthand aliases for groups of RISC-V dot product
    extensions (e.g., `zvdota`, `zvbdota`) to reduce command-line verbosity.
  quote: As can be seen very "neatly" here, the need to specify effectively every
    insn's extension separately (really only one of zvqwdota8i and zvqwdota16i should
    be necessary to spell out) is getting unwieldy. The situation is even worse with
    what patch 2 adds. Could we consider a shorthand zvdota here (and zvbdota in patch
    2), covering all extensions in one go?
- author: Jiawei
  role: proposer
  position: Agrees to add `zvdota` and `zvbdota` as roll-up names for RISC-V dot product
    extensions in `binutils`, which will imply corresponding individual extensions,
    and plans to update tests and propose these aliases in the ISA specification.
  quote: 'Yes, I agree. I will add zvdota and zvbdota as roll-up names in v2: zvdota
    -> zvqwdota8i + zvqwdota16i + zvfwdota16bf + zvfqwdota8f zvbdota -> zvqwbdota8i
    + zvqwbdota16i + zvfwbdota16bf + zvfqwbdota8f + zvfbdota32f'
primer_expert: This discussion revolves around the RISC-V Zvdota (vector dot product)
  and Zvbdota (vector BFloat16 dot product) instruction set extensions. In `binutils`,
  specifying individual sub-extensions via the `-march` flag (e.g., `rv64gc_zvqwdota8i_zvqwdota16i`)
  can become cumbersome. The proposal is to introduce 'roll-up' aliases like `zvdota`
  and `zvbdota` that implicitly enable a group of related dot product extensions.
  This simplifies the command-line interface for assemblers and compilers while maintaining
  the granular gating of instructions by their individual extension classes within
  `riscv-op…
primer_general: Imagine a computer processor (CPU) has many specialized abilities,
  like crunching numbers very quickly using 'dot product' math. These abilities are
  called 'extensions.' On RISC-V processors, these extensions are often named with
  specific codes like `zvqwdota8i`. When you're telling a tool (like `binutils`, which
  includes an assembler) to prepare code for a RISC-V processor, you might need to
  list many of these extension codes, which can get very long and confusing on the
  command line. This proposal suggests creating shorthand names, like `zvdota` and
  `zvbdota`, that automatically include a whole group of these dot product extensions.
  This makes it much easier to specify the desired features for the processor without
  having to type out every single one. It’s like having a single button that turns
  on a whole set of related options, simplifying how developers tell the tools what
  the chip can do.
series_id: cd961258-afd2-4726-846f-7b27c8b875c3
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/cd961258-afd2-4726-846f-7b27c8b875c3@iscas.ac.cn
bugzilla_url: null
date: '2026-06-16'
is_stub: false
---

Jan Beulich identified a verbosity issue with specifying individual RISC-V dot product extensions (e.g., `zvqwdota8i`, `zvqwdota16i`) on the command line. In response, Jiawei proposes adding shorthand aliases, `zvdota` and `zvbdota`, to represent groups of these extensions. These roll-up names will simplify the `-march` specification while maintaining individual extension gating for instructions, with plans to update tests and potentially propose these aliases in the ISA specification.
