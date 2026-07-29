---
project: binutils
subsystem: binutils
patch_id: null
tags:
- security
- linker
- elf
- dynamic linking
- audit libraries
discussion_id: 87mrvb2zdb.fsf@redhat.com
source_type: public_inbox
title: 'RFC: Should the linker warn about and/or control the propagation of audit
  libraries ?'
headline: Linker warning for audit library propagation
tldr: 'RFC: Should the linker warn about or control the automatic propagation of audit
  libraries?'
proposer: Nick Clifton <nickc@redhat.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: 6
technical_tradeoffs:
- Adding control over audit library propagation enhances security but introduces complexity
  in build configurations.
- Changing the default behavior might break existing build processes that rely on
  silent propagation.
exchanges:
- author: Nick Clifton <nickc@redhat.com>
  role: proposer
  position: Proposes adding linker control for audit library propagation due to a
    security concern identified by an AI tool, suggesting options like `--audit-library-propagation=[default|silent|warn|refuse]`.
  quote: 'The linker automatically reads DT_AUDIT entries from all

    input shared libraries and adds them as DT_DEPAUDIT entries

    in the output binary, with no warning.  DT_DEPAUDIT causes

    ld.so to load the named audit library at runtime, which can

    intercept all symbol resolutions via the rtld-audit interface

    (la_symbind, la_pltenter, etc.).


    A malicious shared library provided as a dependency (e.g.,

    through…'
- author: Matt Rice <ratmice@gmail.com>
  role: other
  position: Quoted the proposer's initial message multiple times without adding new
    content in these excerpts.
  quote: ''
primer_expert: The linker currently processes `DT_AUDIT` tags in shared libraries
  and automatically adds them as `DT_DEPAUDIT` entries in the linked binary. This
  mechanism allows runtime audit libraries to hook into dynamic linking operations.
  The concern is that this propagation is silent, enabling a malicious dependency
  to inject an audit library without explicit user action, potentially leading to
  security vulnerabilities. The proposal seeks to give users control over this automatic
  behavior.
primer_glossary:
- term: DT_AUDIT
  definition: A dynamic section tag in an ELF object file that specifies an audit
    library to be loaded by the dynamic linker.
- term: DT_DEPAUDIT
  definition: A dynamic section tag in an ELF object file that indicates a dependency
    on an audit library, causing the dynamic linker to load it.
- term: ld.so / rtld
  definition: The dynamic linker/loader responsible for resolving symbols and loading
    shared libraries at runtime.
- term: rtld-audit interface
  definition: An interface provided by the dynamic linker that allows audit libraries
    to intercept and process dynamic linking events, such as symbol resolution.
series_id: null
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/87mrvb2zdb.fsf@redhat.com
bugzilla_url: null
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

An AI tool flagged a potential security issue where the linker silently propagates audit library entries (DT_AUDIT) from input shared libraries to output binaries as DT_DEPAUDIT. This allows a malicious library to force the runtime loader to load an attacker-controlled audit library without user intervention or warning. The proposal is to introduce a new linker option `--audit-library-propagation` with levels like `default`, `silent`, `warn`, or `refuse` to control this behavior.
