---
project: binutils
subsystem: risc-v/gas
patch_id: null
tags:
- binutils
- risc-v
- gas
- attribute
- warning
discussion_id: 90b222f1-b4b0-4748-ba83-3143d8f363d0@suse.com
source_type: public_inbox
title: '[PATCH v4 09/12] RISC-V/gas: warn about non-boolean unaligned-access attribute'
headline: 'RISC-V/gas: warn about non-boolean unaligned-access attribute'
tldr: Warn about non-boolean values for the RISC-V unaligned-access attribute in the
  assembler.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: ready
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Introduces a warning for non-compliant attribute values.
- Does not actively merge or normalize values within gas, relying on BFD for that
  logic.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Adds a warning to gas for non-boolean values of the unaligned_access attribute.
  quote: The attribute being a boolean one, values should be solely 0 or 1.
- author: Jiawei <jiawei@iscas.ac.cn>
  role: reviewer
  position: Asked if attributes should accumulate rather than being set individually,
    similar to BFD's behavior.
  quote: null
primer_expert: This change enhances the RISC-V assembler's handling of the `Tag_RISCV_unaligned_access`
  attribute. It warns if the value provided via the `.attribute` directive is not
  strictly 0 or 1, ensuring that this boolean flag is correctly interpreted. This
  is important for security and correctness, as unaligned access behavior can have
  performance and security implications.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture (ISA) that is gaining popularity
    for its modularity and extensibility.
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package.
- term: .attribute
  definition: An assembler directive used to specify object file attributes, such
    as target architecture or features.
- term: Tag_RISCV_unaligned_access
  definition: An ELF tag specific to RISC-V that indicates whether unaligned memory
    access is permitted.
series_id: 'binutils:risc-v/gas: warn about non-boolean unaligned-access attribute'
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/90b222f1-b4b0-4748-ba83-3143d8f363d0@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

This patch introduces a warning in the RISC-V GNU Assembler (gas) when the `.attribute unaligned_access` directive is used with a value other than 0 or 1. This helps catch potential errors where developers might incorrectly specify this boolean attribute, ensuring better adherence to the RISC-V specification.
