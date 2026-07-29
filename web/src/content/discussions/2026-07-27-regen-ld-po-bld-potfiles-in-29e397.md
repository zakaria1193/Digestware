---
project: binutils
subsystem: binutils
patch_id: null
tags:
- binutils
- linker
- localization
- gettext
discussion_id: ambhAl_W4xnVmZyq@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: regen ld/po/BLD-POTFILES.in'
headline: Regen ld/po/BLD-POTFILES.in
tldr: Remove commented-out file from POTFILES.in and clarify translation process.
proposer: Jan Beulich <jbeulich@suse.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: 7
technical_tradeoffs:
- Removing an obsolete file entry simplifies maintenance.
- Explicitly listing generated files for internationalization adds complexity but
  ensures correct string extraction.
exchanges:
- author: Jan Beulich
  role: proposer
  position: Removed a commented-out file from ld/po/BLD-POTFILES.in and questioned
    the need to enumerate generated files for translation.
  quote: 'Otoh - why do generated files need enumerating here? Aren''t translations

    done on the sources (i.e. the templates and whatever massages them)?'
- author: Alan Modra
  role: reviewer
  position: Confirmed the need for the change and explained that specific quoting
    issues in shell scripts require the explicit file enumeration for the translation
    process.
  quote: 'See commit 33589acbfe  Shell script quoting in .em files confuses

    xgettext.'
primer_expert: This discussion concerns the `ld/po/BLD-POTFILES.in` file within the
  GNU Binutils project. This file lists the template files that `xgettext` processes
  to extract translatable strings for the linker (`ld`). The change removes an obsolete
  entry and a contributor clarifies why certain generated files, despite not being
  source code, must be explicitly listed due to how `xgettext` handles shell script
  syntax within them.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: po
  definition: Portable Object file, a standard format for translated messages used
    by the gettext internationalization system.
- term: BLD-POTFILES.in
  definition: A file used in GNU build systems that lists source files from which
    translatable strings should be extracted.
- term: xgettext
  definition: A command-line tool that scans source code files to find translatable
    string literals and writes them into a template PO file (.pot).
- term: gettext
  definition: A widely used internationalization and localization (i18n and l10n)
    system for software, providing tools and libraries to translate messages.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/681abeda-7cbc-4f92-87ff-77896cfb5a68@suse.com
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

Jan Beulich proposed removing a commented-out file entry from ld/po/BLD-POTFILES.in. Alan Modra agreed the file needed updating and questioned why generated files are listed for translation. Modra clarified that specific shell script quoting issues in related files necessitate the explicit listing in BLD-POTFILES.in.
