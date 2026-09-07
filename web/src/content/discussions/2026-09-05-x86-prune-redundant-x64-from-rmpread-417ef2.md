---
project: binutils
subsystem: x86
patch_id: null
tags:
- x86
- assembly
- instruction syntax
- amd
discussion_id: PH0PR12MB81496A17107CB187927F2796EEB42@PH0PR12MB8149.namprd12.prod.outlook.com
source_type: public_inbox
title: 'RE: [PATCH] x86: prune redundant x64 from RMPREAD'
headline: 'x86: prune redundant x64 from RMPREAD'
tldr: Rohan Shenoy questions the need for explicit operands in RMPREAD, suggesting
  an operand-less form is implied by AMD's APM.
proposer: '"Shenoy, Rohan Radhesh" <RohanRadhesh.Shenoy@amd.com>'
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs:
- Explicit vs. implicit operand specification for RMPREAD.
exchanges:
- author: Shenoy, Rohan Radhesh <RohanRadhesh.Shenoy@amd.com>
  role: proposer
  position: Questions the necessity of explicit operands for RMPREAD, referencing
    the AMD APM which suggests implicit register usage.
  quote: I do not see a reason why RMPREAD exclusively needs this. And I believe we
    do require an operand-less form of RMPREAD, as according to the latest APM it
    uses implicit operands (rax, rcx), and nowhere suggests explicitly spelling out
    its registers.
primer_expert: This discussion concerns x86 assembly instructions, specifically the
  RMPREAD mnemonic within binutils' assembler. The debate is whether RMPREAD should
  require explicit register operands or if it should implicitly use RAX and RCX as
  suggested by the AMD Architecture Programmer's Manual (APM).
primer_glossary:
- term: RMPREAD
  definition: A x86 assembly instruction, likely related to memory protection or management,
    whose specific function is not detailed here but is the subject of operand syntax
    debate.
- term: x86
  definition: A family of instruction set architectures (ISAs) commonly used in desktop
    and server computers. Binutils provides tools to assemble and link code for this
    architecture.
- term: operands
  definition: The data or registers that an assembly instruction acts upon. Explicit
    operands are listed directly in the instruction, while implicit operands are used
    automatically by the instruction.
- term: AMD APM
  definition: AMD Architecture Programmer's Manual, a comprehensive document detailing
    AMD's processor features and instruction set.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/PH0PR12MB81496A17107CB187927F2796EEB42@PH0PR12MB8149.namprd12.prod.outlook.com
bugzilla_url: null
date: '2026-09-05'
is_stub: false
stub_reason: ''
---

Rohan Shenoy questions why RMPREAD, unlike other RMP instructions, requires explicit operands. He believes an operand-less form is implied by the latest AMD APM, which suggests implicit use of RAX and RCX registers for RMPREAD.
