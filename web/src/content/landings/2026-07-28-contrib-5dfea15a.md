---
project: gcc
subsystem: contrib
patch_id: null
tags:
- style
- whitespace
commit_hash: 5dfea15a44343841a5d3d18ee736eaeb4f48fb1d
source_type: github
author: Torbjörn SVENSSON
headline: 'contrib: Style checker handles tabs in the middle of lines'
tldr: Style checker correctly calculates line length with tabs not at the start.
impact_score: 1
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `check_GNU_style_lib.py` script, used for checking GCC's C source
  code style, has been modified to account for the visual width of tab characters
  even when they are not at the beginning of a line. This corrects a bug where lines
  containing middle-of-line tabs were incorrectly measured, leading to false positives
  in line-length checks.
primer_glossary: []
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://github.com/gcc-mirror/gcc/commit/5dfea15a44343841a5d3d18ee736eaeb4f48fb1d
date: '2026-07-28'
is_stub: true
stub_reason: low_score
---

The style checker script for GCC source code has been updated to correctly handle tabs that appear in the middle of a line. Previously, the script would miscalculate line lengths when tabs were not at the beginning of a line, potentially flagging lines as too long when they were within the limit. This change ensures accurate length calculation for better adherence to coding standards.
