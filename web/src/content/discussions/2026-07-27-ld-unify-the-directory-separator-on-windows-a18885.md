---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- linker
- windows
- paths
- normalization
discussion_id: 6e4578f2-06bc-487b-b4db-291d8cc2e12e@suse.com
source_type: public_inbox
title: 'Re: [PATCH] ld: Unify the directory separator on Windows.'
headline: 'ld: Unify the directory separator on Windows.'
tldr: Discussion on whether `ld` consistently uses forward slashes on Windows; current
  patch aims to unify directory separators.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Simplifies path handling on Windows by enforcing a single separator style.
- Prevents potential errors caused by mixed or incorrect directory separators.
- The primary tradeoff is determining if the change is strictly necessary given existing
  behavior or Windows API tolerance.
exchanges:
- author: Jan Dubiec
  role: contributor
  position: Proposes a patch to unify directory separators on Windows in `ld`, citing
    examples of mixed-slash paths causing issues and asserting that forward slashes
    are now standard.
  quote: 'This patch is a spin-off of the following discussion: https://inbox.sourceware.org/binutils/20260717101723.1022175-1-jdx@o2.pl/


    When the linker searches for a file, it constructs the full file name by

    concatenating the search path, the directory separator, and the file name.

    As a result, on Windows users may encounter paths like this:


    [...] attempt to open D:/Works/binutils/ld/testsuite/ld-arch…'
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Requests evidence that `ld` has historically used forward slashes on Windows,
    as he is not convinced by the argument alone.
  quote: I'd like to have evidence of this.
- author: Jan Dubiec
  role: contributor
  position: Argues that the lack of regression and the logical consistency of unified
    separators, along with previous statements from Jan Beulich, support the necessity
    and safety of the change.
  quote: "Isn't the absence of any regressions sufficient evidence? There's also a\
    \ \nsimple logical argument: as you noted in another thread, \"Clearly, with \n\
    the many slashes in the paths that you quoted, one more slash won't \nbreak things\"\
    ."
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Clarifies that he was asking for evidence of `ld` using forward slashes,
    and points out that an example from a test suite does not constitute proof of
    `ld`'s internal handling.
  quote: 'My earlier reply looks to have been ambiguous: I was asking for evidence
    of

    ld using slashes. And ...


    >> In an earlier discussion ("ld: Skip

    >> p33265-2 and pr33265-2 tests on Windows") you pointed at a piece of code

    >> in the testsuite, which doesn''t qualify as reference here. Is there any

    >> path handling which indeed inserts slashes unconditionally (rather than

    >> properly using ...'
primer_expert: This thread discusses a patch for the GNU `ld` linker that aims to
  normalize path separators on Windows systems. Historically, Windows file paths can
  use either backslashes (`\`) or forward slashes (`/`). The patch intends to ensure
  that `ld` consistently uses forward slashes when constructing file paths, regardless
  of the input search paths or system conventions. This is considered a safe change
  because many Windows APIs and applications already handle forward slashes correctly,
  and it prevents potential issues arising from mixed or incorrect separator usage,
  particularly when dealing with l…
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: Windows
  definition: Microsoft's family of operating systems, common on desktop and server
    computers.
- term: Directory separator
  definition: The character used in file system paths to separate directory names
    from each other and from the file name. On Windows, this is typically '\', but
    '/' is often accepted.
- term: Patch
  definition: A set of changes to a file or set of files that describes the difference
    between two versions of the code. In software development, patches are often submitted
    for review and integration into a project.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/binutils/6e4578f2-06bc-487b-b4db-291d8cc2e12e@suse.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This discussion revolves around a patch intended to unify directory separators on Windows, resolving issues where `ld` might produce paths with mixed forward and backslashes (e.g., `D:/path\to/file`). Jan Beulich questions the claim that `ld` has long used forward slashes, requesting evidence. The author argues that the absence of regressions and the logical inconsistency of mixed separators suffice as evidence, especially given that other parts of the toolchain might handle this. The core of the patch is to ensure `ld` consistently uses one type of separator.
