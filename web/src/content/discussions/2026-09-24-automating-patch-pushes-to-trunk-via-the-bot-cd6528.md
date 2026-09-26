---
project: gcc
subsystem: gcc
patch_id: null
tags:
- automation
- workflow
- git
- contribution
discussion_id: b1b8d4db-390e-4d00-a3d8-b157725dc941@arm.com
source_type: public_inbox
title: 'Re: [RFC] Automating patch pushes to trunk via the bot'
headline: Automating patch pushes to trunk via the bot
tldr: A proposal to allow a bot to automatically push approved patches to the GCC
  trunk is being discussed, with considerations for existing workflows and potential…
proposer: '"Richard Earnshaw (foss)" <Richard.Earnshaw@arm.com>'
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Potential for errors if automation is not robust.
- Need to ensure all review and CI checks are properly integrated before merging.
exchanges:
- author: Yuao Ma
  role: proposer
  position: Proposes enabling a bot to automatically merge approved patches to the
    GCC trunk, similar to OpenJDK's workflow, to streamline the contribution process.
  quote: 'I am wondering if we could enable the bot account to push/merge patches
    on our behalf. A good precedent for this is OpenJDK''s workflow, which uses the
    Skara bot (open-sourced at https://github.com/openjdk/skara). For example, contributors
    can trigger integration directly from the PR interface:


    https://github.com/openjdk/jdk/pull/32721#issuecomment-5749064779


    Could we explore doing something sim…'
- author: Claudio Bantaloukas
  role: reviewer
  position: Acknowledges the proposal and notes that the current forge-to-mailing-list
    process has been working acceptably, but agrees that automating merges would add
    significant value and improve engagement.
  quote: 'In the past year me and others tried to bridge contributions on the forge
    with the mailing list by making sure that everything done on the forge gets emailed.
    Some hiccups occurred but it seems to me that the process has been working well
    enough for a while now. I''d love to get feedback that this is not the case so
    I can address it BTW.


    With that in place, the question becomes how to get more va…'
- author: Jonathan Wakely
  role: reviewer
  position: Asks for clarification on the specific benefits and potential drawbacks
    of automating patch pushes.
  quote: null
- author: Richard Earnshaw (foss)
  role: reviewer
  position: Asks for clarification on the current state of the forge integration and
    how it currently interacts with the mailing list.
  quote: null
primer_expert: This RFC discusses automating the merging of reviewed patches from
  the GCC web forge directly into the main repository. It contrasts with the current
  manual merge process and seeks to improve developer workflow efficiency, similar
  to other projects.
primer_glossary:
- term: Forge
  definition: A web-based platform for code hosting, review, and collaboration, such
    as the one used for GCC development.
- term: Trunk
  definition: The main development branch of a software project, where new features
    and changes are integrated.
- term: RFC
  definition: Request For Comments, a type of proposal seeking community feedback
    before implementation.
- term: CI
  definition: Continuous Integration, an automated process of frequently merging code
    changes from developers into a central repository.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/b1b8d4db-390e-4d00-a3d8-b157725dc941@arm.com
bugzilla_url: null
date: '2026-09-24'
is_stub: false
stub_reason: ''
---

Yuao Ma proposes enabling a bot to automatically push/merge approved patches to the GCC trunk, citing OpenJDK's Skara bot as a precedent. This aims to streamline the contribution process by reducing manual interaction after code reviews. The discussion touches on the current workflow, the value proposition of using a web-based system for merging, and the need for more engagement with the forge.
