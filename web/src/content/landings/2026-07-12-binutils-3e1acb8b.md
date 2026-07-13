---
project: binutils
subsystem: binutils
patch_id: null
tags:
- release
- versioning
- binutils
commit_hash: 3e1acb8b1db513f52dff29e6d3276b2b41c40a07
source_type: public_inbox
author: Nick Clifton <nickc@sourceware.org>
headline: Update binutils version to 2.46.90 for 2.47 branch
tldr: Sets the version number to 2.46.90 on the binutils-2.47-branch and regenerates
  related files.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: This commit sets the version number to 2.46.90 on the binutils-2.47-branch
  and regenerates Autoconf-generated files (configure scripts) and POT files used
  for internationalization. This is a routine step for managing development branches
  and preparing for future releases.
primer_glossary:
- term: Autoconf
  definition: A tool that automatically configures source code packages to adapt to
    different operating systems and environments. It generates shell scripts (configure
    scripts) that check for system-specific features and settings.
- term: POT file
  definition: Portable Object Template file used in GNU gettext for internationalization.
    It contains extracted translatable strings from source code, serving as a template
    for creating language-specific .po files.
- term: binutils-2_47-branch
  definition: A development branch for version 2.47 of the GNU Binutils package. Development
    on this branch typically precedes a formal release.
discussion_id_link: public_inbox:binutils#17512
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20260712093453.D9BA04BA2E05@sourceware.org
date: '2026-07-12'
is_stub: false
stub_reason: ''
---

This commit sets the version number for the binutils suite to 2.46.90 and regenerates associated configuration files and translation templates. This is part of the process for creating and managing the binutils-2_47-branch, preparing for upcoming releases.
