---
project: gcc
subsystem: gcc/debug
patch_id: null
tags:
- debug
- reproducibility
- compiler
- plugins
- DWARF
discussion_id: e7bb6bf1-8d23-458b-8c32-6e6f4d1837fc@app.fastmail.com
source_type: public_inbox
title: 'Re: RFC: Should -fplugin and -fplugin-arg options be excluded from DW_AT_producer
  recording?'
headline: 'RFC: Exclude -fplugin options from DW_AT_producer'
tldr: Proposes excluding absolute plugin paths from DW_AT_producer debug metadata
  to improve build reproducibility.
proposer: Pietro Monteiro <pietro.gcc@sociotechnical.xyz>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Excluding plugin paths enhances reproducibility but removes potentially useful information
  from DW_AT_producer.
- Relying on the `NoDWARFRecord` mechanism requires careful maintenance as compiler
  options evolve.
exchanges:
- author: Pietro Monteiro
  role: proposer
  position: Suggests excluding -fplugin and -fplugin-arg from DW_AT_producer to prevent
    host-specific paths from being embedded in debug metadata.
  quote: "As an experiment, I modified:\n\n gcc/common.opt\n\nand marked:\n\n -fplugin=\n\
    \ -fplugin-arg-*\n\nwith NoDWARFRecord."
- author: Richard Biener
  role: reviewer
  position: Acknowledges the proposal and the issue of build-path leakage via plugin
    paths in DW_AT_producer.
  quote: "On Wed, Aug 12, 2026 at 12:40 PM Jaihind Yadav\n<jaihindy@qti.qualcomm.com>\
    \ wrote:\n> \n> Hi,\n> \n> \n> \n> While investigating a build-path leakage issue,\
    \ I noticed that\n> \n> -fplugin=<path> and -fplugin-arg-* options are currently\
    \ recorded in\n> \n> DW_AT_producer when -grecord-gcc-switches is enabled.\n>\
    \ \n> \n> \n> As a result, an absolute plugin path may become embedded in debug\n\
    > \n> metadata."
- author: Jaihind Yadav
  role: contributor
  position: Initially identified the issue where absolute plugin paths are recorded
    in DW_AT_producer, impacting reproducibility.
  quote: This introduces host-specific path information into the generated artifact
    and may negatively affect reproducibility.
primer_expert: This discussion concerns the `DW_AT_producer` attribute in DWARF debug
  information, which records the compiler invocation. The proposal is to prevent absolute
  paths specified via `-fplugin` and `-fplugin-arg-*` from being included in this
  string. This is to avoid embedding host-specific build environment details, thereby
  improving the reproducibility of builds, a goal that has informed previous `NoDWARFRecord`
  additions.
primer_glossary:
- term: DW_AT_producer
  definition: A DWARF debugging information attribute that stores a string identifying
    the compiler and its version, along with some command-line options used during
    compilation.
- term: DWARF
  definition: A debugging data format used by many compilers and debuggers to represent
    information about program variables, types, and code locations.
- term: Reproducibility
  definition: The ability to reliably produce the same output (e.g., executable binary)
    from the same source code and build environment across different times and systems.
- term: GCC plugin
  definition: A mechanism allowing external code to hook into the GCC compiler's optimization
    passes and front-end processing.
- term: NoDWARFRecord
  definition: A GCC internal mechanism to mark compiler options that should not be
    recorded in the DWARF DW_AT_producer attribute.
- term: Build-path leakage
  definition: The unintentional inclusion of host-specific directory paths from the
    build environment into the compiled artifact, which can hinder reproducibility.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/e7bb6bf1-8d23-458b-8c32-6e6f4d1837fc@app.fastmail.com
bugzilla_url: null
date: '2026-08-16'
is_stub: false
stub_reason: ''
---

This RFC proposes excluding GCC's -fplugin and -fplugin-arg options from being recorded in the DW_AT_producer debug metadata. Currently, absolute paths to plugins can be embedded, potentially compromising build reproducibility. The suggested change uses GCC's existing `NoDWARFRecord` mechanism, which has previously been employed for similar reproducibility concerns.
