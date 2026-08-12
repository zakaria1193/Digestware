---
project: gcc
subsystem: gcc
patch_id: null
tags:
- dwarf
- debugging
- gcc
- arm
- embedded
discussion_id: CAEyVarHYT=o+xyA4snHmSgS3A+YBz=DO2ZtOAe7uat3sY2WfHw@mail.gmail.com
source_type: public_inbox
title: DW_OP_GNU_uninit emitted with -gstrict-dwarf
headline: DW_OP_GNU_uninit emitted with -gstrict-dwarf
tldr: Investigating if DW_OP_GNU_uninit is correctly emitted with -gstrict-dwarf for
  arm-none-eabi toolchain.
proposer: Stephen Illingworth <stephen.illingworth@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Stephen Illingworth
  role: proposer
  position: Asks whether the `DW_OP_GNU_uninit` debug information operator should
    be emitted when compiling with the `-gstrict-dwarf` flag.
  quote: Given that the '-gstrict-dwarf' has been specified I don't expect DW_OP_GNU_uninit
    to be emitted. Is this current behaviour correct? Am I doing something wrong?
primer_expert: The user is querying the DWARF debug information generation for an
  embedded ARM target. Specifically, they observe the `DW_OP_GNU_uninit` operation,
  which typically indicates uninitialized local variables, being present despite using
  the `-gstrict-dwarf` flag. This flag is intended to enforce stricter adherence to
  DWARF standards, and its interaction with uninitialized variable reporting in this
  context is under scrutiny.
primer_glossary:
- term: DW_OP_GNU_uninit
  definition: A DWARF opcode that indicates an uninitialized local variable. Its presence
    suggests that the compiler is explicitly marking variables as uninitialized in
    the debug information.
- term: DWARF
  definition: A debugging data format used by many Unix-like systems to support debuggers.
    It contains information about variables, types, functions, and control flow.
- term: -gstrict-dwarf
  definition: A GCC compiler flag that enforces stricter adherence to DWARF debugging
    information standards. It aims to produce more correct and compliant debug symbols.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAEyVarHYT=o+xyA4snHmSgS3A+YBz=DO2ZtOAe7uat3sY2WfHw@mail.gmail.com
bugzilla_url: null
date: '2026-08-11'
is_stub: false
stub_reason: ''
---

Stephen Illingworth questions the emission of `DW_OP_GNU_uninit` when compiling with `-gstrict-dwarf` for the `arm-none-eabi` toolchain. He observed this operator in the debug information of an object file and seeks confirmation on whether this behavior is correct or if he is misusing the flag.
