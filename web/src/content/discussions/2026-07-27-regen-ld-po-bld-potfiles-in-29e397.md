---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- i18n
- gettext
- maintenance
- ld
discussion_id: ambhAl_W4xnVmZyq@squeak.grove.modra.org
source_type: public_inbox
title: regen ld/po/BLD-POTFILES.in
headline: regen ld/po/BLD-POTFILES.in
tldr: Updates `ld/po/BLD-POTFILES.in` to remove an outdated entry.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 1
sentiment_score: 9
technical_tradeoffs:
- Keeps the translation infrastructure clean and up-to-date.
- No functional change to the linker's operation.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a change to update `ld/po/BLD-POTFILES.in` by removing a now-obsolete
    entry.
  quote: "diff --git a/ld/po/BLD-POTFILES.in b/ld/po/BLD-POTFILES.in\nindex d7d0c517307..fe46c510261\
    \ 100644\n--- a/ld/po/BLD-POTFILES.in\n+++ b/ld/po/BLD-POTFILES.in\n@@ -230,7\
    \ +230,6 @@ ehppalinux.c\n ehppanbsd.c\n ehppaobsd.c\n ei386aout.c\n-ei386beos.c\n\
    \ ei386bsd.c\n ei386go32.c\n ei386lynx.c"
- author: Jan Beulich <jbeulich@suse.com>
  role: reviewer
  position: Acknowledges the correction and thanks the author for cleaning up a file
    that needed updating.
  quote: 'Darn, I meanwhile should know this file also needs updating. Thanks for

    once again cleaning up after me.'
- author: Alan Modra <amodra@gmail.com>
  role: contributor
  position: Explains that the removal of `ei386beos.c` was necessary due to a past
    commit that confused `xgettext` and required manual cleanup by removing the entry.
  quote: 'See commit 33589acbfe  Shell script quoting in .em files confuses

    xgettext.'
primer_expert: This is a routine maintenance change for the GNU `ld` linker's internationalization
  (i18n) setup. The `BLD-POTFILES.in` file lists source files that `xgettext` scans
  to generate Portable Object (PO) template files for translations. The change removes
  an entry for `ei386beos.c`, implying this file is no longer relevant or does not
  contain translatable strings, possibly due to its removal or changes in how strings
  are handled. This ensures that the translation infrastructure correctly identifies
  translatable messages.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: po/BLD-POTFILES.in
  definition: A file within the GNU translation infrastructure that lists source files
    to be scanned for translatable strings (gettext support).
- term: xgettext
  definition: A program that extracts translatable string literals from source code
    files.
- term: POTFILES.in
  definition: Portable Object Template Files. A list of files to be scanned for translatable
    strings when building internationalized software.
- term: GNU translation infrastructure
  definition: The set of tools and conventions used by GNU projects to manage and
    build translations for their software.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ambhAl_W4xnVmZyq@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This commit updates the `ld/po/BLD-POTFILES.in` file by removing the `ei386beos.c` entry. This is a maintenance task related to internationalization (i18n) and gettext, ensuring that the list of files scanned for translatable strings is accurate. The change was prompted by a user's cleanup effort.
