---
project: gcc
subsystem: gcc
patch_id: null
tags:
- web
- performance
- bot-detection
discussion_id: SJ5PPF77D28E3C266CFBC1F2644FD5E8B82ECD32@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
source_type: public_inbox
title: Anubis check stuck?
headline: Anubis check stuck?
tldr: Users are experiencing delays when accessing GCC websites, possibly due to issues
  with the Anubis bot check.
proposer: Jiang, Haochen
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 5
technical_tradeoffs: []
exchanges:
- author: Jiang, Haochen
  role: proposer
  position: Reports that accessing GCC websites like gitweb and the wiki results in
    a stuck state, taking a long time to load.
  quote: When I am trying to access websites using Anubis check for bots, including
    wiki, gitweb, etc, it seems to me stuck there and taking forever.
- author: Mark Wielaard
  role: reviewer
  position: Asks for more specific URLs and details about what "stuck" means to aid
    in investigation.
  quote: 'Could you give a bit more detail on the exact URL you are trying to

    access (gitweb and the wiki use different anubis setups, one uses the

    meta-refresh challenge, the other a javascript based one). And what

    exactly "stuck" means?'
- author: Jiang, Haochen
  role: contributor
  position: Provides specific URLs for gitweb and the wiki, noting that gitweb is
    "calculating forever" and the wiki pages get stuck.
  quote: 'For gitweb, it is simple https://gcc.gnu.org/cgit/gcc/


    For wiki, I am trying to access no matter which wiki page, it always

    stucked,

    like https://gcc.gnu.org/wiki/A_guide_to_testcase_reduction or

    https://gcc.gnu.org/wiki/cauldron2024'
- author: Adhemerval Zanella Netto
  role: other
  position: Appears to be part of the email chain but does not contribute new information
    to the problem.
  quote: null
- author: Alice Carlotti
  role: other
  position: Acknowledge Mark Wielaard's previous message and Haochen's response.
  quote: null
primer_expert: The Anubis check is a bot detection mechanism used on GCC's web infrastructure.
  When users access sites like gitweb or the wiki, they encounter a delay or hang,
  suggesting a performance or functional issue with the Anubis integration, possibly
  triggered by a recent upgrade.
primer_glossary:
- term: Anubis check
  definition: A bot detection system used to protect websites from automated access
    and malicious activity.
- term: gitweb
  definition: A web-based interface for browsing Git repositories.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/SJ5PPF77D28E3C266CFBC1F2644FD5E8B82ECD32@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-08-05'
is_stub: false
stub_reason: ''
---

Users are reporting that they are stuck when trying to access GCC websites like gitweb and the wiki, indicating a potential problem with the Anubis bot check system. The issue appears to have started after an Anubis upgrade, and developers are seeking more details to investigate the exact URLs and the nature of the "stuck" behavior.
