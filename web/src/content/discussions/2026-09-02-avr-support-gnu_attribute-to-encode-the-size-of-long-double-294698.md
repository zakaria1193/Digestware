---
project: binutils
subsystem: avr
patch_id: null
tags:
- avr
- elf
- attributes
- abi
- linker
discussion_id: 55570124-c5b7-4065-ab90-11a34104bd94@gjlay.de
source_type: public_inbox
title: 'Re: AVR: Support .gnu_attribute to encode the size of [long] double'
headline: 'AVR: Support .gnu_attribute to encode the size of [long] double'
tldr: Adds .gnu_attribute support to binutils for AVR to encode double/long double
  sizes, enabling ABI compatibility checks.
proposer: Georg-Johann Lay <avr@gjlay.de>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increases the complexity of ELF parsing and attribute handling in binutils.
- Ensures ABI compatibility, preventing potential runtime errors or difficult-to-debug
  issues.
exchanges:
- author: Georg-Johann Lay <avr@gjlay.de>
  role: proposer
  position: Adds new .gnu_attribute tags for AVR to encode double/long double sizes,
    enabling linker checks for ABI compatibility.
  quote: "AVR GCC allows to chose the size of double and long double at\ncompile time\
    \ by means of -m[long-]double={32|64}.  As these\noptions select a different ABI,\
    \ Binutils should complain when\nan attempt is being made to link incompatible\
    \ object files.\n\nThis patch adds\n    .gnu_attribute 8 (Tag_GNU_AVR_BITS_DOUBLE)\n\
    \    .gnu_attribute 12 (Tag_GNU_AVR_BITS_LONG_DOUBLE)\nand some simple test cases.\n\
    \nA tag val…"
primer_expert: This change adds AVR-specific ELF `.gnu_attribute` support to binutils.
  The goal is to ensure link-time compatibility when the AVR GCC toolchain allows
  user selection of `double` and `long double` precision (32/64 bits), which implies
  different ABIs. Binutils will now record these choices in object files and enforce
  compatibility during linking.
primer_glossary:
- term: .gnu_attribute
  definition: An ELF section that stores arbitrary metadata about the object file,
    often used by toolchains to convey information relevant to compilation, linking,
    or runtime behavior.
- term: ABI
  definition: Application Binary Interface. Defines how compiled code interacts with
    the operating system and hardware, including function calling conventions and
    data type representations. Mismatched ABIs can lead to link errors or runtime
    crashes.
- term: Tag_GNU_AVR_BITS_DOUBLE
  definition: A specific .gnu_attribute tag used to indicate the bit size of the 'double'
    floating-point type for AVR targets.
- term: Tag_GNU_AVR_BITS_LONG_DOUBLE
  definition: A specific .gnu_attribute tag used to indicate the bit size of the 'long
    double' floating-point type for AVR targets.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/55570124-c5b7-4065-ab90-11a34104bd94@gjlay.de
bugzilla_url: null
date: '2026-09-02'
is_stub: false
stub_reason: ''
---

This patch introduces support for `.gnu_attribute` tags (Tag_GNU_AVR_BITS_DOUBLE and Tag_GNU_AVR_BITS_LONG_DOUBLE) in binutils for the AVR architecture. This allows the compiler to encode the size of `double` and `long double` (32 or 64 bits) into object files. The linker can then use these attributes to detect and reject attempts to link object files with incompatible floating-point ABI settings, ensuring ABI consistency.
