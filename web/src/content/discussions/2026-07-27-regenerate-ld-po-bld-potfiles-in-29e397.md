---
project: binutils
subsystem: binutils
patch_id: null
tags:
- build system
- internationalization
- linker
- patch
discussion_id: ambhAl_W4xnVmZyq@squeak.grove.modra.org
source_type: public_inbox
title: regen ld/po/BLD-POTFILES.in
headline: Regenerate ld/po/BLD-POTFILES.in
tldr: A simple patch to regenerate the BLD-POTFILES.in file for the ld/po directory.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 2
sentiment_score: null
technical_tradeoffs:
- Removes a specific file from the internationalization process, potentially meaning
  fewer translated messages for that component if it were still relevant.
- Simplifies the build process by removing an obsolete entry.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: Submits a patch to regenerate `ld/po/BLD-POTFILES.in`, removing an obsolete
    file entry.
  quote: "diff --git a/ld/po/BLD-POTFILES.in b/ld/po/BLD-POTFILES.in\nindex d7d0c517307..fe46c510261\
    \ 100644\n--- a/ld/po/BLD-POTFILES.in\n+++ b/ld/po/BLD-POTFILES.in\n@@ -230,7\
    \ +230,6 @@ ehppalinux.c\n ehppanbsd.c\n ehppaobsd.c\n ei386aout.c\n-ei386beos.c\n\
    \ ei386bsd.c\n ei386go32.c\n ei386lynx.c"
primer_expert: This patch updates the `BLD-POTFILES.in` file within the `ld/po` directory
  of the binutils source tree. This file is typically used in the build system to
  manage internationalization (i18n) files, specifically for generating POT (Portable
  Object Template) files used for translations. The change involves removing an entry
  for `ei386beos.c`, suggesting that support or translation for this specific component
  is being deprecated or removed.
primer_glossary:
- term: po
  definition: A directory commonly used in software projects for translation files,
    often in conjunction with the gettext utility.
- term: POTFILES.in
  definition: A file used in GNU gettext build systems to list source files that contain
    translatable strings, used to generate a .pot template file.
- term: regen
  definition: Short for 'regenerate'. In this context, it means the patch is re-creating
    or updating build system files, often using an automated script.
- term: ld
  definition: The linker, a component of the GNU Binutils that combines object files
    into an executable or library.
- term: ei386beos.c
  definition: A C source file likely related to specific linker support for the BeOS
    operating system on the Intel 386 architecture.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/ambhAl_W4xnVmZyq@squeak.grove.modra.org
bugzilla_url: null
date: '2026-07-27'
is_stub: false
stub_reason: ''
---

This is a routine patch that regenerates the `ld/po/BLD-POTFILES.in` file. The change involves removing a single line (`ei386beos.c`) from the file, likely indicating that this file is no longer relevant or is being removed from the build process.
