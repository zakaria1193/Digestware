---
project: binutils
subsystem: binutils
patch_id: null
tags: []
discussion_id: alpine.DEB.2.21.2605041254140.23161@angie.orcam.me.uk
source_type: public_inbox
title: 'Re: Binutils 2.46 tarball was packaged with ''development=true'''
headline: Binutils 2.46 tarball was packaged with 'development=true'
tldr: The Binutils 2.46 tarball was packaged with 'development=true' due to different
  commits used for the two tarballs.
proposer: '"Maciej W. Rozycki" <macro@orcam.me.uk>'
consensus: Proposed
outcome: proposed
impact_score: null
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Maciej W. Rozycki <macro@orcam.me.uk>
  role: proposer
  position: Asks if the release packaging script is supposed to pick the release tag
    automagically.
  quote: Weird, isn't the release packaging script supposed to pick the release tag
    automagically?
primer_expert: N/A
primer_general: N/A
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/alpine.DEB.2.21.2605041254140.23161@angie.orcam.me.uk
bugzilla_url: null
date: '2026-05-04'
---

The Binutils 2.46 tarball was packaged with 'development=true' because the two tarballs were created from slightly different commits.  The author questions whether the release packaging script should pick the release tag automagically.
