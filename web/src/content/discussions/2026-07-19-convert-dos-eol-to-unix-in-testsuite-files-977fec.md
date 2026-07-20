---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- testsuite
- line-endings
- git
- workflow
discussion_id: alxgW4zf6GgfSfUk@squeak.grove.modra.org
source_type: public_inbox
title: convert dos eol to unix
headline: Convert DOS EOL to Unix in testsuite files
tldr: Fixes line endings in many binutils testsuite files to prevent patch application
  failures.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- The tradeoff is between maintaining existing (but problematic) line ending conventions
  and improving the developer experience by standardizing on Unix-style endings.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch to convert DOS-style CRLF line endings to Unix-style LF
    in numerous testsuite files to prevent patch application failures.
  quote: null
primer_expert: This change affects the line endings within the testsuite files of
  the GNU Binutils project. The goal is to normalize all files to use Unix-style line
  endings (LF), thereby preventing `git am` from failing on patches that modify these
  files due to CRLF mismatches.
primer_glossary:
- term: EOL
  definition: End Of Line. Refers to the character(s) used to signify the end of a
    line in text files. DOS/Windows typically uses CRLF (Carriage Return + Line Feed),
    while Unix-like systems use LF (Line Feed).
- term: testsuite
  definition: A collection of tests designed to verify the correctness of the software.
- term: git am
  definition: A Git command used to apply patches that are in thembox format, typically
    found in email archives.
- term: patch failure
  definition: Indicates that a patch could not be applied cleanly to the target code,
    often due to differences in line endings, whitespace, or code structure.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alxgW4zf6GgfSfUk@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-19'
is_stub: false
stub_reason: ''
---

This patch addresses inconsistent line endings (CRLF vs. LF) in various testsuite files across the Binutils project. By converting these to Unix-style line endings, the author aims to prevent 'git am' failures for contributors submitting patches, ensuring a smoother development workflow.
