---
project: gcc
subsystem: gcc
patch_id: null
tags:
- build system
- autoconf
- automake
- release cycle
discussion_id: 460f8630-a032-4353-9ccb-f1226484edcc@app.fastmail.com
source_type: public_inbox
title: 'Re: Upgrading autoconf and automake'
headline: Upgrading autoconf and automake
tldr: Proposes upgrading autoconf and automake in GCC; seeks feedback on timing and
  versions.
proposer: Pietro Monteiro <pietro.gcc@sociotechnical.xyz>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Risk of build system regressions versus potential benefits of newer toolchain features
  or bug fixes.
exchanges:
- author: Pietro Monteiro <pietro.gcc@sociotechnical.xyz>
  role: proposer
  position: Proposes upgrading autoconf and automake to latest versions and seeks
    feedback on timing and version choices.
  quote: 'I decided to try upgrading autoconf and automake to the latest available
    versions, respectively 2.73 and 1.19. I put the result in a branch on the forge
    (https://forge.sourceware.org/pietro/gcc.git branch upgrade-autotools) and I''m
    doing some basic testing. ... Before I go any further on this and start looking
    into upgrading binutils-gdb tree too I wanted to ask: 1) Is this something we
    want to d…'
primer_expert: This discussion concerns updating the build system generation tools
  for GCC. Autoconf and Automake are used to generate the configure scripts and Makefiles.
  Upgrading these tools can introduce changes in how the build system behaves, potentially
  affecting the build process or compatibility with different build environments.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/460f8630-a032-4353-9ccb-f1226484edcc@app.fastmail.com
bugzilla_url: null
date: '2026-11-12'
is_stub: false
stub_reason: ''
---

Pietro Monteiro is proposing to upgrade autoconf and automake to their latest versions (2.73 and 1.19, respectively) within the GCC project. They have created a branch with the changes and are seeking community input on whether this is an appropriate time in the release cycle and if the chosen versions are acceptable before proceeding further. The patch also depends on other pending changes for libiberty.
