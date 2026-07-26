---
project: binutils
subsystem: binutils
patch_id: null
tags:
- release
- build
- binutils
- regression
discussion_id: 553cd7ba-750e-4de8-b3ac-18ab530c2294@redhat.com
source_type: public_inbox
title: 'Re: Does anyone need to delay the 2.47 release ?'
headline: Does anyone need to delay the 2.47 release ?
tldr: A build failure in generated files might delay the binutils 2.47 release.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Ready to Land
outcome: ready
impact_score: 6
sentiment_score: 7
technical_tradeoffs:
- Delaying the release to fix a build issue versus releasing on time with a potential
  minor defect.
- Ensuring release stability versus adhering to a fixed release schedule.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Asked whether a build failure in generated files should delay the binutils
    2.47 release, noting that such failures are undesirable in release trees, yet
    generated files usually don't require regeneration for releases.
  quote: Question is whether the build failure addressed by [1] is enough of a reason
    to delay. Generally generated files shouldn't need re-generation in release trees,
    and hence the tools to generate such files shouldn't need building in the first
    place. Yet otoh having such a build failure in a release also isn't very nice.
- author: Nick Clifton
  role: maintainer
  position: Inquired if the proposed patch is sufficient to resolve the build failure
    or if further action is needed before the 2.47 release.
  quote: Is applying [1] a sufficient solution to this problem or are there other
    build
- author: Alice Carlotti
  role: contributor
  position: Acknowledged the proposed solution and apologized for causing issues with
    the build.
  quote: OK, thanks - and apologies again for the breakage.
primer_expert: This discussion concerns the binutils 2.47 release timeline. Jan Beulich
  identified a build failure related to generated files in the release branch. The
  core issue is whether this failure, and the fix proposed in [1], warrants delaying
  the release, as generated files and their build tools are typically not part of
  release artifacts.
primer_glossary: []
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/00040067-2460-4da8-ad7e-23324ddab26f@suse.com
bugzilla_url: null
date: '2026-07-24'
is_stub: false
stub_reason: ''
---

Jan Beulich raised a concern about a build failure in generated files potentially delaying the upcoming binutils 2.47 release. Nick Clifton is seeking confirmation if applying a specific fix is sufficient or if other issues necessitate a postponement. Alice Carlotti acknowledged the fix and apologized for the breakage.
