---
project: gcc
subsystem: gcc
patch_id: null
tags:
- infrastructure
- rate limiting
- Git
- nginx
- access issues
discussion_id: 7fd28b9d-856f-4d62-b2bb-7ca028b4a968@gmail.com
source_type: public_inbox
title: gcc git 429 Too Many Requests nginx
headline: Experiencing 429 Too Many Requests errors on GCC Git web interface
tldr: Users are encountering '429 Too Many Requests' errors when accessing the GCC
  Git web interface, indicating rate limiting is in effect.
proposer: Jonathan Grant <jgrantonline@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: 7
technical_tradeoffs:
- Implementing rate limiting to protect infrastructure versus potentially blocking
  legitimate users.
- Identifying the source of excessive traffic (e.g., scrapers) versus addressing the
  symptom (rate limiting).
exchanges:
- author: Jonathan Grant <jgrantonline@gmail.com>
  role: proposer
  position: Reports encountering '429 Too Many Requests' errors when accessing the
    GCC Git web interface, including the summary and commitdiff pages.
  quote: 'Anyone else getting 429 error on the gcc git web page?


    I''ve been seeing this for a few days on:


    https://gcc.gnu.org/git/?p=gcc.git;a=summary


    429 Too Many Requests

    nginx'
- author: Richard Earnshaw (foss) <Richard.Earnshaw@arm.com>
  role: other
  position: Confirms experiencing the same '429 Too Many Requests' errors on the GCC
    Git web page.
  quote: 'On 24/08/2026 12:48, Jonathan Grant via Gcc wrote:

    > Hello

    >

    > Anyone else getting 429 error on the gcc git web page?'
- author: Mark Wielaard <mark@klomp.org>
  role: other
  position: Confirms experiencing the 429 errors and attributes them to "AI scraperbots"
    being active.
  quote: Sadly yes. The AI scraperbots are again in full force using
- author: Kevin Stefanov <kevinstefanov15@gmail.com>
  role: other
  position: Reports being blocked from accessing Bugzilla and even `git pull` with
    429 errors, indicating a broader issue affecting multiple GCC services.
  quote: 'I have also been getting blocked

    from accessing bugzilla and even

    "git pull" stopped working for me.

    It keeps giving error 429.'
primer_expert: This discussion reports widespread '429 Too Many Requests' errors from
  the nginx web server serving the GCC Git repository. This indicates that the server
  is actively rate-limiting access, likely due to excessive traffic. The problem affects
  access to the Git web interface and potentially other services like Bugzilla and
  Git operations.
primer_glossary:
- term: 429 Too Many Requests
  definition: An HTTP status code indicating that the user has sent too many requests
    in a given amount of time ('rate limiting').
- term: nginx
  definition: A high-performance web server often used as a reverse proxy, load balancer,
    and HTTP cache. In this context, it serves the GCC Git web interface and is enforcing
    rate limits.
- term: GCC Git web page
  definition: The web interface for browsing the GCC project's Git repository, typically
    hosted on Sourceware.
- term: commitdiff
  definition: A display showing the differences between two consecutive commits in
    a version control system like Git.
- term: rate limiting
  definition: A technique used to control the amount of traffic sent or received by
    a network connection. It restricts repeated requests from the same source within
    a specified time period.
- term: Bugzilla
  definition: A popular open-source bug tracking system used by many projects, including
    GCC, to manage reported issues.
- term: git pull
  definition: A Git command used to fetch changes from a remote repository and merge
    them into the current local branch.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/7fd28b9d-856f-4d62-b2bb-7ca028b4a968@gmail.com
bugzilla_url: null
date: '2026-08-24'
is_stub: false
stub_reason: ''
---

Jonathan Grant reports experiencing persistent '429 Too Many Requests' errors from nginx when trying to access the GCC Git web pages and specific commit diffs. This issue has been ongoing for several days, suggesting a problem with rate limiting on the server. Other users confirm facing similar blocking issues.
