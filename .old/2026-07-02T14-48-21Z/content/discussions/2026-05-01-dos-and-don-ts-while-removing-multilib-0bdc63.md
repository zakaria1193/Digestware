---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- s390
- multilib
- library paths
discussion_id: afR3U-92dz6eYpOm@li-819a89cc-2401-11b2-a85c-cca1ce6aa768.ibm.com
source_type: public_inbox
title: '[RFC] Dos and don''ts while removing multilib'
headline: Dos and don'ts while removing multilib
tldr: An RFC discusses how to properly remove multilib support for s390 after dropping
  31-bit support, while maintaining library directory conventions.
proposer: Stefan Schulze Frielinghaus <stefansf@linux.ibm.com>
consensus: Under Review
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Removing multilib support simplifies the build process but requires careful configuration
  to ensure libraries are installed in the correct directories.
- Maintaining the /usr/lib64 convention may require custom configuration beyond simply
  removing multilib macros.
exchanges:
- author: Stefan Schulze Frielinghaus <stefansf@linux.ibm.com>
  role: proposer
  position: Seeks advice on removing multilib support for s390 while maintaining the
    convention of using /usr/lib64 for 64-bit libraries.
  quote: Naively removing MULTILIB_{OPTIONS,DIRNAMES,OSDIRNAMES} from Makefile config/s390/t-linux64
    and the define MULTILIB_DEFAULTS results in choosing the wrong library dir `lib`
    instead of `lib64`.
- author: Andreas Schwab <schwab@linux-m68k.org>
  role: other
  position: Points out that alpha-linux and ia64-linux, also 64-bit targets without
    multilib, put their libraries in /lib.
  quote: 'There are two other 64-bit targets without multilib: alpha-linux and ia64-linux.  But
    both of them put their libraries in /lib, not /lib64.'
primer_expert: Multilib in GCC allows building code for multiple target architectures
  from a single source tree.  It uses macros like MULTILIB_OPTIONS and MULTILIB_DIRNAMES
  to configure the build process and library installation paths. Removing multilib
  requires careful adjustment of these macros to ensure correct library placement.
primer_general: Multilib is a mechanism that allows a single compiler to build binaries
  for multiple target architectures. This is useful when an operating system supports
  both 32-bit and 64-bit applications.  It involves configuring the compiler to generate
  code for different architectures and placing the resulting libraries in separate
  directories to avoid conflicts during linking. The configuration files need to be
  adjusted to ensure libraries are placed in their correct directories.  This proposal
  discusses how to handle library installation directories after only one architecture
  is supported.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/afR3U-92dz6eYpOm@li-819a89cc-2401-11b2-a85c-cca1ce6aa768.ibm.com
bugzilla_url: null
date: '2026-05-01'
---

Stefan Schulze Frielinghaus is preparing a patch to remove -m31 support for s390, which would make multilib obsolete. The author seeks guidance on how to remove multilib while preserving the convention of installing 64-bit libraries under /usr/lib64 instead of /usr/lib. Andreas Schwab notes that alpha-linux and ia64-linux place their libraries in /lib, even without multilib.
