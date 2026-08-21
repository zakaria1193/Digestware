---
project: gcc
subsystem: libsanitizer
patch_id: null
tags:
- libsanitizer
- DEC Alpha
- LLVM
- synchronization
- porting
discussion_id: CAEdQ38Exx-Y3CEbdGbXdhamsTckcurEAfvZwMtNaqZkcgsLmww@mail.gmail.com
source_type: public_inbox
title: libsanitizer sync needed for DEC Alpha support
headline: libsanitizer sync needed for DEC Alpha support
tldr: Seeking assistance to sync DEC Alpha support for libsanitizer from LLVM to GCC
  in time for the GCC 17 release.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: ready
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Integrating code from another project (LLVM) requires careful merging to avoid regressions
  and maintain compatibility within GCC's infrastructure.
exchanges:
- author: Matt Turner <mattst88@gmail.com>
  role: proposer
  position: Reports that DEC Alpha support for libsanitizer has been added to upstream
    LLVM and is working locally with GCC, but needs assistance to sync into GCC.
  quote: 'I added DEC Alpha support to libsanitizer in upstream LLVM a few months
    ago [1]


    I''ve sync''d it to my gcc tree locally and confirmed that it works

    (with a couple of local gcc patches that I''ll send). I''ve looked into

    the process of syncing libsanitizer into gcc and it doesn''t seem like

    something that can be reasonably done by someone without commit

    access.


    Who can I bribe to do this for me? :)'
- author: Matt Turner <mattst88@gmail.com>
  role: contributor
  position: Asks for an acknowledgement that the sync will happen soon enough for
    his remaining Alpha support work.
  quote: 'Happy to wait if this is on someone''s TODO list. Would just like to

    get some ack that we''ll do this sync in plenty of time for me to get

    the remaining bits of Alpha support in before gcc-17.'
primer_expert: This discussion concerns the synchronization of the libsanitizer component
  between LLVM and GCC. Specifically, DEC Alpha architecture support, recently added
  to LLVM's libsanitizer, needs to be integrated into GCC's version of libsanitizer.
  This is a cross-project integration effort requiring someone with GCC commit access
  to perform the merge.
primer_glossary:
- term: libsanitizer
  definition: A collection of runtime libraries in LLVM and GCC that provide sanitizers
    for detecting various runtime errors, such as memory errors (AddressSanitizer)
    and undefined behavior (UndefinedBehaviorSanitizer).
- term: DEC Alpha
  definition: A 64-bit Reduced Instruction Set Computer (RISC) microprocessor architecture
    originally developed by Digital Equipment Corporation (DEC). It was known for
    its high performance in the 1990s and early 2000s.
- term: GCC 17
  definition: The anticipated next major stable release of the GNU Compiler Collection.
    Release cycles typically span several months, with feature freezes and stabilization
    periods preceding the final release.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAEdQ38Exx-Y3CEbdGbXdhamsTckcurEAfvZwMtNaqZkcgsLmww@mail.gmail.com
bugzilla_url: null
date: '2026-08-20'
is_stub: false
stub_reason: ''
---

Matt Turner added DEC Alpha support to libsanitizer in LLVM and has locally integrated it into GCC with pending patches. He is requesting help to sync this change from LLVM to GCC, as it requires commit access. The goal is to complete this before the GCC 17 release cycle.
