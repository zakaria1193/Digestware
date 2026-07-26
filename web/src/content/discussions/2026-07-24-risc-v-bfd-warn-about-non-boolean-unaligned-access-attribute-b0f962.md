---
project: binutils
subsystem: risc-v/bfd
patch_id: null
tags:
- binutils
- risc-v
- bfd
- elf
- attribute
discussion_id: 822a807f-ed59-4307-a108-3372f6a4c912@suse.com
source_type: public_inbox
title: '[PATCH v4 11/12] RISC-V/bfd: warn about non-boolean unaligned-access attribute'
headline: 'RISC-V/bfd: warn about non-boolean unaligned-access attribute'
tldr: Warn about and normalize non-boolean values for the RISC-V unaligned-access
  attribute.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: ready
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Normalizes eclectic input values to a boolean interpretation, simplifying attribute
  handling.
- Warns users about potentially incorrect attribute usage without outright rejecting
  the object file.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes to warn about and convert non-boolean values for the RISC-V unaligned_access
    attribute.
  quote: 'The attribute being a boolean one, incoming values should be solely 0 or

    1. Convert other non-zero values to 1.'
- author: Jiawei jiawei@iscas.ac.cn
  role: reviewer
  position: Reviewed the patch, suggesting an underscore in the diagnostic message
    in version 4.
  quote: null
primer_expert: This change in binutils' BFD frontend addresses the `Tag_RISCV_unaligned_access`
  ELF attribute. It ensures that values other than 0 or 1 are reported as warnings
  and normalized to 1, correctly enforcing the boolean nature of this attribute for
  accurate code generation and security-related checks (e.g., related to speculative
  execution vulnerabilities that might be mitigated by alignment).
primer_glossary:
- term: BFD
  definition: Binary File Descriptor library, a GNU component that abstracts different
    object file formats.
- term: ELF
  definition: Executable and Linkable Format, a standard file format for executables,
    object code, shared libraries, and core dumps.
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is gaining popularity
    for its modularity and extensibility.
- term: Tag_RISCV_unaligned_access
  definition: An ELF tag specific to RISC-V that indicates whether unaligned memory
    access is permitted.
series_id: 'binutils:risc-v/bfd: warn about non-boolean unaligned-access attribute'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/822a807f-ed59-4307-a108-3372f6a4c912@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch enhances the RISC-V BFD implementation to warn when the `unaligned_access` attribute is set to a value other than 0 or 1. Non-zero values are converted to 1, normalizing the attribute's interpretation. This ensures that the boolean nature of the attribute is respected and potential misconfigurations are flagged.
