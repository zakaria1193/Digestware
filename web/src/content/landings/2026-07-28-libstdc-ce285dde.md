---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- performance
- timezone
- c++
commit_hash: ce285dde2110f453fdbbd89fbb2f85a4d039705d
source_type: github
author: Tomasz Kamiński
headline: 'Timezone database loading: calculate DST save adjustment upfront'
tldr: Improves performance of timezone lookups after the first call by pre-calculating
  DST offsets.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: The `tzdb` loading mechanism in libstdc++ (`chrono::reload_tzdb`) now
  preemptively calls `ZoneInfo::calc_save` for all zones. This function computes the
  DST offset. Previously, this was deferred to `time_zone::_M_get_sys_info`, leading
  to repeated iterator adjustment checks on cached results. Moving the calculation
  to load time amortizes this cost, improving performance for repeated, cached timezone
  queries at the expense of a slightly longer initial load.
primer_glossary:
- term: tzdb
  definition: The timezone database, containing information about time zones, historical
    time and DST changes, and political boundaries for timekeeping.
- term: Daylight Saving Time (DST)
  definition: A practice of advancing clocks during warmer months so that darkness
    falls at a later hour of the clock. The 'save' adjustment refers to the amount
    of time DST shifts the clock forward.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/ce285dde2110f453fdbbd89fbb2f85a4d039705d
date: '2026-07-28'
is_stub: false
stub_reason: ''
---

This change optimizes timezone handling in libstdc++ by calculating daylight saving time (DST) save adjustments when the timezone database is loaded, rather than on-demand. Previously, calculating these adjustments could incur a performance cost on subsequent lookups, even with caching. By performing the calculation during the initial database load, subsequent calls to retrieve time zone information are faster, though the initial load time increases slightly.
