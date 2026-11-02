---
project: binutils
subsystem: mach-o
patch_id: null
tags:
- binutils
- mach-o
- security
- vulnerability
- bfd
discussion_id: 4c182aba-5bb8-49a8-a153-de5ddebd6572@suse.com
source_type: public_inbox
title: 'Re: [PATCH v3] mach-o: fix out-of-bounds read in bfd_mach_o_read_prebound_dylib'
headline: 'mach-o: fix out-of-bounds read in bfd_mach_o_read_prebound_dylib'
tldr: Reviewer confirms patch was committed, reprimands author for private emails
  and lack of CC.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Committed
outcome: committed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Fixing memory safety issues like out-of-bounds reads is critical for software stability
  and security.
- Effective communication protocols (using mailing lists, clear subject lines, timely
  follow-ups) are vital for efficient open-source development.
exchanges:
- author: Jan Beulich
  role: reviewer
  position: States the patch has been committed and admonishes the author for sending
    duplicate emails and for failing to keep the mailing list CC'd on private communications.
  quote: 'First - why two pings (one here and one on the v1 thread)? And then, did

    you check the repo before sending the ping? I did commit your change on

    Friday.


    Also, please don''t send private mails, always keep the list on Cc.'
- author: Venkateswara Reddy
  role: proposer
  position: Followed up on the status of their patch, inquiring if further updates
    were needed.
  quote: 'Following up to check if v3 of the patch looks good to be pushed, or

    if there are any further updates needed.'
primer_expert: This discussion is about a patch submitted to the binutils project,
  specifically targeting the `bfd` (Binary File Descriptor) library's handling of
  the mach-o object file format. The patch corrects an out-of-bounds read vulnerability
  within the `bfd_mach_o_read_prebound_dylib` function, which parses prebound dynamic
  libraries information in mach-o files. The reviewer confirms the patch was committed
  but criticizes the author's communication practices.
primer_glossary:
- term: mach-o
  definition: Mach Object file format, the standard object file format used on macOS
    and iOS.
- term: bfd
  definition: Binary File Descriptor library, part of binutils, providing a common
    interface to various object file formats.
- term: out-of-bounds read
  definition: A memory access error where a program attempts to read data beyond the
    allocated buffer boundaries, potentially leading to crashes or security vulnerabilities.
- term: prebound dylib
  definition: Refers to dynamic libraries in macOS that have their symbol addresses
    pre-resolved at link time, rather than at runtime.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/4c182aba-5bb8-49a8-a153-de5ddebd6572@suse.com
bugzilla_url: null
date: '2026-11-02'
is_stub: false
stub_reason: ''
---

The reviewer, Jan Beulich, informs the author that their patch to fix an out-of-bounds read in the mach-o parser within binutils has already been committed. The reviewer also expresses frustration with the author for sending duplicate emails (one to the thread, one private) and for not keeping the mailing list CC'd on private correspondence.
