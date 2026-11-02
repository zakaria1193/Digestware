---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- ELF
- byte-order
- FreeBSD
- powerpc
discussion_id: auXI8bAY0TIz-6MK@talos-powerpc64le
source_type: public_inbox
title: 'Re: [PATCH] ld: read the FreeBSD ELF hints file in either byte order'
headline: 'ld: read the FreeBSD ELF hints file in either byte order'
tldr: Piotr Kubaj adds a Signed-off-by line to a patch that allows the FreeBSD ELF
  hints file to be read correctly on big-endian systems.
proposer: Piotr Kubaj <pkubaj@anongoth.pl>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensuring cross-endian compatibility for configuration files is important for portability.
- Default behaviors of utilities like `ldconfig` can create cross-platform compatibility
  challenges.
exchanges:
- author: Piotr Kubaj <pkubaj@FreeBSD.org>
  role: proposer
  position: Submitted a patch to address an issue where FreeBSD's ELF hints file,
    written in little-endian, caused problems on big-endian systems.
  quote: 'FreeBSD''s ldconfig writes the hints file in little-endian byte order on
    all architectures unless it is run with -B, so the header is not necessarily in
    host byte order.


    This causes an issue when trying to link some software on powerpc64 (big-endian
    POWER).'
- author: Jan Beulich
  role: reviewer
  position: Requested clarification on patch submission and noted the need for a 'Signed-off-by'
    line if a copyright assignment with FSF was not in place.
  quote: 'Okay, preferably with ...


    Oh, also - unless you have a copyright assignment in place with the FSF, this
    would need a Signed-off-by of yours.'
- author: Piotr Kubaj <pkubaj@anongoth.pl>
  role: proposer
  position: Added the missing Signed-off-by line to the patch.
  quote: Added missing Signed-off-by.
primer_expert: This patch addresses a byte-order issue in how the GNU linker (`ld`)
  reads FreeBSD's `ldconfig` hints file. On big-endian architectures (like powerpc64),
  `ldconfig` writes this file in little-endian format by default. The linker now correctly
  interprets the hints file regardless of its byte order, ensuring compatibility.
primer_glossary:
- term: FreeBSD ELF hints file
  definition: A file used by FreeBSD's linker (`ldconfig`) to store information about
    shared libraries, aiding in faster library loading and resolution.
- term: little-endian
  definition: A byte order where the least significant byte is stored at the lowest
    memory address.
- term: big-endian
  definition: A byte order where the most significant byte is stored at the lowest
    memory address.
- term: powerpc64
  definition: A 64-bit version of the PowerPC architecture, typically employing big-endian
    byte order.
- term: ldconfig
  definition: A command-line utility on FreeBSD (and similar systems) that builds
    the cache `ld.so` uses to locate shared libraries.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/auXI8bAY0TIz-6MK@talos-powerpc64le
bugzilla_url: null
date: '2026-10-31'
is_stub: false
stub_reason: ''
---

Piotr Kubaj has revised a patch to correctly handle the byte order of FreeBSD's ELF hints file. Previously, the file was always written in little-endian, causing issues on big-endian architectures like powerpc64. This patch ensures the linker can read the hints file regardless of its byte order. A missing 'Signed-off-by' line was also added.
