---
project: gcc
subsystem: gcc
patch_id: null
tags:
- sourceware.org
- Forgejo
- access control
- authentication
discussion_id: SL2P216MB2271D9633CE16A65BCC9C18DEF672@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
source_type: public_inbox
title: Cannot access Forgejo if logged in, but can if not
headline: Cannot access Forgejo if logged in
tldr: User reports being unable to access the Forgejo repository for GCC when logged
  into sourceware.org, but can access it when logged out.
proposer: Zhongteng Gui <dragon-archer@outlook.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 5
technical_tradeoffs: []
exchanges:
- author: Zhongteng Gui <dragon-archer@outlook.com>
  role: proposer
  position: Reports an issue where the GCC Forgejo repository is inaccessible (404
    Not Authorized) when logged into sourceware.org, but accessible when logged out.
  quote: 'When I''m logged in, trying to access https://forge.sourceware.org/gcc/gcc
    returns 404, with a message says:

    "The page you are trying to reach either does not exist, has been removed or you
    are not authorized to view it."'
- author: Richard Earnshaw (foss) <Richard.Earnshaw@arm.com>
  role: other
  position: Acknowledges the user's report of access issues with the Forgejo repository
    when logged in.
  quote: null
primer_expert: This is a user support request regarding access control on sourceware.org's
  Forgejo instance. The user, Zhongteng Gui, is unable to access the GCC project's
  Forgejo repository (`forge.sourceware.org/gcc/gcc`) when authenticated. This suggests
  a potential misconfiguration in Forgejo's authorization or authentication system,
  possibly related to new user accounts or specific group memberships that prevent
  access to project resources.
primer_glossary:
- term: Forgejo
  definition: A free and open-source software code hosting platform, forked from Gitea.
    It is used by sourceware.org to host various open-source projects.
- term: 404 error
  definition: An HTTP status code indicating that the server could not find the requested
    resource. In this context, it also includes an authorization denial message.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/SL2P216MB2271D9633CE16A65BCC9C18DEF672@SL2P216MB2271.KORP216.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-10-20'
is_stub: false
stub_reason: ''
---

A user registered on sourceware.org is experiencing an issue where they receive a 404 error, stating they are not authorized, when trying to access the GCC Forgejo repository while logged in. However, the same page is accessible when logged out or using a private browsing mode. The user suspects it might be due to their newly registered account or a configuration issue.
