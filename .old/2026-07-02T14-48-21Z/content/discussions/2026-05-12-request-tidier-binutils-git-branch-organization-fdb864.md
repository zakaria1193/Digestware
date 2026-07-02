---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- git
- repository
- branching
- organization
discussion_id: 7737a224-755c-4c5b-bc7b-3de165f8a254@suse.com
source_type: public_inbox
title: git branches
headline: Request tidier binutils git branch organization.
tldr: Jan Beulich suggests tidying the binutils git repository by keeping only official
  branches at the top level and moving user branches under `users/`.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Requires a policy decision and consistent enforcement.
- May inconvenience developers who are accustomed to the current layout.
exchanges: []
primer_expert: This concerns the organization of the binutils git repository.  The
  goal is to reduce the number of refs that developers need to fetch, especially when
  using sparse-checkout configurations.
primer_general: Git repositories store code and its history in branches.  This discussion
  is about organizing the branches in the binutils Git repository to make it easier
  for developers to manage and download the code they need, especially when they're
  only interested in specific parts of the project.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/7737a224-755c-4c5b-bc7b-3de165f8a254@suse.com
bugzilla_url: null
date: '2026-05-12'
is_stub: false
---

Jan Beulich suggests organizing the binutils git repository by limiting the top-level branches to official ones, and placing user-specific branches under the `users/` namespace. This is to reduce the amount of data fetched by developers who selectively fetch branches.
