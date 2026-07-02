---
project: binutils
subsystem: pe/coff
patch_id: null
tags:
- PE/COFF
- bigobj
- linker
- object file format
- Windows
discussion_id: f510870a-2069-4a30-8045-a9607059be2f@suse.com
source_type: public_inbox
title: 'Re: [PATCH] PE/COFF: auto-promote to bigobj target when section count overflows'
headline: 'PE/COFF: auto-promote to bigobj target when section count overflows'
tldr: This patch enables automatic promotion to the bigobj target format in Binutils'
  PE/COFF backend when the section count overflows, but review questions limit it…
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Under Review
outcome: under_review
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Automatically handles section count overflows, preventing build failures for large
  projects that exceed standard PE/COFF limits.
- Introduces complexity in the automatic detection and promotion logic, requiring
  robust testing to ensure correctness across various scenarios.
- Improves compatibility with larger codebases and modern development practices that
  might generate numerous sections.
exchanges:
- author: Jan Beulich <jbeulich@suse.com>
  role: proposer
  position: Proposes to automatically promote PE/COFF object files to the `bigobj`
    target when the section count overflows in the standard format, and questions
    the limiting of its test case to MinGW targets.
  quote: Especially since the new "default to big-obj if needed" isn't (directly)
    target dependent, the new test also should cover all targets which are affected
    by the change.
primer_expert: PE/COFF (Portable Executable/Common Object File Format) is an executable
  file format used in Windows and some embedded systems. Object files and executables
  are divided into 'sections' (e.g., `.text` for code, `.data` for initialized data,
  `.bss` for uninitialized data). The standard PE/COFF format has a limit on the number
  of sections. The `bigobj` format is an extension that lifts this limitation, allowing
  for a much larger number of sections. This patch concerns Binutils' handling of
  PE/COFF and its logic for automatically switching to the `bigobj` format when the
  standard section limit is…
primer_general: When a computer program is built, its various parts (code, data, etc.)
  are organized into logical blocks called 'sections' within specialized files. The
  PE/COFF format is one way these files are structured, primarily used on Windows
  computers. The standard PE/COFF format has a technical limit on how many sections
  an individual file can have. If a program becomes very large or complex, it might
  exceed this limit. The 'bigobj' format is like an upgraded version that removes
  this restriction. This proposal suggests that Binutils, a set of tools for working
  with these files, should automatically switch to using the 'bigobj' format whenever
  the normal section limit is reached, preventing errors during the build process
  and allowing larger programs to be created for Windows-based systems.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/f510870a-2069-4a30-8045-a9607059be2f@suse.com
bugzilla_url: null
date: '2026-06-23'
is_stub: false
stub_reason: ''
---

This patch proposes that Binutils' PE/COFF backend automatically promote an object file to the `bigobj` target format if the number of sections overflows the capacity of the standard format. A reviewer questioned why the associated test case was restricted to MinGW targets, arguing that the underlying change is not target-specific and should be tested more broadly to ensure it covers all affected targets. The reviewer, while not demanding immediate action on broadening existing tests, suggests aligning the new test's scope with the general applicability of the change.
