---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- error handling
- architecture parsing
discussion_id: 36f9cb9f-0dc3-470e-b42d-da0c45694108@iscas.ac.cn
source_type: public_inbox
title: 'Re: [PATCH 14/19] RISC-V: error handling for subset parsing'
headline: 'RISC-V: Error handling for subset parsing'
tldr: When parsing RISC-V architecture subsets, keep the previous ISA state upon parsing
  failures, instead of partially updating the subset list.
proposer: Jiawei <jiawei@iscas.ac.cn>
consensus: Ready to Land
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased code complexity due to the temporary subset approach.
- Potential performance overhead due to copying the subset list, though likely negligible.
exchanges:
- author: Jiawei <jiawei@iscas.ac.cn>
  role: proposer
  position: Agrees with the temporary-subset approach in ``riscv_update_subset()``,
    noting that keeping the previous ISA state is safer for ``.option arch`` and ``.attribute``
    parsing failures.
  quote: The temporary-subset approach in riscv_update_subset() looks right to me.
    For .option arch and .attribute parsing failures, keeping the previous ISA state
    is safer than leaving the current subset list partially updated.
primer_expert: The RISC-V backend parses architecture strings (e.g. from ``-march``)
  to determine enabled extensions. This patch ensures that errors during parsing of
  these strings do not lead to a corrupted state, where partially parsed extensions
  are enabled. Specifically, it modifies ``riscv_update_subset`` in ``bfd/elfxx-riscv.c``
  to use a temporary subset during parsing, reverting to the original state on error.
primer_general: When compiling code for RISC-V, the compiler needs to know which extensions
  the target processor supports (e.g., compressed instructions, floating-point, etc.).  This
  is specified via the architecture string (the ``-march`` option). This patch ensures
  that if the compiler fails to understand the architecture string, it doesn't end
  up in a broken state where it incorrectly assumes certain extensions are available.
series_id: 'binutils:risc-v: error handling for subset parsing'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/36f9cb9f-0dc3-470e-b42d-da0c45694108@iscas.ac.cn
bugzilla_url: null
date: '2026-04-29'
---

This patch improves error handling when parsing RISC-V architecture subsets (``-march`` and ``.option arch``). If parsing fails, the previous ISA state is kept, preventing partially updated subset lists. The change ensures that conflicting extensions are not unexpectedly enabled due to parsing errors.
