---
project: gcc
subsystem: gcc
patch_id: null
tags:
- server
- outage
discussion_id: SJ5PPF77D28E3C2E227340C2D940AF3ADD7ECB12@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
source_type: public_inbox
title: 502 on gcc.gnu.org and sourceware.org?
headline: 502 errors on gcc.gnu.org and sourceware.org
tldr: Website experienced 502 errors due to a server issue, which has now been resolved.
proposer: '"Jiang, Haochen" <haochen.jiang@intel.com>'
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 8
technical_tradeoffs: []
exchanges:
- author: Jiang, Haochen
  role: proposer
  position: Reported experiencing 502 bad gateway errors on gcc.gnu.org and sourceware.org,
    inquiring if it was a server issue or a local problem.
  quote: 'I am meeting issues on visiting gcc.gnu.org

    (including mail archive, Bugzilla, etc.) and sourceware.org

    (like Binutils archive) with 502 bad gateway.


    Is the server totally down or it is the issue from my side?'
- author: Mark Wielaard
  role: other
  position: Confirmed a server issue where the httpd server had fallen over and could
    not automatically restart due to a failed SSL socket setup.
  quote: 'It was a server issue. The httpd server had fallen over (still

    investigating why) and couldn''t automatically restart because it tied

    to also setup a listening ssl socket. Which failed because tha'
- author: Jiang, Haochen
  role: other
  position: Acknowledged Mark Wielaard's explanation regarding the server issue.
  quote: null
- author: Mark Wielaard
  role: other
  position: Provided further details on the server issue.
  quote: null
primer_expert: N/A
primer_glossary:
- term: 502 Bad Gateway
  definition: An HTTP status code indicating that one server on the internet received
    an invalid response from another server.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/SJ5PPF77D28E3C2E227340C2D940AF3ADD7ECB12@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-09-08'
is_stub: false
stub_reason: ''
---

Haochen Jiang reported intermittent 502 bad gateway errors when trying to access gcc.gnu.org and sourceware.org. Mark Wielaard confirmed it was a server issue caused by the httpd server falling over and unable to restart automatically. The issue has since been resolved.
