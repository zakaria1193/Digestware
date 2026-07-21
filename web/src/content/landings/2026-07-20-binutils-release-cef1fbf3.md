---
project: binutils
subsystem: binutils/release
patch_id: null
tags:
- release
- binutils
- maintenance
commit_hash: cef1fbf3b02ff6e5bc62e1b8a7d30c0a32b8b9f7
source_type: public_inbox
author: Nick Clifton <nickc@sourceware.org>
headline: Update release contact details for binutils crontab entry
tldr: Changes contact persons for updating the binutils crontab on SourceWare.
impact_score: 2
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit updates the `README-how-to-make-a-release` file for binutils.
  It changes the contact persons responsible for updating the SourceWare crontab entry
  which likely automates release-related tasks. The previous contact, Joel Brobecker,
  has been replaced by Andrew Burgess and Simon Marchi.
primer_glossary:
- term: crontab
  definition: A time-based job scheduler in Unix-like operating systems. A crontab
    file contains the list of jobs to run at specified times.
- term: SourceWare
  definition: A web-based hosting service for open-source projects, particularly those
    related to GNU software, providing version control, bug tracking, and build services.
- term: binutils
  definition: A set of programming tools for editing binary files. It includes the
    assembler, linker, and other utilities essential for software development.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260720103847.59BAC4BA79A5@sourceware.org
date: '2026-07-20'
is_stub: true
stub_reason: low_score
---

Contact information for updating the SourceWare crontab entry for binutils has been updated. Joel Brobecker is no longer the primary contact; instead, users should reach out to Andrew Burgess or Simon Marchi for assistance with crontab modifications related to binutils releases.
