---
project: gcc
subsystem: gcc
patch_id: null
tags:
- libsanitizer
- DEC Alpha
- synchronization
- GCC
- LLVM
discussion_id: CAEdQ38HDKGRqLw45=96bONhEXoi=zCymaAhP05w_nHxq6T5dHw@mail.gmail.com
source_type: public_inbox
title: 'Re: libsanitizer sync needed for DEC Alpha support'
headline: libsanitizer sync needed for DEC Alpha support
tldr: Matt Turner has updated libsanitizer for DEC Alpha support and is seeking a
  maintainer to integrate it into GCC.
proposer: Matt Turner <mattst88@gmail.com>
consensus: Proposed
outcome: ready
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Manual merging of external codebases can be time-consuming and error-prone.
- Ensuring ABI and API compatibility between LLVM's libsanitizer and GCC's runtime
  library.
exchanges:
- author: Matt Turner <mattst88@gmail.com>
  role: proposer
  position: Seeking a GCC maintainer to sync LLVM's libsanitizer changes for DEC Alpha
    support into the GCC tree.
  quote: 'I''ve gotten an additional fix into compiler-rt upstream and have a branch
    to sync things into libsanitizer.


    The branch is available in

    https://github.com/alphalinux-org/gcc/tree/libsanitizer-sync-v2 -- if

    someone would like to review and/or commit the resync bits, that''d be

    great. I''ve got more patches in there that I''ll have to send for

    review but need the sync to be able to actually test.'
primer_expert: This discussion concerns the synchronization of libsanitizer components
  between LLVM's compiler-rt and GCC. The proposer has added DEC Alpha support to
  libsanitizer in LLVM and needs this integrated into GCC's tree to test further patches.
  The complexity lies in the process of merging external codebases and ensuring compatibility
  within GCC's build and testing infrastructure.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAEdQ38HDKGRqLw45=96bONhEXoi=zCymaAhP05w_nHxq6T5dHw@mail.gmail.com
bugzilla_url: null
date: '2026-09-21'
is_stub: false
stub_reason: ''
---

Matt Turner reports that DEC Alpha support for libsanitizer, previously merged to LLVM, is now updated with further fixes and available in his GCC tree. He is requesting assistance from someone with commit access to merge this synchronization into GCC, as it's necessary for testing additional Alpha-specific patches and ensuring timely inclusion before the GCC 17 release.
