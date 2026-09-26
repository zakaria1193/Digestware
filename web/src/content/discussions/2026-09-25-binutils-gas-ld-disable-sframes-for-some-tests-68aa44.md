---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- gas
- ld
- testing
- sframe
discussion_id: d09148c3-88d4-421a-a43e-41e7347646e1@suse.com
source_type: public_inbox
title: 'Re: [PATCH v2 1/2] binutils, gas, ld: Disable SFrames for some tests'
headline: 'binutils, gas, ld: Disable SFrames for some tests'
tldr: Discussion around disabling SFrame tests in binutils, gas, and ld, with a review
  focusing on the unconditional setting of SFrames and the intent of specific te…
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Ensuring test accuracy when default behaviors are modified.
- Maintaining clear test objectives while accommodating different build configurations.
exchanges:
- author: Sam James
  role: proposer
  position: Submits a patch to disable SFrame tests and later clarifies a cleanup
    error, confirming the first modification is the intended one.
  quote: 'Sorry, pasto. I''d changed my mind and didn''t clean it up.


    The first one is the one that should stay.'
- author: Jan Beulich
  role: reviewer
  position: Questions the unconditional setting of `--gsframe=no` and the rationale
    for disabling SFrames within a test suite that specifically targets SFrame behavior.
  quote: 'With this, ...


    ... why this further (and unconditional) setting?


    And then, as we''re in a section of SFrame specific tests, why would it want disabling
    here at all?'
- author: Sam James
  role: proposer
  position: Explains that the test aims to catch undue SFrame upgrades and that passing
    `--gsframe=no` does not undermine the test's intent.
  quote: 'The test is checking whether an object gets "upgraded" to SFrames

    unduly. If SFrames are default-enabled, the test fails becuse it thinks

    the upgrade happened. I think ideally would have a way to check if it is

    default-enabled or not and only disable in that case, but it''s one test,

    and from my reading of it, I don''t think passing --gsframe=no undermines

    the intent of it.'
- author: Jan Beulich
  role: reviewer
  position: Agrees with the adjusted change but seeks confirmation on a specific aspect
    of the SFrame test from Indu.
  quote: 'With this adjusted, the change is okay except for ...


    ... this one aspect, which I''d like Indu to confirm.'
primer_expert: This discussion concerns a patch series for binutils, gas, and ld that
  adjusts test suite behavior related to SFrames. SFrames are a feature likely related
  to stack frame unwind information. The core of the debate is whether SFrames should
  be unconditionally disabled during certain tests or if disabling them undermines
  the test's purpose, particularly when SFrames might be default-enabled. The maintainer
  seeks clarification on the test's intent and its interaction with default SFrame
  behavior.
primer_glossary:
- term: SFrame
  definition: Likely refers to a mechanism for generating stack frame unwind information,
    possibly related to debugging or exception handling. The exact nature is not fully
    specified but relates to code generation in gas/ld.
- term: gas
  definition: The GNU Assembler, part of the binutils package. It translates assembly
    language code into machine code.
- term: ld
  definition: The GNU linker, part of the binutils package. It combines object files
    and libraries to create an executable or shared library.
- term: Testsuite
  definition: A collection of tests designed to verify the correctness of a software
    component.
series_id: 'binutils:binutils, gas, ld: disable sframes for some tests'
series_role: reply
series_parts:
- title: 'binutils, gas, ld: Disable SFrames for some tests'
  url: https://inbox.sourceware.org/binutils/87cxu1bptk.fsf@gentoo.org
  n: 1
  total: 2
- title: 'binutils, gas, ld: Disable SFrames for some tests'
  url: https://inbox.sourceware.org/binutils/1cdc1ce7-f76f-439d-aa03-326873e17f13@suse.com
  n: 1
  total: 2
- title: 'binutils, gas, ld: Disable SFrames for some tests'
  url: https://inbox.sourceware.org/binutils/945ac77c9462c3d8b678ce521c978ef1288b2f3a.1790321423.git.sam@gentoo.org
  n: 1
  total: 2
url: https://inbox.sourceware.org/binutils/d09148c3-88d4-421a-a43e-41e7347646e1@suse.com
bugzilla_url: null
date: '2026-09-25'
is_stub: false
stub_reason: ''
---

Jan Beulich reviews a patch intended to disable SFrame tests in binutils, gas, and ld. The discussion revolves around the correct placement and necessity of disabling SFrames, particularly in test cases. Beulich questions an unconditional setting of `--gsframe=no` and the purpose of disabling SFrames in a test designed to check for undue 'upgrade' to SFrames.
