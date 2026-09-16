---
project: binutils
subsystem: h8300-elf
patch_id: null
tags:
- binutils
- ld
- h8300-elf
- linker-script
- testing
discussion_id: 20260823201052.1569259-1-jdx@o2.pl
source_type: public_inbox
title: '[PING] [PATCH v3] h8300-elf: ld: Use USER_LABEL_PREFIX when generating linker
  scripts [REPOST]'
headline: 'h8300-elf: ld: Use USER_LABEL_PREFIX when generating linker scripts'
tldr: Patch reposted to add H8/300 simulator testsuite change for USER_LABEL_PREFIX.
proposer: Jan Dubiec <jdx@o2.pl>
consensus: Proposed
outcome: proposed
impact_score: 3
sentiment_score: 7
technical_tradeoffs:
- Ensures consistent label handling across different tools and environments.
- Requires a separate review for the testsuite modification.
exchanges:
- author: Jan Dubiec <jdx@o2.pl>
  role: proposer
  position: Reposts the patch, noting that the binutils part is accepted and the remaining
    change to the H8/300 simulator testsuite requires GDB/sim maintainer approval.
  quote: "Gentle ping. Although this patch modifies files in both binutils and the\
    \ \nH8/300 simulator testsuite, it constitutes a single logical change. The \n\
    binutils part has already been accepted, and now only the small and \nstraightforward\
    \ change to the simulator testsuite awaits approval from a \ngdb/sim maintainer."
- author: Hans-Peter Nilsson <hp@bitrange.com>
  role: reviewer
  position: Responded to the ping, indicating awareness of the need for a GDB maintainer's
    review.
  quote: "Regarding your recent ping for a gdb maintainer for this part \nof your\
    \ patch:\n\nOn Sun, 23 Aug 2026, Jan Dubiec wrote:\n\n> This version does not\
    \ explicitly set the entry symbol; the default one\n> is used instead.\n>\n> The\
    \ patch also changes one file in the H8/300 simulator testsuite, as it\n> is affected\
    \ by the change to the entry symbol. The patch has therefore\n> also been posted\
    \ to the gdb-patches…"
primer_expert: This patch for the h8300-elf target in binutils' ld linker modifies
  how linker scripts are generated. Specifically, it introduces the use of `USER_LABEL_PREFIX`
  to ensure consistency with how labels are handled, especially concerning the entry
  symbol. A related change to the H8/300 simulator testsuite is pending review.
primer_glossary:
- term: ld
  definition: The GNU linker, responsible for combining object files and libraries
    into an executable or shared library.
- term: linker script
  definition: A file that controls how the linker assigns addresses to output sections
    and what symbols are defined. It allows customization of the output binary's memory
    layout.
- term: USER_LABEL_PREFIX
  definition: A configuration option or macro used by the linker to prepend a specific
    prefix to user-defined labels, ensuring proper symbol resolution, especially in
    cross-compilation environments.
- term: H8/300
  definition: A family of microcontrollers from Renesas (formerly Hitachi). The h8300-elf
    target refers to the toolchain for this architecture using the ELF object file
    format.
- term: simulator testsuite
  definition: A collection of tests designed to verify the correct functionality of
    a CPU simulator, often part of a larger toolchain.
series_id: 20260823201052.1569259-1-jdx@o2.pl
series_role: cover
series_parts: []
url: https://inbox.sourceware.org/binutils/b81761f4-4110-4a6d-871e-0f1b4c7e56e9@o2.pl
bugzilla_url: null
date: '2026-09-15'
is_stub: false
stub_reason: ''
---

This is a repost of a patch series for the h8300-elf target in binutils, which has been split into two logical parts. The binutils linker script modification has been accepted, and this repost focuses on the smaller, straightforward change to the H8/300 simulator testsuite. The author is seeking approval from a GDB/sim maintainer for this remaining part.
