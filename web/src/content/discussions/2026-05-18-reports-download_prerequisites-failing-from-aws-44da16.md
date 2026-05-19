---
project: gcc
subsystem: gcc
patch_id: null
tags:
- build
- prerequisites
- AWS
- GMP
- networking
discussion_id: SJ5PPF77D28E3C2D559FDCCD4AD1401D043EC032@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
source_type: public_inbox
title: download_prerequisites prohibit some AWS IPs?
headline: Reports download_prerequisites failing from AWS
tldr: Haochen Jiang reports that `download_prerequisites` script fails with a 403
  Forbidden error when run on AWS systems, suspecting potential IP blocking.
proposer: '"Jiang, Haochen" <haochen.jiang@intel.com>'
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: null
technical_tradeoffs: []
exchanges:
- author: Jiang, Haochen <haochen.jiang@intel.com>
  role: proposer
  position: Reports encountering 403 Forbidden errors when using `download_prerequisites`
    on AWS systems and suspects potential IP blocking.
  quote: 'https://gcc.gnu.org/pub/gcc/infrastructure/gmp-6.3.0.tar.bz2:

    2026-05-18 08:02:11 ERROR 403: Forbidden.

    error: Cannot download gmp-6.3.0.tar.bz2 from https://gcc.gnu.org/pub/gcc/infrastructure/'
- author: Mark Wielaard <mark@klomp.org>
  role: other
  position: Suggests checking with system administrators to rule out intentional blocking
    and to investigate further.
  quote: null
- author: Jiang, Haochen <haochen.jiang@intel.com>
  role: other
  position: Acknowledges the suggestion and mentions having reported the issue internally.
  quote: null
primer_expert: The `download_prerequisites` script is used to download necessary libraries
  (like GMP, MPFR, and MPC) required to build GCC.  A 403 Forbidden error indicates
  that the server is refusing access, possibly due to IP-based blocking or rate limiting.  This
  can impact automated build processes relying on external dependencies.
primer_general: Building GCC often requires external libraries. The `download_prerequisites`
  script automates the process of downloading these dependencies. A 403 Forbidden
  error suggests the server is blocking the request, preventing the build from proceeding.
  This might happen if the server detects suspicious activity from the requesting
  IP address, such as automated bots or excessive requests.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/SJ5PPF77D28E3C2D559FDCCD4AD1401D043EC032@SJ5PPF77D28E3C2.namprd11.prod.outlook.com
bugzilla_url: null
date: '2026-05-18'
is_stub: false
---

Haochen Jiang reports that the `download_prerequisites` script fails with a 403 Forbidden error when trying to download GMP from `gcc.gnu.org` while building GCC on AWS. The issue seems to occur only on certain days, leading to the suspicion that some AWS IPs might be temporarily prohibited due to potential bot attacks. This could impact GCC builds performed on AWS infrastructure.
