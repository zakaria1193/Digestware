---
project: binutils
subsystem: ld
patch_id: null
tags:
- linker
- ld
- ELF
- read-only sections
- linker script
discussion_id: 20260331181527.884535-1-hjl.tools@gmail.com
source_type: public_inbox
title: 'Re: [PATCH] ld: Handle special ELF readonly output sections'
headline: 'Ld: Handle special ELF readonly output sections'
tldr: A patch proposes handling special ELF readonly output sections based on their
  name, but a reviewer suggests using the READONLY keyword instead.
stakes: Incorrectly handling read-only sections can lead to security vulnerabilities
  if writable data ends up in a read-only section, or functional bugs if code expects
  to be able to write to a section marked read-only.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Under Review
outcome: proposed
sentiment_score: 5
sentiment_rationale: The reviewer raises a valid concern about relying solely on names,
  suggesting a more explicit and user-controlled approach.
technical_tradeoffs:
- Relying on section names is simpler to implement but less explicit and potentially
  error-prone.
- Using the `READONLY` keyword in linker scripts provides explicit control but requires
  users to be aware of and use the feature.
- Naming conventions can be useful for automatically determining default properties,
  but explicit configuration provides more flexibility and avoids ambiguities.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Argues against relying solely on the section name to determine if it is
    read-only. Suggests using the READONLY keyword in the linker script instead.
  quote: This once again being solely name-based, ... what's wrong with using the
    READONLY keyword here instead?
- author: H.J. Lu <hjl.tools@gmail.com>
  role: proposer
  position: Did not respond to the reviewer.
  quote: null
primer_expert: The linker (ld) combines object files into an executable. ELF (Executable
  and Linkable Format) is a common file format for executables, object code, shared
  libraries, and core dumps. Read-only sections in ELF files are memory regions marked
  as non-writable at runtime. The discussion involves how ld determines whether output
  sections should be marked read-only, and the tradeoffs between relying on naming
  conventions verses explicit flags in linker scripts.
primer_general: The linker (ld) is a tool that combines compiled code (object files)
  into a final executable program.  Executables are often divided into sections (e.g.
  code, data, read-only data).  Read-only sections are memory regions that the operating
  system prevents the program from writing to.  This helps prevent accidental modification
  of code or constant data. This discussion is about how the linker decides which
  sections should be read-only, and whether it should be based on the section's name
  or an explicit marker.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/2e800b3d-25f3-40ae-82e8-e57bcfdc543b@suse.com
bugzilla_url: null
date: '2026-04-22'
---

This patch introduces a mechanism in the linker (ld) to identify special ELF readonly output sections based on their names. A reviewer questions the approach of relying solely on section names and suggests using the `READONLY` keyword in linker scripts instead, as this would allow users to explicitly control the read-only status of sections they create.
