---
project: gcc
subsystem: gcc
patch_id: null
tags:
- mirrors
- infrastructure
- Algeria
- North Africa
discussion_id: LO4P265MB65399DD953315230CBBD534280A42@LO4P265MB6539.GBRP265.PROD.OUTLOOK.COM
source_type: public_inbox
title: New GCC mirror in Algiers, Algeria - mirror.hostarts.dz
headline: New GCC mirror in Algiers, Algeria
tldr: A proposal for a new GCC mirror located in Algiers, Algeria, to improve access
  for users in North Africa and the MENA region.
proposer: Houssam Chergui <h.chergui@hostarts.com>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: null
technical_tradeoffs:
- Ensuring consistent and timely synchronization of the mirror with the official GCC
  servers is crucial for its utility.
exchanges:
- author: Houssam Chergui <h.chergui@hostarts.com>
  role: proposer
  position: Proposes a new GCC mirror in Algiers, Algeria, detailing its technical
    specifications and geographic benefits.
  quote: "We would like to offer a new GCC mirror, located in Algiers, Algeria.\n\n\
    Mirror URL:    https://mirror.hostarts.dz/gcc/\n            http://mirror.hostarts.dz/gcc/\n\
    \                   rsync://mirror.hostarts.dz/gcc/\n  Location:  Algiers, Algeria\
    \ (AS329667)\n  Contact:   Houssam Chergui <h.chergui@hostarts.com>\n  Sponsor:\
    \   HOSTARTS - https://hostarts.dz"
primer_expert: This is a proposal to add a new mirror for GCC releases and snapshots.
  The proposer highlights the geographic location in Algeria, aiming to improve download
  speeds and availability for users in North Africa and the Middle East, complementing
  the existing mirror in Morocco.
primer_glossary:
- term: mirror
  definition: A server that duplicates the content of another server. For GCC, mirrors
    provide distributed download locations for releases, snapshots, and other project
    resources, improving accessibility and reducing load on primary servers.
- term: rsync
  definition: A remote synchronization protocol and utility used for efficiently transferring
    and synchronizing files between computers over a network. It is often used for
    mirroring file distributions.
- term: MENA region
  definition: An acronym for Middle East and North Africa, a geographic region encompassing
    countries in North Africa and Western Asia.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/LO4P265MB65399DD953315230CBBD534280A42@LO4P265MB6539.GBRP265.PROD.OUTLOOK.COM
bugzilla_url: null
date: '2026-08-20'
is_stub: false
stub_reason: ''
---

HOSTARTS is proposing to establish a new GCC mirror in Algiers, Algeria, to serve users in North Africa and the MENA region. The mirror would be synchronized twice daily from gcc.gnu.org and offer HTTP, HTTPS, and rsync access. This would be the second mirror in Africa and the first in Algeria, aiming to reduce latency for users in the region.
