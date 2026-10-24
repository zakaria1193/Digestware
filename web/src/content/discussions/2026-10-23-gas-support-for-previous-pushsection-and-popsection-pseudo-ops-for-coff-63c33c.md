---
project: binutils
subsystem: gas
patch_id: null
tags:
- binutils
- gas
- coff
- pseudo-ops
- section management
discussion_id: 80c6bb3a-5586-4946-ac9a-17884448ba41@johannesthoma.com
source_type: public_inbox
title: 'Re: [PATCH v5] gas: support for .previous, .pushsection and .popsection pseudo
  ops for coff'
headline: 'gas: support for .previous, .pushsection and .popsection pseudo ops for
  coff'
tldr: Developer inquires about the status of a patch adding section management pseudo-ops
  to COFF targets in gas.
proposer: Johannes Khoshnazar-Thoma <johannes@johannesthoma.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensuring the new pseudo-ops behave identically to their ELF counterparts in the
  COFF context.
- Testing thoroughly across various COFF targets and scenarios to catch edge cases.
- The complexity introduced by more advanced section management might make assembly
  code harder to write or debug for those unfamiliar with it.
exchanges:
- author: Johannes Khoshnazar-Thoma
  role: proposer
  position: Inquired about the merging status of a patch that adds section management
    pseudo-ops for COFF targets.
  quote: Any plans to get that merged? Do you need anything else?
- author: Johannes Khoshnazar-Thoma
  role: proposer
  position: Originally submitted the patch, explaining its purpose and context.
  quote: "This patch adds support for the .previous, .pushsection and\n.popsection\
    \ pseudo-ops for COFF targets. The semantics are\nthe same as their ELF counterparts.\
    \ \n\nThis patch is one building block for compiling the Linux kernel\nas a Windows/ReactOS\
    \ driver."
primer_expert: This discussion is a follow-up on a patch series (v5) that aims to
  enhance the GNU Assembler's (gas) support for the COFF object file format. Specifically,
  it introduces pseudo-operations like `.previous`, `.pushsection`, and `.popsection`,
  which provide more granular control over section management, mirroring ELF's capabilities.
  The primary motivation cited is enabling the compilation of the Linux kernel for
  Windows/ReactOS driver development, which requires robust COFF support.
primer_glossary:
- term: gas
  definition: The GNU Assembler, part of the GNU Binutils package, responsible for
    translating assembly language into machine code.
- term: .previous
  definition: A pseudo-operation that instructs the assembler to return to the section
    that was current before the most recent `.section` or `.pushsection` directive.
- term: .pushsection
  definition: A pseudo-operation that saves the current section and starts a new one,
    similar to `push` on a stack.
- term: .popsection
  definition: A pseudo-operation that restores the section that was previously saved
    by `.pushsection`, similar to `pop` from a stack.
- term: COFF
  definition: Common Object File Format, an older object file format used on Windows
    and some other systems. It is the precursor to PE.
- term: ELF
  definition: Executable and Linkable Format, the standard object file format used
    on most Unix-like systems, including Linux.
- term: pseudo-ops
  definition: Pseudo-operations, also known as assembler directives, are instructions
    to the assembler that do not generate machine code themselves but control the
    assembly process (e.g., defining sections, symbols, or macros).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/80c6bb3a-5586-4946-ac9a-17884448ba41@johannesthoma.com
bugzilla_url: null
date: '2026-10-23'
is_stub: false
stub_reason: ''
---

Johannes Khoshnazar-Thoma is following up on a previously submitted patch (v5) that adds support for `.previous`, `.pushsection`, and `.popsection` pseudo-operations to the GNU Assembler (gas) for COFF targets. He notes that this patch is a prerequisite for compiling the Linux kernel as a Windows/ReactOS driver and asks for an update on its merging status, inquiring if any further action is needed.
