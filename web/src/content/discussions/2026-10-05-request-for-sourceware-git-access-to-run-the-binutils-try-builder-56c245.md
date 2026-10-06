---
project: binutils
subsystem: binutils
patch_id: null
tags:
- CI
- contributor workflow
- git access
- patch testing
discussion_id: CAOX--DRrBRN5C-ph+wuZbMGGnLrFj_ApHwAC+ZYgioF-0YbTJw@mail.gmail.com
source_type: public_inbox
title: Request for Sourceware Git access to run the Binutils try builder
headline: Request for Sourceware Git access to run the Binutils try builder
tldr: Harshit Kumar requests guidance on obtaining Sourceware Git access to run the
  Binutils try builder for a submitted patch.
proposer: Harshit Kumar <harshit7kr@gmail.com>
consensus: Under Review
outcome: under_review
impact_score: 4
sentiment_score: 7
technical_tradeoffs:
- Establishing clear CI workflows for external contributors without direct Git access
  can increase the project's onboarding friction but ensures patches are tested before
  merging.
exchanges:
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Requests Sourceware Git access to run the Binutils try builder for a patch
    he submitted, seeking guidance on the process.
  quote: null
- author: Jan Beulich <jbeulich@suse.com>
  role: other
  position: Acknowledges the request and suggests looking into the process, noting
    that the mailing list was dropped from a previous reply.
  quote: null
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Follows up, asking for information on triggering the binutils try builder
    from a personal Sourceware Forge fork or alternative workflows for contributors
    without Sourceware Git access.
  quote: null
- author: Mark Wielaard <mark@klomp.org>
  role: other
  position: Offers to explain the current workflow for CI coverage, referencing a
    recent talk on the subject and providing links to related resources.
  quote: null
- author: Harshit Kumar <harshit7kr@gmail.com>
  role: proposer
  position: Confirms understanding of the provided explanation and expresses willingness
    to use the preferred workflow for pre-commit CI coverage, regardless of whether
    it involves Patchwork, Forge, or Buildbot.
  quote: null
primer_expert: This thread discusses the practicalities of Continuous Integration
  (CI) for binutils contributions. Harshit Kumar, an external contributor, needs to
  run the project's try builder to validate his patch but lacks the necessary Sourceware
  Git access. The discussion explores the established workflows for such scenarios,
  including the use of Patchwork, Sourceware Forge, and Buildbot, highlighting the
  need for clear processes for contributors without direct commit rights.
primer_glossary:
- term: try builder
  definition: An automated testing system used in open-source projects to compile
    and test patches before they are merged into the main codebase.
- term: Sourceware Git access
  definition: Permissions to push code to the Git repositories hosted on Sourceware,
    which is necessary for direct contribution and for triggering certain automated
    build and test systems.
- term: Patchwork
  definition: A web-based system for managing patches submitted to open-source projects,
    often used to track patch status and trigger CI builds.
- term: Sourceware Forge
  definition: A platform providing developers with tools for code hosting, issue tracking,
    and collaboration, often used by projects hosted on Sourceware.
- term: Buildbot
  definition: An open-source framework for automating software builds and tests, commonly
    used as a CI system.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/CAOX--DRrBRN5C-ph+wuZbMGGnLrFj_ApHwAC+ZYgioF-0YbTJw@mail.gmail.com
bugzilla_url: null
date: '2026-10-05'
is_stub: false
stub_reason: ''
---

Harshit Kumar has submitted a patch to binutils and wishes to test it using the project's try builder. He is seeking Sourceware Git SSH access to push a temporary branch for this purpose and is asking for assistance from a maintainer or clarification on the correct process, as his Sourceware Bugzilla account is active but Git access is missing. The discussion evolves to explore alternative workflows for contributors without direct Git push access.
