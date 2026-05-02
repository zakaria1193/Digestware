---
project: binutils
subsystem: ld
patch_id: null
tags:
- ld
- linker
- LDFLAGS
- build system
- binutils
discussion_id: afM1J1xjtf7Fbvh7@squeak.grove.modra.org
source_type: public_inbox
title: 'Re: [PATCH] ld: Append LDFLAGS to flags variable in default_ld_link'
headline: 'ld: Append LDFLAGS to flags variable in default_ld_link'
tldr: A patch to append LDFLAGS to the flags variable in default_ld_link is being
  reconsidered.
proposer: Alan Modra <amodra@gmail.com>
consensus: Proposed
outcome: proposed
impact_score: 4
sentiment_score: null
technical_tradeoffs:
- Convenience of automatically including `LDFLAGS` versus explicit control in test
  scripts.
- Potential for unexpected behavior if `LDFLAGS` contains flags that conflict with
  default settings.
- Reduced verbosity in test scripts if `LDFLAGS` is handled automatically.
exchanges:
- author: Alan Modra <amodra@gmail.com>
  role: proposer
  position: States that appending `LDFLAGS` to the flags in `default_ld_link` is acceptable
    if it ensures all `ld_link` calls utilize `LDFLAGS`, and suggests removing any
    now-unnecessary `LDFLAGS` additions.
  quote: That was likely why I did it that way, but if you need all occurrences of
    ld_link to use LDFLAGS then I'm happy for you to put it in default_ld_link, and
    ideally remove the then unnecessary places I added LDFLAGS.
primer_expert: The `ld` linker combines object files into executables or shared libraries.
  `LDFLAGS` is an environment variable commonly used to specify linker flags. The
  `default_ld_link` function likely sets up default flags for the linking process.
  The core question is whether to incorporate `LDFLAGS` into these defaults versus
  passing them explicitly in test scripts (`.exp` files), balancing convenience and
  control.
primer_general: The linker (`ld`) is a crucial tool in the software build process.
  It takes compiled object files and combines them into a single executable program
  or library.  The linking process often requires specific flags to control how the
  files are combined such as specifying library paths or defining symbols. These flags
  can be passed to the linker via the `LDFLAGS` environment variable. This discussion
  revolves around whether to automatically include `LDFLAGS` in the default linker
  settings or to specify them explicitly in test scripts.
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/binutils/afM1J1xjtf7Fbvh7@squeak.grove.modra.org
bugzilla_url: null
date: '2026-04-30'
---

John David Anglin is revisiting a patch that appends `LDFLAGS` to the `flags` variable in `default_ld_link` within the binutils linker (`ld`). Alan Modra indicates that the original approach intentionally avoided this, updating `.exp` files instead, but is open to the change if all `ld_link` instances should use `LDFLAGS`, potentially simplifying the configuration by removing redundant `LDFLAGS` specifications in `.exp` files.
