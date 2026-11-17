---
project: binutils
subsystem: binutils/gnulib
patch_id: null
tags:
- build
- gnulib
- scripting
commit_hash: 155b473af41b1556d285aa2e8326e0f13919d8e7
source_type: public_inbox
author: Tom de Vries <vries@sourceware.org>
headline: Skip 3rd-party m4 files when updating gnulib scripts.
tldr: Update-gnulib.sh now ignores system-wide m4 files to prevent unintended changes.
impact_score: 3
performance_win: false
breaking_change: false
outcome: committed
primer_expert: The `update-gnulib.sh` script uses `aclocal` to regenerate configuration
  files. By default, `aclocal` searches system-wide directories for `.m4` macros.
  This change explicitly tells `aclocal` to ignore system directories by setting `ACLOCAL_PATH=""`
  and `--system-acdir="<empty dir>"`. This prevents macro definitions from external
  packages (like `gettext-tools`) from being included, which was causing unwanted
  diffs during script regeneration.
primer_glossary:
- term: gnulib
  definition: A library of common, portable C code intended to be used by GNU programs,
    providing a consistent API across different platforms.
- term: aclocal
  definition: A tool that generates an `aclocal.m4` file for use by `autoconf`. It
    searches for macro definitions in `.m4` files, including system-wide directories.
- term: m4
  definition: A macro processor used in many Unix/Linux systems, often used by build
    tools like autoconf to generate configuration scripts.
- term: PIC code
  definition: Position-Independent Code. Code that can be loaded and executed at any
    memory address without modification. Essential for shared libraries.
discussion_id_link: null
bugzilla_pr: null
series_id: null
series_parts: []
url: https://inbox.sourceware.org/binutils-cvs/20261116204311.069924B92093@sourceware.org
date: '2026-11-16'
is_stub: true
stub_reason: low_score
---

The update-gnulib.sh script previously picked up system-installed m4 files, leading to unnecessary changes in the repository. This commit modifies the script to run aclocal with an empty ACLOCAL_PATH and an empty system ac-directory. This ensures that only gnulib's own m4 files are considered, preventing the inclusion of third-party m4 files and stopping spurious modifications.
