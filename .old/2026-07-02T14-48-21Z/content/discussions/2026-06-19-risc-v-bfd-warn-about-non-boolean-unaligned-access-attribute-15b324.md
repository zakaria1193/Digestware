---
project: binutils
subsystem: risc-v/bfd
patch_id: null
tags:
- risc-v
- bfd
- attributes
- unaligned access
- warnings
discussion_id: 3ecb6e90-f46f-46de-ba79-f4188e25e58f@suse.com
source_type: public_inbox
title: '[PATCH v3 12/13] RISC-V/bfd: warn about non-boolean unaligned-access attribute'
headline: 'RISC-V/bfd: warn about non-boolean unaligned-access attribute'
tldr: This patch adds warnings in RISC-V BFD for non-boolean `unaligned-access` attributes,
  converting non-zero values to 1.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Introduces new warnings for developers using non-boolean `unaligned-access` attributes.
- Implicitly converts invalid non-boolean `unaligned-access` values to 1, potentially
  masking the original intent if the larger number had a specific, albeit non-standard,
  meaning (though a warning is issued).
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes to introduce warnings in BFD for RISC-V `unaligned-access` attributes
    that are not strictly boolean (0 or 1), converting any non-zero, non-one values
    to 1.
  quote: The attribute being a boolean one, incoming values should be solely 0 or
    1. Convert other non-zero values to 1.
primer_expert: In the RISC-V `bfd` component, specifically within `bfd/elfxx-riscv.c`,
  the `riscv_merge_attributes` function processes object file attributes. `Tag_RISCV_unaligned_access`
  (Tag 3) is a boolean attribute indicating whether unaligned memory accesses are
  permitted. The existing implementation might encounter values other than 0 or 1
  from the assembler (`gas`) for this boolean attribute, potentially due to flags
  or other settings being represented as larger integers. This patch introduces an
  explicit check for `out_attr[i].i > 1` during the initial processing and for `in_attr[i].i
  > 1` during me…
primer_general: This discussion is about how the linker (`bfd`) in the binutils toolchain
  handles certain information for RISC-V processors. Specifically, it's about an "attribute"
  called `unaligned-access`. This attribute tells the system whether the program can
  access memory addresses that are not perfectly aligned (like trying to read a 4-byte
  number from an address that isn't a multiple of 4). This attribute is supposed to
  be a simple "yes" (represented by 1) or "no" (represented by 0). The problem is
  that sometimes, the attribute might be set to a different number. This patch makes
  sure that if the `unaligned-access` attribute is anything other than 0 or 1, the
  linker will issue a warning to the developer. It will also automatically treat any
  non-zero value as "yes" (1), ensuring that the program's behavior remains consistent
  and as expected.
series_id: 'binutils:risc-v/bfd: warn about non-boolean unaligned-access attribute'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/3ecb6e90-f46f-46de-ba79-f4188e25e58f@suse.com
bugzilla_url: null
date: '2026-06-19'
is_stub: false
---

This patch for RISC-V BFD modifies `riscv_merge_attributes` to improve the handling of the `Tag_RISCV_unaligned_access` attribute. Since this attribute is strictly boolean (0 or 1), the change introduces a warning for any non-zero value greater than 1, and subsequently converts such values to 1, ensuring the attribute remains semantically correct during merging.
