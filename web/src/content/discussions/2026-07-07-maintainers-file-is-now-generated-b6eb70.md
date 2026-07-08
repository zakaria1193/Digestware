---
project: gcc
subsystem: gcc
patch_id: null
tags:
- process
- maintenance
- developer workflow
- gcc
discussion_id: 92341a31-aecc-4261-bc8c-f3077fe31c1d@arm.com
source_type: public_inbox
title: MAINTAINERS file is now generated
headline: MAINTAINERS file is now generated
tldr: The MAINTAINERS file in GCC is now generated from MAINTAINERS.yml, with a script
  to assist in adding new entries.
proposer: '"Richard Earnshaw (foss)" <Richard.Earnshaw@arm.com>'
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Automation reduces manual errors and ensures consistency but requires maintaining
  the generation script and YAML format.
- New contributors need to learn the YAML format and script usage instead of direct
  editing of the MAINTAINERS file.
exchanges:
- author: Richard Earnshaw (foss) <Richard.Earnshaw@arm.com>
  role: proposer
  position: Announces that the MAINTAINERS file is now generated from MAINTAINERS.yml,
    providing a script for adding new entries and mentioning testsuite updates and
    web page documentation.
  quote: 'Just a heads up that the MAINTAINERS file is now a generated file.  The
    master copy for the input is now in MAINTAINERS.yml, which lives along-side it.


    For new write-after accounts there is a script that should do most of the work
    of creating a new entry in MAINTAINERS.yml; just run contrib/add-write-after.py.


    The testsuite has been updated to validate that the MAINTAINERS file is in sync
    with…'
primer_expert: GCC has automated the generation of its `MAINTAINERS` file, historically
  a manually curated list of subsystem maintainers and reviewers. The new process
  uses `MAINTAINERS.yml` as the source of truth, managed via a script (`contrib/add-write-after.py`)
  for new entries, and validated by the testsuite. This change impacts how project
  contributors and maintainers are registered and keeps the `MAINTAINERS` file in
  sync with the `.yml` source.
primer_glossary:
- term: MAINTAINERS file
  definition: A file in a software project repository that lists the individuals responsible
    for maintaining different parts of the codebase. It's used to direct patch reviews
    and queries to the appropriate people.
- term: MAINTAINERS.yml
  definition: A YAML-formatted file used as the source for generating the MAINTAINERS
    file in GCC. It likely contains structured data about maintainers, reviewers,
    and subsystems.
- term: write-after
  definition: Refers to a reviewer who has been granted commit rights or a similar
    trusted status for a specific subsystem.
- term: testsuite
  definition: A collection of tests designed to verify the correctness and functionality
    of the software.
- term: commit rights
  definition: The permission granted to a user to directly commit changes to the project's
    version control repository.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/92341a31-aecc-4261-bc8c-f3077fe31c1d@arm.com
bugzilla_url: null
date: '2026-07-07'
is_stub: false
stub_reason: ''
---

The MAINTAINERS file within the GCC project is now automatically generated, with `MAINTAINERS.yml` serving as the master source. A script, `contrib/add-write-after.py`, is provided to help with the creation of new entries in the YAML file. The testsuite has been updated to ensure synchronization, and web pages have been updated to reflect the new process.
