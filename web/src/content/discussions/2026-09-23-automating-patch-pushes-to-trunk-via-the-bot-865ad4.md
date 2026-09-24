---
project: gcc
subsystem: gcc
patch_id: null
tags:
- automation
- workflow
- git
- forge
- gcc
discussion_id: CA+m0iR8+W3YcgoXMB2vZgTbtUWvjyc9A=HnGs1wpCTNePGqzKg@mail.gmail.com
source_type: public_inbox
title: 'Re: [RFC] Automating patch pushes to trunk via the bot'
headline: Automating patch pushes to trunk via the bot
tldr: RFC to enable a bot to automatically merge approved patches to the GCC trunk,
  inspired by OpenJDK's Skara bot.
proposer: Claudio Bantaloukas
consensus: Under Review
outcome: under_review
impact_score: 7
sentiment_score: 6
technical_tradeoffs:
- Increased automation streamlines the contribution process but requires robust bot
  infrastructure and careful conflict resolution.
- Reliance on a bot for merges could introduce new failure modes or security concerns
  if not implemented securely.
- Balancing the convenience of automated merges with the need for human oversight
  and review.
exchanges:
- author: Claudio Bantaloukas
  role: proposer
  position: Suggests enabling a bot to automatically merge approved patches to the
    GCC trunk, citing OpenJDK's Skara bot as a precedent for a more streamlined workflow.
  quote: I am wondering if we could enable the bot account to push/merge patches on
    our behalf. A good precedent for this is OpenJDK's workflow, which uses the Skara
    bot (open-sourced at https://github.com/openjdk/skara).
- author: Yuao Ma
  role: contributor
  position: Reiterates the need for automation, noting that using a web-based forge
    system only to manually merge patches defeats the purpose and suggests that merging
    via a single command or click would add significant value.
  quote: This is IMO one of the main reasons why more people are not engaging with
    the forge. It makes little sense to use a web based system only to then have to
    manually merge the patches on the git repo.
- author: Jonathan Wakely
  role: reviewer
  position: Acknowledges the proposal and asks for feedback on the current forge-to-mailing-list
    integration, suggesting that if there are issues, they should be addressed first.
  quote: In the past year me and others tried to bridge contributions on the forge
    with the mailing list by making sure that everything done on the forge gets emailed.
    Some hiccups occurred but it seems to me that the process has been working well
    enough for a while now. I'd love to get feedback that this is not the case so
    I can address it BTW.
primer_expert: This discussion explores automating patch merging in GCC via a bot.
  Currently, contributions merged on the forge require manual CLI pushes. The RFC
  proposes a bot-driven merge, inspired by OpenJDK's Skara, to simplify this. The
  core technical challenge lies in integrating the forge's CI/review system with the
  Git repository for automated, conflict-aware merges, while also considering non-technical
  adoption barriers.
primer_glossary:
- term: RFC
  definition: Request For Comments. A document asking for feedback on a proposed change
    or idea.
- term: forge
  definition: A platform for software development, typically including version control,
    issue tracking, and code review (e.g., SourceHut, GitHub, GitLab).
- term: CI
  definition: Continuous Integration. The practice of frequently merging code changes
    from multiple developers into a central repository, followed by automated builds
    and tests.
- term: trunk
  definition: The main development branch in a version control system, representing
    the latest integrated code.
- term: Skara bot
  definition: An automation tool used in the OpenJDK project for managing pull requests
    and integrating changes.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/ae168574-3b7e-47b9-a823-5851953df3da@arm.com
bugzilla_url: null
date: '2026-09-23'
is_stub: false
stub_reason: ''
---

This RFC proposes automating patch merges to the GCC trunk using a bot, similar to OpenJDK's Skara bot workflow. The goal is to streamline the process, as currently, approved patches require manual CLI pushes. While acknowledging technical challenges, the discussion also touches upon the non-technical hurdles in adopting such automation.
