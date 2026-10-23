---
project: binutils
subsystem: risc-v
patch_id: null
tags:
- binutils
- risc-v
- assembler
- directives
- release
discussion_id: CA+yXCZDKfoQQEs401yMi+b0VmAjfN7jZPgHzwA6q7ZKj0O8Nqw@mail.gmail.com
source_type: public_inbox
title: 'Re: [PATCH v9 0/1] RISC-V: Support ".option [no]exact" assembler directives'
headline: 'RISC-V: Support ".option [no]exact" assembler directives.'
tldr: The patch series for RISC-V assembler directives ".option [no]exact" has been
  rebased and merged.
proposer: Kito Cheng <kito.cheng@gmail.com>
consensus: Proposed
outcome: committed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Provides finer control over instruction emission for RISC-V.
- May require users to be more aware of specific instruction details.
exchanges:
- author: Kito Cheng
  role: proposer
  position: Announces that the patch series for RISC-V ".option [no]exact" directives
    has been rebased and merged.
  quote: 'Rebased to trunk and pushed!


    Kito Cheng <kito.cheng@gmail.com> 於 2026年2月11日週三 下午2:26寫道：

    >

    > Reversed ping, it already pass the release period of 2.45, I assume

    > this is OK for trunk now? does anyone can commit that?'
- author: Nelson Chu
  role: reviewer
  position: Previously LGTM'd the patch, pending regression tests, and suggested merging
    before the 2.45 release.
  quote: LGTM if passing regressions of riscv-gnu-toolchain.  I think this isn't urgent,
    but if people in the risc-v community want it in the 2.45 release, then I think
    it's better to merge before the 2.45 branch is created.  We don't have much time
    for now, so hope won't cause trouble in a rush.
- author: Tsukasa OI
  role: contributor
  position: Rebased the patch on Nelson's changes and asked for review/merge.
  quote: 'PING!


    Nelson''s refined C extension handling changes some instruction classes and

    I rebased on it.


    And to Jan, I''m so sorry that I didn''t notice some of your questions.

    I hope that you accept the changes if it seems okay,

    as Nelson asked you as in:

    <https://sourceware.org/pipermail/binutils/2025-May/141144.html>.'
- author: Jan Beulich
  role: reviewer
  position: Raised questions about handling of macro instructions and extensions in
    'exact' mode.
  quote: 'zext.h only has a C alias, which needs treating like other compressed aliases.

    Same for the C alias for zext.w; the Zba alias likely also needs treating

    like that, but then there''s only the macro one left.'
primer_expert: This discussion confirms the merge of a patch series that adds `.option
  [no]exact` directives to the RISC-V assembler. These directives likely provide finer
  control over instruction emission, potentially preventing the assembler from using
  macro-like expansions or certain extensions when 'exact' mode is enabled, ensuring
  closer adherence to the RISC-V specification. The merge was expedited due to its
  proximity to a release branch cut.
primer_glossary:
- term: RISC-V
  definition: An open-source instruction set architecture based on RISC principles.
- term: assembler directives
  definition: Instructions to the assembler that do not produce machine code, but
    rather control the assembly process itself, such as defining symbols, sections,
    or assembly modes.
- term: .option [no]exact
  definition: Assembler directives that likely control whether the assembler should
    strictly adhere to emitting specified instructions or if it can use internal macros
    or extensions to achieve the same result.
- term: macro instructions
  definition: In assembly language, a shorthand for a sequence of instructions that
    is expanded by the assembler into the underlying machine instructions.
- term: trunk
  definition: The main development branch of a version control system, typically containing
    the latest unreleased code.
series_id: 'binutils:risc-v: support ".option [no]exact" assembler directives'
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/CA+yXCZDKfoQQEs401yMi+b0VmAjfN7jZPgHzwA6q7ZKj0O8Nqw@mail.gmail.com
bugzilla_url: null
date: '2026-10-22'
is_stub: false
stub_reason: ''
---

Kito Cheng reports that the patch series enabling RISC-V assembler directives ".option [no]exact" has been rebased onto the trunk and successfully merged. This follows previous discussions and a ping to expedite the merge, with Nelson Chu having previously approved contingent on passing regressions. The directives likely control the exactness of instruction emission, addressing concerns about macro instructions and potential extensions.
