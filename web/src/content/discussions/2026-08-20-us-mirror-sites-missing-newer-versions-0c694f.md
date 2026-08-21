---
project: gcc
subsystem: gcc
patch_id: null
tags:
- mirrors
- website
- maintenance
discussion_id: CAD5rEwpHaeBvgi3uY6Meqj+y7SiWGWY-T0rpRigoKozoCeCFbg@mail.gmail.com
source_type: public_inbox
title: 'Patch for Re: US mirror sites missing newer versions'
headline: US mirror sites missing newer versions
tldr: The bigsearcher.com US mirror has been removed from the GCC mirror list due
  to its prolonged failure to host recent releases.
proposer: Gerald Pfeifer <gerald@pfeifer.com>
consensus: Proposed
outcome: committed
impact_score: 3
sentiment_score: 5
technical_tradeoffs: []
exchanges:
- author: Gerald Pfeifer <gerald@pfeifer.com>
  role: proposer
  position: Removed the bigsearcher.com mirror from the GCC mirrors list due to its
    failure to provide recent releases.
  quote: "Thank you for the report, Michael, which originally slipped through on my\
    \ \nend (and apparently everyone else's).\n\ninfo@bigsearcher.com - is this a\
    \ \"temporary\" issue you are planning to \naddress? \n\nFor the time being I'm\
    \ remove the mirror from the GCC mirror list per the \npatch below; happy to restore\
    \ once it's mirroring again. And in any case: \nthank you for your support in\
    \ the past."
- author: Gerald Pfeifer <gerald@pfeifer.com>
  role: maintainer
  position: Confirmed the removal of the bigsearcher.com mirror and provided context
    from previous reports.
  quote: First reported to lack a current release in February 2025, 18 months ago.
primer_expert: This administrative change involves updating the GCC website's list
  of mirrors. The discussion clarifies that a specific US-based mirror, bigsearcher.com,
  was removed due to a persistent lack of synchronization with the latest GCC releases,
  indicating a failure in its maintenance or availability.
primer_glossary:
- term: mirror
  definition: A mirror is a server that duplicates the content of another server.
    In the context of software projects like GCC, mirrors provide geographically distributed
    access points for downloading releases and source code, improving availability
    and reducing load on the primary servers.
series_id: null
series_role: reply
series_parts: []
url: https://inbox.sourceware.org/gcc/7e7c2bb1-9d18-a33a-aa3f-b400d407bc45@pfeifer.com
bugzilla_url: null
date: '2026-08-20'
is_stub: false
stub_reason: ''
---

Gerald Pfeifer has removed the bigsearcher.com US mirror from the GCC mirrors list because it had not hosted new releases for at least 18 months, as reported in February 2025. This action was taken after the issue was identified and no immediate resolution was apparent. The mirror may be restored if it begins mirroring again.
