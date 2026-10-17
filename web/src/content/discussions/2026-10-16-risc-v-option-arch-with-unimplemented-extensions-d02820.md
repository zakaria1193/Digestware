---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- risc-v
- assembler
- directives
- architecture
- specification
discussion_id: 34d385da-b75d-407a-9cde-f70f8818ab77@suse.com
source_type: public_inbox
title: '[PATCH] RISC-V: ".option arch" with unimplemented extensions'
headline: 'RISC-V: ".option arch" with unimplemented extensions'
tldr: Corrects assembler behavior for RISC-V architecture extensions, ensuring unimplemented
  extensions are rejected.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Ensures stricter adherence to the RISC-V specification by rejecting unimplemented
  extensions.
- Improves assembler robustness by correctly distinguishing between explicit and implicit
  extension specifications.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Proposes changes to `riscv_update_subset1` to correctly reject unimplemented
    RISC-V extensions specified via `.option arch`.
  quote: 'While full specifications like rv32ip are rejected, +p was accepted so

    far. The same diagnostic wants issuing there, though. As it turns out,

    riscv_update_subset1() unconditionally passing "true" to

    riscv_parse_add_subset() is wrong. As it further turns out,

    riscv_update_subset1()''s "explicit_subset" parameter is really used as

    only a boolean. Convert it to a real boolean (inverting sense), and r…'
primer_expert: This patch modifies the RISC-V assembler's handling of the `.option
  arch` directive, specifically concerning the `riscv_update_subset1` function in
  `elfxx-riscv.c`. Previously, the assembler incorrectly accepted syntax like `.option
  arch,+p`, even though the '+p' extension might not be fully implemented or recognized.
  The fix refactors `riscv_update_subset1` to correctly use its parameters to distinguish
  between explicit `.option arch` arguments and implicit extensions. It renames `explicit_subset`
  to `exts` and converts an implicit boolean flag into a proper `bool` parameter,
  ensuring that u…
primer_glossary:
- term: RISC-V
  definition: An open-standard instruction set architecture (ISA) based on reduced
    instruction set computer principles. It is modular and extensible.
- term: .option arch
  definition: An assembler directive used in binutils to specify or modify the target
    architecture and its extensions for RISC-V code generation.
- term: extension
  definition: In the context of RISC-V, an extension is a set of additional instructions
    that augment the base ISA (e.g., 'M' for integer multiplication/division, 'A'
    for atomic operations, 'F'/'D' for floating-point, 'V' for vector operations).
    They are often denoted by letters appended to the base ISA, like 'RV64IMAFD'.
- term: assembler directive
  definition: A command within an assembly language source file that provides information
    to the assembler, such as defining data, controlling the assembly process, or
    specifying target features.
- term: ISA
  definition: Instruction Set Architecture. The part of the processor architecture
    visible to the assembly language programmer or compiler writer.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/34d385da-b75d-407a-9cde-f70f8818ab77@suse.com
bugzilla_url: null
date: '2026-10-16'
is_stub: false
stub_reason: ''
---

This patch addresses an issue in the RISC-V assembler where certain unimplemented extensions, like '+p', were accepted when using the `.option arch` directive. The fix modifies the `riscv_update_subset1` function to correctly handle the `explicit_subset` parameter, ensuring that only valid and implemented extensions are accepted. This change aims to prevent the assembler from incorrectly processing or ignoring unsupported architecture features, thereby maintaining stricter adherence to the RISC-V specification.
