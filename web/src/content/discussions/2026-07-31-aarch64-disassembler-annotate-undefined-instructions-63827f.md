---
project: binutils
subsystem: rfc
patch_id: null
tags:
- binutils
- aarch64
- disassembler
- objdump
- arm
discussion_id: 5de93e0f-46bc-0f2b-f0cd-f4be1c577238@e124511.cambridge.arm.com
source_type: public_inbox
title: 'Re: RFC: AArch64 Disassembler: Annotate undefined instructions'
headline: 'AArch64 Disassembler: Annotate undefined instructions'
tldr: Discussion continues on the AArch64 disassembler's heuristic for annotating
  undefined instructions, with concerns about accuracy and user interpretation.
proposer: Alice Carlotti <alice.carlotti@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Accuracy of disassembler heuristics versus code complexity and maintainability.
- Balancing the desire to provide helpful annotations with the risk of misinterpretation.
- Informing users about the limitations and assumptions of automated annotation features.
exchanges:
- author: Alice Carlotti <alice.carlotti@arm.com>
  role: proposer
  position: Clarifies that the AArch64 disassembler's annotation of undefined instructions
    targets `objdump` users and addresses concerns about the heuristic's accuracy
    and interpretation.
  quote: 'I''m referring to the user who runs objdump, not the user who creates the

    binary.  It looks like it will usually require the objdump -D option to get any

    of these notes emitted.'
- author: Nick Clifton <nick.clifton@arm.com>
  role: reviewer
  position: Acknowledges Alice's points and suggests potential improvements to the
    heuristic, while noting the feature's inclusion in a release.
  quote: 'True.  I suppose that the heuristic could be improved to test to see if
    a

    following 32-bit value could be combined with the current 32-bit value to

    make a valid symbolic address.  But if you are already unhappy with the

    feature then maybe this is going a step too far.'
primer_expert: This discussion concerns the AArch64 disassembler's heuristic for annotating
  what appear to be undefined instructions. Concerns have been raised about how the
  disassembler conflates 32-bit values with 64-bit addresses and misinterprets content
  as data when users expect instructions. Alice Carlotti clarifies the intended audience
  and limitations, while Nick Clifton suggests improvements to the heuristic, though
  the feature is already committed.
primer_glossary:
- term: AArch64
  definition: The 64-bit ARM architecture.
- term: Disassembler
  definition: A tool that translates machine code into human-readable assembly language.
- term: undefined instruction
  definition: A machine code instruction that is not recognized by the processor,
    often resulting in an exception.
- term: objdump
  definition: A standard Unix utility that displays information from object files,
    including disassembled code.
- term: heuristic
  definition: A practical approach or rule of thumb used to solve a problem, which
    may not be optimal or perfect but is sufficient for the immediate goals.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/5de93e0f-46bc-0f2b-f0cd-f4be1c577238@e124511.cambridge.arm.com
bugzilla_url: null
date: '2026-07-31'
is_stub: false
stub_reason: ''
---

Alice Carlotti clarifies that the AArch64 disassembler's heuristic for annotating undefined instructions is primarily for the `objdump` user, not binary creators. She acknowledges issues with conflating 32-bit and 64-bit values and potential misinterpretations when content is treated as data instead of instructions. Nick Clifton suggests improvements but notes the feature is already committed.
