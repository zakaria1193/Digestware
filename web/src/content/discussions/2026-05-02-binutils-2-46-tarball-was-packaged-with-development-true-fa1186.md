---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- build
- Werror
discussion_id: c4e611d0-2ef2-4495-8623-7ec82df3f101@gmail.com
source_type: public_inbox
title: Binutils 2.46 tarball was packaged with 'development=true'
headline: Binutils 2.46 tarball was packaged with 'development=true'.
tldr: The binutils 2.46 release tarball incorrectly has 'development=true', causing
  -Werror to be enabled and builds to fail.
proposer: Sönke Holz <sholz8530@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 7
sentiment_score: null
technical_tradeoffs:
- Setting development=true enforces stricter code quality but can prevent users from
  building the software.
- Setting development=false allows more users to build the software but may hide potential
  issues.
- The correct setting depends on the intended audience and the goals of the release.
exchanges:
- author: Sönke Holz <sholz8530@gmail.com>
  role: proposer
  position: Reports that the binutils 2.46 tarball was packaged with 'development=true',
    causing build failures due to -Werror being enabled.
  quote: 'The ''development'' variable in bfd/development.sh is set to true, which

    causes ''-Werror'' to be enabled by default, resulting in build failures

    on my system.'
primer_expert: The `development` variable in `bfd/development.sh` controls whether
  `-Werror` is enabled by default during the build. Enabling `-Werror` treats all
  compiler warnings as errors, causing the build to fail if any warnings are present.
  This is typically enabled during development but disabled for releases.
primer_general: During software builds, compiler warnings can be treated as errors
  using the `-Werror` flag.  This ensures that the codebase is free of warnings, which
  can sometimes indicate potential bugs.  However, for release tarballs, this is often
  disabled to allow users with different environments and compiler setups to build
  the software without encountering errors due to warnings.  The `development` flag
  usually controls this behavior.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/c4e611d0-2ef2-4495-8623-7ec82df3f101@gmail.com
bugzilla_url: null
date: '2026-05-02'
---

The binutils 2.46 release tarball was packaged with the `development` variable set to `true` in `bfd/development.sh`. This setting enables `-Werror` by default, causing build failures on systems where warnings are present. The reporter notes that the "with-gold" release was packaged with `development=false`, suggesting the issue is unintended in the main release.
