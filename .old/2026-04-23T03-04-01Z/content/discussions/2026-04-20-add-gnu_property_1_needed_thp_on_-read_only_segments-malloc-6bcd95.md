---
project: binutils
subsystem: binutils
patch_id: null
tags:
- THP
- GNU properties
- binutils
- performance
- memory management
discussion_id: CAMe9rOqExArVw7g2UHpn9EWSZwD1Lx1Nx0ZCLJTBCe04om2-NA@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]'
headline: Add GNU_PROPERTY_1_NEEDED_THP_ON_[READ_ONLY_SEGMENTS|MALLOC]
tldr: Propose adding GNU properties to control THP usage per application, but question
  arises whether the main executable should control THP behavior for shared libr…
stakes: Controlling THP usage can avoid performance regressions or memory waste in
  applications and databases. This change would allow developers fine-grained control
  over THP.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
sentiment_score: 6
sentiment_rationale: Initial proposal with a question raised about the scope of control,
  indicating a need for further discussion and clarification.
technical_tradeoffs:
- Increased complexity in managing THP usage.
- Potential for misconfiguration if THP properties are not set correctly.
- Requires careful consideration of THP eligibility criteria to avoid performance
  regressions.
- May introduce compatibility issues with older systems that do not support the new
  GNU properties.
- Impacts the linking process and requires thorough testing.
exchanges:
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Proposes adding GNU properties to enable per-application control over
    THP usage, specifically for read-only segments.
  quote: 'To enable developers per-application control over THP usage under madvise

    THP mode, add the following bits to GNU_PROPERTY_1_NEEDED:


    1. GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Questions why the main executable should control THP behavior for all
    shared libraries, suggesting each binary should have its own say.
  quote: 'Why would one (the main) executable control behavior for all involved

    shared libraries? Shouldn''t each binary get its own say?'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: Responds that library developers may not always know whether THP usage
    will improve or hurt application performance.
  quote: 'Normally library developers don''t know if THP usage in the library will

    improve or hurt application performance.'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Asks for clarification on the definition of "normally".
  quote: '"Normally" as in what exactly? An enti'
- author: H.J. Lu <hjl.tools@gmail.com>
  role: contributor
  position: States that most library developers don't have the infrastructure to test
    THP impact.
  quote: 'Because library developers don''t have the infrastructure to do

    performance testing and don''t know if THP usage in the library will

    improve or hurt application performance.'
primer_expert: 'This RFC concerns the addition of new GNU properties, specifically
  to the ``GNU_PROPERTY_1_NEEDED`` section in ELF binaries, managed by binutils. These
  properties would control THP usage for read-only segments and malloc. Binutils would
  be responsible for adding and interpreting these properties during linking and object
  file manipulation. The discussion touches on the scope of THP control: executable
  vs. shared library.'
primer_general: Binutils is a collection of tools used for working with binary files,
  including executables and libraries. This proposal involves adding new properties
  to these files to control how Transparent Huge Pages (THP) are used. THP is a Linux
  kernel feature that can improve performance, but it can also cause problems in some
  cases. The new properties would allow developers to specify whether THP should be
  enabled for certain parts of their programs. The discussion revolves around whether
  the main program should control THP usage for all the libraries it uses, or whether
  each library should have its own setting.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/304411c8-46b1-447b-923f-fddcbec26093@suse.com
bugzilla_url: null
date: '2026-04-20'
---

This RFC proposes adding GNU properties to enable per-application control over THP usage under madvise THP mode. It suggests adding ``GNU_PROPERTY_1_NEEDED_THP_ON_READ_ONLY_SEGMENTS`` to opt-in THP usage on read-only segments. A question was raised whether the main executable should control the behavior for all involved shared libraries.
