---
project: gcc
subsystem: gcc
patch_id: null
tags:
- gcc
- bugzilla
- usability
- community
discussion_id: CALvbMcAcHfB1Zp+U0HvqeT2Br_ao5hiJDkLmS3oBRb06s33n_g@mail.gmail.com
source_type: public_inbox
title: 'Re: Re-enabling account signup on Bugzilla'
headline: Re-enabling account signup on Bugzilla
tldr: Discussion on re-enabling self-serve account creation for GCC's Bugzilla, with
  proposals for mitigations against spam.
proposer: Andrea Pinski <andrew.pinski@oss.qualcomm.com>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs:
- Increased accessibility for bug reporting vs. potential for increased spam and abuse.
- Implementing and maintaining automated signup with security measures requires ongoing
  effort.
- Finding the right balance of security and usability for account creation.
exchanges:
- author: Sam James <sam@gentoo.org>
  role: proposer
  position: Proposes re-enabling self-account signup on Bugzilla, citing that the
    current manual process deters bug reporting. Offers to help manage accounts and
    mitigate spam.
  quote: 'This has come up on IRC a few times. I think we should re-enable self-account
    signup on Bugzilla.


    Andrea and I at least have seen people put off by having to email to get an account
    and they end up just not filing a bug at all and only complaining on social media,
    or not even that.'
- author: Andrea Pinski <andrew.pinski@oss.qualcomm.com>
  role: contributor
  position: Agrees with re-enabling account signup and offers to help monitor Bugzilla
    activity, sharing the sentiment that manual signup is a barrier.
  quote: 'I agree.


    Likewise with respect to all of bugzilla activity when I am not busy. Even the
    recent bug reports have been great (some even have the known to work and known
    to fail filled in which is super nice).'
- author: Sam James <sam@gentoo.org>
  role: contributor
  position: Suggests implementing a Bugzilla extension similar to Gentoo's, which
    bans URLs from new accounts for 24 hours, and proposes to implement this with
    whitelisting.
  quote: 'I can implement this part with the overseers as we have an extension on
    our side that does almost all of it, it just needs a whitelist added (which I
    can do).


    Any suggestions for what URLs/domains please? cppreference, godbolt/compilerexplorer,
    stackexchange, maybe reddit (as we'
- author: Andrea Pinski <andrew.pinski@oss.qualcomm.com>
  role: contributor
  position: Expresses inability to help with the technical implementation of the Bugzilla
    extension but supports the idea.
  quote: Agreed. I don't know bugzilla enough to be able to help implement this though.
primer_expert: This discussion concerns the usability of GCC's Bugzilla instance.
  The core issue is the friction caused by requiring manual email requests for new
  user accounts, which discourages bug reporting. The proposed solution involves re-enabling
  automated signups, potentially with rate-limiting or URL-filtering mechanisms to
  prevent abuse, drawing parallels to similar systems used in other projects like
  Gentoo's Bugzilla.
primer_glossary:
- term: Bugzilla
  definition: An open-source bug tracking system widely used by software projects,
    including GCC, to manage bug reports, feature requests, and other issues.
- term: IRC
  definition: Internet Relay Chat, a real-time text messaging protocol used for communication
    in many open-source communities, including discussions about GCC development.
- term: URL
  definition: Uniform Resource Locator, the address of a resource on the internet.
    In the context of bug reports, URLs are often used to link to relevant code snippets,
    build logs, or online tools like Godbolt.
- term: Godbolt
  definition: An online compiler-explorer tool (colloquially 'Godbolt') that allows
    users to compile code with various compilers and view the generated assembly output,
    useful for debugging and understanding compiler behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CALvbMcAcHfB1Zp+U0HvqeT2Br_ao5hiJDkLmS3oBRb06s33n_g@mail.gmail.com
bugzilla_url: null
date: '2026-10-18'
is_stub: false
stub_reason: ''
---

This thread discusses re-enabling self-serve account creation on GCC's Bugzilla instance to make it easier for users to report bugs. Participants express concerns about potential spam and abuse, but also note that the current manual account creation process deters bug reporting. They propose implementing measures such as URL blacklisting for new accounts, similar to what Gentoo uses, to mitigate risks while improving accessibility. Agreement is reached on the need for such a feature and willingness to implement and manage it.
