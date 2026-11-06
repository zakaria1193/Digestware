---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- timezone
- data update
commit_hash: 9f5edf2dd4d69ca222f218c26bbdbe05ae68f3b0
source_type: github
author: Tomasz Kamiński
headline: Update timezone data in libstdc++ to tzdata 2026f.
tldr: The timezone database used by libstdc++ has been updated to version 2026f, with
  no changes to leap seconds.
impact_score: 4
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `libstdc++-v3/src/c++20/tzdata.zi` file, which provides the C++20
  timezone database implementation within libstdc++, has been updated by importing
  the `tzdata.zi` file from the `tzdata 2026f` release. This update brings the C++
  standard library's timezone information in line with the latest IANA Time Zone Database.
  Importantly, the `tzdata 2026f` release does not contain any new leap seconds, aligning
  with the stated policy of CGPM (Coordination Group for Meteorological<bos>) to cease
  adding new leap seconds. This ensures that C++ applications using `std::chrono`
  or related timezone funct…
primer_glossary:
- term: libstdc++
  definition: The C++ standard library implementation provided by the GNU Compiler
    Collection (GCC). It includes components for input/output, strings, algorithms,
    and more, including timezone support.
- term: tzdata
  definition: The IANA Time Zone Database, a widely used collection of data specifying
    the time rules (historical and future) for various regions around the world. It
    includes information on standard time offsets and daylight saving time transitions.
- term: tzdata.zi
  definition: A specific file format or compiled representation of the IANA Time Zone
    Database used internally by some systems, including libstdc++, for efficient lookup
    of timezone information.
- term: leap second
  definition: An extra second added occasionally to Coordinated Universal Time (UTC)
    to keep it synchronized with mean solar time. Leap seconds are announced by the
    International Earth Rotation and Reference Systems Service (IERS).
- term: C++20
  definition: The 2020 version of the C++ programming language standard. It introduced
    new features and improvements, including enhancements to the `<chrono>` library
    for better timezone support.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/9f5edf2dd4d69ca222f218c26bbdbe05ae68f3b0
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

The timezone data (`tzdata.zi`) within libstdc++ has been updated to the latest release, 2026f. This update incorporates the most recent information regarding time zones and daylight saving rules. Notably, this version does not include any new leap seconds, reflecting a policy decision to stop adding them. The update is imported directly from the official tzdata release.
