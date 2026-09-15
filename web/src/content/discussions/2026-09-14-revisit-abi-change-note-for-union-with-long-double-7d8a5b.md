---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- abi
- warning
- long double
- union
discussion_id: 8361a782-d57d-4ad8-96dd-51fd426c512d@gmail.com
source_type: public_inbox
title: 'note: the ABI of passing union with ‘long double’ has changed in GCC 4.4'
headline: Revisit ABI change note for union with long double
tldr: Question if GCC's ABI change note for union/long double is still relevant.
proposer: Jonathan Grant <jgrantonline@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Maintaining backward compatibility and ABI stability versus cleaning up old diagnostic
  notes.
- The impact of removing a warning note on users who might still rely on the older
  ABI behavior or are unaware of the change.
exchanges:
- author: Jonathan Grant <jgrantonline@gmail.com>
  role: proposer
  position: Asks if the ABI change note for unions with `long double` is still relevant
    in modern GCC versions and can be removed.
  quote: 'I know this was useful back when it was added, is it worth revisiting and
    considering if it could be left out now GCC is on version 16?


    To save adding -Wno-psabi, or using pragma around it.'
- author: Jonathan Grant <jgrantonline@gmail.com>
  role: contributor
  position: Notes a related Bugzilla report concerning the same issue.
  quote: 'Saw someone reported on bugzilla


    https://gcc.gnu.org/bugzilla/show_bug.cgi?id=118676


    Jonathan'
primer_expert: 'This discussion concerns a diagnostic note emitted by GCC related
  to Application Binary Interface (ABI) stability. Specifically, it questions the
  continued relevance of a note pointing out an ABI change in GCC 4.4 for passing
  unions containing `long double`. The author suggests that with GCC now at version
  16, this specific ABI behavior might be stable or less critical, and the note could
  potentially be removed to clean up diagnostics, possibly referencing Bugzilla #118676.'
primer_glossary:
- term: ABI
  definition: Application Binary Interface. Defines how compiled code interacts at
    the binary level, including function calling conventions, data type representation,
    and system call interfaces.
- term: union
  definition: A composite data type in C and C++ that can hold one of several different
    types of values at any given time. Only one member of a union is active at a time.
- term: long double
  definition: A floating-point data type that typically offers greater precision or
    range than `double`.
- term: GCC 4.4
  definition: A specific release version of the GNU Compiler Collection, known for
    introducing an ABI change related to the discussed topic.
- term: pragma
  definition: A compiler directive that provides additional information to the compiler,
    often used to control aspects like code generation, warnings, or optimization.
- term: -Wno-psabi
  definition: A GCC compiler flag to suppress warnings related to the C++ ABI.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/8361a782-d57d-4ad8-96dd-51fd426c512d@gmail.com
bugzilla_url: null
date: '2026-09-14'
is_stub: false
stub_reason: ''
---

The author questions whether a compiler note, originally added to inform about an ABI change in GCC 4.4 concerning unions with `long double`, is still necessary given GCC's current version (16). They provide a Godbolt link demonstrating the note's appearance and ask if it can be removed to avoid requiring pragmas or `-Wno-psabi` flags. A related Bugzilla entry (118676) is also mentioned.
