---
project: binutils
subsystem: loongarch
patch_id: null
tags:
- binutils
- loongarch
- linker
- relocation
- testing
discussion_id: 2575c03c-44e6-4272-a99d-984651e69bb9@loongson.cn
source_type: public_inbox
title: 'Re: [PATCH v2] LoongArch: Detect relocations out of section range'
headline: 'LoongArch: Relocation out-of-section detection acknowledged'
tldr: The submitter acknowledges feedback on the LoongArch relocation detection patch
  and will post revisions soon.
proposer: mengqinggang <mengqinggang@loongson.cn>
consensus: Proposed
outcome: needs_revision
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: mengqinggang
  role: proposer
  position: Acknowledges feedback and plans to submit revised patches.
  quote: "Thanks a lot for the feedback. I'll post some new patches to address \n\
    these issues soon."
- author: Harshit Kumar
  role: reviewer
  position: Provided feedback on the v2 patch, confirming its correctness for several
    tests but highlighting three remaining issues.
  quote: "Thanks for picking this up again. I ran v2 through the checks I used\nfor\
    \ the AArch64 and ARM versions, on a loongarch64-linux-gnu cross of\nmaster ba2f46b2e4:\n\
    \n   - check-ld: only the new test changes (943 -> 944 expected passes,\n    \
    \ no failures).\n   - An ASan run over every LoongArch relocation type (ELF32\
    \ and ELF64; \n     a field crossing the end, starting at the end, or far away;\
    \ static,…"
primer_expert: This discussion concerns a patch aimed at improving the robustness
  of the LoongArch linker implementation within binutils. The patch introduces checks
  to ensure that relocation entries do not extend beyond the bounds of their respective
  sections. Feedback indicates the patch functions correctly for its intended purpose
  and passes various test cases, but three additional issues related to ULEB128 termination,
  relaxation logic, and shared object linking with non-PIC code have been identified
  for future work.
primer_glossary:
- term: LoongArch
  definition: A RISC-based instruction set architecture developed in China, used in
    processors manufactured by Loongson.
- term: relocation
  definition: The process by which the linker or loader adjusts memory addresses in
    code or data to reflect the final location of program segments.
- term: section
  definition: A distinct part of an object file or executable, such as the .text section
    for code, .data section for initialized data, or .bss section for uninitialized
    data.
- term: ULEB128
  definition: Unsigned Little Endian Base 128, a variable-length encoding format for
    integers, often used in DWARF debugging information and other compiler-generated
    data.
- term: ASan
  definition: AddressSanitizer, a memory error detector for C/C++ that finds bugs
    like use-after-free or buffer overflows.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/2575c03c-44e6-4272-a99d-984651e69bb9@loongson.cn
bugzilla_url: null
date: '2026-11-26'
is_stub: false
stub_reason: ''
---

Mengqinggang acknowledges feedback on the v2 patch for detecting LoongArch relocations that extend beyond their section boundaries. The feedback, provided by Harshit Kumar, included positive results from cross-checks against other architectures and noted three potential issues still present on the master branch. Revisions to address these points will be posted shortly.
