---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gas
- Xtensa
- assertion
- assembly
discussion_id: avFKCpfKgeJSleKh@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: xtensa_insnbuf_from_chars buffer overflow checking'
headline: xtensa_insnbuf_from_chars buffer overflow checking
tldr: Discussion about an assertion failure in xtensa_insnbuf_from_chars when assembling
  with --text-section-literals and a custom Xtensa configuration.
proposer: Max Filippov <max.filippov@gmail.com>
consensus: Under Review
outcome: under_review
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- The trade-off is between strict assertion of correct instruction decoding and allowing
  for variations in Xtensa configurations that might lead to legitimate decoding failures.
exchanges:
- author: Max Filippov
  role: contributor
  position: Reports an assertion failure in `xtensa_insnbuf_from_chars` when using
    a custom Xtensa configuration and `--text-section-literals`, and questions the
    validity of asserting success in this function.
  quote: 'I don''t see a reason to assert that xtensa_insnbuf_from_chars()

    always succeeds, the callers of'
- author: Alan Modra
  role: reviewer
  position: Initially questions the test case, then acknowledges that a custom Xtensa
    configuration with a different length decoder might cause the `xtensa_insnbuf_from_chars`
    function to return a failure, which triggers the assertion.
  quote: "Right, the one that said\n      /* This should never happen when the byte\
    \ stream contains a\n\t valid instruction.  Just read the maximum number of bytes....\
    \  */\nbut now returns a failure because we don't have a valid insn with\na different\
    \ xtensa-modules.c length_decoder."
primer_expert: This thread discusses a bug in the Xtensa backend of GNU Assembler
  (gas), specifically related to the `xtensa_insnbuf_from_chars` function. An assertion
  `gas_assert (ret)` is failing when processing literals in text sections with a custom
  Xtensa configuration (`--text-section-literals`). The issue arises because the instruction
  length decoding logic, which varies with Xtensa configurations, returns an error
  for a specific input, causing the assertion that expects success to fail.
primer_glossary:
- term: xtensa_insnbuf_from_chars
  definition: A function within the binutils assembler that converts a character buffer
    into an Xtensa instruction buffer (insnbuf).
- term: Xtensa
  definition: A configurable microprocessor architecture that allows for custom instruction
    set extensions.
- term: --text-section-literals
  definition: An assembler option that enables the handling of literal data within
    the text section, potentially affecting instruction decoding.
- term: frag
  definition: A fragment, a piece of data or code being assembled, used internally
    by the GNU Assembler.
- term: assertion
  definition: A statement in a program that is believed to be true during execution.
    If an assertion fails, it typically indicates a programming error and halts the
    program.
series_id: avFKCpfKgeJSleKh@squeak.grove.modra.org
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/avFKCpfKgeJSleKh@squeak.grove.modra.org
bugzilla_url: null
date: '2026-11-09'
is_stub: false
stub_reason: ''
---

This discussion revolves around an assertion failure in the `xtensa_insnbuf_from_chars` function within binutils when assembling code with the `--text-section-literals` option and a custom Xtensa configuration. The assertion `gas_assert (ret)` fails because the function called within it returns an error, specifically when decoding instruction lengths with a non-standard Xtensa module configuration. The participants are investigating why the assertion is triggered and whether it's appropriate to assert success in this context.
