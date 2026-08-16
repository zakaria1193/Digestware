---
project: gcc
subsystem: gcc
patch_id: null
tags:
- nginx
- rate limiting
- gitweb
- cgit
- sourceware.org
discussion_id: CAH6eHdRUOyoKTONSJs7XDD8AS9MSM5p7ksZ50roNy_szQNso4w@mail.gmail.com
source_type: public_inbox
title: 'Re: Anubis check stuck?'
headline: Anubis check stuck?
tldr: Users report persistent 429 Too Many Requests errors on sourceware.org, potentially
  due to a new nginx rate limiter.
proposer: Jonathan Wakely <jwakely.gcc@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 6
sentiment_score: null
technical_tradeoffs:
- Increased security/stability via rate limiting vs. user accessibility.
- Potential need for more authentication mechanisms to bypass rate limits.
exchanges:
- author: Alice Carlotti
  role: contributor
  position: Reported issues with Anubis environments (patchwork.sourceware.org, gcc.gnu.org/bugzilla,
    gcc.gnu.org/git/gitweb.cgi) including stuck states and no visible activity.
  quote: 'I have just had this issue with patchwork.sourceware.org (stuck in a hash
    then

    reload loop) and gcc.gnu.org/bugzilla (no visible activity on anubis

    display; I

    think this affected gcc.gnu.org/git/gitweb.cgi as well).'
- author: David Abdurachmanov
  role: contributor
  position: Observed the "Calculating..." issue on Patchwork and experienced "429
    Too Many Requests" errors on gcc.gnu.org/git/gitweb.cgi and sourceware.org/git/git.git,
    making them difficult to use.
  quote: 'Patchwork got stuck with "Calculating...". Twice, even on Incognito mode.

    > gcc.gnu.org/git/gitweb.cgi or https://sourceware.org/git/?p=glibc.git

    > is basically impossible in general. It''s "429 Too Many Requests" for

    > most of the week in general. You pass Anubis and instantly hit with

    > 429.'
- author: Mark Wielaard
  role: maintainer
  position: Addressed the Anubis cookie issue by updating the cookie prefix and informed
    users that existing cookies are invalidated. Also identified the 429 errors as
    a new nginx rate limiter problem and suggested cgit as a more efficient alternative.
  quote: 'OK. After consultation with Xe I updated all Anubis environments with

    COOKIE_PREFIX=swanubis0806. That should resolve the hickups with

    existing cookies. But also invalidates everyones existing cookies.


    So this isn''t a specific Anubis issue. It is the new nginx rate

    limiter. If your ip is "authenticated" (for example after login to

    bugzilla) you won''t get rate limited. Maybe we need more ways to…'
- author: Jonathan Wakely
  role: contributor
  position: Reported that cgit links are also inaccessible due to the 429 error, indicating
    the issue extends beyond gitweb and affects general access to these services.
  quote: 'I''ve been unable to access any cgit links for at least a week, I get the

    429 error every single time.


    For example, I click the first git commit link at

    https://gcc.gnu.org/bugzilla/show_bug.cgi?id=124378#c3 and get the error

    page. Sometimes immediately, sometimes after the Anubis challenge page.'
primer_expert: Users are encountering repeated HTTP 429 errors on sourceware.org services,
  impacting access to gitweb and cgit. This appears to be a side effect of a new nginx
  rate-limiting configuration rather than an issue with the Anubis authentication
  system itself, though Anubis challenges can precede the 429 errors. The problem
  hinders regular access to version control repositories.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/CAH6eHdRUOyoKTONSJs7XDD8AS9MSM5p7ksZ50roNy_szQNso4w@mail.gmail.com
bugzilla_url: null
date: '2026-08-14'
is_stub: false
stub_reason: ''
---

Users are experiencing repeated "429 Too Many Requests" errors when accessing various sourceware.org services, including gitweb and cgit. Initially thought to be an Anubis authentication issue, it's now believed to be caused by a new nginx rate limiter. While authenticated users might bypass this, the current implementation is hindering general access.
