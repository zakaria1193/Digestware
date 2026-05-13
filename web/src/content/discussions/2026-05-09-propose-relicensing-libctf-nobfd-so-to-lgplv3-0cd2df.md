---
project: binutils
subsystem: binutils
patch_id: null
tags:
- licensing
- libctf
- GPL
- LGPL
- BTF
discussion_id: 87y0hslaey.fsf@esperi.org.uk
source_type: public_inbox
title: 'Re: Relicensing (most of) binutils/libctf to LGPLv3+?'
headline: Propose relicensing libctf-nobfd.so to LGPLv3+
tldr: To allow the Linux kernel and Clang to use libctf, the proposer suggests relicensing
  libctf-nobfd.so from GPLv3+ to LGPLv3+.
proposer: Nick Alcock <nix@esperi.org.uk>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Switching to LGPL may reduce copyleft protections on libctf-nobfd.so.
- Allows wider adoption of libctf by non-GPL projects.
exchanges:
- author: Nick Alcock <nix@esperi.org.uk>
  role: proposer
  position: Proposes to relicense ``libctf-nobfd.so`` from GPLv3+ to LGPL3+ to allow
    the Linux kernel and Clang to use the library.
  quote: What we are asking to do is to relicense libctf-nobfd.so from GPLv3+ to LGPL3+.
primer_expert: '``libctf`` reads metadata about C types from ELF sections. GCC emits
  CTF into object files'' ``.ctf`` sections; the linker then uses ``libctf`` to deduplicate
  the type info when building executables.  The proposal concerns ``libctf-nobfd.so``,
  which avoids linking against ``libbfd``, a large binutils library for object-file
  parsing. Relicensing would allow non-GPL projects like the kernel build system and
  clang to link against ``libctf`` without license conflicts.'
primer_general: Debuggers need metadata describing app-level types (``struct foo``,
  ``my_enum``).  This metadata can be embedded in the compiled executable.  CTF and
  BTF are two formats for encoding this type information.  ``libctf`` is a library
  for reading CTF/BTF data; the GNU linker uses it to deduplicate type info from the
  object files it links.  The proposal would relicense a variant of ``libctf`` under
  LGPL (weaker copyleft than GPL), making it easier for non-GPL projects to use the
  library.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/87y0hslaey.fsf@esperi.org.uk
bugzilla_url: null
date: '2026-05-09'
is_stub: false
---

The thread proposes relicensing ``libctf-nobfd.so`` from GPLv3+ to LGPLv3+.  ``libctf`` is a library within GNU binutils for reading, manipulating, and writing CTF (Compact Type Format) and BTF (Binary Type Format) data, primarily used for debugging. The primary motivation is to allow the Linux kernel and the Clang compiler to use ``libctf`` without GPL license compatibility issues. The kernel needs to manipulate BTF as part of its build, and Clang could benefit from using ``libctf`` to generate CTF.
