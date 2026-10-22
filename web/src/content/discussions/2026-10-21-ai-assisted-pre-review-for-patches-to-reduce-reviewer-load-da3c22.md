---
project: gcc
subsystem: gcc
patch_id: null
tags:
- process
- review
- ai
- workflow
discussion_id: CAFULd4YrGNf=ofefSi3qxwqLg2HKP+L-EgRD+COWdmh=7Spmkw@mail.gmail.com
source_type: public_inbox
title: '[RFC] Expecting AI-assisted pre-review of patches before they hit gcc-patches'
headline: AI-assisted pre-review for patches to reduce reviewer load
tldr: Proposes that maintainers expect AI-assisted pre-review of patches to catch
  common issues before submission, reducing reviewer burden.
proposer: Uros Bizjak <ubizjak@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 7
technical_tradeoffs:
- Potential for AI tools to miss subtle issues or provide false positives.
- Ensuring fair access to AI tools for all contributors.
- Maintaining submitter responsibility for verifying AI findings.
exchanges:
- author: Uros Bizjak <ubizjak@gmail.com>
  role: proposer
  position: Proposes that maintainers expect submitters to perform AI-assisted pre-reviews
    of patches to catch common issues before submission.
  quote: 'I’d like to start a discussion among maintainers about a small process change
    aimed at reducing reviewer load.


    Review capacity is the scarcest resource in GCC. A large share of review rounds
    is spent on issues that could have been caught before the patch was posted: GNU
    style violations, missing or weak testcases, commit message and ChangeLog problems,
    unhandled corner cases, simple logic slips.'
- author: Andrew Pinski <pinskia@gmail.com>
  role: reviewer
  position: Acknowledges the proposal and implicitly asks for clarification by quoting
    the problem statement.
  quote: null
- author: Uros Bizjak <ubizjak@gmail.com>
  role: proposer
  position: Responds to Andrew Pinski, continuing the discussion.
  quote: "On Wed, Oct 21, 2026 at 1:58 PM Andrew Pinski <pinskia@gmail.com> wrote:\n\
    > \n> \n> \n> On Wed, Oct 21, 2026, 4:43 AM Uros Bizjak via Gcc <gcc@gcc.gnu.org>\
    \ wrote:\n>>\n>> Hi all,\n>>\n>> I’d like to start a discussion among maintainers\
    \ about a small process\n>> change aimed at reducing reviewer load.\n>>\n>> Problem\n\
    >>\n>> Review capacity is the scarcest resource in GCC. A large share of\n>> review\
    \ rounds is…"
- author: Richard Biener <richard.guenther@gmail.com>
  role: reviewer
  position: Weighs in on the discussion, quoting previous messages.
  quote: null
- author: DJ Delorie <dj@redhat.com>
  role: contributor
  position: Suggests an automated approach by having a mailing list-subscribed tool
    perform mandatory checks and reply with results.
  quote: 'I think the way to do this is to have something that is subscribed to the
    mailing list, and does our "mandatory" checks on each patch as it''s emailed,
    and sends the results to the list as a reply.


    Whether this is a script, AI, or human, it serves two purposes - it relieves the
    maintainers fr'
- author: Joseph Myers <josmyers@redhat.com>
  role: contributor
  position: Suggests providing AI review functionality within the project's forge,
    possibly via a bot.
  quote: "If we want to suggest AI-assisted review then I think we should provide\
    \ \nfunctionality in the forge (this could be some kind of bot that looks for\
    \ \nparticular comments and acts on them, it doesn't need any"
primer_expert: This proposal suggests integrating AI-assisted pre-review into the
  GCC patch submission workflow. It aims to offload common, deterministic checks (style,
  tests, commit messages) from human reviewers to AI tools, thereby preserving reviewer
  capacity for more complex aspects of patch review. The RFC clarifies that AI review
  is supplementary, not a replacement for manual verification or adherence to GCC's
  existing AI policy.
primer_glossary:
- term: AI-assisted review
  definition: The use of artificial intelligence tools to analyze code changes (patches)
    for potential issues before human review.
- term: patch
  definition: A piece of code representing a proposed change to a software project's
    codebase.
- term: reviewer
  definition: A developer responsible for examining and approving or rejecting submitted
    patches.
- term: maintainer
  definition: A developer who has primary responsibility for a specific subsystem
    or port of the project.
- term: commit message
  definition: The text accompanying a code commit that explains the changes made.
- term: ChangeLog
  definition: A file or section in commit messages that documents significant changes
    for users.
- term: RFC
  definition: Request For Comments; a type of discussion document used to solicit
    feedback on a proposed change or idea.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAFULd4YrGNf=ofefSi3qxwqLg2HKP+L-EgRD+COWdmh=7Spmkw@mail.gmail.com
bugzilla_url: null
date: '2026-10-21'
is_stub: false
stub_reason: ''
---

Uros Bizjak proposes a process change where maintainers expect submitters to perform AI-assisted pre-reviews of patches. This aims to reduce reviewer load by catching common issues like style violations, weak testcases, and commit message errors before a patch is posted for review. The proposal clarifies that this is not a hard gate and emphasizes submitter responsibility for verifying AI findings.
