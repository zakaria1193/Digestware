---
project: glibc
subsystem: unknown
patch_id: null
discussion_id: mvmjyu76k3p.fsf@suse.de
source_type: public_inbox
title: 'Re: [PATCH v3 1/8] tests: Allow tests to append tunables'
proposer: Andreas Schwab <schwab@suse.de>
consensus: Proposed
sentiment_score: 5
technical_tradeoffs: []
url: https://inbox.sourceware.org/libc-alpha/mvmjyu76k3p.fsf@suse.de
bugzilla_url: null
date: '2026-04-16'
---

On Apr 16 2026, Yury Khrustalev wrote:

> +# Concatenate elements in the list using colon.
> +# Two spaces after 'subst' are intentional.
> +emptystring :=
> +spacestring := $(emptystring) # one space
