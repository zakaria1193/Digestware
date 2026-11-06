---
project: gcc
subsystem: gcc
patch_id: null
tags:
- build system
- autoconf
- automake
- toolchain
- release cycle
discussion_id: 18b284b3-1b50-481a-a7ee-6e3e12073df0@app.fastmail.com
source_type: public_inbox
title: Upgrading autoconf and automake
headline: Upgrading autoconf and automake
tldr: Pietro Monteiro proposes upgrading GCC's autoconf and automake versions and
  seeks community input on timing, versions, and testing.
proposer: Pietro Monteiro <pietro@sociotechnical.xyz>
consensus: Proposed
outcome: proposed
impact_score: 5
sentiment_score: 5
technical_tradeoffs:
- Risk of introducing build system regressions with newer autoconf/automake versions
  vs. benefits of using updated tools.
- Effort required for comprehensive testing across all GCC targets vs. potential issues
  discovered post-upgrade.
- Timing of the upgrade within the GCC release cycle; potential impact on release
  stability.
exchanges:
- author: Pietro Monteiro
  role: proposer
  position: Proposes upgrading autoconf and automake to latest versions (2.73 and
    1.19) and seeks community input on timing, version choice, and testing strategies.
  quote: 'I decided to try upgrading autoconf and automake to the latest

    available versions, respectively 2.73 and 1.19. I put the result in a

    branch on the forge (https://forge.sourceware.org/pietro/gcc.git

    branch upgrade-autotools) and I''m doing some basic testing. The patch

    at the tip of that branch depends on some patches I''ve sent

    recently[1,2,3] and a patch I haven''t sent yet hat does the same as

    pat…'
- author: Eric Gallager
  role: other
  position: Acknowledges the proposal, quoting Pietro's initial message without adding
    new commentary.
  quote: "On Thu, Nov 5, 2026 at 12:02 PM Pietro Monteiro via Gcc <gcc@gcc.gnu.org>\
    \ wrote:\n> \n> I decided to try upgrading autoconf and automake to the latest\n\
    > available versions, respectively 2.73 and 1.19. I put the result in a\n> branch\
    \ on the forge (https://forge.sourceware.org/pietro/gcc.git\n> branch upgrade-autotools)\
    \ and I'm doing some basic testing. The patch\n> at the tip of that branch depends\
    \ on…"
- author: Sam James
  role: other
  position: Quotes Eric Gallager's reply, which in turn quotes Pietro Monteiro's original
    proposal, without adding new input.
  quote: "Eric Gallager via Gcc <gcc@gcc.gnu.org> writes:\n\n> On Thu, Nov 5, 2026\
    \ at 12:02 PM Pietro Monteiro via Gcc <gcc@gcc.gnu.org> wrote:\n>> \n>> I decided\
    \ to try upgrading autoconf and automake to the latest\n>> available versions,\
    \ respectively 2.73 and 1.19. I put the result in a\n>> branch on the forge (https://forge.sourceware.org/pietro/gcc.git\n\
    >> branch upgrade-autotools) and I'm doing some basic te…"
- author: Sam James
  role: other
  position: Quotes Pietro Monteiro's original proposal, without adding new input.
  quote: 'Pietro Monteiro via Gcc <gcc@gcc.gnu.org> writes:


    > I decided to try upgrading autoconf and automake to the latest

    > available versions, respectively 2.73 and 1.19. I put the result in a

    > branch on the forge (https://forge.sourceware.org/pietro/gcc.git

    > branch upgrade-autotools) and I''m doing some basic testing. The patch

    > at the tip of that branch depends on some patches I''ve sent

    > recently…'
- author: Pietro Monteiro
  role: proposer
  position: Responds to Eric Gallager's quoted reply, reiterating the original proposal
    and its context.
  quote: "On Thu, Nov 5, 2026, at 12:19 PM, Eric Gallager via Gcc wrote:\n> On Thu,\
    \ Nov 5, 2026 at 12:02 PM Pietro Monteiro via Gcc <gcc@gcc.gnu.org> wrote:\n>>\
    \ \n>> I decided to try upgrading autoconf and automake to the latest\n>> available\
    \ versions, respectively 2.73 and 1.19. I put the result in a\n>> branch on the\
    \ forge (https://forge.sourceware.org/pietro/gcc.git\n>> branch upgrade-autotools)\
    \ and I'm doing…"
primer_expert: This RFC proposes upgrading the build system tools, autoconf and automake,
  used by GCC. The proposal involves moving to newer versions (2.73 and 1.19, respectively)
  and assesses the impact and required testing across various GCC targets. The core
  concern is maintaining build system stability and compatibility during the toolchain
  update.
primer_glossary:
- term: autoconf
  definition: A GNU tool that automatically configures source code packages to adapt
    to a particular operating system when compiling them. It generates shell scripts
    that check for dependencies and system characteristics.
- term: automake
  definition: A GNU tool that automatically builds a `Makefile` from a simpler, higher-level
    `Makefile.am` input. It helps maintain consistency across different systems and
    GNU packages.
- term: toolchain
  definition: A set of programming tools used to perform a complex process, typically
    software development. For GCC, this includes the compiler, assembler, linker,
    and other utilities.
- term: targets
  definition: In the context of GCC, a target refers to the combination of CPU architecture,
    operating system, and ABI that the compiler is configured to generate code for
    (e.g., x86_64-linux-gnu).
series_id: null
series_role: standalone
series_parts: []
url: https://inbox.sourceware.org/gcc/18b284b3-1b50-481a-a7ee-6e3e12073df0@app.fastmail.com
bugzilla_url: null
date: '2026-11-05'
is_stub: false
stub_reason: ''
---

Pietro Monteiro proposes upgrading GCC to autoconf 2.73 and automake 1.19, maintaining the changes in a git branch. He seeks community feedback on the timing of this upgrade, the suitability of the chosen versions, and the necessary testing procedures, especially for non-GNU toolchain targets. The discussion is ongoing, with initial questions posed to the community.
