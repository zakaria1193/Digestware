---
project: gcc
subsystem: gcc/libstdc++
patch_id: null
tags:
- libstdc++
- chrono
- timezone
commit_hash: cc195f7b11a4061ff8b0261372faadbef22791ee
source_type: github
author: Jonathan Wakely
headline: Use realpath for /etc/localtime symlink resolution
tldr: libstdc++ now uses realpath to resolve /etc/localtime symlinks, correctly identifying
  time zone names.
impact_score: 5
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `chrono::tzdb` implementation in `libstdc++` previously used `readlink`
  to resolve `/etc/localtime`. This fails when `/etc/localtime` is a symlink to another
  symlink (e.g., on read-only `/etc` mounts). This commit replaces `readlink` with
  `realpath` (or `filesystem::canonical` as a fallback) to fully resolve all symlinks
  to a physical file, extracting the correct timezone name. It also removes manual
  handling of redundant slashes, as `realpath` handles this. A potential downside
  is that entirely dangling symlinks might now cause `current_zone()` to fail instead
  of attempting to derive a z…
primer_glossary:
- term: libstdc++
  definition: The standard C++ library implementation used by GCC.
- term: realpath
  definition: A system call that returns the canonicalized absolute pathname of a
    given path, resolving all symbolic links and.. components.
- term: symlink
  definition: Symbolic Link. A type of file that acts as a pointer to another file
    or directory. When a symlink is accessed, the operating system follows the link
    to its target.
- term: chrono
  definition: A C++ library (in the <chrono> header) providing types and functions
    for measuring, representing, and manipulating time.
- term: tzdb
  definition: Time Zone Database. A database containing information about time zones
    worldwide, including historical data and daylight saving rules.
- term: current_zone()
  definition: A function within the C++ chrono library that attempts to determine
    and return the current system's time zone information.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/cc195f7b11a4061ff8b0261372faadbef22791ee
date: '2026-06-06'
is_stub: false
stub_reason: ''
---

Libstdc++'s timezone database now uses `realpath` to resolve the `/etc/localtime` symlink, addressing an issue where chained symlinks could prevent correct timezone identification. This change ensures that even complex symlink configurations correctly resolve to the underlying timezone file, allowing `chrono::current_zone()` to function reliably. The previous `readlink`-based approach could fail if `/etc/localtime` pointed to another symlink.
