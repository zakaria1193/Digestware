---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- forge
- patches
- workflow
discussion_id: d21bf3f0-38f5-42fe-9ffe-79ac1bf62565@arm.com
source_type: public_inbox
title: Changes in emails sent by the forge
headline: Changes in emails sent by the forge
tldr: Forge bot updates simplify patch emails, making them easier to thread and manage.
proposer: Claudio Bantaloukas <claudio.bantaloukas@arm.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Simplifies email notifications at the potential cost of some historical context
  within threaded discussions.
- Reduces email noise for maintainers and reviewers by streamlining patch submission
  notifications.
exchanges:
- author: Claudio Bantaloukas <claudio.bantaloukas@arm.com>
  role: proposer
  position: Announces updates to the forge bot, including changes to patch email threading,
    cover letters, and rebasing notifications. Recommends adding a new remote for
    easier pull request management.
  quote: 'I''ve pushed a couple of updates to the batrachomyomachia bot. As a consequence:
    - patch versions sent by the bot will no longer be threaded (this was an explicit
    ask) - single commits will no longer carry an additional cover letter - pure rebases
    will no longer generate a new patch version - the cover letter / additional text
    added by the bot after the patch divider is now easier to read and prov…'
primer_expert: Updates to the GCC forge bot streamline patch notification emails.
  Changes include de-threading patch versions, removing cover letters for single commits
  and rebases, and enhancing instructions for fetching pull requests via git. A new
  remote 'forge-upstream' is recommended for easier workflow integration.
primer_glossary:
- term: forge
  definition: Refers to the Sourceware Forge, a platform for hosting and collaborating
    on open-source projects, including GCC.
- term: patch version
  definition: A specific iteration or revision of a code change submitted for review,
    often with a numbering scheme.
- term: cover letter
  definition: An introductory email or message accompanying a patch series, providing
    an overview and context for the changes.
- term: rebase
  definition: A git operation that reapplies commits from one branch onto another,
    creating a linear history.
- term: pull request
  definition: A mechanism in version control systems (like git) where a developer
    proposes changes from their branch to be merged into another.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/d21bf3f0-38f5-42fe-9ffe-79ac1bf62565@arm.com
bugzilla_url: null
date: '2026-08-07'
is_stub: false
stub_reason: ''
---

Claudio Bantaloukas announces updates to the batrachomyomachia bot for GCC's forge. These changes aim to streamline the email notifications for patches, specifically by removing threading from patch versions, eliminating cover letters for single commits and pure rebases, and improving the readability of bot-added text. Developers are advised to add a new remote to their local clones for easier fetching of pull requests.
