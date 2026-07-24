---
project: gcc
subsystem: libstdc++
patch_id: null
tags:
- libstdc++
- chrono
- formatting
- iostream
commit_hash: e906bebbf21dc50a5c4db9afa358db6e48d4706b
source_type: github
author: Anlai Lu
headline: 'Libstdc++: Use __chrono_write for chrono ostream insertion.'
tldr: Libstdc++ chrono output now uses a new helper function for improved formatting
  and buffer management.
impact_score: 5
performance_win: true
breaking_change: false
outcome: committed
primer_expert: Libstdc++'s chrono I/O has been updated with the introduction of `__detail::__chrono_write`.
  This internal helper leverages `std::format_to_n` with `_S_empty_fs()` for efficient
  formatting into a stack buffer, controlled by a `_BufSize` non-type template parameter.
  The `operator<<` overloads for all chrono types now utilize this helper, abstracting
  away the underlying formatting and stream insertion mechanisms and improving buffer
  management by sizing it to the maximum expected output for each type.
primer_glossary:
- term: chrono
  definition: The C++ standard library header for time utility facilities, providing
    types for durations, time points, and clocks.
- term: ostream insertion
  definition: The process of writing data to an output stream, typically using the
    `operator<<` overload.
- term: std::format_to_n
  definition: A C++20 formatting function that writes formatted output to a buffer
    and limits the number of characters written.
- term: stack buffer
  definition: A temporary memory buffer allocated on the program's call stack, used
    for short-lived data.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/e906bebbf21dc50a5c4db9afa358db6e48d4706b
date: '2026-06-30'
is_stub: false
stub_reason: ''
---

The C++ standard library's chrono formatting for `operator<<` has been refactored to use a new helper function, `__detail::__chrono_write`. This function formats chrono objects into a stack buffer using `std::format_to_n` and then writes the output via `__ostream_insert`. This change consolidates formatting logic, allows per-type buffer tuning via a `_BufSize` template parameter, and replaces older methods like `std::format`, `std::vformat`, and `basic_stringstream` for chrono output.
